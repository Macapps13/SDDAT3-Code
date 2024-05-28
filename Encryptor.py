from cryptography.fernet import Fernet
from customtkinter import *
from tkinter import messagebox as msg
from PIL import Image

key = Fernet.generate_key()


fernet = Fernet(key)

def back2():
        return


def encryptor(fernet): 
    quit = 0
    encryptWindow = CTk()
    encryptWindow.geometry("500x400")
    encryptWindow.minsize(500,400)
    encryptWindow.maxsize(500, 400)
    set_appearance_mode("dark")
    

    def back():
            encryptWindow.withdraw()
            encryptWindow.quit()
            return

    def on_closing():
        response = msg.askyesnocancel("Confirm Exit", "Are you sure you want to exit?")
        if response is None:
        # User clicked "Cancel"
            return
    
        elif response:
            print("Exited with code 0")
            os._exit(0)

    quitBtn = CTkButton(master=encryptWindow, text="Exit", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=on_closing)
    

    def copy(msg):
        encryptWindow.clipboard_clear()
        encryptWindow.clipboard_append(msg)
        encryptWindow.update()
    
    copyBtn = CTkButton(master=encryptWindow, text="Copy To Clipboard", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=copy)
    

    def decrypt():

        

        def decryptText():
            enteredMsg = decryptEntry.get()
            decryptTextbox.configure(state="normal")
            decryptTextbox.delete("0.0", "end")
            try:
                decryptedMsg = fernet.decrypt(enteredMsg).decode() 
                decryptTextbox.insert("0.0", decryptedMsg)
                decryptTextbox.configure(state="disabled")
            except:
                 decryptTextbox.insert("0.0", "Error: Message uses invalid key")
            encryptWindow.update()
        
        def goCopy():
            msg = decryptTextbox.get("0.0", "end")
            back(msg)


        backBtn = CTkButton(master=encryptWindow, text="Back", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=back)
        copyBtn = CTkButton(master=encryptWindow, text="Copy To Clipboard", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=goCopy)
        copyBtn.place(relx=0.5, rely=0.85, anchor="center")
        backBtn.place(relx=0.3, rely=0.95, anchor="center")
        quitBtn.place(relx=0.7, rely=0.95, anchor="center")
        backBtn2.place_forget()
        titleLabel.place_forget()
        encryptorBtn.place_forget()
        decryptorBtn.place_forget()
        decryptMsg = CTkLabel(master=encryptWindow, text="Enter your message to be decrypted", font=("Arial Bold", 20))
        decryptMsg.place(relx=0.5, rely=0.10, anchor="center")
        decryptEntry = CTkEntry(master=encryptWindow, width=300, fg_color="#EEEEEE", border_color="#598eb2", 
                         border_width=1, text_color="#000000")
        decryptEntry.place(relx=0.5, rely=0.25, anchor="center")
        decryptMsg2 = CTkLabel(master=encryptWindow, text="Decrypted Message:", font=("Arial Bold", 20))
        decryptMsg2.place(relx=0.5, rely=0.55, anchor="center")
        decryptBtn = CTkButton(master=encryptWindow, text="Decrypt", corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=150, font=("ArialBold", 16), command=decryptText)
        decryptBtn.place(relx=0.5, rely=0.4, anchor="center")

        decryptTextbox = CTkTextbox(master=encryptWindow, corner_radius=5, width=350, height=50, text_color="#FFFFFF")
        decryptTextbox.place(relx=0.5, rely=0.7, anchor="center")
        decryptTextbox.configure(state="disabled")
        encryptWindow.update()


    def encrypt():

        

        def encryptText():
            enteredMsg = encryptEntry.get()
            encryptTextbox.configure(state="normal")
            encryptTextbox.delete("0.0", "end")
            encryptedMsg = fernet.encrypt(enteredMsg.encode())  
            encryptTextbox.insert("0.0", encryptedMsg)
            encryptTextbox.configure(state="disabled")
            encryptWindow.update()

        def goCopy():
            msg = encryptTextbox.get("0.0", "end")
            copy(msg)


        backBtn = CTkButton(master=encryptWindow, text="Back", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=back)
        copyBtn = CTkButton(master=encryptWindow, text="Copy To Clipboard", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=goCopy)
        backBtn.place(relx=0.3, rely=0.9, anchor="center")
        quitBtn.place(relx=0.7, rely=0.9, anchor="center")
        copyBtn.place(relx=0.5, rely=0.8, anchor="center")
        backBtn2.place_forget()
        titleLabel.place_forget()
        encryptorBtn.place_forget()
        decryptorBtn.place_forget()
        encryptMsg = CTkLabel(master=encryptWindow, text="Enter your message to be encrypted", font=("Arial Bold", 20))
        encryptMsg.place(relx=0.5, rely=0.10, anchor="center")
        encryptEntry = CTkEntry(master=encryptWindow, width=300, fg_color="#EEEEEE", border_color="#598eb2", 
                         border_width=1, text_color="#000000")
        encryptEntry.place(relx=0.5, rely=0.25, anchor="center")
        encryptMsg2 = CTkLabel(master=encryptWindow, text="Encrypted Message:", font=("Arial Bold", 20))
        encryptMsg2.place(relx=0.5, rely=0.55, anchor="center")
        encryptBtn = CTkButton(master=encryptWindow, text="Encrypt", corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=150, font=("ArialBold", 16), command=encryptText)
        encryptBtn.place(relx=0.5, rely=0.4, anchor="center")

        encryptTextbox = CTkTextbox(master=encryptWindow, corner_radius=5, width=350, height=50, text_color="#FFFFFF")
        encryptTextbox.place(relx=0.5, rely=0.7, anchor="center")
        encryptTextbox.configure(state="disabled")
        encryptWindow.update()


    titleLabel = CTkLabel(master=encryptWindow, text="Encryptor", 
                        font=("Calibri", 35))
    titleLabel.place(relx=0.5, rely=0.15, anchor="center")

    decryptorBtn = CTkButton(master=encryptWindow, text="Decrypt", corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=150, font=("ArialBold", 16), command=decrypt)

    encryptorBtn = CTkButton(master=encryptWindow, text="Encrypt", corner_radius=10, fg_color="#FFFFFF", hover_color="#598eb2"
                          , border_color="#FFFFFF", border_width=2, text_color="#000000", width=150, font=("ArialBold", 16), command=encrypt)
    
    decryptorBtn.place(relx = 0.7, rely=0.5, anchor="center")

    encryptorBtn.place(relx=0.3, rely=0.5, anchor="center")

    def back2():
         encryptWindow.withdraw()
         encryptWindow.quit()
         print("123")
         global quit
         quit = 1
         return quit   

    backBtn2 = CTkButton(master=encryptWindow, text="Back", corner_radius=10, fg_color="transparent", 
                     hover_color="#598eb2", border_color="#FFFFFF", border_width=2, command=back2)
    
    backBtn2.place(relx=0.3, rely=0.85, anchor="center")
    
    quitBtn.place(relx=0.7, rely=0.85, anchor="center")


    encryptWindow.title("MHS Sybersecurity Management Platform")

    encryptWindow.protocol("WM_DELETE_WINDOW", on_closing)

    encryptWindow.mainloop()


