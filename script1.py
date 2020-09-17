from tkinter import *

window = Tk()


def km_to_miles():
    text.insert(END, float(e1_value.get()) * 1.6)


button = Button(window, text="Execute", command=km_to_miles)

button.grid(row=0, column=0)
e1_value = StringVar()

e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

text = Text(window, height=1, width=20)
text.grid(row=0, column=2)
window.mainloop()
