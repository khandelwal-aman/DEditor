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
        if file!= None:
            file.write(inputValue)


    def openFile(self):
        files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')]
        file =  askopenfilename(initialdir = "/",title = "Select file",filetypes = files)
        filepath = file
        print(filepath)
        if filepath != '':
            with open(filepath,'r') as d:
                data = d.read()
            self.text.insert("end-1c",data)


    def execute(self):
        self.text = Text(self.root)
        self.text.pack()
        #buttonCommit=Button(self.root, height=1, width=10, text="Save File", command=lambda: self.retrieve_input())
        #buttonCommit.pack()
        #buttonOpen=Button(self.root, height=1, width=10, text="Open File", command=lambda: self.openFile())
        #buttonOpen.pack()
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label="Save", command = self.retrieve_input)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.root.quit)
        
        menubar.add_cascade(label = "File", menu = filemenu)
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label = "Open File", command = self.openFile)
        helpmenu.add_command(label = "About", command = self.openFile)
        
        menubar.add_cascade(label = "Help", menu = helpmenu)
        
        
        self.root.config(menu=menubar)
        self.root.title('DEditor')
        self.root.mainloop()


load = DEditor()
load.execute()