import tkinter as tk
import config.stylings as style


class WinnerScreen():

    winnerScreenWindow = None

    def __init__(self, numberOfClicks):
        # create the winner screen window
        self.winnerScreenWindow = tk.Tk()
        self.winnerScreenWindow.title("You have actually won this game!")
        self.winnerScreenWindow.configure(background=style.mainBgColor)
        
        # get the screen size
        screen_width = self.winnerScreenWindow.winfo_screenwidth()
        screen_height = self.winnerScreenWindow.winfo_screenheight()

        # set the window size
        window_width = 600
        window_height = 400
        
        # set the window position
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # set the window geometry
        self.winnerScreenWindow.geometry(f"{window_width}x{window_height}+{x}+{y}")

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
        textLabel.pack()

