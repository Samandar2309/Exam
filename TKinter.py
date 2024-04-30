from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('TKinter')


def Hello():
    print('Hello')


btn = Button(root, text='Hello', background='green', fg='black', command=Hello)
btn.place(x=10, y=100)
root.mainloop()
