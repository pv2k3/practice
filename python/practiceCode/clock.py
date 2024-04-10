from time import *
from tkinter import *

def get_time():
    return strftime("%I : %M : %S")

root = Tk()
root.title("Clock")
root.geometry("+500+100")

l = Label(root, text=get_time(), font="Jokerman 40", fg="cyan", bg="blue")
l.pack()

try:
    while True:
        time = get_time()
        l['text'] = time
        root.update()
except:
    print("Exit")

root.mainloop()
