#By Ben Alvaro, Started 22/05/24
#Cybersecurity Management Platform for SDD AT3

from customtkinter import *
from PIL import Image
import Keylogger
import Network
import Encryptor
import time
#Imports the appropriate libraries for GUI interface
#Also imports other files to ensure efficiency and prevent project from being too big

def openMenu():
    app.destroy()
    menu = CTk()
    menu.geometry("500x400")
    menu.maxsize(500, 400)
    menu.minsize(500,400)
    menu.mainloop()


app = CTk()
app.geometry("500x400")
app.minsize(500,400)
app.maxsize(500, 400)
set_appearance_mode("dark")
#Establishes the window, window size, and appearance


userImg_data = Image.open("user.png")
passwordImg_data = Image.open("password.png")
userImg = CTkImage(dark_image=userImg_data)
passwordImg = CTkImage(dark_image=passwordImg_data)

usernameLabel = CTkLabel(master=app, text="  Username:", anchor="w", justify="left", font=("Arial Bold", 14), image=userImg, compound="left")
usernameLabel.place(relx=0.275, rely= 0.32, anchor="w")
usernameEntry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#598eb2", border_width=1, text_color="#000000")
usernameEntry.place(relx=0.5, rely=0.4, anchor="center")


passwordLabel = CTkLabel(master=app, text="  Password:", anchor="w", justify="left", font=("Arial Bold", 14), image=passwordImg, compound="left")
passwordLabel.place(relx=0.275, rely= 0.52, anchor="w")
passwordEntry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#598eb2", border_width=1, text_color="#000000", show="*")
passwordEntry.place(relx=0.5, rely=0.6, anchor="center")

unsuccessfulLogInMessage = CTkLabel(master=app, text=" ", text_color="#EE4B2B", anchor="center", font=("ArialBold", 12))
unsuccessfulLogInMessage.place(relx=0.5, rely=0.9, anchor="center")

def logInPressed():
    enteredUsername = usernameEntry.get()
    enteredPword = passwordEntry.get()
    print("enteredUsername = " + enteredUsername + "\nenteredPword = " + enteredPword)
    if enteredUsername == "admin" and enteredPword == "Merewether2024":
        openMenu()
    else:
        print("Unsuccessful")
        unsuccessfulLogInMessage.configure(text="Unsuccessful Login Attempt, Please Try Again")
        app.update_idletasks()
        app.after(5000, unsuccessfulLogInMessage.configure(text=" "))
        
        



welcomeLabel = CTkLabel(master=app, text="Welcome to the MHS Cybersecurity Dashboard", font=("Calibri", 20))
instructionLabel = CTkLabel(master=app, text="Please log in with your administor credentials", font=("Calibri", 20))
#Creates labels for welcome message and assigns properties

welcomeLabel.place(relx=0.5, rely=0.1, anchor="center")
instructionLabel.place(relx=0.5, rely=0.2, anchor="center")
#Places the labels in the middle horizontally, and slightly up

logInBtn = CTkButton(master=app, text="Log In", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=logInPressed)
logInBtn.place(relx=0.5, rely=0.8, anchor="center")
#Creates and places the login button


def on_closing():
    print("Exited with code 0")
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
#Opens the window