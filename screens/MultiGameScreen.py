import tkinter as tk
import config.stylings as style


class MultiGameScreen():

    MultiGameScreenWindow = None

    def __init__(self):
        self.MultiGameScreenWindow = tk.Tk()
        self.MultiGameScreenWindow.title("Multiplayer")
        self.MultiGameScreenWindow.geometry("600x400")
        self.MultiGameScreenWindow.configure(background=style.mainBgColor)

        guideLabel = tk.Label(self.MultiGameScreenWindow, text="Mutliplayer ist under contruction", **style.textStyle)
        guideLabel.grid(row=5, column=1)
