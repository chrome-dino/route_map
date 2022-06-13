import argparse
import route_mao


def main():
    parser = argparse.ArgumentParser()

    # cmd line args
    valid = ''
    for x in os_whitelist:
        valid += "'" + x + "',"
    valid = valid[:-1]
    parser.add_argument("-f", "--host_file", help="Name of the host file containing line seperated list of IPs or FQDNs. Defaults to hosts.txt",required=False)
    parser.add_argument("-o", "--operating_systems", help="Comma seperated list of operating systems. Valid OSs are as follows: " + valid,required=True)


    
    
    args = parser.parse_args()

    os_list = args.operating_systems.split(',')
    os_final = []
    
    # catch invalid OS entries
    for x in os_list:
        if x.strip() not in os_whitelist:
            print(x.strip() + ' is an invalid OS. Valid OSs are as follows:')
            for y in os_whitelist:
                print(y)
            exit(-1)
        else:
            os_final.append(x.strip())

    audit = patch_compliance.PatchCompliance(os_list=os_final,host_file=args.host_file)
    audit.run()
    
if __name__ == "__main__":
    main()
