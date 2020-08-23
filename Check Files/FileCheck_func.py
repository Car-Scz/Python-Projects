#   -----------------------------------------------------------------------------------------------------------------------------
#       Name:                  FileCheck_func.py
#       Python Ver:         3.8.2
#       Author:                Carol Schultz
#       Purpose:             Python program to create a file explorer in Tkinter to synchronize
#                                    with HQ.
#       Tested OS:          Windows 10.
#   -----------------------------------------------------------------------------------------------------------------------------

#   Import needed external modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import shutil, sys, time, os
import sqlite3

# pass in the tkinter frame (master) reference and the w and h
def center_window(self, w, h):
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def src_dir(self):
    dirpath = filedialog.askdirectory()
    x = dirpath + "/"
    self.src_ent.insert(END, x)
    return

def dest_dir(self):
    dir_path = filedialog.askdirectory()
    x = dir_path + "/"
    self.dest_ent.insert(END, x)
    return

#  File move based on update/new files within 24 hours
def fileMove(self):
    sourcePath = self.src_ent.get()
    destPath = self.dest_ent.get()

    files = os.listdir(sourcePath)
    now = time.time()
    for f in files:
        src = os.path.join(sourcePath, f)
        dest = os.path.join(destPath, f)

        if os.stat(src).st_mtime > now - 1 * 86400:
            if os.path.isfile(src):
                shutil.move(src, dest)

if __name__ == "__main__":
    pass
