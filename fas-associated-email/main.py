from fedora.client.fas2 import AccountSystem

def main():
	fas = AccountSystem(username='m1m3', password='#R0b0t_Fuxc')
	uname = input("Enter a vaild FAS Username: ")
	user_list = fas.people_by_key(key = u'username',search = uname, fields = ['email'])
	user = str(user_list)
	email_raw = user.find("'email': ") + 9
	email = user[email_raw:-4]
	print()
	if not email:
		print("[-] Username Not Found! Please enter a valid username")
	else:
	
		print("[+] Email Found: " + email)
while True:
    try :
        main()
        print()
        restart = input("Would you like to run the script again?(y/n): ")
        print()
        if restart.lower() != 'y':
            break

    except:
        print("An Error Occured, Try running the script again.")
        restart = input("Would you like to run the script again?(y/n): ")
        print()
        if restart.lower() != 'y':
            break
