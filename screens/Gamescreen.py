import tkinter as tk
class GameScreen(tk.Frame):

  def __init__(self, parent):
    super().__init__(parent)
    tk.Label(self, text = "This is the Gamescreen").pack(padx = 10, pady = 10)
    
# Erstellung der Karten (hier als Labels)
symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
cards = symbols * 2  # 8 Paare
card_labels = []
for i in range(4):
    for j in range(4):
        card = tk.Label(game_frame, text="", font=("Arial", 24), width=3, height=2, relief="groove")
        card.grid(row=i, column=j, padx=5, pady=5)
        card_labels.append(card)

# Start des GUI-Loops
root.mainloop()