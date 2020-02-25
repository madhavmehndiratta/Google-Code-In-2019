from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", '--url', dest="url", help="Specify the URL")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Please Specify a URL, use --help for more info.")
    return options

def read_url(url):
    url = url.replace(" ","%20")
    requests = Request(url)
    a = urlopen(requests).read()
    soup = BeautifulSoup(a, 'html.parser')
    element = (soup.find_all('a'))
    for i in element:
        file_name = i.extract().get_text()
        url_new = url + file_name
        url_new = url_new.replace(" ","%20")
        if(file_name[-1]=='/' and file_name[0]!='.'):
            read_url(url_new)
        print(url_new)

options = get_arguments()
read_url(options.url)