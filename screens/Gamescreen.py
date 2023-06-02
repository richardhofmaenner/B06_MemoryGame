import tkinter as tk

from tkinter import ttk

import config.stylings as style



class Gamescreen():

    clicks = 0
    gameWindow = None
    countButton = None

    def __init__(self): 
        self.gameWindow = tk.Tk()
        self.gameWindow.title("Game Screen")
        self.gameWindow.geometry("600x400")
        self.gameWindow.configure(background=style.mainBgColor)


        for x in range(6):
            self.gameWindow.rowconfigure(x, weight=1)


        for y in range(6):
           self.gameWindow.columnconfigure(y, weight=1)


        cardButtons = []

        for i in range(16):

            row = i // 4 + 1

            column = i % 4 + 1

            cardButton = tk.Button(self.gameWindow, text=f"Card {i+1}", width=10, height=5, command=self.count_clicks)
            cardButton.grid(row=row, column=column)

            cardButtons.append(cardButton)


        startButton = tk.Button(self.gameWindow, text="Start Game", **style.buttonStyle, command=lambda: print("Start Game"), width=10, height=3)

        startButton.grid(row=0, column=0)
        

        quitButton = tk.Button(self.gameWindow, text="Quit", **style.buttonStyle, command=lambda: self.gameWindow.destroy())

        quitButton.grid(row=6, column=6)

        self.countButton = tk.Button(self.gameWindow, text=f"Click Counts: {self.clicks}", width=10, height=3 )
        self.countButton.grid(row=0, column=5)

        self.gameWindow.mainloop()
        


    def count_clicks(self):
        self.clicks += 1
        self.countButton.config(text=f"Total clicks: {self.clicks}")
        print(f"Total clicks: {self.clicks}")


    def get_clicks_text(self):
        return f"Total Clicks: {self.clicks}"