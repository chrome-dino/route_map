import argparse
import route_map


def main():
    parser = argparse.ArgumentParser()

    # cmd line args
    parser.add_argument("-f", "--file", help="Path to input pcap file.",required=False)
    parser.add_argument("-t", "--trace", help="Endpoint to trace to.",required=False)
    parser.add_argument("-o", "--output", help="Path to output kml file. Defaults to route_map.kml.",required=False)
    parser.add_argument("-p", "--public", help="Define public IP. Leave blank to auto retrieve.",required=False)
    parser.add_argument("-l", "--local", help="Define local IP. Leave blank to auto retrieve.",required=False)
    
    args = parser.parse_args()
    if not args.file and not args.trace:
        print('Requires either a pcap file input (-f) or a endpoint to trace to (-t)')
        exit(-1)
    route_map_obj = route_map.RouteMap(pcap=args.file,trace=args.trace,out=args.output,public=args.public,local=args.local)
    route_map_obj.run()
    
if __name__ == "__main__":
    main()
