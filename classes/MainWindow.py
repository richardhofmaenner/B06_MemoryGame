import tkinter as tk

from screens.StartScreen import StartScreen


class MainWindow():
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10, pady=10, fill='both', expand=1)
        self.windowNum = 0

        self.framelist = []
        self.framelist.append(StartScreen(mainframe))
        # self.framelist.append(SecondWindow(mainframe))
        # self.framelist[1].forget()

        def switchWindows(self):
            # self.framelist[self.windowNum].forget()
            # self.windowNum = (self.windowNum + 1) % len(self.framelist)
            # self.framelist[self.windowNum].tkraise()
            # self.framelist[self.windowNum].pack(padx = 10, pady = 10)
            pass
