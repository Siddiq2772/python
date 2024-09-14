# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QApplication,QMainWindow
# import sys

# app = QApplication(sys.argv)
# win = QMainWindow()
# win.setGeometry(200,300,400,500)
# win.setWindowTitle("hello world")
# win.show()

# sys.exit(app.exec())

import tkinter as tk

# Create a root window
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("440x330")
# Create a label and a button
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=root.quit)
button.pack()

# Run the application
root.mainloop()





