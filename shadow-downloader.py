import requests
from tkinter import messagebox
import tkinter as tk
import customtkinter

def save_website_source():
    url = e1.get()  
    name = e2.get()
    file_name = name
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, "w", encoding='utf-8') as f:
                f.write(response.text)
                print(f"The source of the website has been saved in '{file_name}'.")
                messagebox.showinfo("successful", f"The source of the website has been saved in '{file_name}'.")
        else:
            print(f"Error: Failed to fetch the website. Status code: {response.status_code}")
            messagebox.showinfo("Oops!", f"Error: Failed to fetch the website. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.geometry("600x480")
app.resizable(width=False, height=False)
app.title("SHADOW-DOWNLOADER")

frame = customtkinter.CTkFrame(master=app, width=500, height=370, corner_radius=15)
frame.place(x=50, y=60)
l1 = customtkinter.CTkLabel(app, text="Website Template Downloader By --> ZELROTH", font=("Arial", 20))
l1.place(x=300, y=30, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(app, text="Created By ZELROTH", font=("Arial", 20))
l2.place(x=300, y=350, anchor=tk.CENTER)

e1 = customtkinter.CTkEntry(master=app, placeholder_text="                   Enter The Web Site URL ",width=300, border_color="#7600bc", font=("none", 20))
e1.place(x=150, y=150)

e2 = customtkinter.CTkEntry(master=app, placeholder_text="    Enter The File Name ",width=150, border_color="#7600bc", font=("none", 20))
e2.place(x=220, y=185)


button8 = customtkinter.CTkButton(master=frame, width=115, height=40, corner_radius=6, text="Download", font=("Arial", 20), text_color="white", hover_color="#4b006e", fg_color="#4c00b0", command=save_website_source)
button8.place(x=188, y=180)

app.mainloop()
