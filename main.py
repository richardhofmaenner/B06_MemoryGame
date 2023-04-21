import tkinter as tk
from classes.MainWindow import MainWindow

def main():
  root = tk.Tk()
  root.minsize(600,400)
  window = MainWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()