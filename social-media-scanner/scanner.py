
import requests
import re
from bs4 import BeautifulSoup
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", '--username', dest="username", help="Specify the Username")
    (options, arguments) = parser.parse_args()
    if not options.username:
        parser.error("[-] Please Specify Username, use --help for more info.")
    return options

def twitter():
	uname = "https://twitter.com/"+str(username)
	response = requests.get(uname)
	bsoup = BeautifulSoup(response.text, 'html.parser')
	if response.status_code == 404 : 
	    print("Twitter account not found")
	else:
	    print("Twitter account found")

def instagram():
	uname = "https://instagram.com/"+str(username)
	reponse = requests.get(uname)
	bsoup = BeautifulSoup(reponse.text, 'html.parser')
	if bsoup.findAll(text = re.compile('Sorry, this page isn\'t available.')): 
	     print("Instagram account not found")
	else:
	     print("Instagram account found")

def facebook():
	uname = "https://facebook.com/"+str(username)
	response = requests.get(uname)
	bsoup = BeautifulSoup(response.text, 'html.parser')
	if response.status_code == 404 : 
	     print("Facebook account not found")
	else:
	     print("Facebook account found")

options = get_arguments()
username = options.username
twitter()
instagram()
facebook()

