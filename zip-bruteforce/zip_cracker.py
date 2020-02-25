'''Programmed By m1m3'''
import zipfile
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-f", '--file', dest="zipfile", help="Specify The Zipfile")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Specify The Wordlist")

    (options, arguments) = parser.parse_args()
    if not options.zipfile:
        parser.error("[-] Please Specify a zipfile, use --help for more info.")
    elif not options.wordlist:
        parser.error("[-] Please Specify a wordlist, use --help for more info.")
    return options
options = get_arguments()
def bruteforce(zip_file, wordlist):
    	try:
		    zip_ = zipfile.ZipFile(zip_file)
        except zipfile.BadZipfile:
		    print "The filetype is not supported"
		    quit()
	password = None 
	i = 0 
	
	with open(wordlist, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			try:
				zip_.extractall(pwd=password)
				print "\n [*] Password Found :)\n" + " [*] Password: "+password+"\n" 
				quit()
			except Exception:
				pass
		print "No password found!"
		quit()
bruteforce(options.zipfile, options.wordlist)
options = get_arguments()