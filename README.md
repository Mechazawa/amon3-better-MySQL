Amon3 better MySQL
=====================
This plugin is aimed at providing more insight into your MySQL server. It should be able 
to run alongside the original MySQL plugin for [Amon][1] without any issues. 

This plugin extends the original mysql plugin by adding `tracked` variables. This is used
to generate `x` per second graphs. Where `x` is the `tracked` variable. 

## Current status
The plugin is generating data but due to the lack of documentation it is not sending 
the names in the right format. This should be fixed in a future release.

## Please note:
This project is still in development and is currently not in a working state

## License
This project is licensed under the [MIT license](/LICENSE).
The base of this project has been copied from the [official amon-plugins repository][2]

[1]: https://amon.cx/
[2]: https://github.com/amonapp/amon-plugins