import tkinter as tk
from tkinter import ttk
import sv_ttk

# Function to add hint text to entry fields
def add_hint(entry, hint):
    """Add hint text to the entry widget and manage focus events for hint visibility."""
    entry.insert(0, hint)
    entry.config(foreground='grey')

    def on_focus_in(event):
        if entry.get() == hint:
            entry.delete(0, 'end')
            entry.config(foreground='black')
           

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, hint)
            entry.config(foreground='grey')
            

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def apply_theme(theme):
    if theme == "dark":
        sv_ttk.set_theme("dark")
        bg_color = "#202123"
        fg_color = "white"
        btn_color = "#40414f"
    else:
        sv_ttk.set_theme("light")
        bg_color = "#f0f0f0"
        fg_color = "black"
        btn_color = "#d0d0d0"

    style = ttk.Style()
    style.configure("TFrame", background=bg_color)
    style.configure("TLabel", background=bg_color, foreground=fg_color)
    style.configure("TButton", background=btn_color, foreground=fg_color)
    style.configure("new.TButton", background=btn_color, foreground=fg_color)

def toggle_theme():
    global current_theme
    if current_theme == "dark":
        current_theme = "light"
        theme_btn.config(text="Switch to Dark Theme")
    else:
        current_theme = "dark"
        theme_btn.config(text="Switch to Light Theme")
    apply_theme(current_theme)

root = tk.Tk()
root.title("ChatGPT-style App")
root.geometry("1000x600")

current_theme = "light"
apply_theme(current_theme)

main_paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
main_paned.pack(fill=tk.BOTH, expand=True)

sidebar = ttk.Frame(main_paned, width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y)
main_paned.add(sidebar, weight=1)

chat_area = ttk.Frame(main_paned)
main_paned.add(chat_area, weight=4)

logo_label = ttk.Label(sidebar, text="ChatGPT", font=("Arial", 16, "bold"))
logo_label.pack(pady=10, anchor=tk.W, padx=10)

new_chat_btn = ttk.Button(sidebar, text="+ New chat",style="new.TButton")
new_chat_btn.pack(pady=5, padx=10, fill=tk.X)

history_frame = ttk.Frame(sidebar)
history_frame.pack(fill=tk.BOTH, expand=True, pady=10)
history_label = ttk.Label(history_frame, text="Today", font=("Arial", 12))
history_label.pack(anchor=tk.W, padx=10)

history_items = ["Modernize Tkinter Login Page", "Simple Login Page Python"]
for item in history_items:
    ttk.Button(history_frame, text=item, style="TButton").pack(pady=2, padx=10, fill=tk.X)

theme_btn = ttk.Button(sidebar, text="Switch to Dark Theme", command=toggle_theme)
theme_btn.pack(side=tk.BOTTOM, pady=10, padx=10, fill=tk.X)

chat_display = tk.Text(chat_area, bg="#ffffff", fg="black", wrap=tk.WORD)
chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

input_frame = ttk.Frame(chat_area)
input_frame.pack(fill=tk.X, padx=10, pady=10)

message_entry = ttk.Entry(input_frame)
add_hint(message_entry,"💬 Type your message here")
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

mic_button = ttk.Button(input_frame, text="🎤")
mic_button.pack(side=tk.LEFT, padx=5)

send_button = ttk.Button(input_frame, text="Send")
send_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()
