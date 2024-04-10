import tkinter as tk
from smtplib import SMTP
from tkinter.messagebox import askyesno

class LabeledEntry(tk.LabelFrame):
	""" just like labeledEntry but having a bottom label to display any alert or messages """
	def __init__(self,parent, lbltext,imglocation='',*args, **kwargs):
		tk.LabelFrame.__init__(self,parent,*args, **kwargs)
		self.configure(text=lbltext,bd=0)
		
		self.entryVar=tk.StringVar()
		#label to diaplay input box icon
		self.imglbl=tk.Label(self,anchor='nw', **kwargs)
		self.entry = tk.Entry(self,textvariable=self.entryVar,borderwidth=1,font=('Arial',11),highlightthickness=0,relief='flat',width=18,**kwargs)
		#to display messages on the bottom is anu error occurs 
		self.errormessage=tk.Label(self,fg='red',bd=0,font=('',8), anchor='nw',**kwargs)
		#to create bottom line effect 
		self.lining = tk.Frame(self,relief='raised')
		
		if imglocation!='':
			self.im=tk.PhotoImage(file=imglocation)
			self.imglbl['image']=self.im
			self.imglbl.image=self.im
		#bind functions
		self.entry.bind('<FocusIn>',self.Focusin)
		#pack widgets
		self.imglbl.pack(anchor='nw',side='left',fill='y')
		self.entry.pack(anchor='nw',side='top',fill='both',expand=1)
		self.lining.pack(side='top',fill='x')
		self.errormessage.pack(side='top',fill='x')

	def get(self): return self.entryVar.get()
	def Focusin(self,event):
		#if input box gets the focus claer alert message
		self.errormessage['text']=''
		self.lining['bg']='white'
	def err(self, txt):
		self.errormessage['text']=txt
		self.lining['bg']='red'


class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		#background  500x500
		self.bg_img = tk.PhotoImage(file='pc.png')
		tk.Label(self, image = self.bg_img).pack()
		tk.Label(self, text='With love from Elsker Elvish.py').pack()

		self.login_frame()

	def login_frame(self):
		self.window = tk.Frame(self)
		self.window.place(x=280,y=100)
		
		self.uid = LabeledEntry(self.window, "Email", 'user.png')
		self.uid.pack(pady=20,padx=20)
		
		self.psw = LabeledEntry(self.window, "Password",'key.png')
		self.psw.pack(pady=20,padx=20)
		self.psw.entry['show']='*'
		self.psw.err("Right click to see password!")
		self.psw.entry.bind("<Button-3>",self.show_psw)
		self.psw.entry.bind("<ButtonRelease-3>",self.hide_psw)

		tk.Button(self.window, text='Login',bg='#9ff',relief='ridge',
								command=self.on_login).pack(fill='x',pady=20,padx=20)

	def on_login(self):
		uid = self.uid.get().lower().strip()
		psw = self.psw.get().strip()

		if uid == '' or psw=='':
			self.uid.err("This is required field")
			self.psw.err("This is required field")
		else:
			try:
				#port no of google mail  587
				self.id_login = SMTP('smtp.gmail.com', 587)
				#starttls() for security layer
				self.id_login.starttls() 
				#login to user provided id
				ret=self.id_login.login(uid, psw)
				
				#destroy login window and create new window for message typing
				self.window.destroy()
				self.message_window(uid)
			except Exception as e:
				print(e)
				self.psw.err("Invalid user name or password")

	def message_window(self,email):
		tk.Label(self,text=email).place(x=20,y=10)

		send_to = LabeledEntry(self, 'To ')
		send_to.place(x=20,y=50)

		txt = tk.Text(self,height=20,width=57)
		txt.place(x=20,y=100)

		def send_message():
			message = txt.get(1.0,tk.END)
			self.id_login.sendmail(email, send_to.get(), bytes(message, encoding='utf-8'))
			
			ans = askyesno(title="Info",message='message sent Successfully',detail="Want to close?")
			if ans:
				self.id_login.quit()
				self.destroy()
		
		tk.Button(self, text='Send',bd=0, bg='#9ff', width=20,command=send_message).place(x=180,y=450)

	def show_psw(self,event):
		self.psw.entry['show']=''
	def hide_psw(self,event):
		self.psw.entry['show']='*'


if __name__ == "__main__":
	ap = App()
	ap.resizable(0,0)
	ap.title("Email App with love from Elsker_Elvish.py")
	ap.mainloop()