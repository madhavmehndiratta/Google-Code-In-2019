from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-H", '--handle', dest="handle", help="Specify a unique handle.")
    parser.add_option("-e", '--email', dest="email", help="Specify a valid mail")
    parser.add_option("-p", '--passwd', dest="passwd", help="Specify a password. Minimum 8 characters long.")
    (options, arguments) = parser.parse_args()       
    return options

def main(handle, email, passwd):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://codeforces.com/register')
    field1 = driver.find_element_by_name('handle')
    field1.send_keys(handle)
    field2 = driver.find_element_by_name('email')
    field2.send_keys(email)
    field3 = driver.find_element_by_name('password')
    field3.send_keys(passwd)
    field4 = driver.find_element_by_name('passwordConfirmation')
    field4.send_keys(passwd)
    register = driver.find_element_by_class_name('submit')
    register.click()

options = get_arguments()

if not options.handle:
    handle = input("Enter the Handle: ")
else:
    handle = options.handle
if not options.email:    
    email = input("Enter the Email: ")
else:
    email = options.email    
if not options.passwd:
    passwd = input("Enter a Password (Minimum 8 Character Long): ")
else:
    passwd = options.passwd   

main(handle, email, passwd)
