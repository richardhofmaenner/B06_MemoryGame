import tkinter as tk
 
class FirstWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text = "This is Window 1").pack(padx = 10, pady = 10)
        tk.Button(self, text="Hello World").pack()
        self.pack(padx = 10, pady = 10)
 
class SecondWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text = "This is Window 2").pack(padx = 10, pady = 10)
        self.pack(padx = 10, pady = 10)
 
class MainWindow():
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10, pady=10, fill='both', expand=1)
        self.windowNum = 0
 
        self.framelist = []
        self.framelist.append(FirstWindow(mainframe))
        # self.framelist.append(SecondWindow(mainframe))
        # self.framelist[1].forget()
 
        bottomframe = tk.Frame(master)
        bottomframe.pack(padx=10, pady=10)
 
        switch = tk.Button(bottomframe, text = "Switch", command=self.switchWindows)
        switch.pack(padx=10, pady=10)
     
    def switchWindows(self):
        # self.framelist[self.windowNum].forget()
        # self.windowNum = (self.windowNum + 1) % len(self.framelist)
        # self.framelist[self.windowNum].tkraise()
        # self.framelist[self.windowNum].pack(padx = 10, pady = 10)
        pass
 
root = tk.Tk()
window = MainWindow(root)
root.mainloop()