from tkinter import (
					Frame,
					Scrollbar,
					Canvas,
					Entry,
					LabelFrame,
					Tk,
					StringVar,
					PhotoImage,
					Label,
					Button
						)
from time import sleep
from threading import Thread
from PIL import Image, ImageTk






class ScrollingFrame( Frame ):
	""" Frame with x and y scrollbars add contents  using  <object-name>.container
		
		Required parameters - 

					parent_window , scroll_region = Tuple(width, height)
					[,*args, **kwargs] and configurations. 
		
		WIDGET-SPECIFIC OPTIONS -  
					X_scroll (by default True) pass False to hide bottom scroll bar
					Y_scroll (by default True) pass False to hide left scroll bar
					
		"""


	def __init__(self,parent,scroll_region,X_scroll=False,Y_scroll=True,*args ,**kwargs):
		Frame.__init__(self,parent)

		self.configure(bd=2, relief="groove")

		self.region = scroll_region
		
		if Y_scroll: #if True
			self.y_scroll=Scrollbar(self,orient="vertical")
			self.y_scroll.pack(side="right",fill="y")
		
		if X_scroll:
			self.x_scroll=Scrollbar(self,orient="horizontal")
			self.x_scroll.pack(side="bottom",fill="x", anchor='nw')
		
		self.canvas=Canvas(self,relief="ridge",**kwargs) 
		self.canvas.pack(side="top")
		#used canvas here because after Listbox() and Text() widgets Canvas() is only widget which supports yscrollcommand
		# or xscrollcommand parameters and can be used to add widgets too... 
		#by using create_window((pos x, pos y), window=window_name) created a frame inside and bounded the frames in a limited region
		#if region exceeded scrollbars will be active

		if Y_scroll:
			self.canvas.configure(yscrollcommand=self._set_scrollbary)
			self.y_scroll.configure( command=self.canvas.yview )
		
		if X_scroll:
			self.canvas.configure(xscrollcommand=self._set_scrollbarx)
			self.x_scroll.configure( command=self.canvas.xview )

		self.container=Frame(self.canvas, height=self.region[0], width=self.region[1]) #wideget continer...
		self.canvas.create_window((0,0),window=self.container,anchor='nw')
		self.container.bind("<Configure>",self._scroll)
		#configure is a event called when there is a change in size of a widgets
		#here <Configure> id called when size of container frame exceeded from specified scroll_region
	def _scroll(self,event):
		""" .bbox("all") >> Return a tuple of X1,Y1,X2,Y2 coordinates for a rectangle
        which encloses all items with tags specified as arguments."""
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=self.region[1], height=self.region[0])
	
	def _set_scrollbary(self,first, last):
		#manages Y scrolling.
		self.y_scroll.set(first, last)
		self.update() # to overcome not responding issues..
	
	def _set_scrollbarx(self,first, last):
		#manages X scrolling.
		self.x_scroll.set(first, last)
		self.update() # to overcome not responding issues..



class LabeledEntry(LabelFrame):
	""" 
		Just like labeledEntry but having a bottom label to display any alert or messages 
			lbltext =>  for entry box title and Placeholder
			
			imglocation => to display any icon (pass location of image only)
		
		
		WIDGET-SPECIFIC OPTIONS -

			password_mode => by default False to on pass tuple containig (True, what to show instead chars like "*") => (True,"*")
			char_counter => counts the number of character input (by default false)

			DEFAULT_UNDERLINE_CLR
			DEFAULT_ERR_CLR

		WIDGET-SPECIFIC METHODS -

			get() = returns Entry Value
			err("error message")

		"""
	
	def __init__(self,parent, lbltext,imglocation='',password_mode=False,char_counter=False,DEFAULT_UNDERLINE_CLR = "black", *args, **kwargs):
		LabelFrame.__init__(self,parent,*args, **kwargs)
		self.configure(text="     ",bd=0)
		
		self.password_mode = password_mode
		self.lbltext = lbltext
		self.entryVar=StringVar()
		self.entryVar.set(lbltext)

		self.DEFAULT_UNDERLINE_CLR = DEFAULT_UNDERLINE_CLR

		
		#get parent frame color
		colr = self['bg']
		#label to diaplay input box icon
		
		self.imglbl=Label(self,anchor='nw', **kwargs)
		
		self.entry = Entry(self,textvariable=self.entryVar,fg='#999', bd=0,font=('Arial',11), width=18,**kwargs)
		self.entry['bg']=colr
		
		#to display messages on the bottom is anu error occurs 
		self.errormessage=Label(self,bd=0,font=('',8), anchor='nw',**kwargs)
		
		#to create bottom line effect 
		self.lining = Frame(self,relief='raised',bg=self.DEFAULT_UNDERLINE_CLR)
		
		if char_counter: self.char_counter = Label(self,fg='green',text=0, bd=0, **kwargs)

		if imglocation!='':
			self.im=PhotoImage(file=imglocation)
			self.imglbl['image']=self.im
			self.imglbl.image=self.im
		
		#bind functions
		self.entry.bind('<FocusIn>',self._Focusin)
		self.entry.bind('<FocusOut>',self._FocusOut)
		
		if char_counter:self.entryVar.trace('w',self._count_chars)
		
		#pack widgets
		self.errormessage.pack(side='bottom',fill='x',expand=1)
		self.lining.pack(side='bottom',fill='x',anchor='nw', expand=1)
		self.imglbl.pack(anchor='nw',side='left')
		if char_counter:self.char_counter.pack(anchor='nw',side='right')
		self.entry.pack(fill='both',expand=1,anchor='nw')
		
		if self.password_mode:
			self.entry['show']= self.password_mode[1]
			self.entry.bind("<Button-3>",self._show_psw)
			self.entry.bind("<ButtonRelease-3>",self._hide_psw)

	
	def get(self):
		return self.entryVar.get().strip()

	def erase(self):
		#clear error message 
		self._Focusin(None)

	def _Focusin(self,event):
		#if input box gets the focus claer alert message
		self.errormessage['text']=''
		self.lining['bg']=self.DEFAULT_UNDERLINE_CLR
		if self.get() == self.lbltext:
			self.entryVar.set("")
			self['text']= self.lbltext
			self.entry['fg'] = "#000"
	
	def _FocusOut(self,e):
		if self.get() == "":
			self["text"] = "     "
			self.entry['fg'] = "#999"
			self.entryVar.set(self.lbltext)

	def err(self, txt, err_clr = "red"):
		self.errormessage['text']=txt
		self.errormessage['fg']=err_clr
		self.lining['bg']= self.DEFAULT_UNDERLINE_CLR
		self.update()
	
	def _show_psw(self,event): self.entry['show']=''
	def _hide_psw(self,event): self.entry['show']= self.password_mode[1]
	def _count_chars(self,a,b,c): self.char_counter['text']=len(self.entryVar.get())





class ElskerButton( Frame ):
	""" 
	A Button class created by Button and Frame widget to display gif images...
	
	parent   >>  root, 
	label    >>  text (to be displayed on the button),
	file     >>  gif (A gif file path),
	command  >>  command (command for button default None)
	duration >>  ( default=0.0299 ,sleep time in changing a simple frame), *args, **kwargs.
	infinite >>  default True runs infinitely  if False runs one time.
	"""

	def __init__(self,parent, text, gif,auto=False ,command=None,infinite=True, duration=0.02,*args,**kwargs):
		Frame.__init__(self, parent)
		self.gif_fp = gif
		self.duration = duration
		self.infinite = infinite
		
		self.new_frame = Image.open(self.gif_fp)
		self.no_of_frames = self.new_frame.n_frames

		self.ll = Label(self,text=text,compound='left', *args, **kwargs)
		self.ll.pack(fill="both")

		if not command == None:
			self.ll.bind("<Button-1>", lambda e: command())

		if not auto:
			self.bind("<Enter>", self.__hover_in)
			self.bind("<Leave>", self.__hover_out)
		else:
			self.__hover_in(None)
		
		self.__default_image()
		
	def __hover_in(self, event):
		self.animate_thread =  Thread(target=self.__animate, daemon=True)
		self.animate_thread.start()

	def __default_image(self):
		self.img = ImageTk.PhotoImage(file=self.gif_fp)
		self.ll['image']=self.img
		self.ll.image = self.img

	def __animate(self):
		try:

			#lets display the gif !
			j = 0
			while j <= self.no_of_frames:

				if j >= self.no_of_frames:
					if self.infinite:
						j = 0 #run infinitly
					else:
						break
				elif not self.animate_thread.is_alive(): break  #closes as button loses focus!
				else:
					self.i = ImageTk.PhotoImage(self.new_frame)
					self.new_frame.seek(j)
					
					self.ll['image']= self.i
					self.ll.image = self.i
					# #UPDATE IDLE TASKS TO overcome not responding and update window each moment
					self.update()
					self.update_idletasks()
					# wait for a few secs to make it look good!
					sleep(self.duration)
					j += 1

			self.__default_image()#display defaukt if user hover out.
		except : pass

	def __hover_out(self, e):
		if self.animate_thread.is_alive():
			self.animate_thread._tstate_lock.release()
			self.animate_thread._stop()


class StreamView( Frame ):
	""" This class take a singgle stream as parameter and displays the inforamtion about
	 like video type size and resolution 

	have download Button too. to download the stream
	 """
	def __init__(self, parent, stream,img, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.thumbnail = ImageTk.PhotoImage(Image.open(img).resize((50,50)))
		self.icon = PhotoImage(file='media/download.png')

		Label(self,image=self.thumbnail, **kwargs).pack(side='left', fill='y')

		self.dload_btn = Button(self,image=self.icon,bd=0,fg='blue', **kwargs)
		self.dload_btn.pack(side='right',fill='y')
		Label(self,text=f"Name: {stream.title[0:90]}...",anchor='nw',**kwargs,width=40 ).pack(side='top', fill='both',expand=1)
		Label(self,text=f"Size: {int(stream.filesize) // 1000000 } MB",anchor='nw',**kwargs,width=40 ).pack(side='top', fill='both',expand=1)
		Label(self,text=f"Format : {stream.type}, {stream.subtype}, {stream.resolution} ",anchor='nw',**kwargs,width=40 ).pack(side='top', fill='both',expand=1)
		Label(self,text="-", font=("",15)).pack()

