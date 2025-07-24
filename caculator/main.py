# on cree une calculatrice basique avec tkinter
# hyper basique, 4 columns 5 rows
from tkinter import Tk, Button, Label, Frame

class MyWindow(Tk):
    
    def __init__(self):
        # super init
        super().__init__()
        
        # container en haut a gauche
        left_container = Frame(self, width=150, height=200)
        left_container.place(x=0, y=0)
        
        first_label = Label(left_container, text='Label (10, 10)', fg='white', bg='#FF00FF')
        first_label.place(x=10, y=10)
        
        second_label = Label(left_container, text='Label (50, 50)', fg='white', bg='green')
        second_label.place(x=50, y=50)
        
        # container de droite
        right_container = Frame(self, width=150, height=200, relief='raised', borderwidth=5)
        right_container.place(x=150, y=0)
        
        button = Button(right_container, text='Button (10, 10)')
        button.place(x=10, y=10)
        
        self.geometry('300x200')
        self.title('Hello workd!')    
        


window = MyWindow()
window.mainloop()