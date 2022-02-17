# -*- coding: utf-8 -*-
"""

Primary Email Sorting Interface

"""

import tkinter as tk
import json
import imap_gmail
import AppFrame


class App(tk.Tk):
    def __init__(self,root):
        super().__init__()
        root.title("Email Sorting")
        width = 900
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
    
    def getMail(self):
        credentialsJSON = "credentialsGoogle.json"
        with open(credentialsJSON) as handler:
            credentials = json.load(handler)
        mail = imap_gmail.imap(credentials["user"], credentials["password"])
    
if __name__ == '__main__':
    app = App()
    app.mainloop()