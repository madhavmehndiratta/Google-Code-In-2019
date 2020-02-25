import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+] %d/tcp open' % tgtPort
        print '[+] ' + str(results)
    except:
        screenLock.acquire()
        print '[-] %d/tcp closed' % tgtPort
    finally:
	screenLock.release()
	connSkt.close()	

def get_arguments():
    parser = optparse.OptionParser('usage %prog '+\
                                   '-t <target host> -p <target port>')
    parser.add_option('-t', '--target', dest='trgtHost', type='string',\
                      help='Please Specify the Target Host')
    parser.add_option('-p', '--port', dest='tgtPort', type='string',\
                      help='Please Specify the Target Port[s] Separated by Comma')
    
    (options, arguments) = parser.parse_args()
    return options

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host" %tgtHost
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()

def main(tgtHost,tgtport):

    tgtPorts = str(tgtport).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
	print parser.usage
        exit(0)

    portScan(tgtHost, tgtPorts)

options = get_arguments()
if __name__ == '__main__':
    main(options.trgtHost, options.tgtPort)
