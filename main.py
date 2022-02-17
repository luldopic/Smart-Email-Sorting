# -*- coding: utf-8 -*-
"""

Primary Email Sorting Interface

"""

import tkinter as tk
from tkinter import ttk
import requests
import json
import imap_gmail

class mailboxFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

class emailFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

class sortingFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.__create_widget()
    def __create_widget(self):
        Actionable = tk.StringVar(self) #Actionable vs Non-actionable
        Urgency = tk.StringVar(self) #High(1-2 day) vs Medium(3-7 days) vs Low (>7 days)
        Purpose = tk.StringVar(self) #Personal vs Business
        Action = tk.StringVar(self) #Archived vs Deleted
        

class TopbuttonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        

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
        
    
    def fetchEmail(self):
        pass
    
if __name__ == '__main__':
    app = App()
    app.mainloop()