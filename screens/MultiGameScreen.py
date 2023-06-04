import tkinter as tk
import config.stylings as style


class MultiGameScreen():

    MultiGameScreenWindow = None

    def __init__(self):
        self.MultiGameScreenWindow = tk.Tk()
        self.MultiGameScreenWindow.title("Multiplayer")
        self.MultiGameScreenWindow.geometry("600x400")
        self.MultiGameScreenWindow.configure(background=style.mainBgColor)

        guideLabel = tk.Label(self.MultiGameScreenWindow, text="Mutlipalyer ist under contruction", **style.h1Style)
        guideLabel.grid(row=2, column=1)
