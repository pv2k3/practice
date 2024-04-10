import cv2 as cv
from tkinter import *
from tkinter.filedialog import asksaveasfile

root = Tk()
root.title('My Camera created bt @Elsker Elvish')

run =True #for infinite loop
cam_port = 0
image_name = "myimage.png"
cam = cv.VideoCapture(cam_port) #start the camera

display_label = Label(root)
display_label.pack(fill='both',expand=1)

capture_btn = Button(root,text='Capture')
capture_btn.place(x=300,y=450)

def configureLabel(image_location):
	""" configures the label and changes the image of every frame """
	v = PhotoImage(file=image_location) #load tk image
	display_label['image']=v #configure the label to change image
	display_label.image = v
	#change the icon of parent window continuesly
	root.iconphoto(False, v)

def save_image():
	#ask where to save the image
	files = [ ('PNG', '*.png'),  ('JPG', '*.jpg'),  ('JPEG', '*.jpeg') ] 
	location = asksaveasfile(filetypes = files, defaultextension = files) 
	
	if not location.name == "":
		print('saving image...', location.name)
		cv.imwrite(location.name, data)
		print('saved..')
	else: print('Saving Canceled...')

def turn_off(e=None):
	global run
	run=False
	#release the opened camera 
	cam.release()
	#save file
	save_image()

capture_btn.configure(command=turn_off)
root.bind("<Return>",turn_off) #captire on click Enter button

while run:
	#read every frame of the camera
	ret, data = cam.read()
	#save in image in png i.e (image_name) format
	cv.imwrite(image_name, data)
	#configure the look!
	configureLabel( image_name )	

	#update root everytime to overcome not responding!
	root.update()
	#may use this
	root.update_idletasks()

root.mainloop()

#created by @Elsker Elvish.py