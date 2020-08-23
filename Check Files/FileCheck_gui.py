#   -----------------------------------------------------------------------------------------------------------------------------
#       Name:                  FileCheck_gui.py
#       Python Ver:         3.8.2
#       Author:                Carol Schultz
#       Purpose:             Phonebook App demonstrating OOP, Tkinter GUI module,
#                                    using Tkinter Parent and Child relationships.
#       Tested OS:          Tested on Windows 10.
#   -----------------------------------------------------------------------------------------------------------------------------

#  Import needed external modules
from tkinter import *
import tkinter as tk

#   import the other file check modules
import FileCheck_main
import FileCheck_func

#   load Frame with the tkinter widgets describing the gui window
def load_gui(self):
    
    # Define frame widgets
    self.src_lbl = tk.Label(self.master, text="Choose Source Directory:",
                            font=("Helvetica", 14), fg="#fff", bg="#333")
    self.src_ent = tk.Entry(self.master, width=50,
                            font=("Helvetica", 14), fg="#333", bg="#fff")
    self.src_btn = tk.Button(self.master, text="Browse", width=12,
                             font=("Helvetica", 12), fg="#000", bg="#ff0000",
                             command=lambda:FileCheck_func.src_dir(self))

    self.dest_lbl = tk.Label(self.master, text="Choose Destination Directory:",
                            font=("Helvetica", 14), fg="#fff", bg="#333")
    self.dest_ent = tk.Entry(self.master, width=50,
                            font=("Helvetica", 14), fg="#333", bg="#fff")
    self.dest_btn = tk.Button(self.master, text="Browse", width=12,
                             font=("Helvetica", 12), fg="#000", bg="#ffff00",
                             command = lambda:FileCheck_func.dest_dir(self))
    
    self.btn_close = tk.Button(self.master, text="Quit", width=10,
                             font=("Helvetica", 12), fg="#fff", bg="#333",
                             command = lambda: FileCheck_func.ask_quit(self))
    self.btn_move = tk.Button(self.master, text="Move Files", width=12,
                             font=("Helvetica", 12), fg="#000", bg="#00ff00",
                             command = lambda:FileCheck_func.fileMove(self))
   
    # Define frame widget positioning
    self.src_lbl.grid(row=0, column=0, ipadx=4, ipady=4, padx=(30,0), pady=(50,0), sticky=W)
    self.src_ent.grid(row=1, column=0, columnspan=2, ipadx=4, ipady=4, padx=(30,0), pady=(20,0))
    self.src_btn.grid(row=1, column=3, ipadx=3, ipady=2, padx=(10,0), pady=(20,0))

    self.dest_lbl.grid(row=3, column=0, ipadx=4, ipady=4, padx=(30,0), pady=(50,0), sticky=W)
    self.dest_ent.grid(row=4, column=0, columnspan=2, ipadx=4, ipady=4, padx=(30,0), pady=(20,0))
    self.dest_btn.grid(row=4, column=3, ipadx=3, ipady=2, padx=(10,0), pady=(20,0))
    
    self.btn_close.grid(row=6, column=0, ipadx=3, ipady=2, padx=(30,0), pady=(50,0), sticky=W)
    self.btn_move.grid(row=6, column=3, ipadx=3, ipady=2, padx=(10,0), pady=(50,0), sticky=W)


if __name__ == "__main__":
        pass
