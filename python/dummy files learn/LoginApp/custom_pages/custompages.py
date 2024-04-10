from tkinter import *
from re import search

class LabeledEntry(LabelFrame):
	""" just like labeledEntry but having a bottom label to display any alert or messages 
		
		lbltext =>  for entry box title
		
		imglocation => to display any icon (pass location of image only)
		
		password_mode => by default False to on pass tuple containig (True,what to show instead chars) => (True,"*")

		char_counter => counts the number of character input (by default false)

		"""
	def __init__(self,parent, lbltext,imglocation='',password_mode=False,char_counter=False,*args, **kwargs):
		LabelFrame.__init__(self,parent,*args, **kwargs)
		self.configure(text=lbltext,bd=0)
		
		self.password_mode = password_mode
		self.entryVar=StringVar()
		#get parent frame color
		colr = self['bg']
		#label to diaplay input box icon
		self.imglbl=Label(self,anchor='nw', **kwargs)
		self.imglbl['bg']=colr
		self.entry = Entry(self,textvariable=self.entryVar,borderwidth=1,font=('Arial',11),
				highlightthickness=0,relief='flat',width=18,**kwargs)
		self.entry['bg']=colr
		#to display messages on the bottom is anu error occurs 
		self.errormessage=Label(self,fg='red',bd=0,font=('',8), anchor='nw',**kwargs)
		#to create bottom line effect 
		self.lining = Frame(self,relief='raised',bg='black')
		
		self.char_counter = Label(self,fg='green',text=0, bd=0, **kwargs)
		self.char_counter['bg']=colr		

		if imglocation!='':
			self.im=PhotoImage(file=imglocation)
			self.imglbl['image']=self.im
			self.imglbl.image=self.im
		#bind functions
		self.entry.bind('<FocusIn>',self.Focusin)
		self.entryVar.trace('w',self.count_chars)
		#pack widgets
		self.errormessage.pack(side='bottom',fill='x',expand=1)
		self.lining.pack(side='bottom',fill='x',anchor='nw', expand=1)
		self.imglbl.pack(anchor='nw',side='left')
		if char_counter:self.char_counter.pack(anchor='nw',side='right')
		self.entry.pack(fill='x',anchor='nw')
		
		if not self.password_mode == False:
			self.entry['show']= self.password_mode[1]
			self.entry.bind("<Button-3>",self.show_psw)
			self.entry.bind("<ButtonRelease-3>",self.hide_psw)

	def get(self):
		return self.entryVar.get()

	def Focusin(self,event):
		#if input box gets the focus claer alert message
		self.errormessage['text']=''
		self.lining['bg']='black'
	def err(self, txt):
		self.errormessage['text']=txt
		self.lining['bg']='red'

	def show_psw(self,event):
		self.entry['show']=''

	def hide_psw(self,event):
		self.entry['show']= self.password_mode[1]

	def count_chars(self,a,b,c):
		self.char_counter['text']=len(self.entryVar.get())






class Register_Page( Frame ):

	def __init__(self, parent):
		Frame.__init__(self , parent)

		self.bg = PhotoImage(file='media/bg/reg.png')
		self.close_img = PhotoImage(file='media/icons/close.png')

		Label(self, image=self.bg, bd=0).pack()

		Button(self,image=self.close_img, bd=0, bg='#b4d1df', activebackground='#b4d1df', command= lambda : self.destroy() ).place(x=670, y=2)

		self.fname = LabeledEntry(self, "First Name")
		self.fname.place(x=170, y=110)

		self.lname = LabeledEntry(self, "Last Name")
		self.lname.place(x=360, y=110)

		self.email = LabeledEntry(self, "Email id")
		self.email.entry['width']=42
		self.email.place(x=170, y=192)

		self.psw = LabeledEntry(self, "Password ",password_mode=(True, "#"), char_counter=True)
		self.psw.place(x=170, y=280)

		self.re_psw = LabeledEntry(self, "Retype Password ",password_mode=(True, "#"), char_counter=True)
		self.re_psw.place(x=360, y=280)

		self.submit_button = Button(self, text="Submit",fg='blue', bd=0, width=20, command=self.check_form)
		self.submit_button.place(x=280, y=360)
	
	def check_form(self):
		a = [self.fname,self.lname, self.email, self.psw , self.re_psw ]

		vals = []
		for widgets in a:
			if widgets.get()=="":
				widgets.err("This is a required field!")
			else:
				vals.append(widgets.get())

		v = search("""^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$""", self.email.get())

		if v:
			print(vals)
			return vals
		else:
			self.email.err("Enter a valid email!")

		



		



class Login_Page( Frame ):
	def __init__(self, parent):
		Frame.__init__(self , parent)

		#set background
		self.bg = PhotoImage(file='media/bg/loginPage.png')

		Label(self, image=self.bg, bd=0).pack()

		self.ID = LabeledEntry(self, "User id","media/icons/user.png")
		self.ID.place(x=180, y=160)
		self.ID.entry['width']=30

		self.psw = LabeledEntry(self, "Password " ,"media/icons/key.png", password_mode=(True, "*"), char_counter=True)
		self.psw.place(x=180, y=230)
		self.psw.entry['width']=29
		#show a warning
		self.psw.err("Right Click to see password!")

		save_psw = Checkbutton(self, text='Save Password')
		save_psw.place(x=180, y = 300)

		Button(self, text='Login', bg='#64dfdf',  bd=0, width=16, height=1, command=self.retunInput).place(x=180, y=340)
		
		self.regbtn = Button(self, text='Register', bg='#11698e',  bd=0, width=16, height=1 )
		self.regbtn.place(x=320, y=340)

	def retunInput(self):
		Id = self.ID.get()
		psw = self.psw.get()

		if Id == '':
			self.ID.err('This is a required field!')
		elif psw == '':
			self.psw.err('This is a required field!')
		else:
			return ( Id, psw)