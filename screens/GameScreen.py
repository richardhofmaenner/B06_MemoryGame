import os
import random
import time
import tkinter as tk
from classes.Card import Card
import config.stylings as style
from PIL import Image, ImageTk

import screens.StartScreen
from screens.WinnerScreen import WinnerScreen


class GameScreen():

    clicks = 0
    gameWindow = None
    triesLabel = None
    placeholderImage = None
    photos = []
    cardButtons = []
    selectedCards = []
    endTime = None
    timeText = None

    def __init__(self):
        
        self.startTime = time.time()  # Startzeit erfassen
        self.endTime = None             # aktuellen Zeitpunkt initialisieren
        
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
            command=lambda: self.quitPopUp(),
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
    
    def backToStartScreen(self):
        self.gameWindow.destroy()
        screens.StartScreen.StartScreen()
        
    
    def quitPopUp(self):
            popup = tk.Toplevel(self.gameWindow)
            popup.title("Quit")
            
            # get the screen size
            screen_width = popup.winfo_screenwidth()
            screen_height = popup.winfo_screenheight()

            # set the window size
            window_width = 200
            window_height = 100
            
            # set the window position
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # set the window geometry
            popup.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            label = tk.Label(popup, text="Are you sure you want to quit?")
            label.grid(row=0, column=2, columnspan=2, padx=20, pady=10)
            
            menuButton = tk.Button(popup, text="Main Menu", command= self.backToStartScreen, **style.smallButtonStyle)
            menuButton.grid(row=1, column=2, padx=20, pady=20)
                
            quitButton = tk.Button(popup, text="Quit", command=self.gameWindow.destroy, **style.smallButtonStyle)
            quitButton.grid(row=1, column=3, padx=20, pady=25)

            # Start der Zeitaktualisierung



    
    def updateTime(self):
        if self.endTime is None:  # Wenn das Spiel noch läuft
            elapsedTime = time.time() - self.startTime  # Berechnung der verstrichenen Zeit
            minutes = int(elapsedTime // 60)
            seconds = int(elapsedTime % 60)
            self.timeText = f"Time: {minutes:02d}:{seconds:02d}"
            self.gameWindow.after(1000, self.updateTime)  # Aktualisierung alle 1 Sekunde
            self.triesLabel.config(text=f"Total tries: {self.clicks}\n{self.timeText}")
            self.triesLabel.update()
        else:
            # Wenn das Spiel beendet wurde
            elapsedTime = self.endTime - self.startTime  # Berechnung der Gesamtzeit
            minutes = int(elapsedTime // 60)
            seconds = int(elapsedTime % 60)
            self.timeText = f"Time: {minutes:02d}:{seconds:02d}"
            #self.triesLabel.config(text=f"Total tries: {self.clicks}\n{timeText}\n\nCongratulations!\nYou completed the game in {minutes:02d}:{seconds:02d}.")
            #self.triesLabel.update()


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
                tk.Label(sub, text="You won!", height= 8, background=style.mainBgColor, fg=style.mainFgColor).pack()
                tk.Label(sub, text=f"Tries needed: {self.clicks}", height= 2, background=style.mainBgColor, fg=style.mainFgColor).pack()
                tk.Label(sub, text=f"{self.timeText}", height= 2, background=style.mainBgColor, fg=style.mainFgColor).pack()

                

