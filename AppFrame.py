# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 18:45:38 2022

@author: luldo
"""
import tkinter as tk
from tkinter import ttk

class mainFrame(ttk.Frame):
    def __init__(self, container):
        super.__init__(container)
        

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
    def __create_widgets(self):
        Actionable = tk.StringVar(self) #Actionable vs Non-actionable
        Actionable.set("Actionable")
        Urgency = tk.StringVar(self) #High(1-2 day) vs Medium(3-7 days) vs Low (>7 days)
        Urgency.set("Medium (3-7 days)")
        Purpose = tk.StringVar(self) #Personal vs Business
        Purpose.set("Business")
        Action = tk.StringVar(self) #Labelled vs Deleted
        Action.set("Labelled")
        
        paddings = {'padx': 5, 'pady':5}
        
        Actionable_Menu = ttk.OptionMenu(self, Actionable, "Actionable", "Non-actionable")
        Actionable_Menu.pack(**paddings)
        Urgency_Menu = ttk.OptionMenu(self, Actionable, "High(1-2 days)", "Medium(3-7 days)","Low(>7 days)")
        Urgency_Menu.pack(**paddings)
        Purpose_Menu = ttk.OptionMenu(self, Actionable, "Personal", "Business")
        Purpose_Menu.pack(**paddings)
        Action_Menu = ttk.OptionMenu(self, Actionable, "To label", "To delete")
        Action_Menu.pack(**paddings)

class TopbuttonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)