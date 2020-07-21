#   -----------------------------------------------------------------------------------------------------------------------------
#       Name:                  phonebook_main.py
#       Python Ver:         3.8.2
#       Author:                Carol Schultz
#       Purpose:             Phonebook App demonstrating OOP, Tkinter GUI module,
#                                    using Tkinter Parent and Child relationships.
#       Tested OS:          Windows 10.
#   -----------------------------------------------------------------------------------------------------------------------------

#   Tkinter is the standard GUI toolkit library for Python.
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#   import the other phonebook modules
import phonebook_gui
import phonebook_func

#   Frame is the Tkinter from class that our class will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        #   define the master frame configuation
        self.master = master
        self.master.minsize(500,350)    # (Height, Width)
        self.master.maxsize(500,350)
        #   This CenterWindow method will center the app on the user's screen
        phonebook_func.center_window(self,500, 350)
        self.master.title("The Tkinter Phonebook App")
        self.master.config(bg="#F0F0F0")
        #   This protocol method is a tkinter built-in method to catch if
        #   the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #   Load in the GUI widgets from a separate module,
        #   keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook App") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        
        self.master.config(menu=menubar, borderwidth='1')

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
