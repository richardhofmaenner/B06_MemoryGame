import os
import tkinter as tk
import config.stylings as style
from PIL import Image, ImageTk
import screens.StartScreen

class MultiGameScreen():

    MultiGameScreenWindow = None

    def __init__(self):
        self.MultiGameScreenWindow = tk.Tk()
        self.MultiGameScreenWindow.title("Multiplayer")
        self.MultiGameScreenWindow.geometry("600x400")
        self.MultiGameScreenWindow.configure(background=style.mainBgColor)

        screen_width = self.MultiGameScreenWindow.winfo_screenwidth()
        screen_height = self.MultiGameScreenWindow.winfo_screenheight()

        window_width = 600
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.MultiGameScreenWindow.geometry(f"{window_width}x{window_height}+{x}+{y}")


        

        guideLabel = tk.Label(self.MultiGameScreenWindow, text="The game mode <Mutliplayer> is under construction", **style.textStyle)
        guideLabel.grid(row=2, column=1, sticky="nsew")
        
        allImages = os.listdir("images/MultiPlayer")
        for i, imageName in enumerate(allImages):
            photo = Image.open(f"images/MultiPlayer/{imageName}")
            photo = photo.resize((150, 150))
            photo = ImageTk.PhotoImage(photo)

            imageLabel = tk.Label(self.MultiGameScreenWindow, image=photo)
            imageLabel.image = photo
            imageLabel.grid(row=i+1, column=i+1, sticky="nsew")

        # Anpassung der Zeilen- und Spaltengrößen an den Bildschirm
        self.MultiGameScreenWindow.grid_rowconfigure(0, weight=1)
        self.MultiGameScreenWindow.grid_rowconfigure(1, weight=1)
        self.MultiGameScreenWindow.grid_rowconfigure(len(allImages)+2, weight=1)
        self.MultiGameScreenWindow.grid_columnconfigure(0, weight=1)
        self.MultiGameScreenWindow.grid_columnconfigure(len(allImages)+1, weight=1)
        
        quitButton = tk.Button(
        self.MultiGameScreenWindow, text="Quit", **style.buttonStyle,
        command=lambda: self.quitPopUp(),
        )
        quitButton.grid(row=i+5, column=i+5, sticky="nsew")
        
    def quitPopUp(self):
            popup = tk.Toplevel(self.MultiGameScreenWindow)
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
                
            quitButton = tk.Button(popup, text="Quit", command=self.MultiGameScreenWindow.destroy, **style.smallButtonStyle)
            quitButton.grid(row=1, column=3, padx=20, pady=25)    
        
        
    def backToStartScreen(self):
        self.MultiGameScreenWindow.destroy()
        screens.StartScreen.StartScreen()
