import os
import tkinter as tk
import config.stylings as style
from PIL import Image, ImageTk

class MultiGameScreen():

    MultiGameScreenWindow = None

    def __init__(self):
        self.MultiGameScreenWindow = tk.Tk()
        self.MultiGameScreenWindow.title("Multiplayer")
        self.MultiGameScreenWindow.geometry("600x400")
        self.MultiGameScreenWindow.configure(background=style.mainBgColor)

        guideLabel = tk.Label(self.MultiGameScreenWindow, text=" The Game <Mutliplayer> ist under contruction", **style.textStyle)
        guideLabel.grid(row=2, column=1)
        
        allImages = os.listdir("images/MultiPlayer")
        for i, imageName in enumerate(allImages):
            photo = Image.open(f"images/MultiPlayer/{imageName}")
            photo = photo.resize((150, 150))
            photo = ImageTk.PhotoImage(photo)

            imageLabel = tk.Label(self.MultiGameScreenWindow, image=photo)
            imageLabel.image = photo
            imageLabel.grid(row=10, column=i+1)
