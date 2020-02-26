import requests
from bs4 import BeautifulSoup as bs4

def main():
    key = input("Enter an indivisual's name or e-mail address : ")

    link = "https://viewdns.info/reversewhois/?q=" + key

    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
    headers = {"User-Agent": user_agent}
    req = requests.get(link, headers=headers)

    table = bs4(req.content, "html5lib")
    table = table.findAll('table')[3].encode()

    tr = bs4(table, "html5lib")
    rows = tr.findAll('tr')

    try:
        for element in rows:
            element = str(element)
            value = element[element.index("<td>") + 4: element.index("</td>")]
            if value == "Domain Name":
                print()
                print("[+] Domain names owned by " + key + " are: ")
                print()

            else:
                print(value)

    except:
        print()
        print("[-] " + key + " doesn't have any registered domain names")


while True:
    try :
        main()
        print()
        restart = input("Would you like to run the script again?(y/n): ")
        print()
        if restart.lower() != 'y':
            break

    except:
        print('An Error Occured... Try running the script again')
        restart = input("Would you like to run the script again?(y/n): ")
        print()
        if restart.lower() != 'y':
            break
