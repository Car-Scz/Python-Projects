#   -----------------------------------------------------------------------------------------------------------------------------
#       Name:                  FileCheck_main.py
#       Python Ver:         3.8.2
#       Author:                Carol Schultz
#       Purpose:             Python program to create a file explorer in Tkinter to synchronize
#                                    with HQ.
#       Tested OS:          Windows 10.
#   -----------------------------------------------------------------------------------------------------------------------------

# import all components from the tkinter library 
from tkinter import *
import tkinter as tk
import os
import shutil
from datetime import time

#   import the other FileCheck modules
import FileCheck_gui
import FileCheck_func

#   Frame is the Tkinter from class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #   define the master frame configuation
        self.master = master
        self.master.maxsize(800, 500)
        self.master.minsize(800, 500)
        self.master.title("Check for Files")
        self.master.config(bg="#333")
        self.master.protocol('WM_DELETE_WINDOW',
                             lambda: FileCheck_func.quit_message(self))

        #   This CenterWindow method will center the app on the user's screen
        FileCheck_func.center_window(self,800, 500)
        self.master.title("Check for Files")
        self.master.config(bg="#F0F0F0")

        #   This protocol method is a tkinter built-in method to catch if
        #   the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: FileCheck_func.ask_quit(self))
        arg = self.master
        
        #   Load in the GUI widgets from a separate module,
        FileCheck_gui.load_gui(self)

# Let the window wait for any events
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
