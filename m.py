from tkinter import *

class DEditor:

    def __init__(self):
        self.version = 0.1
        self.root = Tk()


    def execute(self):
        text = Text(self.root)
        text.pack()
        self.root.title('DEditor')
        self.root.mainloop()


load = DEditor()
load.execute()