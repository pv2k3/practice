from threading import Thread
import time
from tkinter import *

def getTime():
	return time.strftime("%I:%M:%S")

root = Tk()
root['bg'] = "#ddd"

root.geometry("+1000+15")

root.overrideredirect(True)
root.wm_attributes()
root.title("Watch")

l = Label(root, text=getTime(), font=("Jokerman", 40), bg="#ddd", fg="red")
l.pack()

#start thread to update time every seconds...

def timeUpdate():
		#to update label 
	while True:
		time = getTime()
		l['text'] = time
		root.update()

# t = Thread(target=timeUpdate)
# t.start()
# the above thread will work properly but will raise an error
# as you close your appliction because root will be destroyed and as
# the l['text']=time function will going to execute there is no
# window to update (app closed). so either you can use exception handelling or:

t = Thread(target=timeUpdate, daemon=True, name="Watch")
t.start()

# metioning daemon= True it will automatically close itself as the main process relted with 
# it gets closed here main process is reference to Tk()

root.mainloop()
