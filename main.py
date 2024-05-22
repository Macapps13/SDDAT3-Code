from customtkinter import *
from PIL import *

app = CTk()
app.geometry("500x400")
app.minsize(500,400)
app.maxsize(1000, 800)
set_appearance_mode("dark")

welcomeLabel = CTkLabel(master=app, text="Welcome to the MHS Cybersecurity Dashboard", font=("Arial", 20))
instructionLabel = CTkLabel(master=app, text="Please log in with your administor credentials", font=("Arial", 20))

welcomeLabel.place(relx=0.5, rely=0.2, anchor="center")
instructionLabel.place(relx=0.5, rely=0.3, anchor="center")

logInBtn = CTkButton(master=app, text="Log In", corner_radius=10, bg_color="#112361", hover_color="#598eb2")
logInBtn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()
