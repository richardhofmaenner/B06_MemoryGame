import tkinter as tk
import config.stylings as style


class WinnerScreen():

    winnerScreenWindow = None

    def __init__(self, numberOfClicks):
        self.winnerScreenWindow = tk.Tk()
        self.winnerScreenWindow.title("You have actually won this game!")
        self.winnerScreenWindow.geometry("600x400")
        self.winnerScreenWindow.configure(background=style.mainBgColor)

        contentFrame = tk.Frame(self.winnerScreenWindow, bg=style.mainBgColor)
        contentFrame.place(anchor="center", relx=0.5, rely=0.5)

        titleLabel = tk.Label(contentFrame, text="Congratulation!!", **style.h1Style)
        titleLabel.pack()

        textLabel = tk.Label(
            contentFrame, 
            text=f"You needed {numberOfClicks} to win this game.",
            **style.textStyle
            )
        textLabel.pack()

