import tkinter as tk
class StartScreen(tk.Frame):

  def __init__(self, parent):
    super().__init__(parent)
    tk.Label(self, text = "This is Window 1").pack(padx = 10, pady = 10)
    tk.Button(self, text="Hello World").pack()
    self.pack(padx = 10, pady = 10)