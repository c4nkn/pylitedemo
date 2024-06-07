import tkinter as tk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the __init__ method of tk.Tk to initialize the root window
        
        ## Setting up Initial Things
        self.title("Designer")
        self.configure(bg="#797D7F")
        self.geometry("500x500")
        
        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):
        # Create all widgets here
        
        
        Button2 = Button(self,text="Button")
        
        Button2.place(x=166,y=169,width="319px",height="24px")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()  # Start the main loop
