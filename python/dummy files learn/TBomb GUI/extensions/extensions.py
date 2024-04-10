import tkinter as tk
from . import resources as res
from tkinter.messagebox import showinfo
# from concurrent.futures import ThreadPoolExecutor, as_completed

# class BomberStatus( tk.Frame):
	# yet to be updated...

# 	def __init__(self, parent ):
# 		tk.Frame.__init__(self,parent,bd=2, relief="ridge", width=500, height=400, bg='yellow')


# 	def workernode(self, mode, cc_phone, n_sms, delay, max_threads):
# 		api = APIProvider(cc_phone[0], cc_phone[1], mode, delay=delay)
# 		msg=f"""
#     Gearing up the Bomber - Please be patient

#     Please stay connected to the internet during bombing")
    
#     API Version  : {api.api_version}
#     Target       : {cc_phone[0] + cc_phone[1] }
#     Amount       : {str(n_sms)}
#     Threads      : {str(max_threads)} threads 
#     Delay        : {str(delay)} seconds

#     # This tool was made for fun and research purposes only.
#     """
#     	if len(APIProvider.api_providers) == 0:
#     		print("Your country/target is not supported yet")
#     		print("Feel free to reach out to us")
#     		sys.exit()

#     	success, failed =  0,0
#     	while success < n_sms:
#     		with ThreadPoolExecutor(max_workers=max_threads) as executor:
#     			jobs = []
#     			for i in range(n_sms-success):
#                 jobs.append(executor.submit(api.hit))

#             for job in as_completed(jobs):
#                 result = job.result()
#                 if result is None:
#                     print( "Bombing limit for your target has been reached")
#                     print("Try Again Later !!... exiting now")
#                     sys.exit()
#                 if result:
#                     success += 1
#                 else:
#                     failed += 1
#                 # clr()
#                 print(f"Target: +{cc_phone[0]+cc_phone[1]}\n Success :{success}\n Failed :{failed} ")
#     print("\n")
#     return "Bombing completed!"
#     sys.exit()





# 	def get_mail_info(self, target):
# 		mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# 		while True:
# 			if not re.search(mail_regex, target, re.IGNORECASE):
# 				msg = (False,"The mail ({target})".format(target=target) + " that you have entered is invalid")
# 				continue
# 			return msg + (target, )


class OPButtons(tk.Frame):
	def __init__(self, parent, lbl, img, descpn,command, *args, **kwargs):
		tk.Frame.__init__(self, parent,*args,**kwargs)

		self.img = tk.PhotoImage(file=img)

		self.logo = tk.Label(self, image=self.img, bd=0)
		self.logo.pack(side='left', fill='y',padx=10, pady=10)

		container = tk.Frame(self,height=120,width=460, padx=15, pady=15)
		container.pack(side='right', fill='both', expand=1)

		l1 = tk.Label(container, text=lbl, font=("",15))
		l1.place(x=0, y=0)
		l2 = tk.Label(container, text=descpn,font=("",11))
		l2.place(x=0, y=30)

		self.btn  = tk.Button(container, bd=0, fg='blue', text=f'Start {lbl.lower()}' , command=command)
		self.btn.place(x=290, y=70)

		self.wids  =  [self, self.logo, container, l1, l2 ,self.btn ]

		self.hover_out(None)

		self.bind("<Enter>", self.hover_in)
		self.bind("<Leave>", self.hover_out)
	def hover_in(self, e=None):
		for w in self.wids: w['bg'] = '#ccc'
	def hover_out(self, e):
		for w in self.wids: w['bg'] = '#ddd'

class LabeledEntry(tk.LabelFrame):
	""" just like labeledEntry but having a bottom label to display any alert or messages 
		lbltext =>  for entry box title
		imglocation => to display any icon (pass location of image only)
		"""
	def __init__(self,parent, lbltext,imglocation='',*args, **kwargs):
		tk.LabelFrame.__init__(self,parent,*args, **kwargs)
		self.configure(text="     ",bd=0)

		self.lbltext = lbltext
		self.entryVar=tk.StringVar()
		self.entryVar.set(lbltext)
		#get parent frame color
		colr = self['bg']
		#label to diaplay input box icon
		self.imglbl=tk.Label(self,anchor='nw', **kwargs)
		self.entry = tk.Entry(self,textvariable=self.entryVar,fg='#999', bd=0,font=('Arial',11), width=18,**kwargs)
		self.entry['bg']=colr
		#to display messages on the bottom is anu error occurs 
		#to create bottom line effect 
		self.lining = tk.Frame(self,relief='raised',bg='black')
	

		if imglocation!='':
			self.im=tk.PhotoImage(file=imglocation)
			self.imglbl['image']=self.im
			self.imglbl.image=self.im
		#bind functions
		self.entry.bind('<FocusIn>',self.Focusin)
		self.entry.bind('<FocusOut>',self.FocusOut)
		#pack widgets
		self.lining.pack(side='bottom',fill='x',anchor='nw', expand=1)
		self.imglbl.pack(anchor='nw',side='left')
		self.entry.pack(fill='both',expand=1,anchor='nw')

	def get(self):
		return self.entryVar.get().strip()

	def Focusin(self,event):
		#if input box gets the focus claer alert message
		if self.get() == self.lbltext:
			self.entryVar.set("")
			self['text']= self.lbltext
			self.entry['fg'] = "#000"
			
	def FocusOut(self,e):
		if self.get() == "":
			self["text"] = "     "
			self.entry['fg'] = "#999"
			self.entryVar.set(self.lbltext)

class CallBombingUI( tk.Frame ):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)


		tk.Label(self, text="SMS Bombing",bd=0, font=("",45)).place(x=5,y=10)


		self.c_code = LabeledEntry(self,"Your country code (Without +)")
		self.c_code.entry['width'] = 50
		self.c_code.place(x=80, y=100)

		self.mn = LabeledEntry(self,"Target mobile number")
		self.mn.entry['width'] = 50
		self.mn.place(x=80, y=170)

		self.n_sms = LabeledEntry(self,"Number of SMS to send (Max 500)")
		self.n_sms.entry['width'] = 50
		self.n_sms.place(x=80, y=240)

		self.delay = LabeledEntry(self,"Delay time (in seconds)")
		self.delay.entry['width'] = 50
		self.delay.place(x=80, y=310)

		self.n_threads = LabeledEntry(self,"Number of Thread (Recommended: 1)")
		self.n_threads.entry['width'] = 50
		self.n_threads.place(x=80, y=390)

		self.start_btn = tk.Button(self,text="Start", bd=1, relief="ridge",font=("",12), padx=50,fg="blue",command=self.confirm_bombing_details)
		self.start_btn.place(x=200, y= 450,)

		self.master.bind("<Return>", self.confirm_bombing_details)

	def confirm_bombing_details(self, e=None):
		from tkinter.messagebox import askyesno

		ans = askyesno(title="Gearing up the Bomber..",
			message=f"""
Please stay connected to the internet during bombing

	API Version	: 2.3
	Target		: {self.mn.get()}
	Amount		: {self.n_sms.get()}
	Threads		: {self.n_threads.get()}
	Delay		: {self.delay.get()} seconds

This tool was made for fun and research purposes only
			""", detail="Do you wish to continue?")


		if ans:
			self.start_btn["state"] = "disabled"
			self.start_btn["text"] = "Bombing is in progress please wait...."
			self.update()


			# new = BomberStatus(self)
			# new.place(x=30,y=90)
			ret = res.selectnode("sms", 
				( self.c_code.get(), self.mn.get() ), 

				int(self.n_sms.get()), 
				int(self.delay.get()), 
				int(self.n_threads.get())
				)

			showinfo(title="TBomb", message=ret)
			self.start_btn["state"] = "normal"
			self.start_btn["text"] = "Start"
			self.update()
		else:
			pass


	def start_bombing(self):
		pass