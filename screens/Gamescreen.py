from screens.StartScreen import GameScreen
import tkinter as tk
from tkinter import ttk
import config.styleings as style


class Gamescreen():
    def Gamescreen(self): ## 
        window = tk.Tk()
        window.title("Game Screen")
        window.geometry("600x400")
        window.configure(background=style.mainBgColor)

        for x in range(4):
            window.rowconfigure(x, weight=1)

        for y in range(6):
            window.columnconfigure(y, weight=1)

        startButton = tk.Button(window, text="Start Game", **style.buttonStyle, command=lambda: print("Start Game"))
        startButton.grid(row=1, column=1)
        
        quitButton = tk.Button(window, text="Quit", **style.buttonStyle, command=lambda: window.destroy())
        quitButton.grid(row=4, column=6)
        
        Gamescreen.mainloop() 
        
    def Createcards(self): ##
        window = tk.Tk()    
            
        window.mainloop() 