import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from round_button import RoundedButton
import function as m


# Function to add hint text to entry fields
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


# Function to switch to the login frame
def open_login():
    signup_frame.place_forget()  # Hide signup frame
    forgot_frame.place_forget()  # Hide forgot password frame
    login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Show login frame centered

# Function to switch to the signup frame
def open_signup():
    login_frame.place_forget()  # Hide login frame
    forgot_frame.place_forget()  # Hide forgot password frame
    signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Show signup frame centered

# Function to switch to the forgot password frame
def open_forgot_password():
    login_frame.place_forget()  # Hide login frame
    signup_frame.place_forget()  # Hide signup frame
    forgot_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Show forgot password frame centered

# Initialize the root window
root = tk.Tk()
root.title("Modern Login and Sign-Up Page")
root.geometry('400x600')
root.minsize(height=600, width=400)
# root.config(bg='#34a4eb')

# Centering the frames dynamically in the window
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Call this after widgets are placed to center the window
root.after(100, lambda: center_window(root))

# ========================== LOGIN FRAME ==========================
login_frame = tk.Frame(root, width=350, height=400, bg='#ffffff', padx=30, pady=5)

# Image and Title for Login
login_im = tk.PhotoImage(file="userlogin.png")
login_ilabel = tk.Label(login_frame, image=login_im, bg='#ffffff')
login_ilabel.pack()
login_title_label = tk.Label(login_frame, text="Login", font=("Helvetica", 24, "bold"), bg='#ffffff', fg='#333')
login_title_label.pack()

# Login Entry Fields
login_e1 = tk.Entry(login_frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
login_e2 = tk.Entry(login_frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")

add_hint(login_e1, "👤 Enter your username")
add_hint(login_e2, "🔑 Enter your password", is_password=True)

def handle_login():
    m.handle_login_click(login_e1.get(),login_e2.get(),root)
# Login Button and "Forgot Password"
login_b1 = RoundedButton(login_frame,width=100, height=30, corner_radius=10,padding=4,color='lightblue', hover_color='skyblue', text="LOGIN", command=handle_login)




forgot_password_label = tk.Label(login_frame, text="Forgot Password?", font=("Helvetica", 10, "underline"), bg='#ffffff', fg='#3a86ff', cursor="hand2")
forgot_password_label.bind("<Button-1>", lambda e: open_forgot_password())
Signup_label = tk.Label(login_frame, text="Create New Account?", font=("Helvetica", 10, "underline"), bg='#ffffff', fg='#3a86ff', cursor="hand2")
Signup_label.bind("<Button-1>", lambda e: open_signup())

login_e1.pack(pady=(30, 5), ipadx=10, ipady=7)
login_e2.pack(pady=5, ipadx=10, ipady=7)
forgot_password_label.pack(pady=(10, 5))
login_b1.pack(pady=(30, 0))
Signup_label.pack(pady=(10, 5))

# ========================== SIGNUP FRAME ==========================
signup_frame = tk.Frame(root, width=350, height=450, bg='#ffffff', padx=50, pady=5)

# Image and Title for Signup
signup_im = tk.PhotoImage(file="userlogin.png")
signup_ilabel = tk.Label(signup_frame, image=signup_im, bg='#ffffff')
signup_ilabel.pack(pady=(10, 10))
signup_title_label = tk.Label(signup_frame, text="Sign Up", font=("Helvetica", 24, "bold"), bg='#ffffff', fg='#333')
signup_title_label.pack(pady=(0, 20))

# Signup Entry Fields
signup_e1 = tk.Entry(signup_frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
signup_e2 = tk.Entry(signup_frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
signup_e3 = tk.Entry(signup_frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
signup_e4 = tk.Entry(signup_frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")

add_hint(signup_e1, "👤 Enter your username")
add_hint(signup_e2, "📧 Enter your email")
add_hint(signup_e3, "🔑 Enter your password", is_password=True)
add_hint(signup_e4, "🔒 Confirm your password", is_password=True)


def handle_signup_click():
    m.handle_signup_click(signup_e1.get(),signup_e2.get(),signup_e3.get(),signup_e4.get(),root)

# Signup Button and "Already have an account?"
signup_b1 = RoundedButton(signup_frame,width=100, height=30, corner_radius=10,padding=4,color='lightblue', hover_color='skyblue', text="Sign Up", command=handle_signup_click)

Signup_label = tk.Label(signup_frame, text="Already have an Account?", font=("Helvetica", 10, "underline"), bg='#ffffff', fg='#3a86ff', cursor="hand2")
Signup_label.bind("<Button-1>", lambda e: open_login())

signup_e1.pack(pady=(25, 5), ipadx=10, ipady=7, fill=tk.X)
signup_e2.pack(pady=(15, 5), ipadx=10, ipady=7, fill=tk.X)
signup_e3.pack(pady=(15, 5), ipadx=10, ipady=7, fill=tk.X)
signup_e4.pack(pady=(15, 5), ipadx=10, ipady=7, fill=tk.X)
signup_b1.pack(pady=(30, 5),)
Signup_label.pack()

# ========================== FORGOT PASSWORD FRAME ==========================
forgot_frame = tk.Frame(root, width=350, height=400, bg='#ffffff', padx=30, pady=5)

# Title for Forgot Password
forgot_title_label = tk.Label(forgot_frame, text="Forgot Password", font=("Helvetica", 24, "bold"), bg='#ffffff', fg='#333')
forgot_title_label.pack(pady=(20, 10))

# Forgot Password Entry Fields
forgot_e1 = tk.Entry(forgot_frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
add_hint(forgot_e1, "📧 Enter your email")

def handle_forgot_password_click():
    m.handle_forgot_password_click(forgot_e1.get(),root)
# Forgot Password Button
forgot_b1 = RoundedButton(forgot_frame,width=100, height=30, corner_radius=10,padding=4,color='lightblue', hover_color='skyblue', text="Submit", command=handle_forgot_password_click)

# Back to Login button
back_to_login_label = tk.Label(forgot_frame, text="Back to Login", font=("Helvetica", 10, "underline"), bg='#ffffff', fg='#3a86ff', cursor="hand2")
back_to_login_label.bind("<Button-1>", lambda e: open_login())

forgot_e1.pack(pady=(30, 5), ipadx=10, ipady=7, fill=tk.X)
forgot_b1.pack(pady=(30, 5), )
back_to_login_label.pack(pady=(10, 5))

# Start with login frame shown
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the tkinter main loop
root.mainloop()
