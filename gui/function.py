from tkinter import messagebox
import os

# Function to handle the "Login" button click
def handle_login_click(username,password,root):

    # Basic validation
    if username == "" or username == "👤 Enter your username":
        messagebox.showerror("Input Error", "Please enter a valid username.")
        return
    if password == "" or password == "🔑 Enter your password":
        messagebox.showerror("Input Error", "Please enter your password.")
        return

    messagebox.showinfo("Success", "Login successful!")
    print(f"Login Info:\nUsername: {username}\nPassword: {password}")
    root.destroy()
    os.system("python chatgpt.py")


# Function to handle the "Sign Up" button click
def handle_signup_click(username,email,password,confirm_password,root):


    # Basic validation
    if username == "" or username == "👤 Enter your username":
        messagebox.showerror("Input Error", "Please enter a valid username.")
        return
    if email == "" or email == "📧 Enter your email":
        messagebox.showerror("Input Error", "Please enter a valid email.")
        return
    if password == "" or password == "🔑 Enter your password":
        messagebox.showerror("Input Error", "Please enter a password.")
        return
    if confirm_password == "" or confirm_password == "🔒 Confirm your password":
        messagebox.showerror("Input Error", "Please confirm your password.")
        return
    if password != confirm_password:
        messagebox.showerror("Input Error", "Passwords do not match.")
        return

    messagebox.showinfo("Success", "You have successfully signed up!")
    print(f"Signup Info:\nUsername: {username}\nEmail: {email}\nPassword: {password}")
    root.destroy()
    os.system("python chatgpt.py")

# Function to handle forgot password submission
def handle_forgot_password_click(email,root):

    # Basic validation
    if email == "" or email == "📧 Enter your email":
        messagebox.showerror("Input Error", "Please enter your email.")
        return

    messagebox.showinfo("Success", "Password reset link has been sent to your email.")
    print(f"Forgot Password Info:\nEmail: {email}")
    root.destroy()
    os.system("python chatgpt.py")


