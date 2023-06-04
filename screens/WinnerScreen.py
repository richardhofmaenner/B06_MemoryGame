import tkinter as tk
import config.stylings as style



class WinnerScreen():

    winnerScreenWindow = None

    def __init__(self, numberOfClicks, ):           # timetext wie einfügen?
        # create the winner screen window
        self.winnerScreenWindow = tk.Tk()
        self.winnerScreenWindow.title("You have actually won this game!")
        self.winnerScreenWindow.geometry("600x400")
        self.winnerScreenWindow.configure(background=style.mainBgColor)

        # create a frame and center it in the middle of the window
        contentFrame = tk.Frame(self.winnerScreenWindow, bg=style.mainBgColor)
        contentFrame.place(anchor="center", relx=0.5, rely=0.5)

        titleLabel = tk.Label(contentFrame, text="Congratulation!!", **style.h1Style)
        titleLabel.pack()

        textLabel = tk.Label(
            contentFrame, 
            text=f"You needed {numberOfClicks} tries to win this game.",
            **style.textStyle
            )
        #textLabel = tk.Label(                                  ## wie zeitdauer anzeigen lassen?
        #    contentFrame, 
        #    text=f"You completed the game in {timeText}.",
        #    **style.textStyle
        #)
        textLabel.pack()

