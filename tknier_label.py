import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
root = tk.Tk()
root.title("label")
root.geometry("440x440")
label = tk.Label(root, text="hello world")
label.pack()

# im = PhotoImage(file="1.png")
img = Image.open("2.jpg")
im = ImageTk.PhotoImage(img)
l2 = tk.Label(root,image=im)
l2.pack()


root.mainloop()