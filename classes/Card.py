import tkinter as tk
from PIL import Image, ImageTk

class Card(tk.Button):
    
    isReveald = False

    def __init__(self, parent, **args):
        
        # get the placeholder image and resize it to the correct size.
        placeholder = Image.open("images/assets/placeholder.jpg")
        placeholder = placeholder.resize((150, 150))
        placeholder = ImageTk.PhotoImage(placeholder)
        self.placeholderImage = placeholder

        self.customId = args['customId']
        self.memoryImage = args['memoryImage']
        args.pop('customId', None)
        args.pop('memoryImage', None)

        args['image'] = self.placeholderImage

        super().__init__(**args)
    
    def cardPressed(self):
        self.config(image=self.memoryImage)
        self.isReveald = True
        self.update()

    def resetCard(self):
        self.config(image=self.placeholderImage)
        self.isReveald = False

    def isCardRevlead(self):
        return self.isReveald
