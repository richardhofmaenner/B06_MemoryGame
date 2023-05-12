import tkinter as tk
from tkinter import ttk
import config.styleings as style
import screens.HelpScreen as HelpScreen


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
        
        startButton = tk.Button(window, text="Start", **style.buttonStyle, command=lambda: print("Start"))
        startButton.grid(row=2, column=1)
        
        helpbutton = tk.Button(window, text="Help", **style.buttonStyle, command= HelpScreen.HelpScreen)
        helpbutton.grid(row=3, column=1)
        
        quitButton = tk.Button(window, text="Quit", **style.buttonStyle, command=lambda: window.quit())
        quitButton.grid(row=4, column=1)
        
        window.minsize(600, 400)
        window.maxsize(600, 400)
        window.mainloop()
        

