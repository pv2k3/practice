from tkinter import *
import sqlite3
import tkinter.messagebox as mb
from tkinter import filedialog
import cv2 as cv
from PIL import Image as PILimage

def showPassword(event):
	wdgt=event.widget
	wdgt['show']=''

def hidePassword(event):
	wdgt=event.widget
	wdgt['show']='*'

def file2binary(filename):
	#read file in binary mode
	with open(filename, 'rb') as f:
		bin_data=f.read()
		#close opened folder
		f.close()
	return bin_data

def binary2file(bin_data,filename_withExtesion):
	with open(filename_withExtesion,'wb') as f:
		#write in binary mode
		f.write(bin_data)
		f.close()
	return True






class LabeledImage(LabelFrame):
	""" Label com=ntainig a image view label and buttons like to choose images from files or capture images from camera """
	def __init__(self,parent,lbltext,subsample,image_size,*args,**kwargs):
		LabelFrame.__init__(self,parent,*args,**kwargs)
		#set LabelFrame text  property
		self['text']=lbltext
		#attributes
		self._P=parent
		self.subsample=subsample
		self.image_size=image_size
		#image path of uploaded as profile
		self.return_image_location=''
		self.default_image_to_be_shown=r'media/edit_user.png' #set a default value
		#icons used
		self.file=PhotoImage(file='media/folder.png')
		self.cam=PhotoImage(file='media/capture.png')
		self.close_mark=PhotoImage(file='media/close_no_bg.png')
		
		#images displaying label
		self.imglbl = Label(self,bd=0)
		self.remove_photo=Button(self,image=self.close_mark,bd=0,command=self.remove_photo)
		#buttons
		self.btn_container=Label(self)

		btn_configs={'relief':'flat','width':65,'compound':'left','overrelief':'ridge','activebackground':'cyan'}

		self.from_cameraBtn = Button(self.btn_container,text='Camera',command=self.TakePhoto,image=self.cam,**btn_configs)
		self.from_cameraBtn.pack(side='left')

		self.from_fileBtn = Button(self.btn_container,text='Files',command=self.choose_photo,image=self.file,**btn_configs)
		self.from_fileBtn.pack()

		#packing labels
		self.btn_container.pack(side='bottom',fill='x')
		self.imglbl.pack(side='top',fill='both')

		self.remove_photo.place(x=128)
		#set default image to the label
		self.image_resize(self.default_image_to_be_shown)

	def set_photo(self,path):
		x,y=self.subsample
		set_image=PhotoImage(file=path).subsample(x,y)
		self.imglbl.configure(image=set_image)
		self.imglbl.image=set_image
		#change Values 
		self.return_image_location=path

	def image_resize(self,path):
		print('resizing image')
		#image direatory nad name
		imageName='media/cache/from_resized.png'
		#open image and resize
		resized_image=PILimage.open(path).resize(self.image_size)
		resized_image.save(imageName)#save to cache dir
		#dsiplay this image on the image label
		self.set_photo(imageName)

	def TakePhoto(self):
		camport = 0 #deault 0 opens pc's camera
		camera = cv.VideoCapture(camport)
		while True:
			returnVal,cameraImageRead = camera.read() #read image
			cv.imshow('Camera, Press q to capture', cameraImageRead) #show image in window
			key=cv.waitKey(1)  #wait for key press 
			if key==ord('q'): # qiut is pressed q
				break
		#close frame
		cv.destroyAllWindows()
		#close camera
		del(camera)
		#directory where images will be saved as cache
		lcn='media/cache/from_cam_origial.png'
		#write image
		cv.imwrite(lcn, cameraImageRead)
		#resize image now 
		self.image_resize(lcn)

	def choose_photo(self):
		file_seleceted=filedialog.askopenfilename(title='Choose photo',filetypes=( ('PNG','*.png *.jpg *.jpeg'), ('All files','*.*') ))
		print(file_seleceted)
		if file_seleceted:self.image_resize(file_seleceted)

	def remove_photo(self):
		self.image_resize(self.default_image_to_be_shown)
		self.return_image_location=''



class LabeledEntry(LabelFrame):
	"""label fram containig a entry and error display label and a label to add image 
	some parameters:
	parent,
	lbltext :  acts as placeholder,
	err_msg :  by default none if wanted to warn add values get erased as Entry get the focus
	imglcn:  location for icon 
	 """
	def __init__(self,master,lbltext,err_msg,imglcn=None,*args,**kwargs):
		LabelFrame.__init__(self,master,*args,**kwargs)
		self.config(bd=0,text=lbltext)

		self.lbltext=lbltext
		self.err_msg=err_msg

		#variable to hold entry data
		self.Entry_var=StringVar()

		self.ico=PhotoImage(file=imglcn)
		self.imglbl=Label(self,bd=0,image=self.ico,**kwargs)

		self.entry = Entry(self,bd=0,width=35,font=('',12),textvariable=self.Entry_var,bg='#2bc878')
		#frame draws a line just below entry
		self.line=Frame(self,bd=0,width=50,height=2,bg='black')
		#id any error occurs use this to deiplay
		self.error=Label(self,bd=0,fg='white',anchor='nw',text=self.err_msg,**kwargs)

		#packing labels
		self.error.pack(side='bottom',anchor='nw',fill='x')
		self.imglbl.pack(side='left',anchor='nw',fill='y',ipadx=8)
		self.entry.pack(anchor='nw',fill='both',expand=1)
		self.line.pack(anchor='nw',fill='x')
		#binnding
		self.entry.bind("<FocusIn>",self.F_in)
		self.entry.bind("<FocusOut>",self.F_out)
	def F_in(self,event):
		if self.Entry_var.get()==self.lbltext:
			pass
		else:
			self.error['text']=' '
			self.line['bg']='black'
	def F_out(self,event):
		#if entry is empty
		if self.Entry_var.get().strip()=='':
			self.line['bg']='red'
			self.error['text']='\tthis is required field'



class ViewUser(LabelFrame):
	def __init__(self,parent,lbltext,dbData,*args,**kwargs):
		LabelFrame.__init__(self,parent,*args,**kwargs)
		self['text']=lbltext

		fname,lname,psw,imagebin=dbData[0]

		imageName='media/cache/login_cache img.png'
		img_lcn=binary2file(imagebin,imageName) #write image from binary

		#image 
		self.i=PhotoImage(file=imageName)
		self.close_mark=PhotoImage(file='media/close_no_bg.png')

		Button(self,image=self.close_mark,command=self.destroy).pack()

		n=f" Name : {fname} {lname} \n Password : {psw}"
		Label(self,image=self.i,compound='top',text=n).pack()




class LoginPage(Frame):
	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent,*args,**kwargs)
		#change title
		self.master.title('Login System - (Elsker Elvish)')
		#icons used
		self.bg=PhotoImage(file='media/g898.png')
		self.intr=PhotoImage(file='media/internet.png')
		self.wa=PhotoImage(file='media/whatsapp.png')
		self.fb=PhotoImage(file='media/facebook.png')

		#main background image
		Label(self,image=self.bg).pack()


		#take id input and password
		self._id  = LabeledEntry(self,'Your first name here.','','media/users.png',**{'bg':'#2bc87c'})
		self._id.place(x=40,y=300)

		self.psw  = LabeledEntry(self,'Password','','media/users.png',**{'bg':'#2bc87c'})
		self.psw.entry['show']='*' # hiide typing charcters
		self.psw.place(x=40,y=390)
		#show password
		self.psw.entry.bind("<Button-3>",showPassword)
		#on release
		self.psw.entry.bind("<ButtonRelease-3>",hidePassword)
		#login butto
		self.login_btn=Button(self,text='Login',font=('arial',22),width=9,fg='#2bc87c',bg='#020e52',activebackground='#020e52',bd=0)
		self.login_btn.place(x=3,y=480)

		#reber password button
		Checkbutton(self,font=('arial',13),text='Save password?',bg='#2bc87c').place(x=200,y=470)
		#if forgt password
		Button(self,text='Click if you forgot password',font=('arial',13),fg='blue',bg='#2bc87c',bd=0).place(x=200,y=505)
		#register button
		self.register_btn=Button(self,text='Register',font=('arial',22),width=9,fg='#2bc87c',bg='#020e52',activebackground='#020e52',bd=0)
		self.register_btn.place(x=300,y=560)

		#social media buttons 
		Button(self,image=self.intr,bg='#2bc87c',bd=0).place(x=100,y=554)
		Button(self,image=self.fb,bg='#2bc87c',bd=0).place(x=12,y=554)
		Button(self,image=self.wa,bg='#2bc87c',bd=0).place(x=190,y=554)
		#attribution
		Label(self,text='Designed and developed by Elsker Elvish',bg='#2bc87c',font=('arial',13)).place(x=3,y=660)




#register page interface for the app
class RegisterPage(Frame):
	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent,*args,**kwargs)
		#change title
		self.master.title('Register - (Elsker Elvish)')
		#icons used
		self.bg=PhotoImage(file='media/g898.png')
		self.intr=PhotoImage(file='media/internet.png')
		self.wa=PhotoImage(file='media/whatsapp.png')
		self.fb=PhotoImage(file='media/facebook.png')

		#main background image
		Label(self,image=self.bg).pack()

		self.user_image=LabeledImage(self,'User Image',(1,1),(143,143))
		self.user_image.place(x=155,y=51)
		#take id input and password
		default={'bg':'#2bc87c'}
		self.fname  = LabeledEntry(self,'First name','','media/users.png',**default)
		#lower the width of entry
		self.fname.entry['width']=15
		self.fname.place(x=40,y=300)

		self.lanme  = LabeledEntry(self,'Last name','','media/users.png',**default)
		#lower the width of entry
		self.lanme.entry['width']=15
		self.lanme.place(x=220,y=300)


		self.psw  = LabeledEntry(self,'Password','','media/users.png',**default)
		#lower the width of entry
		self.psw.entry.config(width=15,show='*')
		self.psw.place(x=40,y=390)

		self.retype_psw  = LabeledEntry(self,'Retype password','','media/users.png',**default)
		#lower the width of entry
		self.retype_psw.entry.config(width=15,show='*')
		self.retype_psw.place(x=220,y=390)
		#bind a function to hide or show password on right click
		#on press
		self.retype_psw.entry.bind("<Button-3>",showPassword)
		#on release
		self.retype_psw.entry.bind("<ButtonRelease-3>",hidePassword)

		#login butto
		self.register_btn=Button(self,text='Register',font=('arial',22),width=9,fg='#2bc87c',bg='#020e52',
								activebackground='#020e52',bd=0)
		self.register_btn.place(x=3,y=480)
		#register btn
		self.login_btn=Button(self,text='Login',font=('arial',22),width=9,fg='#2bc87c',bg='#020e52',
									activebackground='#020e52',bd=0)
		self.login_btn.place(x=300,y=560)

		#social media buttons 
		Button(self,image=self.intr,bg='#2bc87c',bd=0).place(x=100,y=554)
		Button(self,image=self.fb,bg='#2bc87c',bd=0).place(x=12,y=554)
		Button(self,image=self.wa,bg='#2bc87c',bd=0).place(x=190,y=554)
		#attribution
		Label(self,text='Designed and developed by Elsker Elvish',bg='#2bc87c',font=('arial',13)).place(x=3,y=660)
	def on_register(self):
		a=self.fname.Entry_var.get().strip() #remove spaces before and after usinf strip()
		b=self.lanme.Entry_var.get().strip() #remove spaces before and after usinf strip()
		c=self.psw.Entry_var.get().strip() #remove spaces before and after usinf strip()
		d=self.retype_psw.Entry_var.get().strip() #remove spaces before and after usinf strip()
		image_binary=file2binary(self.user_image.return_image_location)
		if a==b==c==d=='':
			mb.showinfo(message='All fields are required')
		elif c!=d:
			mb.showinfo(message='Retyped password did not matched')
		else:
			db=sqlite3.connect("myDatabse.db")#connect to databse

			# Qry_for_creating tables = """ CREATE TABLE Register(
			# Fname varchar(100),
			# Lname varchar(100),
			# Psw   varchar(100)
			#  )  """

			Qry="""INSERT INTO Register(Fname,Lname,Psw,ImageBin) VALUES(?,?,?,?)"""
			entry_vals=(a,b,c,image_binary)
			
			cursor=db.cursor()#create cursor
			cursor.execute(Qry,entry_vals)#execute the query using the cursor
			db.commit()#commit all changes to database
			
			ask=mb.askyesno(message='Regsitration was succesfull!',detail='Do you want to Login!')
			return ask


