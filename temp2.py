from tkinter import *

win = Tk()
win.geometry("300x100")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack()


def ent_p():
    a = ent.get()
    print(a)

btn = Button(win)
btn.config(text = "로또 당첨 번호 확인")
btn.config(command= ent_p)
btn.pack()


win.mainloop()