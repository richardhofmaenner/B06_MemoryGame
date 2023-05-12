import tkinter as tk
from tkinter import ttk
import config.styleings as style
import screens.StartScreen

class HelpScreen():
    def __init__(self):
        window = tk.Tk()
        window.title("Help Menu")
        window.geometry("600x300")
        window.configure(background=style.mainBgColor)
        
        for x in range(10):
            window.rowconfigure(x, weight=1)

        for y in range(5):
            window.columnconfigure(y, weight=1)
        
        guideLabel = tk.Label(window, **style.labelStyle, text="Guide:")
        guideLabel.grid(row=1, column=1)
        
        backButton = tk.Button(window, text="Back", **style.buttonStyle, command= screens.StartScreen.StartScreen)
        backButton.grid(row=4, column=4)
        
        window.minsize(600, 400)
        window.maxsize(600, 400)
        window.mainloop()