from screens.StartScreen import GameScreen
import tkinter as tk
from tkinter import ttk
import config.styleings as style


class Gamescreen():
    def Gamescreen(self): ## 
        window3 = tk.Tk()
        window3.title("Game Screen")
        window3.geometry("600x400")
        window3.configure(background=style.mainBgColor)

        for x in range(6):
            window3.rowconfigure(x, weight=1)

        for y in range(6):
            window3.columnconfigure(y, weight=1)

        cardButtons = []
        for i in range(16):
            row = i // 4 + 1
            column = i % 4 + 1
            cardButton = tk.Button(self.window3, text=f"Card {i+1}", width=10, height=5)
            cardButton.grid(row=row, column=column)
            cardButtons.append(cardButton)

        startButton = tk.Button(window3, text="Start Game", **style.buttonStyle, command=lambda: print("Start Game"), width=10, height=3)
        startButton.grid(row=0, column=0)
        
        quitButton = tk.Button(window3, text="Quit", **style.buttonStyle, command=lambda: window3.destroy())
        quitButton.grid(row=6, column=6)
        

        
        Gamescreen.mainloop() 
        
    ##def Createcards(self): ## ev. separate def?
    ##    window = tk.Tk()    
        
        
            
    ##    window.mainloop() 