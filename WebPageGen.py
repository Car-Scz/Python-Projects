#  Program to allow users to change web page message

# Importing tkinter module 
from tkinter import *
  
# define root window
root = Tk()

# set windows elements
root.title('Update message')
root.resizable(width=True, height=True)
root.geometry('650x200')

# declare string variable for storing name
msg_var = StringVar() 

# define a function that will get the name and print it on the screen
def submit():
    msg = msg_entry.get()
    mylist =  ["<html><body>\n", msg,"\n<html><body>"]
    f = open("newwebpage.html", "w")
    f.writelines(mylist)
    f.close()
    
    # Checking if the data is written to file or not 
    f = open("newwebpage.html", "r")
    print(f.read()) 
    f.close()

    # reset variable
    msg_var.set("") 
      
# creating a label for  name using widget Label 
msg_label = Label(root, text = 'Type your new message:', 
                   font=('calibre', 12, 'bold')) 
   
# creating an entry for input  name using widget Entry
msg_entry = Entry(root, textvariable = msg_var, width=80,
                   font=('calibre',10,'normal')) 
   
# creating a button using the widget Button that will call the submit function  
sub_btn = Button(root,text = 'Submit', width=10, bg="#8bed4f",
                 command = submit)
quit_btn = Button(root, text = 'Quit', width=10, bg="#333", fg="white",
                  command = root.destroy) 
   
# placing the label and entry in the required position using grid method 
msg_label.grid(row=0, column=0, padx=10, pady=10, sticky = "W", columnspan = 2) 
msg_entry.grid(row=1, column=0, padx=10, pady=5, sticky = "WENS", columnspan = 2)
sub_btn.grid(row=2, column=0, padx=20, pady=20, sticky = "W")
quit_btn.grid(row=2, column=0, padx=0, pady=20) 
   
# performing an infinite loop for the window to display 
if __name__ == '__main__':
    root.mainloop()
