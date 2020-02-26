from tkinter import * 
import requests
import json
from sys import argv

def get_data(handle):
    req = requests.get("http://codeforces.com/api/user.info?handles=" + handle)
    js = json.loads(req.text)
    if js["status"] != "OK":
        return None    
    info = js["result"][0]
    handle = info["handle"] if "handle" in info else "Does not exist"
    crating = info["rating"] if "rating" in info else "Unknown"
    crank = info["rank"] if "rank" in info else "Unknown"
    mrating = info["maxRating"] if "maxRating" in info else "Unknown"
    mrank = info["maxRank"] if "maxRank" in info else "Unknown"
    return handle, crating, crank, mrating, mrank
    
def gui():
    def search():
        data = get_data(handle.get())
        handle.set("")
        if data:
            info1.config(text=data[0])
            info2.config(text=data[1])
            info3.config(text=data[2].capitalize())
            info4.config(text=data[3])
            info5.config(text=data[4].capitalize())
        else:
            info1.config(text="User not found")
            info2.config(text="")
            info3.config(text="")
            info4.config(text="")
            info5.config(text="")

    tk = Tk()
    tk.title("Codeforces Scraper")
    handle = StringVar()
    tk.geometry("500x300")
    tk.resizable(False, False)
    tk.configure(bg="grey77")

    label = Label(tk, text="Welcome to Codeforces Scraper!", bg="grey77")
    label.place(x="140",y="10")

    label1 = Label(tk, text="Enter the Username: ", bg="grey77")
    label1.place(x="20",y="70")

    box = Entry(tk, width="25",textvariable=handle)
    box.place(x="170",y="70")

    btn = Button(tk, text="Search", command=search)
    btn.place(x="390",y="68")

    label2 = Label(tk, text="Handle: ", bg="grey77")
    label2.place(x="20",y="130")

    label4 = Label(tk, text="Current rating: ", bg="grey77")
    label4.place(x="20",y="160")

    label5 = Label(tk, text="Current rank: ", bg="grey77")
    label5.place(x="20",y="190")

    label6 = Label(tk, text="Max rating: ", bg="grey77")
    label6.place(x="20",y="220")

    label7 = Label(tk, text="Max rank: ", bg="grey77")
    label7.place(x="20",y="250")

    info1 = Label(tk, text="", bg="grey77")
    info1.place(x="130",y="130")

    info2 = Label(tk, text="", bg="grey77")
    info2.place(x="130",y="160")

    info3 = Label(tk, text="", bg="grey77")
    info3.place(x="130",y="190")

    info4 = Label(tk, text="", bg="grey77")
    info4.place(x="130",y="220")

    info5 = Label(tk, text="", bg="grey77")
    info5.place(x="130",y="250")

    tk.mainloop()

def cli():
    handle = input("Enter your username: ")
    handle, crating, crank, mrating, mrank = get_data(handle)
    print()
    print("Handle: ", handle)
    print("Current Rating:",crating)
    print("Current Rank:",crank.capitalize())
    print("Max Rating:",mrating)
    print("Max Rank:",mrank.capitalize())
    

if "--gui" in argv:
    gui()

elif "--cli" in argv:
    cli()

else:
    print("Welcome to the CodeForces Scraper!\n")
    print("1. GUI")
    print("2. CLI")
    choice = input("\nEnter your Choice: ")
    if choice == "1":
        gui()
    elif choice == "2":
        cli()
    else:
        print("Invalid choice entered, exiting the program....")
        exit()

        