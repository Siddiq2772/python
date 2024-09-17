import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def add_hint(entry, hint, is_password=False):
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

# Initialize the root window
root = tk.Tk()
root.title("Modern Login Page")
root.geometry('400x500')
root.minsize(height=400,width=500)

# Make the window semi-transparent
root.attributes("-alpha", 0.9)  # Adjust the value between 0.0 and 1.0
# img = Image.open("2.jpg")
# img= img.resize((600,600))
# im2 = ImageTk.PhotoImage(img)

# Create a Canvas with transparency
canvas = tk.Canvas(root, bg='white', highlightthickness=0,width=400, height=500)
canvas.place(relwidth=1, relheight=1)  # Make the canvas cover the entire window
# canvas.create_image(0,0, image=im2, anchor=NW)

# Create a Frame with a semi-transparent effect
frame = tk.Frame(canvas, width=350, height=350, bg='#ffffff', bd=0, relief=tk.RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add a modern border (simulated shadow effect)
# frame.config(highlightbackground="#e0e0e0", highlightthickness=1)

im = PhotoImage(file="userlogin.png")
ilabel = tk.Label(frame,image=im,bg='#ffffff')
ilabel.pack()
# Title Label
title_label = tk.Label(frame, text="Login", font=("Helvetica", 24, "bold"), bg='#ffffff', fg='#333')
title_label.pack()

# Create and style Labels and Entries inside the frame
l1 = tk.Label(frame, text="Username", font=('Helvetica', 12), bg='#ffffff', fg='#555')
e1 = tk.Entry(frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
e1.config(bg='#f5f5f5', insertbackground='#000')

l2 = tk.Label(frame, text="Password", font=('Helvetica', 12), bg='#ffffff', fg='#555')
e2 = tk.Entry(frame, font=('Helvetica', 12), bd=0, relief=tk.FLAT, highlightbackground="#dddddd", highlightthickness=1, highlightcolor="#3a86ff")
e2.config(bg='#f5f5f5', insertbackground='#000')

# Add hint text to entry fields
add_hint(e1, "👤 Enter your username")
add_hint(e2, "🔑 Enter your password", is_password=True)

# Custom modern styled button using ttk
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10, background='#3a86ff', )

# Creating separate styles for normal and hover states
style.configure('TButton.Normal.TButton', background='#3a86ff',font=('Helvetica', 15) )
style.configure('TButton.Hover.TButton', background='#1e5baf', foreground='#1e5baf',font=('Helvetica', 15))

b1 = ttk.Button(frame, text="Login", style="TButton.Normal.TButton", cursor="hand2",)

# Button hover effect using styles
def on_enter(event):
    b1.config(style="TButton.Hover.TButton")

def on_leave(event):
    b1.config(style="TButton.Normal.TButton")

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

# Place the widgets in the frame with appropriate padding
l1.pack(pady=(20, 5))
e1.pack(pady=5, ipadx=10, ipady=7, fill=tk.X)
l2.pack(pady=(20, 5))
e2.pack(pady=5, ipadx=10, ipady=7, fill=tk.X)
b1.pack(pady=30, fill=tk.X)

root.mainloop()