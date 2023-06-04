import os
import tkinter as tk
import time
import tkinter as tk
from classes.Card import Card
import config.stylings as style
from PIL import Image, ImageTk

class MultiGameScreen():

    MultiGameScreenWindow = None

    def __init__(self):
        self.MultiGameScreenWindow = tk.Tk()
        self.MultiGameScreenWindow.title("Multiplayer")
        self.MultiGameScreenWindow.geometry("600x400")
        self.MultiGameScreenWindow.configure(background=style.mainBgColor)

        guideLabel = tk.Label(self.MultiGameScreenWindow, text="Mutliplayer ist under contruction", **style.textStyle)
        guideLabel.grid(row=5, column=1)
        
        for i in range(1):
            allImages = os.listdir("images/gameCards")
            imageName = allImages[i]
            photo = Image.open(f"images/Multipalyer/{imageName}")
            photo = photo.resize((150, 150))
            photo = ImageTk.PhotoImage(photo)
