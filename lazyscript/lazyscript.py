from tkinter import *
import tkinter.messagebox
import subprocess
tk = Tk()
tk.resizable(False, False)
tk.title("The Lazy Script")

gci = Button(tk, text="Google Code In", font='Arial', bg='white', fg='black', command=lambda: gci())
gci.grid(row=0, column=0)

irc = Button(tk, text="Connect to IRC", font='Arial', bg='white', fg='black', command=lambda: irc())
irc.grid(row=0, column=1)

play_music = Button(tk, text="Play Music", font='Arial', bg='white', fg='black', command=lambda: play_music())
play_music.grid(row=0, column=2)


def gci():
    subprocess.call(["firefox", "https://codein.withgoogle.com/dashboard/"])

def irc():
    subprocess.call(["irssi"])

def play_music():
    subprocess.call(["rhythmbox", "/home/m1m3/Music/fav-music.mp3"])

    
tk.mainloop()
  
