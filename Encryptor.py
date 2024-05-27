from cryptography.fernet import Fernet
from customtkinter import *

def encryptor(): 
    encryptWindow = CTk()
    encryptWindow.geometry("500x400")
    encryptWindow.minsize(500,400)
    encryptWindow.maxsize(500, 400)
    set_appearance_mode("dark")

    message = "Hello World!"

    key = Fernet.generate_key()


    fernet = Fernet(key)

    encMessage = fernet.encrypt(message.encode())

    print("original message: ", message)
    print("encrypted string: ", encMessage)

    decMessage = fernet.decrypt(encMessage).decode()

    print("decrypted string: ", decMessage)




    encryptWindow.title("MHS Sybersecurity Management Platform")



    encryptWindow.mainloop()
