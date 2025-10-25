from tkinter import *

root = Tk()
root.title("Student Mark List")
root.geometry("500x400")

l = Label(root, text="Username")
l.pack()  
e = Entry(root)
e.pack()

b = Button(root, text="Login")
b.pack()

root.mainloop()
