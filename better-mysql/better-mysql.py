import MySQLdb
from os import path, chmod
from time import time
from amonagent.modules.plugins import AmonPlugin


class BetterMySQLPLugin(AmonPlugin):

    VERSION = '0.1'

    # Tracked for 'per second'
    TRACKED = [
        'Bytes_sent',
        'Queries',
        'Qcache_hits',
    ]

    GUAGES = {
        'Threads_connected': 'net.connections',

        # Tracked variables
        'Tracked_Bytes_sent': 'net.bytes.per.second',
        'Tracked_Queries': 'performance.queries.per.second',
        'Tracked_Qcache_hits': 'performance.cache.hits.per.second',
    }

    COUNTERS = {
        'Connections': 'net.total.connections',
    }

    def _connect(self):
        host = self.config.get('host', 'localhost')
        port = self.config.get('port', 3306)
        user = self.config.get('user')
        password = self.config.get('password')
        socket = self.config.get('socket')

        if socket:
            self.connection = MySQLdb.connect(unix_socket=socket, user=user, passwd=password)
        else:
            self.connection = MySQLdb.connect(host=host, port=port, user=user, passwd=password)

        self.cursor = self.connection.cursor()
        self.log.debug("Connected to MySQL")

    def _disconnect(self):
        self.cursor.close()
        self.connection.close()
        del self.cursor

    def _cache_init(self):
        file = self.config.get('cache_file', '/tmp/amon-better-mysql')
        if not path.exists(file):
            open(file, 'a').close()  # Touches file
            chmod(file, 700)
        return file

    def _cache_load(self):
        file = self.config.get('cache_file', '/tmp/amon-better-mysql')

        with open(file) as f:
            data = dict([line.split("|", 2) for line in f])

        return data or False

    def _cache_save(self, data):
        file = self.config.get('cache_file', '/tmp/amon-better-mysql')

        content = '\n'.join('%s|%i' % (k, v)
                            for k, v in data.items()
                            if k in self.TRACKED)
        data['cache_timestamp'] = int(time())

        with open(file, 'w') as f:
            f.write(content)

    def collect(self):
        try:
            self._connect()
            self._cache_init()

            self.cursor.execute("SHOW /*!50002 GLOBAL */ STATUS;")
            results = dict(self.cursor.fetchall())
            prev_cache = self._cache_load()

            if isinstance(prev_cache, dict):
                time_diff = int(time()) - prev_cache['cache_timestamp'] or 1

            # Fetch stuff that is up for grabs
            for k, v in results.items():
                if k in self.TRACKED and isinstance(prev_cache, dict):
                    per_sec = (v - prev_cache[k]) // time_diff
                    self.gauge(self.GAUGES['Tracked_' + k], per_sec)
                if k in self.COUNTERS:
                    self.counter(self.COUNTERS[k], v)
                if k in self.GAUGES:
                    self.gauge(self.GAUGES[k], v)

            self._cache_save(results)

            self.cursor.execute("SELECT VERSION();")
            try:
                mysql_version = self.cursor.fetchone()[0]
            except:
                mysql_version = None

            self.version(mysql=mysql_version,
                    plugin=self.VERSION,
                    mysqldb=MySQLdb.__version__)

        finally:
            self._disconnect()
