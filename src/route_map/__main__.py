import argparse
import route_map


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    # cmd line args
    group.add_argument("-f", "--file", help="Path to input pcap file.",required=False)
    group.add_argument("-t", "--trace", help="Endpoint to trace to.",required=False)
    parser.add_argument("-o", "--output", help="Path to output kml file. Defaults to route_map.kml.",required=False)
    parser.add_argument("-p", "--public", help="Define public IP. Leave blank to auto retrieve.",required=False)
    parser.add_argument("-l", "--local", help="Define local IP. Leave blank to auto retrieve.",required=False)
    
    args = parser.parse_args()

    route_map_obj = route_map.RouteMap(pcap=args.file,trace=args.trace,out=args.output,public=args.public,local=args.local)
    route_map_obj.run()
    
if __name__ == "__main__":
    main()
