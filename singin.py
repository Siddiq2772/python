import os
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import funtion


def add_hint(entry, hint, is_password=False):
    """Add hint text to the entry widget and manage focus events for hint visibility."""
    entry.insert(0, hint)
    entry.config(fg='grey')

    def on_focus_in(event):
        if entry.get() == hint:
            entry.delete(0, 'end')
            entry.config(fg='black')
            if is_password:
                entry.config(show="*")  # Mask password if it's the password field

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, hint)
            entry.config(fg='grey')
            if is_password:
                entry.config(show="")  # Show hint text (unmasked)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Function to handle the "Forgot Password?" action
def forgot_password():
    print("Redirect to Forgot Password page...")

def handle_login_click():
    """Handle the 'Login' button click event by validating input."""
    username = e1.get()
    password = e2.get()

    # Basic input validation
    if username == "" or username == "👤 Enter your username":
        messagebox.showerror("Input Error", "Please enter a valid username.")
        return
    if password == "" or password == "🔑 Enter your password":
        messagebox.showerror("Input Error", "Please enter your password.")
        return

    # If all validations pass, show a success message and print the user info
    messagebox.showinfo("Success", "Login successful!")

    # Print user information to the console
    print(f"User Info:\nUsername: {username}\nPassword: {password}")

# Initialize the root window
root = tk.Tk()
root.title("Modern Login Page")
root.geometry('400x500')
root.minsize(height=400, width=500)
root.config(bg='#34a4eb')

# Create a Frame with a semi-transparent effect
frame = tk.Frame(root, width=350, height=350, bg='#ffffff', bd=0, relief=tk.RIDGE, padx=30, pady=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# def open_signup():
#     # subprocess.Popen(["python", "signup.py"])
#     #  os._exit(0)
#     frame.destroy()
     
# Add image to the frame
im = PhotoImage(file="userlogin.png")
ilabel = tk.Label(frame, image=im, bg='#ffffff')
ilabel.pack()

# Title Label
title_label = tk.Label(frame, text="Login", font=("Helvetica", 24, "bold"), bg='#ffffff', fg='#333')

# Create and style Labels and Entries inside the frame
e1 = tk.Entry(frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
e1.config(bg='#f5f5f5', insertbackground='#000')

e2 = tk.Entry(frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
e2.config(bg='#f5f5f5', insertbackground='#000')

# Add hint text to entry fields
add_hint(e1, "👤 Enter your username")
add_hint(e2, "🔑 Enter your password", is_password=True)

# Custom modern styled button using ttk
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10, background='#3a86ff')

# Creating separate styles for normal and hover states
style.configure('TButton.Normal.TButton', background='#3a86ff', font=('Helvetica', 15))
style.configure('TButton.Hover.TButton', background='#1e5baf', foreground='#1e5baf', font=('Helvetica', 15))

b1 = ttk.Button(frame, text="Login", style="TButton.Normal.TButton", cursor="hand2", command=handle_login_click)

# Button hover effect using styles
def on_enter(event):
    b1.config(style="TButton.Hover.TButton")

def on_leave(event):
    b1.config(style="TButton.Normal.TButton")

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

# Add "Forgot Password?" label
forgot_password_label = tk.Label(frame, text="Forgot Password?", font=("Helvetica", 10, "underline"), bg='#ffffff', fg='#3a86ff', cursor="hand2")
Signup_label = tk.Label(frame, text="Create New Account?", font=("Helvetica", 10, "underline"), bg='#ffffff', fg='#3a86ff', cursor="hand2")
Signup_label.bind("<Button-1>", lambda e: funtion.open_signup())
# Bind the click event to the forgot_password function
forgot_password_label.bind("<Button-1>", lambda e: forgot_password())

# Place the widgets in the frame with appropriate padding
title_label.pack()
e1.pack(pady=(30, 5), ipadx=10, ipady=7)
e2.pack(pady=5, ipadx=10, ipady=7)
forgot_password_label.pack(pady=(10, 5))
b1.pack(pady=(30, 0))
Signup_label.pack(pady=(10, 5))

root.mainloop()

