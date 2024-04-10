from pytube import YouTube 
from requests import get #to download thumbnail of video
from threading import Thread
from tkinter.ttk import Notebook, Progressbar, Button as ttkButton
from tkinter import (
	Frame, Label, Radiobutton, StringVar,Text,
	LabelFrame, Tk, PhotoImage, Scrollbar, Canvas, Entry, Button)
from PIL import Image, ImageTk
from tkinter.messagebox import askyesno
from os import startfile
from os import rename

def myYouTube(link):
	yt = YouTube(link)
	return (yt, yt.streams)

about_str  ="""
\t   Elvishaa YouTube Downloader

This is python app works on 
the following python libraries:

tkinter (python builtin Library)
pytube  #pip install pytube
threading (BIL)
PIL   #pip install pillow
os (BIL)
tkinter.messagebox

Author : Elsker Elvish
Create Date : 20th April 2021

Follow:
	Instagram : elsker_elvish.py
	Twitter   : elsker_elvish
	Facebook  : elsker_elvish

For more such source code join Telegram Channel:
		@pythonguibyelskerelvish

Note: 
Beginer's code may have various bugs!
Created with\u2764\uFE0Fby @ElskerElvish.py a little GIFT for @Adiaba Roczyno
	 For education Purpose only! 
"""


class ScrollingFrame( Frame ):
	""" Frame with x and y scrollbars add contents  using  <object-name>.container
		
		Required parameters - parent_window , scroll_region = (width, height)
		Default parameters -  X_scroll (by default True) pass False to hide bottom scroll bar
							  Y_scroll (by default True) pass False to hide left scroll bar
							 [,*args, **kwargs] and configurations. 
		"""

	def __init__(self,parent,scroll_region,X_scroll=False,Y_scroll=True,*args ,**kwargs):
		Frame.__init__(self,parent,*args, **kwargs)

		self.configure(bd=2, relief="groove")

		self.region = scroll_region
		
		if Y_scroll: #if True
			self.y_scroll=Scrollbar(self,orient="vertical")
			self.y_scroll.pack(side="right",fill="y")
		
		if X_scroll:
			self.x_scroll=Scrollbar(self,orient="horizontal")
			self.x_scroll.pack(side="bottom",fill="x", anchor='nw')
		
		self.canvas=Canvas(self,relief="ridge",*args,**kwargs) 
		self.canvas.pack(side="top", fill='both', expand=1)
	
		if Y_scroll:
			self.canvas.configure(yscrollcommand=self.set_scrollbary)
			self.y_scroll.configure( command=self.canvas.yview )
		
		if X_scroll:
			self.canvas.configure(xscrollcommand=self.set_scrollbarx)
			self.x_scroll.configure( command=self.canvas.xview )

		self.container=Frame(self.canvas, height=self.region[0], width=self.region[1], *args, **kwargs) #wideget continer...
		self.canvas.create_window((0,0),window=self.container,anchor='nw')
		self.container.bind("<Configure>",self.scroll)
		#configure is a event called when there is a change in size of a widgets
		#here <Configure> id called when size of container frame exceeded from specified scroll_region
	def scroll(self,event):
		""" .bbox("all") >> Return a tuple of X1,Y1,X2,Y2 coordinates for a rectangle
        which encloses all items with tags specified as arguments."""
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=self.region[1], height=self.region[0])
	def set_scrollbary(self,first, last):
		self.y_scroll.set(first, last)
		self.update()
	def set_scrollbarx(self,first, last):
		self.x_scroll.set(first, last)
		self.update()

class LabeledEntry(LabelFrame):
	""" just like labeledEntry but having a bottom label to display any alert or messages """
	def __init__(self,parent, lbltext,imglocation='',*args, **kwargs):
		LabelFrame.__init__(self,parent,*args, **kwargs)
		self.configure(text=lbltext,bd=0)
		
		self.entryVar=StringVar()
		self.imglbl=Label(self, **kwargs)

		self.entry = Entry(self,textvariable=self.entryVar,bd=1,font=('Arial',11),highlightthickness=0,insertbackground='blue',relief='flat',width=18,*args,**kwargs)
		self.errormessage=Label(self,fg='blue',bd=0,font=('',8), anchor='nw',**kwargs)
		self.entry['bg'] = self['bg']
		self.lining = Frame(self,relief='raised', bg='black')
		#packing
		if imglocation!='':
			self.im=PhotoImage(file=imglocation)
			self.imglbl['image']=self.im
			self.imglbl.image=self.im

		self.errormessage.pack(side='bottom',fill='x')
		self.lining.pack(side='bottom',fill='x')
		self.imglbl.pack(anchor='nw',side='left',fill='y')
		self.entry.pack(anchor='nw',fill='both',expand=1)
		self.entry.bind('<FocusIn>',self.Focusin)
	def err(self, e):
		self.errormessage['text']=e
		self.update()
	def Focusin(self,event):self.errormessage['text']=''
	def get(self): return self.entryVar.get()

class StreamView( Frame ):
	""" This class take a singgle stream as parameter and displays the inforamtion about
	 like video type size and resolution 

	have download Button too. to download the stream
	 """
	def __init__(self, parent, stream, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.thumbnail = ImageTk.PhotoImage(Image.open("resources/media/thumbnail.dat").resize((50,50)))
		self.icon = PhotoImage(file='resources/media/download.png')

		Label(self,image=self.thumbnail, **kwargs).pack(side='left', fill='y')

		self.dload_btn = Button(self,image=self.icon,bd=0,fg='blue', **kwargs)
		self.dload_btn.pack(side='right',fill='y')
		Label(self,text=f"Name: {stream.title[0:90]}...",anchor='nw',**kwargs,width=40 ).pack(side='top', fill='both',expand=1)
		Label(self,text=f"Size: {int(stream.filesize) // 1000000 } MB",anchor='nw',**kwargs,width=40 ).pack(side='top', fill='both',expand=1)
		Label(self,text=f"Format : {stream.type, stream.subtype, stream.resolution} ",anchor='nw',**kwargs,width=40 ).pack(side='top', fill='both',expand=1)

class DownloadProgress( Frame ):
	""" this class again get the inforamtion using link
		and get all availabe streams of the video 
		and then downloads the  stream from the list of streams.
	"""
	def __init__(self,parent, link ,index, filtr,*args, **kwargs):
		Frame.__init__(self,parent, bd=0)
		self.finished = False
		self.link  = link
		self.index = index
		self.filtr =  filtr

		self.info = Label(self,text="Downloading: ... ", anchor='nw')
		self.info.pack(side='top')
		
		self.pb = Progressbar(self, length=180)
		self.pb.pack(fill='x')

		self.status = Label(self,text= "Status: ", anchor='nw')
		self.status.pack(side='bottom')

		self.play_button = Button(self,text= "Play", anchor='nw')
		
		self.t = Thread(target = self.new_yt,daemon = True)
		self.t.start()
	def update_progres(self, stream, chunks, byts):
		dloaded = int(stream.filesize)- int(byts)
		self.pb['value'] = dloaded
		self.pb.value = dloaded
		self.status['text'] = "Status : {:.2f} MB of {:.2f} MB".format(dloaded / 1000000, int(stream.filesize) /1000000)
	def new_yt(self):		
		try:
			newYT = myYouTube(self.link)
			self.info['text']=f"Downloading: {newYT[0].title[0:41]}..."
			# register_on_progress_callback >> YouTube method(callback) and  pass  three parameters to the mentioned 
			# function i.e.    stream , chunks (video bin. data) , bytes recieved
			newYT[0].register_on_progress_callback(self.update_progres)
			streams = newYT[1]
			filterd = []
			for i in streams:
				if self.filtr =="both": filterd = streams
				elif i.type == self.filtr: filterd.append(i)

			to_download = filterd[self.index] #get the stream of that particular index
			self.pb["maximum"] = int(to_download.filesize) #set progress bar 100% value
			try:
				file_saving_location = to_download.download()
				# it by default saves the even audio file into .mp4 format so to play in music player chnage the file extension 
				if to_download.type == "audio":
					new_lcn = file_saving_location.split(".") #split to remove extension
					rename(file_saving_location ,new_lcn[0]+".mp3") #method os the os module
					file_saving_location = new_lcn[0]+".mp3"
					
				self.status.configure(fg='green', text='Status : Finished')
				self.finished = True
				self.play_button.pack(side='bottom')
				self.play_button["command"] = lambda: startfile(file_saving_location)
			except FileExistsError:
				print("File Already Exist!")
				self.status.configure(fg='green', text='Status : File Already Exist')
				self.finished = True

		except Exception as e:
			print(e)
			self.finished = True


class ElvishaaYT(Tk):
	packed_results = []
	download_in_progress = []
	filtr = ""
	def __init__(self):
		Tk.__init__(self)
		self.icon = PhotoImage(file='resources/media/youtube.png').subsample(3)
		self.geometry("400x600")
		self.resizable(0,0)
		self.title("Elvishaa YT Downloader")
		self.iconphoto(False, self.icon )
		self.ui()
		self.wm_protocol("WM_DELETE_WINDOW", self.check_to_close_parent)

	def ui(self):
		notebook = Notebook(self)
		notebook.pack(fill='both', expand=1)
		home = Frame(notebook)
		self.downloads = ScrollingFrame(notebook,(490,365))
		
		filter_frame = Frame(notebook)
		about = Text(notebook, fg='blue', font=("",12))	
		about.insert(1.0, about_str)
		about["state"]= "disabled"

		self.rb_var = StringVar()
		v = Radiobutton(filter_frame, text="Audio Only",variable = self.rb_var, value = "audio", command=self.add_filter)
		v.pack()
		m = Radiobutton(filter_frame, text="Video Only",variable = self.rb_var, value = "video", command=self.add_filter)
		m.pack()
		b = Radiobutton(filter_frame, text="Both",variable = self.rb_var, value = "both", command=self.add_filter)
		b.pack()
		b.invoke()

		notebook.add(home, text='Home')
		notebook.add(self.downloads, text='Downloads')
		notebook.add(filter_frame, text='Filter')
		notebook.add(about, text="About")

		self.dwn_img = PhotoImage(file='resources/media/download.png')

		self.bg = Label(home, image=self.icon, anchor='center')
		self.bg.pack(fill='x',side='top')

		self.container = Frame(home)
		self.container.pack(fill='both', expand=1)

		self.link_entry = LabeledEntry(self.container, "Paste YouTube share link here","resources/media/link.png")
		self.link_entry.pack(fill='x',padx=20)

		self.download_button =ttkButton(self.container,text="Get Info" ,command=self.list_downloads)
		self.download_button.pack()
		#just add to show a blank ScrollingFrame
		self.pack_a_result(None)
	def add_filter(self): self.filtr = self.rb_var.get()
	def pack_a_result(self,lst):
		"""function which will print all the inforamtion of the each stream from the 
 		list of streams (all availabe / downloadable formats) """
		output = ScrollingFrame(self.container,(295,375))
		output.pack(side='bottom')
		#add to list so that all results of a particular link can be by just removing ScrollingFrame .
		# onject of ScrollingFrame will be accesed from the list
		self.packed_results.append(output)
		
		if not lst == None:
			for i in range(len(lst)):
				# output.container  >> object of  a frame of ScrollingFrame Class. 
				v = StreamView(output.container,lst[i], **{"bg":"#ddd"})
				v.pack(side='top',fill='x',pady=5,expand=1)
				# lambda a = i: self.start_new_download(a) try ro uderstand why i have done this
				v.dload_btn.configure(command = lambda a = i: self.start_new_download(a) )
				self.update()
	def remove_a_result(self):
		"""function to delete/destroy the ScrollingFrame so that new frame will be added at that position """
		self.packed_results.pop().destroy() # pop is a list method which returns the removed object from the list

	def start_new_download(self,index):
		new_progress_frame = DownloadProgress(self.downloads.container,self.link_entry.get() , index,filtr =  self.filtr, bd=1, relief='groove')
		new_progress_frame.pack(padx=20, pady=20)
		self.download_in_progress.append(new_progress_frame)

	def list_downloads(self):
		""" function which gets the available formats for the video to be downloaded
			and organise them to display in the ScrollingFrame
		"""
		try:
			lnk =self.link_entry.get() #get video link from the Entry
			if not lnk =="":
				self.link_entry.err("Getting available Video streams")
				yt = myYouTube(lnk)
				streams = yt[1]
				# yt.streams  Returns a list of video stream (can say streams for each available formats like : 360p 1080p etc )
				self.link_entry.err("Getting video thumbnail")
			
				thumbnail_image_data = get(yt[0].thumbnail_url) #using requests module's method get() ...
				with open("resources/media/thumbnail.dat","wb") as f:
					#save the image. Image format is jpg but saving with unknown (.dat) extension
					f.write(thumbnail_image_data.content)
				
				self.remove_a_result() # remove of there any ScrollingFrame exists  
				
				self.link_entry.err("Listing results please wait...")
				#add filter --- 
				filterd = []
				for i in streams:
					if self.filtr =="both": filterd = streams
					elif i.type == self.filtr: filterd.append(i)
				self.pack_a_result(filterd) #add new ScrollingFrame with available data/results
				
				self.link_entry.err(f"Done! {len(filterd)} Results")
			else:
				self.link_entry.err("Paste link here first...")
		except Exception as e:
			self.link_entry.err(e)

	def check_to_close_parent(self):
		l = 0
		for i in self.download_in_progress:
			if not i.finished: l += 1
		if not l == 0:
			if askyesno(message=f'You have {l} items currently downloading..', detail="Are you sure to exit? You may not able to resume.."): self.destroy()
		else:self.destroy()

def main():
	app = ElvishaaYT()
	app.mainloop()
#run app		
if __name__ =="__main__":
	main()