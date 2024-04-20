#from source import *
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

class Window(tk.Tk):


    def __init__(self, w, h, padding):
        super().__init__()

        self.width = w
        self.height = h
        self.padding = padding
        self.title("Chest-X-Ray Predictor")
        self.geometry(f"{w}x{h}")

        self.image_label = tk.Label(self, text = "There isn't a loaded image")
        self.image_label.pack(pady = 20)

        self.load_button = tk.Button(self, text = "Load image", command = self.load_image)
        self.load_button.pack(pady = 10)


    def load_image(self):
        filetypes = (
            ("Images", "*.png"),
            ("Images", "*.jpg"),
            ("Images", "*.jpeg"),
        )
        file_path = filedialog.askopenfilename(
            filetypes = filetypes
        )
        showinfo(
            title = "Selected File",
            message = file_path
        )

        if file_path:
            image = Image.open(file_path)

            # Obtaining and calculating new dimentions
            w, h = image.size
            fixed_width = 400

            # calculating new image dimentions
            if w > fixed_width:
                ratio = w / fixed_width
                w = fixed_width
                h = int(h / ratio)
                image = image.resize((w, h))

            photo = ImageTk.PhotoImage(image)

            # resizing
            self.geometry(f"{w + self.padding}x{h + self.height + self.padding}")

            # putting image
            self.image_label.config(image = photo)
            self.image_label.image = photo
            self.image_label.pack()
            

if __name__ == "__main__":
    app = Window(w = 400, h = 100, padding = 20)
    app.mainloop()
