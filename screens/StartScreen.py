import tkinter as tk
import config.stylings as style
from screens.GameScreen import GameScreen
from screens.HelpScreen import HelpScreen
from screens.MultiGameScreen import MultiGameScreen


class StartScreen():

    startScreenWindow = None

    def __init__(self):
        # create the main menu window
        self.startScreenWindow = tk.Tk()
        self.startScreenWindow.title("Main Menu")
        self.startScreenWindow.configure(background=style.mainBgColor)
        
        # get the screen size
        screen_width = self.startScreenWindow.winfo_screenwidth()
        screen_height = self.startScreenWindow.winfo_screenheight()

        # set the window size
        window_width = 600
        window_height = 400
        
        # set the window position
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # set the window geometry
        self.startScreenWindow.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # create the grid for position the widget
        for x in range(5):
            self.startScreenWindow.rowconfigure(x, weight=1)

        for y in range(3):
            self.startScreenWindow.columnconfigure(y, weight=1)

        titleLabel = tk.Label(self.startScreenWindow,
                              text="Memory: THE GAME", **style.h1Style)
        titleLabel.grid(row=1, column=1, sticky="nsew")

        startButton = tk.Button(self.startScreenWindow, text="Single Player",
                                **style.buttonStyle, command=self.openGameScreen)
        startButton.grid(row=2, column=1)

        startButton = tk.Button(self.startScreenWindow, text="Multi Player",
                                **style.buttonStyle, command=self.openMultiGameScreen)
        startButton.grid(row=3, column=1)

        helpbutton = tk.Button(self.startScreenWindow, text="Help",
                               **style.buttonStyle, command=self.openHelpScreen)
        helpbutton.grid(row=4, column=1)

        quitButton = tk.Button(self.startScreenWindow, text="Quit", **
                               style.buttonStyle, command=self.closeStartScreen)
        quitButton.grid(row=5, column=1, pady=10, padx=10)

        self.startScreenWindow.minsize(600, 400)
        self.startScreenWindow.maxsize(600, 400)
        self.startScreenWindow.mainloop()

    def openGameScreen(self):
        self.startScreenWindow.destroy()
        GameScreen()
        
    def openMultiGameScreen(self):
        self.startScreenWindow.destroy()
        MultiGameScreen()

    def closeStartScreen(self):
        self.startScreenWindow.destroy()

    def openHelpScreen(self):
        self.startScreenWindow.destroy()
        HelpScreen()

