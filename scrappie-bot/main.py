from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
from getpass import getpass

print()
print("Welcome, my name is Scrappie, I can tweet the latest article from Fedora Magazine for you!")
print()
print("For this, you need to login here with you twitter account. Just wait for a mintue....")
print()

url = "https://fedoramagazine.org/"

user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
headers = {'User-Agent': user_agent}
req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.content, 'html5lib')
links = soup.find_all("a")

opts = Options()
opts.set_headless()
assert opts.headless
browser = Firefox(options=opts)
browser.get('https://twitter.com/login')

login = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
login.send_keys(input("Twitter ID/e-mail address: "))

passwd = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
passwd.send_keys(getpass("Twitter Password :"))

browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()

time.sleep(5)

tweet_box = browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')
str = str(links[8])

tweet_box.send_keys(str[str.index('href="')+6 : str.index('/"')])

ActionChains(browser) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.ENTER) \
    .perform()

print()
print("Fetching The latest article...")
print("[+] The Tweet has been posted Successfully!")
