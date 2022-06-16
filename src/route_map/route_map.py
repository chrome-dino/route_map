from scapy.all import *
import requests
import json
from subprocess import Popen, PIPE
import simplekml
import socket
import ipaddress


# https://www.google.com/maps/about/mymaps/


class RouteMap:

    def __init__(self, pcap='', trace='', out='',public='',local=''):
        # Intialize member variables
        self.pcap = pcap
        if public:
            self.public = public
        else:
            self.public = self.get_public()  
        if local:
            self.local = local
        else:
            self.local = self.get_local()
        self.trace = trace
        if out:
            self.out = out
        else:
            self.out = 'route_map.kml'

    @staticmethod
    def geolocate(ip):
        request_url = 'https://geolocation-db.com/jsonp/' + ip
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result = json.loads(result)
        return {'lat': result['latitude'], 'long': result['longitude']}

    @staticmethod
    def get_public():
        endpoint = 'https://ipinfo.io/json'
        response = requests.get(endpoint, verify=True)

        if response.status_code != 200:
            return 'Status:', response.status_code, 'Failed to get public IP. Exiting...'

        data = response.json()

        return data['ip']

    def build_kml(self, route):
        kml = simplekml.Kml()
        hop_no = 1
        for row in route:
            coords = [(row['src']['long'], row['src']['lat']),(row['dst']['long'], row['dst']['lat'])]
            src_pnt = kml.newpoint(name=row['src']['ip'], coords=[coords[0]])
            src_pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_square.png'
            line = kml.newlinestring(name='hop ' + str(hop_no), description=row['src']['ip'] + ' - ' + row['dst']['ip'],
                                     coords=coords)
            line.style.linestyle.color = 'ff0000ff'
            line.style.linestyle.width = 2
            hop_no +=1
        dst_pnt = kml.newpoint(name=route[-1]['dst']['ip'], coords=[(route[-1]['dst']['long'], route[-1]['dst']['lat'])])
        dst_pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_square.png'
        # save KML to a file
        kml.save(self.out)
        return

    def trace_mode(self):
        command = "tracert " + self.trace
        pipe = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)

        trace = []
        while True:
            line = pipe.stdout.readline()
            if line:
                hop = line.decode('ascii')
                validip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", hop)
                if not validip:
                    continue
                else:
                    trace.append(validip[-1])
            if not line:
                break
        trace.pop(0)
        route = []
        trace[0] = self.public
        final = []
        for hop in trace:
            ip = ipaddress.IPv4Address(hop)
            if not ip.is_private and not ip.is_multicast:
                final.append(hop)

        
        for hop in range(len(final) - 1):
            
            src_cood = self.geolocate(final[hop])
            dst_cood = self.geolocate(final[hop + 1])
            route.append({'src': {'ip': final[hop], 'lat': src_cood['lat'], 'long': src_cood['long']},
                          'dst': {'ip': final[hop + 1], 'lat': dst_cood['lat'], 'long': dst_cood['long']}})
        
        self.build_kml(route)
        return
    
    @staticmethod
    def get_local():
        h_name = socket.gethostname()
        local = socket.gethostbyname(h_name)
        return local
        
    def pcap_mode(self):
        ips = set((p[IP].src, p[IP].dst) for p in PcapReader(self.pcap) if IP in p)
        dup = []
        route = []

        for ip in ips:
            src = ip[0]
            dst = ip[1]
            if src == self.local:
                src = self.public
            if dst == self.local:
                dst = self.public
            comb = src + dst
            if comb in dup:
                continue
            else:
                dup.append(comb)
            ip = ipaddress.IPv4Address(src)
            ip2 = ipaddress.IPv4Address(dst)
            if ip.is_private or ip2.is_private or ip.is_multicast or ip2.is_multicast:
                continue
            src_cood = self.geolocate(src)
            dst_cood = self.geolocate(dst)
            route.append({'src': {'ip': src, 'lat': src_cood['lat'], 'long': src_cood['long']},
                          'dst': {'ip': dst, 'lat': dst_cood['lat'], 'long': dst_cood['long']}})

        self.build_kml(route)
        return
    
    def run(self):
        if self.trace is None:
            self.pcap_mode()
        else:
            self.trace_mode()


