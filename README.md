Amon3 better MySQL
=====================
This plugin is aimed at providing more insight into your MySQL server. It should be able 
to run alongside the original MySQL plugin for [Amon][1] without any issues. 

This plugin extends the original mysql plugin by adding `tracked` variables. This is used
to generate `x` per second graphs. Where `x` is the `tracked` variable. 

## Installation
Browse to `/etc/amonagent/plugins` and execute the command `git clone https://github.com/Mechazawa/amon3-better-MySQL better-mysql`. This will clone the repository into the folder `/etc/amonagent/plugins/better-mysql`. After the git command has finished execute `amonpm install better-mysql`. To test the plugin run `amonpm test` **twice**. The first time will be used to grab the seed data. This data will be used to compare things like queries executed, bytes sent, etc. You will only need to run it twice the first time you test it. The file containing the seed data can be found at `/tmp/amon-better-mysql`. 

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
