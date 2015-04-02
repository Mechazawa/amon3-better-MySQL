Amon3 better MySQL
=====================
This plugin is aimed at providing more insight into your MySQL server. It should be able 
to run alongside the original MySQL plugin for [Amon][1] without any issues. 

This plugin extends the original mysql plugin by adding `tracked` variables. This is used
to generate `x` per second graphs. Where `x` is the `tracked` variable. 

## Installation
```sh
cd /etc/amonagent/plugins
git clone https://github.com/Mechazawa/amon3-better-MySQL better-mysql
amonpm install better-mysql && \
amonpm test > /dev/null # Seed data
```
The file containing the seed data can be found at `/tmp/amon-better-mysql`. 

###Example output:
Please note that the output has been prettified and the command will most likely ouput a 'compressed' json object.
```
------------------
  Better-Mysql
------------------
{
    'versions': {
        'mysql': '5.5.41-0+wheezy1',
        'mysqldb': '1.2.5',
        'plugin': '0.4'
    },
    'error': False,
    'gauges': {
        'info.connections': '3',
        'performance.cache_hits_per_second': 1,
        'net.bytes_per_second': 2204,
        'performance.queries_per_second': 2
    },
    'counters': {
        'net.total_connections': '106801'
    }
}

Check: OK
```

## License
This project is licensed under the [MIT license](/LICENSE).
The base of this project has been copied from the [official amon-plugins repository][2]

[1]: https://amon.cx/
[2]: https://github.com/amonapp/amon-plugins
