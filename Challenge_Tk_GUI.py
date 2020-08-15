# import everything from tkinter module 
import tkinter
from tkinter import *
  
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.geometry('{}x{}'.format(830, 300))
        self.master.title('Check files' )

        #  define variables
        self.varE1 = StringVar()
        self.varE2 = StringVar()
        
        #  Define entry fields and window buttons - row 1
        self.btnBrowse1 = Button(self.master, text = "Browse...", font = ("Helvetica", 14), width=15, height=1, bd=4)
        self.btnBrowse1.grid(row=0, column=0, padx=20, pady=30)
        
        self.txtE1 = Entry(self.master, text = "", width=50, font = ("Helvetica", 14))
        self.txtE1.grid(row=0, column=1, padx=10, pady=30, sticky=W+E+N+S)

        #  Define entry fields and window buttons - row 2
        self.btnBrowse2 = Button(self.master, text = "Browse...", font = ("Helvetica", 14), width=15, height=1, bd=4)
        self.btnBrowse2.grid(row=1, column=0)
        
        self.txtE2 = Entry(self.master, text = "", width=50, font = ("Helvetica", 14))
        self.txtE2.grid(row=1, column=1, padx=10, sticky=W+E+N+S)
        
        #  Define entry fields and window buttons - row 3
        self.btnCheck = Button(self.master, text = "Check for files...", font = ("Helvetica", 14), width=15, height=2, bd=4)
        self.btnCheck.grid(row=2, column=0, padx=20, pady=30)

        self.btnClose = Button(self.master, text="Close Program", font = ("Helvetica", 14), width=15, height=2, bd=4, command=self.close)
        self.btnClose.grid(row=2, column=1, sticky=E)

        
        
    def close(self):
        self.master.destroy()       


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
