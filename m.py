from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfilename


class DEditor:

    def __init__(self):
        self.version = 0.1
        self.root = Tk()


    def retrieve_input(self):
        inputValue=self.text.get("1.0","end-1c")
        print(inputValue)
        files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files)
        file.write(inputValue)


    def openFile(self):
        files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')]
        file =  askopenfilename(initialdir = "/",title = "Select file",filetypes = files)
        filepath = file
        with open(filepath,'r') as d:
            data = d.read()
        self.text.insert("end-1c",data)


    def execute(self):
        self.text = Text(self.root)
        self.text.pack()
        buttonCommit=Button(self.root, height=1, width=10, text="Save File", command=lambda: self.retrieve_input())
        buttonCommit.pack()
        buttonOpen=Button(self.root, height=1, width=10, text="Open File", command=lambda: self.openFile())
        buttonOpen.pack()
        self.root.title('DEditor')
        self.root.mainloop()


load = DEditor()
load.execute()