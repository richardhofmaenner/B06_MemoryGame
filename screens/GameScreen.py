import os
import random
import time
import tkinter as tk
from classes.Card import Card
import config.stylings as style
from PIL import Image, ImageTk

from screens.WinnerScreen import WinnerScreen


class GameScreen():

    clicks = 0
    gameWindow = None
    countButton = None
    placeholderImage = None
    photos = []
    cardButtons = []
    selectedCards = []

    def __init__(self):
        self.gameWindow = tk.Tk()
        self.gameWindow.title("Game Screen")
        self.gameWindow.geometry("800x600")
        self.gameWindow.resizable(False, False)
        self.gameWindow.minsize(800, 600)
        self.gameWindow.configure(background=style.mainBgColor)

        for x in range(6):
            self.gameWindow.rowconfigure(x, weight=1)

        for y in range(6):
            self.gameWindow.columnconfigure(y, weight=1)

        # pick 8 random images from /images/gameCards
        allImages = os.listdir("images/gameCards")
        randomImages = []
        random.shuffle(allImages)

        for i in range(8):
            imageName = allImages[i]
            photo = Image.open(f"images/gameCards/{imageName}")
            photo = photo.resize((150, 150))
            photo = ImageTk.PhotoImage(photo)
            
            cardPhoto = {
                "photo": photo,
                "id": imageName,
            }
            randomImages.append(cardPhoto)

        # duplicate the random images
        randomImages = randomImages + randomImages
        random.shuffle(randomImages)

        for i, image in enumerate(randomImages):
            row = i // 4 + 1
            column = i % 4 + 1

            cardButton = Card(
                self.gameWindow, borderwidth=0, customId=image['id'], memoryImage=image['photo'],
            )
            cardButton.bind('<Button-1>', self.cardClicked)
            cardButton.grid(row=row, column=column)
            self.cardButtons.append(cardButton)

        quitButton = tk.Button(
            self.gameWindow, text="Quit", **style.buttonStyle,
            command=lambda: self.gameWindow.destroy(),
        )
        quitButton.grid(row=6, column=6)

        self.countButton = tk.Button(
            self.gameWindow, text="Total clicks: 0", width=10, height=3
        )
        self.countButton.grid(row=0, column=5)

        self.gameWindow.mainloop()

    def get_clicks_text(self):
        return f"Total Clicks: {self.clicks}"
    
    def cardClicked(self, event):
        clickedCard = event.widget

        if clickedCard not in self.selectedCards:
            clickedCard.cardPressed()
            self.selectedCards.append(clickedCard)

        if len(self.selectedCards) == 2:
            time.sleep(2)
            print(f"Card 1 ID: {self.selectedCards[0].customId}")
            print(f"Card 2 ID: {self.selectedCards[1].customId}")
            if self.selectedCards[0].customId == self.selectedCards[1].customId:
                print('A pair has been found.')
            else:
                for card in self.selectedCards:
                    card.resetCard()
            self.selectedCards = []
            self.clicks += 1
            self.countButton.config(text=f"Total Clicks: {self.clicks}")
            self.countButton.update()

            isGameFinished = True
            for card in self.cardButtons:
                if card.isCardRevlead() == False:
                    isGameFinished = False
            
            if isGameFinished:
                print('Game finished.')
                WinnerScreen(self.clicks)