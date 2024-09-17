import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("ChatGPT Interface Mockup")
root.geometry("900x600")
root.configure(bg='#1e1e1e')

# Define colors and styles
sidebar_bg = "#2e2e2e"
main_bg = "#1e1e1e"
text_color = "#ffffff"
button_color = "#3e3e3e"
button_hover = "#4e4e4e"
entry_bg = "#2c2c2c"
entry_fg = "#ffffff"
entry_border_color = "#4e4e4e"

# Sidebar Frame
sidebar = tk.Frame(root, bg=sidebar_bg, width=220)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Sidebar content
header_label = tk.Label(sidebar, text="ChatGPT", font=("Arial Bold", 18), fg=text_color, bg=sidebar_bg)
header_label.pack(pady=20)

explore_label = tk.Label(sidebar, text="Explore GPTs", font=("Arial", 12), fg=text_color, bg=sidebar_bg)
explore_label.pack(pady=10)

separator = ttk.Separator(sidebar, orient='horizontal')
separator.pack(fill='x')

# List of labels (e.g., Today, Yesterday, etc.)
sections = ["Today", "Yesterday", "Previous 7 Days"]
for section in sections:
    section_label = tk.Label(sidebar, text=section, font=("Arial", 10), fg=text_color, bg=sidebar_bg)
    section_label.pack(pady=8, anchor='w', padx=15)

# Create a few dummy entries for topics
topics = ["Modernize Tkinter Login Page", "tkinter docs", "Simple Login Page Python"]
for topic in topics:
    topic_label = tk.Label(sidebar, text=topic, font=("Arial", 10), fg=text_color, bg=sidebar_bg, anchor="w")
    topic_label.pack(fill='x', padx=20, pady=3)

# Main content area
main_content = tk.Frame(root, bg=main_bg)
main_content.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Function to create a modern button
def create_modern_button(text):
    btn = tk.Button(main_content, text=text, font=("Arial", 12), fg=text_color, bg=button_color, activebackground=button_hover, bd=0, height=2, width=50)
    btn.pack(pady=15)
    return btn

# Main content labels
options = [
    "Create an image for my presentation",
    "Pick outfit to look good on camera",
    "Tell me the country with the most Olympic athletes",
    "Superhero shark story"
]

for option in options:
    create_modern_button(option)

# Hover effects for buttons
def on_enter(e):
    e.widget['background'] = button_hover

def on_leave(e):
    e.widget['background'] = button_color

# Apply hover effects to buttons
for widget in main_content.winfo_children():
    if isinstance(widget, tk.Button):
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

# Message input area
message_frame = tk.Frame(main_content, bg=main_bg)
message_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

message_entry = tk.Entry(message_frame, font=("Arial", 14), width=70, fg=entry_fg, bg=entry_bg, bd=1, relief=tk.FLAT)
message_entry.pack(side=tk.LEFT, padx=10, pady=5, ipadx=8, ipady=8)

# Add border around the Entry widget to give a modern look
entry_border = tk.Frame(message_frame, bg=entry_border_color)
entry_border.pack(side=tk.LEFT, ipadx=2, ipady=2, padx=10)
entry_border.pack_propagate(False)

# Put the entry widget inside the border
message_entry.pack(in_=entry_border, fill=tk.BOTH)

# Start the GUI loop
root.mainloop()
