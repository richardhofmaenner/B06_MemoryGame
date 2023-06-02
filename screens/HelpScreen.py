import tkinter as tk
import config.stylings as style


class HelpScreen():

    helpScreenWindow = None

    def __init__(self):
        self.helpScreenWindow = tk.Tk()
        self.helpScreenWindow.title("Help Menu")
        self.helpScreenWindow.geometry("600x400")
        self.helpScreenWindow.configure(background=style.mainBgColor)

        guideLabel = tk.Label(self.helpScreenWindow, text="Guide:", **style.h1Style)
        guideLabel.grid(row=2, column=1)
