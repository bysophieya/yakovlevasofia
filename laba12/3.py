from tkinter import *
class IceCreamStand:
    def __init__(self,flavors):
        self.flavors=flavors

    def info(self):
        for flavor in self.flavors:
            print(flavor)
IceCreamStand1=IceCreamStand(['Клубничное',"Шоколадное","Ванильное","Ананасовое"])
IceCreamStand1.info()

window=Tk()

window.geometry('100x200')
window['bg']='white'

name=Label(window,text="{}".format(IceCreamStand1.info()),fg='pink',)
name.pack()
window.mainloop()