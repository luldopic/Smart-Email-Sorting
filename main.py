# -*- coding: utf-8 -*-
"""

Primary Email Sorting Interface

"""

import tkinter as tk
import json
import imap_gmail
import AppFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Email Sorting")
        width = 900
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.initFrame()
    
    def initFrame(self):
        buttonFrame = AppFrame.TopbuttonFrame(self)
        buttonFrame.grid(column = 0, row = 0)
        
        mainFrame = AppFrame.mailboxFrame(self)
        mainFrame.grid(column = 0, row = 0)
        
        
        
if __name__ == '__main__':
    app = App()
    app.mainloop()