'''programmed by m1m3'''

import nmap
import optparse

def get_arguments():
    parser = optparse.OptionParser('usage %prog '+\
                                   '-t <target host> -p <target port>')
    parser.add_option('-t', '--target', dest='trgtHost', type='string',\
                      help='Please Specify the Target Host')
    parser.add_option('-p', '--port', dest='tgtPort', type='string',\
                      help='Please Specify the Target Port[s] Separated by Comma')
    
    (options, arguments) = parser.parse_args()
    return options
    

def nmapScan(trgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(trgtHost,tgtPort)
    state=nmScan[trgtHost]['tcp'][int(tgtPort)]['state']
    print("[*] " + trgtHost + " tcp/"+tgtPort +" "+state)

def main(trgtHost, tgtPort):
    
    tgtPorts = str(tgtPort).split(',')
    
    for tgtPort in tgtPorts:
        nmapScan(trgtHost, tgtPort)

options = get_arguments()
if __name__ == '__main__':
    main(options.trgtHost, options.tgtPort)

    
