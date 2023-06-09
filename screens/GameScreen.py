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
    triesLabel = None
    placeholderImage = None
    photos = []
    cardButtons = []
    selectedCards = []

    def __init__(self):
        # create the game window
        self.gameWindow = tk.Tk()
        self.gameWindow.title("Game Screen")
        self.gameWindow.resizable(False, False)
        self.gameWindow.configure(background=style.mainBgColor)
        
        # get the screen size
        screen_width = self.gameWindow.winfo_screenwidth()
        screen_height = self.gameWindow.winfo_screenheight()

        # set the window size
        window_width = 800
        window_height = 600
        
        # set the window position
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # set the window geometry
        self.gameWindow.geometry(f"{window_width}x{window_height}+{x}+{y}")
        

        # create the grid for positioning the widgets
        for x in range(6):
            self.gameWindow.rowconfigure(x, weight=1)

        for y in range(6):
            self.gameWindow.columnconfigure(y, weight=1)

        # pick 8 random images from /images/gameCards
        # 8 images = 16 cards
        allImages = os.listdir("images/gameCards")
        randomImages = []
        random.shuffle(allImages)

        # pick the first 8 images of the shuffled images and prepar them to be used as button image
        for i in range(8):
            imageName = allImages[i]
            photo = Image.open(f"images/gameCards/{imageName}")
            photo = photo.resize((150, 150))
            photo = ImageTk.PhotoImage(photo)
            
            # the id is used to identify the pairs later on in the game
            cardPhoto = {
                "photo": photo,
                "id": imageName,
            }
            randomImages.append(cardPhoto)

        # duplicate the prepared images, so we have 16 images / 8 pairs.
        randomImages = randomImages + randomImages
        random.shuffle(randomImages)

        # create the cards on the game board
        for i, image in enumerate(randomImages):

            # calculate the row and column of our game field (4x4 field)
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

        # label for displaying the count of tries to win the game.
        self.triesLabel = tk.Label(
            self.gameWindow, text="Total tries: 0", height=4, background=style.mainBgColor,fg=style.mainFgColor
        )
        self.triesLabel.grid(row=0, column=6)
        
        # Button to restart the game 
        restartButton = tk.Button(
            self.gameWindow, text="Restart", **style.buttonStyle,
            command= self.restartGame,
        )
        restartButton.grid(row=4, column=6, sticky="e")

    def restartGame(self):
        self.gameWindow.destroy()
        GameScreen()
        
        self.gameWindow.mainloop()

    def get_clicks_text(self):
        return f"Total Clicks: {self.clicks}"
    
    # is executed when the a card has been clicked.
    def cardClicked(self, event):
        # get the clicked card widget
        clickedCard = event.widget

        # check if the card has not already been clicked. 
        # If the card has already been clicked, just ignore the click.
        if clickedCard not in self.selectedCards:
            clickedCard.cardPressed()
            self.selectedCards.append(clickedCard)

        # when 2 cards are revlead, check if its not a pair and turn the cards back so 2 new cards can be picked.
        if len(self.selectedCards) == 2:
            time.sleep(1)
            if self.selectedCards[0].customId != self.selectedCards[1].customId:
                for card in self.selectedCards:
                    card.resetCard()
            self.selectedCards = []
            self.clicks += 1
            self.triesLabel.config(text=f"Total tries: {self.clicks}")
            self.triesLabel.update()

            # check if all the cards has been revlead. if so, display the winning screen.
            isGameFinished = True
            for card in self.cardButtons:
                if card.isCardRevlead() == False:
                    isGameFinished = False
            
            if isGameFinished:
                sub = tk.Toplevel(self.gameWindow)
                sub.title("Winner")
                
                # get the screen size
                screen_width = sub.winfo_screenwidth()
                screen_height = sub.winfo_screenheight()

                # set the window size
                window_width = 300
                window_height = 200
                
                # set the window position
                x = (screen_width - window_width) // 2
                y = (screen_height - window_height) // 2
                
                

                # set the window geometry
                sub.geometry(f"{window_width}x{window_height}+{x}+{y}")
                
                sub.resizable(False, False)
                sub.configure(background=style.mainBgColor)
                tk.Label(sub, text="You won!", height=4, background=style.mainBgColor, fg=style.mainFgColor).pack()
                

