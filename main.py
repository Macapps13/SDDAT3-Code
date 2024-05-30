#By Ben Alvaro, Started 22/05/24
#Cybersecurity Management Platform for SDD AT3

from customtkinter import *
from PIL import Image
import Keylogger
import Network
from Encryptor import encryptor
import multiprocessing
from tkinter import messagebox as msg
import os
import time
import threading
from cryptography.fernet import Fernet
from googletrans import Translator

translator = Translator()

#Imports the appropriate libraries for GUI interface
#Also imports other files to ensure efficiency and prevent project from being too big

key = Fernet.generate_key()
fernet = Fernet(key)

global selectedLang


keyLogLabelText = "Keylogger is running..."
keyLogLengthErrorLabelText = "Error: Length Provided was not a valid input (Must be a whole number)"
keyLogLengthLabelText = "How long in minutes should the keylogger run for?"
keyLogLengthBtnText = "Submit"
responseText = "Are you sure you want to exit?"
welcomeLabel2Text = "Cybersecurity Dashboard"
instructionLabelText = "Please select your desired operation"
quitBtnText = "Exit"
unsuccessfulLogInMessageText = "Unsuccessful Login Attempt, Please Try Again"
logInBtnText = "Log In"
keyLogBtnText =  "Keylogger"
networkBtnText =  "Network Surveillance"
encryptBtnText = "Encryption"
welcomeLabelText = "Welcome to the MHS Cybersecurity Dashboard"

global outputs
global ogOutputs

ogOutputs = [keyLogLabelText, keyLogLengthErrorLabelText, keyLogLengthLabelText, keyLogLengthBtnText, responseText, 
           welcomeLabel2Text, instructionLabelText, quitBtnText, unsuccessfulLogInMessageText, logInBtnText, keyLogBtnText,
           networkBtnText, encryptBtnText, welcomeLabelText]

outputs = [keyLogLabelText, keyLogLengthErrorLabelText, keyLogLengthLabelText, keyLogLengthBtnText, responseText, 
           welcomeLabel2Text, instructionLabelText, quitBtnText, unsuccessfulLogInMessageText, logInBtnText, keyLogBtnText,
           networkBtnText, encryptBtnText, welcomeLabelText]


def changeLanguage(event=None):
    global outputs
    global selectedLang
    selectedLang = languageSelector.get()
    print("Language changed to " + selectedLang)
    app.withdraw()
    if selectedLang == "French":
        frTranslations = [translator.translate(o, dest='fr').text for o in ogOutputs]
        outputs = frTranslations
    elif selectedLang == "Italian":
        itTranslations = [translator.translate(o, dest='it').text for o in ogOutputs]
        outputs = itTranslations 
    elif selectedLang == "Spanish":
        esTranslations = [translator.translate(o, dest='es').text for o in ogOutputs]
        outputs = esTranslations
    elif selectedLang == "Japanese":
        jpTranslations = [translator.translate(o, dest='ja').text for o in ogOutputs]
        outputs = jpTranslations
    elif selectedLang == "Arabic":
        arTranslations = [translator.translate(o, dest='ar').text for o in ogOutputs]
        outputs = arTranslations
    elif selectedLang == "Hebrew":
        heTranslations = [translator.translate(o, dest='he').text for o in ogOutputs]
        outputs = heTranslations
    elif selectedLang == "Punjabi":
        paTranslations = [translator.translate(o, dest='pa').text for o in ogOutputs]
        outputs = paTranslations
    elif selectedLang == "Chinese":
        cnTranslations = [translator.translate(o, dest='zh-cn').text for o in ogOutputs]
        outputs = cnTranslations
    elif selectedLang == "English":
        outputs = ogOutputs

    print(outputs)
    quitBtn.configure(text=outputs[7])
    logInBtn.configure(text=outputs[9])
    welcomeLabel.configure(text=outputs[13])
    app.update()
    app.deiconify()
    return

def place():
    keyLogBtn.place()
    networkBtn.place()
    quitBtn.place()
    encryptBtn.place()
    instructionLabel.place()
    keyLogLabel.place_forget()
 


def keylogging():
    welcomeLabel2.place_forget()
    keyLogBtn.place_forget()
    networkBtn.place_forget()
    encryptBtn.place_forget()
    instructionLabel.place_forget()
    quitBtn.place_forget()
    menu.update()

    keyLogLengthErrorLabel = CTkLabel(master=menu, text="", text_color="#EE4B2B", 
                                anchor="center", font=("ArialBold", 12))
    keyLogLengthErrorLabel.place(relx=0.5, rely=0.8, anchor="center")

    def runKeylog():
        keyLogLength = keyLogLengthEntry.get()
        try: 
            keyLogLengthS = int(round(float(keyLogLength)*60))
            if keyLogLengthS <=0:
                raise Exception
            keyLogLengthBtn.place_forget()
            keyLogLengthEntry.place_forget()
            keyLogLengthLabel.place_forget()
            keyLogLengthErrorLabel.place_forget()
            global keyLogLabel
            keyLogLabel = CTkLabel(master=menu, text=outputs[0], font=("Calibri", 20))
            keyLogLabel.place(relx=0.5, rely=0.5, anchor="center")
            menu.update()
    
            Keylogger.start_keylogger(keyLogLengthS)
            time.sleep(keyLogLengthS)

            menu.deiconify()
            quitBtn.place(relx=0.5, rely=0.85, anchor="center")
            keyLogBtn.place(relx=0.5, rely=0.3, anchor="center")
            encryptBtn.place(relx=0.5, rely=0.45, anchor="center")
            networkBtn.place(relx=0.5, rely=0.6, anchor="center")
            instructionLabel.place(relx=0.5, rely=0.15, anchor="center")
            welcomeLabel.place(relx=0.5, rely=0.1, anchor="center")
            keyLogLabel.place_forget()
            

            menu.update()
            return
        except:
            keyLogLengthErrorLabel.configure(text=outputs[1])
            keyLogLengthEntry.delete("0", "end")
            menu.update()
            return

        
        
        


    keyLogLengthLabel = CTkLabel(master=menu, text=outputs[2], wraplength=350, font=("Calibri", 20))
    keyLogLengthLabel.place(relx=0.5, rely=0.2, anchor="center")
    keyLogLengthEntry = CTkEntry(master=menu, width=50, fg_color="#EEEEEE", border_color="#598eb2", 
                        border_width=1, text_color="#000000")
    keyLogLengthEntry.place(relx=0.5, rely=0.4, anchor="center")
    keyLogLengthBtn = CTkButton(master=menu, text=outputs[3], corner_radius=10, fg_color="transparent", 
                    hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=runKeylog)
    keyLogLengthBtn.place(relx=0.5, rely=0.6, anchor="center")


def encrypt():
    currentWindow.withdraw()
    try: 
        encryptor(fernet, selectedLang)
    except:
        encryptor(fernet, "English")
    currentWindow.deiconify()
        

def on_closing():
    response = msg.askyesnocancel("Confirm Exit", str(outputs[4]))
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
    global menu
    menu = CTk()
    currentWindow = menu 
    menu.maxsize(500, 400)
    menu.minsize(500,400)
    w = 500
    h = 400
    x = (ws/2)
    y = (hs/2)

    menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
    menu.title("MHS Sybersecurity Management Platform")

    global welcomeLabel2

    welcomeLabel2 = CTkLabel(master=menu, text="MHS " + outputs[5], 
                        font=("Calibri", 20))
    welcomeLabel2.place(relx=0.5, rely=0.1, anchor="center")

    global instructionLabel

    instructionLabel = CTkLabel(master=menu, text=outputs[6], 
                        font=("Calibri", 20))
    instructionLabel.place(relx=0.5, rely=0.20, anchor="center")

    global keyLogBtn, encryptBtn, networkBtn

    keyLogBtn = CTkButton(master=menu, text=outputs[10], corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=250, font=("ArialBold", 16), command = keylogging)

    encryptBtn = CTkButton(master=menu, text=outputs[12], corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=250, font=("ArialBold", 16), command = encrypt)

    networkBtn = CTkButton(master=menu, text=outputs[11], corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=250, font=("ArialBold", 16))
    
    keyLogBtn.place(relx=0.5, rely=0.35, anchor="center")
    encryptBtn.place(relx=0.5, rely=0.5, anchor="center")
    networkBtn.place(relx=0.5, rely=0.65, anchor="center")

    global quitBtn

    quitBtn = CTkButton(master=menu, text=outputs[7], corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=on_closing)
    quitBtn.place(relx=0.5, rely=0.85, anchor="center")


    menu.protocol("WM_DELETE_WINDOW", on_closing)
    menu.mainloop()





   


print("Lisenced by Ben Alvaro, 2024")
print("Program Starting...")
app = CTk()
global currentWindow
currentWindow = app
app.minsize(500,400)
app.maxsize(500, 400)
set_appearance_mode("dark")
hs = app.winfo_screenheight()
ws = app.winfo_screenwidth()
print("Window Width: " + str(ws))
print("WIndow Height: " + str(hs))
w = 500
h = 400
x = (ws/2)
y = (hs/2)

app.geometry('%dx%d+%d+%d' % (w, h, x, y))
#Establishes the window, window size, and appearance


userImg_data = Image.open("user.png")
passwordImg_data = Image.open("password.png")
userImg = CTkImage(dark_image=userImg_data)
passwordImg = CTkImage(dark_image=passwordImg_data)

usernameLabel = CTkLabel(master=app, text="  Username:", anchor="w", justify="left", font=("Arial Bold", 14), 
                         image=userImg, compound="left")
usernameLabel.place(relx=0.275, rely= 0.25, anchor="w")
usernameEntry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", 
                         border_color="#598eb2", border_width=1, text_color="#000000")
usernameEntry.place(relx=0.5, rely=0.33, anchor="center")


passwordLabel = CTkLabel(master=app, text="  Password:", anchor="w", justify="left", 
                         font=("Arial Bold", 14), image=passwordImg, compound="left")
passwordLabel.place(relx=0.275, rely= 0.45, anchor="w")
passwordEntry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#598eb2", 
                         border_width=1, text_color="#000000", show="*")
passwordEntry.place(relx=0.5, rely=0.53, anchor="center")

unsuccessfulLogInMessage = CTkLabel(master=app, text=" ", text_color="#EE4B2B", 
                                    anchor="center", font=("ArialBold", 12))
unsuccessfulLogInMessage.place(relx=0.5, rely=0.95, anchor="center")

def logInPressed(event=None):
    enteredUsername = usernameEntry.get()
    enteredPword = passwordEntry.get()
    print("enteredUsername = " + enteredUsername + "\nenteredPword = " + enteredPword)
    if enteredUsername != "admin" or enteredPword != "Merewether2024":
        print("Unsuccessful")
        unsuccessfulLogInMessage.configure(text=outputs[8])
        app.update_idletasks()
    else:
        openMenu()

        
        



welcomeLabel = CTkLabel(master=app, text=outputs[13], 
                        font=("Calibri", 20))

#Creates labels for welcome message and assigns properties

welcomeLabel.place(relx=0.5, rely=0.1, anchor="center")
#Places the labels in the middle horizontally, and slightly up

global languageSelector



languageLabel = CTkLabel(master=app, text="Language:")
languageLabel.place(relx=0.35, rely=0.73, anchor="center")
languageSelector = CTkComboBox(master=app, 
                               values=["English", "French", "Italian", 
                                       "Spanish", "Japanese", "Chinese", 
                                        "Hebrew","Arabic", "Punjabi"], state="readonly", command=changeLanguage)
languageSelector.set("English")
languageSelector.place(relx=0.6, rely=0.73, anchor="center")

logInBtn = CTkButton(master=app, text=outputs[9], corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=logInPressed)
logInBtn.place(relx=0.3, rely=0.85, anchor="center")
#Creates and places the login button

quitBtn = CTkButton(master=app, text=outputs[7], corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=on_closing)
quitBtn.place(relx=0.7, rely=0.85, anchor="center")


app.protocol("WM_DELETE_WINDOW", on_closing)

app.bind('<Return>',logInPressed)

app.title("MHS Sybersecurity Management Platform")
app.mainloop()
#Opens the window