# on cree une calculatrice basique avec tkinter
# hyper basique, 4 columns 5 rows
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.pack()
        
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        
        self.contents = tk.StringVar()
        self.contents.set("contenu de la variable")
        self.entrythingy["textvariable"] = self.contents
        
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)
        
    def print_contents(self, event):
        print("Contenu actuel :",
              self.contents.get())
        
root = tk.Tk()
app = App(root)
app.mainloop()