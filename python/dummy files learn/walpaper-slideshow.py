import os
import ctypes
from threading import Thread
from time import sleep
from tkinter import *


photo_dir = r"D:\walpaper"
sleep_time = 10  #decreasing the sleep time increases CPU usage and may lower pc perfomance
#so it is recommended to keep at least 10 seconds sleep time
def a():
	global sleep_time
	p = os.listdir(photo_dir)
	c = 0
	while c <= len(p):
		try:
			img_path = p[c]
			j_path = os.path.join(photo_dir,img_path)
			ctypes.windll.user32.SystemParametersInfoW(20, 0, j_path , 0)
			sleep(sleep_time)
		except:
			pass

		c+=1
		if c >= len(p):
			c = 0

def increase_speed():
	global sleep_time
	if not (sleep_time-1) <= 1: sleep_time -= 1
def decrease_speed():
	global sleep_time
	sleep_time += 1

root = Tk()
root.overrideredirect(True)
m = Menu(root, tearoff=0)
m.add_command(label="Increase Speed", command = increase_speed)
m.add_command(label="Decrease Speed", command = decrease_speed)
m.add_command(label="Exit",command=root.destroy)

def f(e):
	m.post(e.x_root,e.y_root)

def move_widget(e):
	root.geometry("+{}+{}".format(e.x_root, e.y_root))


img = PhotoImage(file="p.png")

l = Label(root, image=img,bg='#ddd')
l.image = img
l.pack()
l.bind("<Button-3>", f)
l.bind("<B1-Motion>",move_widget)

root.wm_attributes("-transparentcolor","#ddd")
t = Thread(target=a, daemon=True)
t.start()

root.mainloop()