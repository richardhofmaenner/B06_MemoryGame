import tkinter as tk
from tkinter import ttk
import config.stylings as style
from screens.Gamescreen import Gamescreen


class StartScreen():
    def __init__(self):
        window = tk.Tk()
        window.title("Main Menu")
        window.geometry("600x300")
        window.configure(background=style.mainBgColor)

        for x in range(5):
            window.rowconfigure(x, weight=1)

        for y in range(3):
            window.columnconfigure(y, weight=1)


        titleLabel = tk.Label(window, text="Memory: THE GAME", **style.h1Style)
        titleLabel.grid(row=1, column=1, sticky="nsew")
        
        startButton = tk.Button(window, text="Single Player", **style.buttonStyle, command=self.Gamescreen)
        startButton.grid(row=2, column=1)
        
        helpbutton = tk.Button(window, text="Help", **style.buttonStyle, command= HelpScreen.HelpWindow)
        helpbutton.grid(row=4, column=1)
        
        quitButton = tk.Button(window, text="Quit", **style.buttonStyle, command=lambda: window.destroy())
        quitButton.grid(row=5, column=1)
        
        window.minsize(600, 400)
        window.maxsize(600, 400)
        window.mainloop()
    

    def Gamescreen(self):
        gameScreenWindow = Gamescreen()
        # window3 = tk.Tk()
        # window3.title("GameScreen")
        # window3.geometry("600x300")
        # window3.configure(background=style.mainBgColor)

        # for x in range(4):
        #     window3.rowconfigure(x, weight=1)

        # for y in range(6):
        #     window3.columnconfigure(y, weight=1)
        
        # startButton = tk.Button(window3, text="Start Game", **style.buttonStyle, command=lambda: print("Start Game"))
        # startButton.grid(row=1, column=1)
        
        # quitButton = tk.Button(window3, text="Quit", **style.buttonStyle, command=lambda: window3.destroy())
        # quitButton.grid(row=4, column=6)
        
        # window3.minsize(600, 400)
        # window3.maxsize(600, 400)
        # window3.mainloop()


class HelpScreen():
    def HelpWindow():
        window2 = tk.Tk()
        window2.title("Help Menu")
        window2.geometry("300x200")
        window2.configure(background=style.mainBgColor)
        
        Guidelabel = tk.Label(window2, text="Guide:")
        Guidelabel.grid(row=2, column=1)