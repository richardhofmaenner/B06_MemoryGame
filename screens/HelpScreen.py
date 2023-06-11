import tkinter as tk
import config.stylings as style
import screens.StartScreen
import screens.StartScreen


class HelpScreen():

    helpScreenWindow = None

    def __init__(self):
        self.helpScreenWindow = tk.Tk()
        self.helpScreenWindow.title("Help Menu")
        self.helpScreenWindow.geometry("600x400")
        self.helpScreenWindow.configure(background=style.mainBgColor)
        
        screen_width = self.helpScreenWindow.winfo_screenwidth()
        screen_height = self.helpScreenWindow.winfo_screenheight()

        window_width = 600
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.helpScreenWindow.geometry(f"{window_width}x{window_height}+{x}+{y}")

        guideLabel = tk.Label(self.helpScreenWindow, text="Wie funktioniert das Spiel: \n", **style.h1Style)
        guideLabel.pack()
        
        guideText1 = tk.Label(self.helpScreenWindow, text="1. Das Spiel besteht aus 16 Karten, die auf dem Spielfeld verteilt sind. ", **style.textStyle)
        guideText1.pack()
        
        guideText2 = tk.Label(self.helpScreenWindow, text="2. Ziel des Spiels ist es, alle Kartenpaare zu finden. ", **style.textStyle)
        guideText2.pack()
        
        guideText3 = tk.Label(self.helpScreenWindow, text="3. Dazu werden immer zwei Karten aufgedeckt. ", **style.textStyle)
        guideText3.pack()
        
        guideText4 = tk.Label(self.helpScreenWindow, text="4. Wenn die Karten gleich sind, bleiben sie aufgedeckt.", **style.textStyle)
        guideText4.pack()
        
        guideText5 = tk.Label(self.helpScreenWindow, text="5. Wenn die Karten nicht gleich sind, werden sie wieder umgedreht.", **style.textStyle)
        guideText5.pack()
        
        guideText6 = tk.Label(self.helpScreenWindow, text="Das Spiel ist beendet, wenn alle Kartenpaare gefunden wurden. \n", **style.textStyle)
        guideText6.pack()
        
        buttonBack = tk.Button(self.helpScreenWindow, text="Back",
                        **style.buttonStyle, command=self.backToStartScreen)
        buttonBack.pack()
        
    def backToStartScreen(self):
        self.helpScreenWindow.destroy()
        screens.StartScreen.StartScreen()
