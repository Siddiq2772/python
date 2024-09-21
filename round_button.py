import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, corner_radius, padding, color, hover_color, text='', command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0)
        self.command = command
        self.default_color = color
        self.hover_color = hover_color

        if corner_radius > 0.5*width:
            corner_radius = 0.5*width
        if corner_radius > 0.5*height:
            corner_radius = 0.5*height

        # Create the button shape and text
        self.shape = self._draw_rounded_rect(width, height, corner_radius, color)
        self.shape_id = self.create_image(0, 0, anchor='nw', image=self.shape)
        self.text_id = self.create_text(width/2, height/2, text=text)
        
        self.configure(width=width, height=height)
        
        # Bind events for button press and hover
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def _draw_rounded_rect(self, width, height, corner_radius, fill_color):
        image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle([0, 0, width, height], corner_radius, fill=fill_color)
        return ImageTk.PhotoImage(image)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

    def _on_enter(self, event):
        # Change to hover color when mouse enters the button
        self.shape = self._draw_rounded_rect(self.winfo_width(), self.winfo_height(), 10, self.hover_color)
        self.itemconfig(self.shape_id, image=self.shape)

    def _on_leave(self, event):
        # Revert to default color when mouse leaves the button
        self.shape = self._draw_rounded_rect(self.winfo_width(), self.winfo_height(), 10, self.default_color)
        self.itemconfig(self.shape_id, image=self.shape)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    button = RoundedButton(root, width=100, height=30, corner_radius=10, 
                           padding=4, color='lightblue', hover_color='skyblue', 
                           text="Click Me!", command=lambda: print("Button Clicked!"))
    button.pack(pady=20)
    root.mainloop()
