"""k.llllll...

Author:  Caeden Jackson
Date written: 04/15/25
Assignment:   Module8 exercise1 part1 (1 or 2), etc.
Short Desc:   This program is my final project of developing a working GUI Breezy application.
This application is a GUI for a restaurant inventory management system.

"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage, N,S,W,E

class Inventory(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "Inventory Management System", width = 800, height = 600)

        """Label for title"""
        headerLabel = self.addLabel(text = "Inventory Management System", row = 1, column = 0, sticky = "N,S,W,E")
        headerLabel.grid(row = 0, column = 0, padx = 5, pady = 5)
        font = ("Arial", 20)
        headerLabel["font"] = font
        headerLabel["bg"] = "blue"
        headerLabel["fg"] = "white"

        homeLabel = self.addLabel(text = "Home", row = 2, column = 0, sticky = "N,S,W,E")
        homeLabel.grid(row = 2, column = 0, padx = 5, pady = 5)
        imageLabel = self.addLabel(text="", row=2, column=0, sticky="N,S,W,E")
        self.image = PhotoImage(file="header.png")




Inventory().mainloop()