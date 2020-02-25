import shodan
import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-k", '--key', dest="key", help="Specify your Shodan API key")
    (options, arguments) = parser.parse_args()
    return options
                                                                                      		
def host():
	host_name = str(input("Enter the host name :"))
	host_info = api.host(host_name , history=True)
	print("-----------------------------------------------------------------------------------------------------------------")
	print("IP: %s"%host_info["ip_str"])
	print("Hostnames:\n")
	for element in host_info["hostnames"]:
			print ("  [+] %s\n"%str(element))
	print("Organization: %s"%host_info.get("org", "n/a"))
	print("Operating System: %s"%host_info.get("os", "n/a"))
	print("Latitude: %s"%host_info["latitude"])
	print("Longitude: %s"%host_info["longitude"])
	print("City: %s"%host_info["city"])
	print("-----------------------------------------------------------------------------------------------------------------")
		
def search():
	query = str(input("Enter Search Query: "))
	res = api.search(query)
	for service in res['matches']:
		print(service['ip_str'] + '   |   ' + str(service['port']) + '   |   ' + str(service['org']))

def ip():
#    subprocess.call(["shodan", "init", api])
    subprocess.call(["shodan", "myip"])
    print(ip)

def main():
	print("1. Host scan")
	print("2. Search for your query")
	print("3. What's my IP?")
	print("0. Exit") 
	option = int(input("Enter choice : "))
	if option == 1:
		host()
	elif option == 2:
		search()
	elif option == 3:
		ip()
	else:
		exit()

options = get_arguments()

if not options.key:
    key = str(input("Enter you Shodan API key: "))
    if not key:
        print("No Key Supplied, Exiting the Program...")
else:
    key = options.key

api = shodan.Shodan(key)
main()
