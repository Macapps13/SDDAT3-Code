#By Ben Alvaro, Started 22/05/24
#Cybersecurity Management Platform for SDD AT3

from customtkinter import *
from PIL import Image
from Keylogger import keylogger
import Network
import Encryptor
import time
import threading
from tkinter import messagebox as msg
import sys

#Imports the appropriate libraries for GUI interface
#Also imports other files to ensure efficiency and prevent project from being too big

threadK = threading.Thread(target=keylogger,args=[1])

def keylogging():
    response = msg.askyesnocancel("Confirm Keylogger", "Are you sure you want to begin keylogger?")
    if response is None:
        # User clicked "Cancel"
        return
    elif response:
        threadK.start()
        return

def on_closing():
    response = msg.askyesnocancel("Confirm Exit", "Are you sure you want to exit?")
    if response is None:
        # User clicked "Cancel"
        return
    elif response:
    # Close the application
        print("Exited with code 0")
        global currentWindow
        currentWindow.withdraw()
        os._exit(0)

def openMenu():
    app.withdraw()
    app.quit()
    global currentWindow
    menu = CTk()
    currentWindow = menu 
    menu.geometry("500x400")
    menu.maxsize(500, 400)
    menu.minsize(500,400)
    menu.title("MHS Sybersecurity Management Platform")

    instructionLabel = CTkLabel(master=menu, text="Please select your desired operation", 
                        font=("Calibri", 20))
    instructionLabel.place(relx=0.5, rely=0.15, anchor="center")
   
    keyLogBtn = CTkButton(master=menu, text="Keylogger", corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=250, font=("ArialBold", 16), command=keylogging)
    encryptBtn = CTkButton(master=menu, text="Encryption", corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=250, font=("ArialBold", 16))
    networkBtn = CTkButton(master=menu, text="Network Surveillance", corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=250, font=("ArialBold", 16))
    
    keyLogBtn.place(relx=0.5, rely=0.3, anchor="center")
    encryptBtn.place(relx=0.5, rely=0.45, anchor="center")
    networkBtn.place(relx=0.5, rely=0.6, anchor="center")

    quitBtn = CTkButton(master=menu, text="Exit", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=on_closing)
    quitBtn.place(relx=0.5, rely=0.85, anchor="center")


    menu.protocol("WM_DELETE_WINDOW", on_closing)
    menu.mainloop()




app = CTk()
global currentWindow
currentWindow = app
app.geometry("500x400")
app.minsize(500,400)
app.maxsize(500, 400)
set_appearance_mode("dark")
#Establishes the window, window size, and appearance


userImg_data = Image.open("user.png")
passwordImg_data = Image.open("password.png")
userImg = CTkImage(dark_image=userImg_data)
passwordImg = CTkImage(dark_image=passwordImg_data)

usernameLabel = CTkLabel(master=app, text="  Username:", anchor="w", justify="left", font=("Arial Bold", 14), 
                         image=userImg, compound="left")
usernameLabel.place(relx=0.275, rely= 0.32, anchor="w")
usernameEntry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", 
                         border_color="#598eb2", border_width=1, text_color="#000000")
usernameEntry.place(relx=0.5, rely=0.4, anchor="center")


passwordLabel = CTkLabel(master=app, text="  Password:", anchor="w", justify="left", 
                         font=("Arial Bold", 14), image=passwordImg, compound="left")
passwordLabel.place(relx=0.275, rely= 0.52, anchor="w")
passwordEntry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#598eb2", 
                         border_width=1, text_color="#000000", show="*")
passwordEntry.place(relx=0.5, rely=0.6, anchor="center")

unsuccessfulLogInMessage = CTkLabel(master=app, text=" ", text_color="#EE4B2B", 
                                    anchor="center", font=("ArialBold", 12))
unsuccessfulLogInMessage.place(relx=0.5, rely=0.7, anchor="center")

def logInPressed(event=None):
    enteredUsername = usernameEntry.get()
    enteredPword = passwordEntry.get()
    print("enteredUsername = " + enteredUsername + "\nenteredPword = " + enteredPword)
    if enteredUsername != "admin" or enteredPword != "Merewether2024":
        print("Unsuccessful")
        unsuccessfulLogInMessage.configure(text="Unsuccessful Login Attempt, Please Try Again")
        app.update_idletasks()
    else:
        openMenu()

        
        



welcomeLabel = CTkLabel(master=app, text="Welcome to the MHS Cybersecurity Dashboard", 
                        font=("Calibri", 20))
instructionLabel = CTkLabel(master=app, text="Please log in with your administor credentials", 
                            font=("Calibri", 20))
#Creates labels for welcome message and assigns properties

welcomeLabel.place(relx=0.5, rely=0.1, anchor="center")
instructionLabel.place(relx=0.5, rely=0.2, anchor="center")
#Places the labels in the middle horizontally, and slightly up

logInBtn = CTkButton(master=app, text="Log In", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=logInPressed)
logInBtn.place(relx=0.3, rely=0.85, anchor="center")
#Creates and places the login button

quitBtn = CTkButton(master=app, text="Exit", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=on_closing)
quitBtn.place(relx=0.7, rely=0.85, anchor="center")


app.protocol("WM_DELETE_WINDOW", on_closing)

app.bind('<Return>',logInPressed)

app.title("MHS Sybersecurity Management Platform")
app.mainloop()
#Opens the window