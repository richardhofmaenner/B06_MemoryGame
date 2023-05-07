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

        for x in range(6):
            window.rowconfigure(x, weight=1)

        for y in range(6):
            window.columnconfigure(y, weight=1)

        startButton = tk.Button(window, text="Start Game", **style.buttonStyle, command=lambda: print("Start Game"), width=10, height=3)
        startButton.grid(row=0, column=1)
        
        quitButton = tk.Button(window, text="Quit", **style.buttonStyle, command=lambda: window.destroy())
        quitButton.grid(row=6, column=1)
        
        for i in range(4):
            for j in range(4):
                cardButton = tk.Button(window, text=f"Button {(i*4)+j+1}", **style.buttonStyle, command=lambda: print("Button {(i*4)+j+1}"), width=10, height=5)
                cardButton.grid(row=1+i, column=1+j)
        
        Gamescreen.mainloop() 
        
    def Createcards(self): ##
        window = tk.Tk()    
        
        
            
        window.mainloop() 