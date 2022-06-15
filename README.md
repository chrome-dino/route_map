# Route Map 

Route Map is a tool that can be track network traffic, map it via geolocation, and present the data in a visual fashion. This can be utilized for marketing purposes by organizations by helping to better understand their customer base. For internal resources, the tool can help to geolocate legitimate traffic which can help to whitelist it. Finally, the tool can help to identify suspicious traffic and includes a mode to trace the traffic back to its source. This can potentially be used for atribution when it comes to a post mortem of an attack. 


## Table of Contents
* <a href="#key-features">Key Features</a></br>
* <a href="#installation">Installation</a></br>
* <a href="#how-to-use">How To Use</a> </br>
* <a href="#notes">Notes</a></br>
* <a href="#license">License</a>


## Key Features

* Parse a pcap file, extracting IP addresses and geolocating them
* Build a kml file from geolocation data which can be viewed in Google Maps
* Trace the route of potentially interesting traffic  


## Installation

```bash
# Clone this repository
$ git clone https://github.com/chrome-dino/route_map.git

# From the directory containing your git projects
$ pip install -e route_map
```

Uses the following python libraries:
* scapy
* requests
* json
* subprocess
* simplekml
* socket
* argparse

## How To Use

### Help Menu

```bash
usage: __main__.py [-h] -db HOSTNAME -u USERNAME -p PASSWORD [-port PORT] [-s SCHEMA] [-t TABLE] [-a | --admin | --no-admin]
                   [-v | --verbose | --no-verbose]

options:
  -h, --help            show this help message and exit
  -db HOSTNAME, --hostname HOSTNAME
                        IP address or hostname of the target database
  -u USERNAME, --username USERNAME
                        Login username
  -p PASSWORD, --password PASSWORD
                        Login Password
  -port PORT, --port PORT
                        Port number (Defaults to 3306)
  -s SCHEMA, --schema SCHEMA
                        Name of the schema to be used in table extraction mode. Requires the table option
  -t TABLE, --table TABLE
                        Name of the table to be used in table extraction mode. Requires the schema option
  -a, --admin, --no-admin
                        Enable admin mode to extract database user info. Requires admin credentials
  -v, --verbose, --no-verbose
                        List additional details in the user report
```

### Video
* https://youtu.be/ENCz8EvVfuc

### Examples

```bash
# run the report generator with a standard user
$ py -m mysql_enumerator -db hostname -u user -p password

# run the report generator with elevated permissions and extract info on database users
$ py -m mysql_enumerator -db hostname -u root -p password -a

# extract the rows from a table
$ py -m mysql_enumerator -db hostname -u user -p password -s schema_name -t table_name1,table_name2
```


## Notes

* Tested on python 3.10.4


## License

MIT
