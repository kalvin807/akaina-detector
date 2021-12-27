import os
import tkinter as tk
from pathlib import Path
from random import choice

from PIL import Image, ImageTk


def random_unlabeled_img():
    path = Path("datasets/cropped")
    random_path = list(path.iterdir())[0]
    return random_path


def must_folder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)


def write_labeled(label, isTrue, image):
    postfix = "yes" if isTrue else "no"
    image.save(f"datasets/labeled/{label}_{postfix}.png")


def remove_file(path):
    os.remove(path)


class App:
    def __init__(self, root):
        # setting title
        root.title("Entry")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.root = root

        # GButton_save = tk.Button(root)
        # GButton_save["text"] = "Save"
        # GButton_save.place(x=500, y=430, width=70, height=25)
        # GButton_save["command"] = self.save
        # self.GButton_save = GButton_save

        # GInput_captcha = tk.Entry(root)
        # GInput_captcha["text"] = "captcha"
        # GInput_captcha.place(x=30, y=400, width=439, height=54)
        # self.GInput_captcha = GInput_captcha

        # GButton_next = tk.Button(root)
        # GButton_next["text"] = "Skip"
        # GButton_next.place(x=500, y=400, width=70, height=25)
        # GButton_next["command"] = self.next_image
        # self.GButton_next = GButton_next

        GLabel_image = tk.Label(root, image=None)
        GLabel_image.place(x=110, y=110, width=374, height=168)
        self.GLabel_image = GLabel_image
        # Init
        self.load_img()
        # self.GInput_captcha.focus()
        root.bind("z", lambda _: self.save(True))
        root.bind("x", lambda _: self.save(False))

    def next_image(self):
        self.load_img()

    def save(self, isTrue):
        must_folder("labeled")
        # label = self.GInput_captcha.get()
        write_labeled(self.img_name, isTrue, self.img_buf)
        remove_file(self.img_path)
        self.next_image()

    def load_img(self):
        self.img_path = random_unlabeled_img()
        self.img_buf = Image.open(self.img_path)
        self.img_root = ImageTk.PhotoImage(self.img_buf)
        self.GLabel_image.configure(image=self.img_root)
        self.img_name = self.img_path.stem


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
