# on cree une calculatrice basique avec tkinter
# hyper basique, 4 columns 5 rows
from tkinter import Tk, Label

class MyWindow(Tk):
    
    def __init__(self):
        # super init
        super().__init__()
        
        first_label = Label(self, text='side=top', fg='white', bg='#FF00FF')
        first_label.pack(
            side='top',
            fill='x'
            )
        
        second_label = Label(self, text='side=bottom', fg='white', bg='green')
        second_label.pack(side='bottom', fill='x')
        
        third_label = Label(self, text='side=left', fg='white', bg='blue')
        third_label.pack(side='left', fill='y')
        
        fourth_label = Label(self, text='side=right', fg='white', bg='#00FFFF')
        fourth_label.pack(side='right', fill='y')
        
        self.geometry('500x200')
        self.title('Positionnement de widgets via pack ')    
        


window = MyWindow()
window.mainloop()