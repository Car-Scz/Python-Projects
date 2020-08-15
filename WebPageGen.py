from tkinter import *
from tkinter.ttk import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry("600x200")
        self.master.title("Update web message")
        self.master.config(bg="#333")

        self.entry_field_variable = StringVar()

        self.labelMsg = Label(self.master, width= 20, text="Enter the message:", font = ("Helvetica", 16))
        self.labelMsg.grid(row=0, column=0, padx=10, pady=20, sticky = "W")
        self.entryInput = Entry(self.master, width=48, textvariable = self.entry_field_variable, font = ("Helvetica", 16))
        self.entryInput.grid(row=1, column=0, padx=10, pady=5, sticky = "WENS")
        
        #self.btnQuit = Button(self.master, width=10, text="Quit", command = self.master.destroy)
        #self.btnQuit.grid(row=2, column=0, padx=10, pady=20, sticky = "W")
        self.btnSave = Button(self.master, width=10, text="Save", command = save(self))
        self.btnSave.grid(row=2, column=1, padx=40, pady=20, sticky = "W")
        
        

def save(self):
    preMsg = "<html><body>"
    postMsg = "<html><body>"
    inp = self.entryInput.get()
    
    f = "newwebpage.html"
    with open(f, 'w'):
        f.write(preMsg + inp + postMsg)
        f.close()

if __name__ == '__main__':
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
