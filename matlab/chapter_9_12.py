from tkinter import *

click_count = 0

def clicked():
    global click_count
    click_count = click_count + 1
    lbl.configure(text=f'Кнопка нажата: {click_count}')
window = Tk()
window.title(f'Кнопка нажата: {click_count}')
window.geometry('350x200')
lbl = Label(window, text="Привет!")
lbl.grid(column=0, row=0)
btn = Button(window, text="Нажми меня", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()

