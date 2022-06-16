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
* Ability to choose to manually define or automatically retrieve local/public IP


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
usage: __main__.py [-h] [-f FILE] [-t TRACE] [-o OUTPUT] [-p PUBLIC] [-l LOCAL]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to input pcap file.
  -t TRACE, --trace TRACE
                        Endpoint to trace to.
  -o OUTPUT, --output OUTPUT
                        Path to output kml file. Defaults to route_map.kml.
  -p PUBLIC, --public PUBLIC
                        Define public IP. Leave blank to auto retrieve.
  -l LOCAL, --local LOCAL
                        Define local IP. Leave blank to auto retrieve.
```

### Video
* https://youtu.be/vI9GrCCFhMQ

### Examples

```bash
# develop a route map based on the traffic within the input pcap file. Output file will default to route_map.kml
$ py -m route_map -f file.pcap

# trace a route to a target IP address or url and build a kml map file. The output file has been defined as trace.kml
$ py -m route_map -t TARGET_IP -o trace.kml

# manually define the public and local IP. Useful when analyzing a pcap on a system other than the one it was generated on
$ py -m route_map -f file.pcap -l LOCAL_IP -p PUBLIC_IP
```


## Notes

* Tested on python 3.10.4


## License

MIT
