import tkinter as tk
from tkinter import *
import os 
from PIL import Image,ImageTk
root = tk.Tk()

image_folder="C:\\Users\\siddi\\Downloads"
file_list=os.listdir(image_folder)
image_files=[file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
list =[]
listsPhot=[]
for image in image_files:
    full_path=os.path.join(image_folder,image)
    im = ImageTk.PhotoImage(Image.open(full_path))
    l = tk.Label(root,image=(im))
    listsPhot.append(im)
    list.append(l)

for l in list:
    l.pack()

root.mainloop()
# img = Image.open("2.jpg")
# img= img.resize((600,600))
# im2 = ImageTk.PhotoImage(img)
# frame.config(highlightbackground="#e0e0e0", highlightthickness=1)
