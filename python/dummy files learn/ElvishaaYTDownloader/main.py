from tkinter import *
from PIL import Image, ImageTk
from res import extensions as ext
from os import system
from time import sleep
from tkinter.ttk import Button as ttkButton,Progressbar
from pytube import YouTube 
from requests import get #to download thumbnail of video
from threading import Thread
from os import startfile
from pyperclip import copy as pcopy

about_str  ="""
---------------------------------
Elvishaa YouTube Video Downloader
---------------------------------
Dependencies:

pytube >> pip install pytube
tkinter >> BIL
os >> BIL
PIL >> pip install pillow
requests >> pip install requests
pyperclip >> pip install pyperclip
threading >> BIL
tkinter  >> BIL
tkinter.ttk >> BIL
time >> BIL

Author: Elsker Elvish
First Release Date: 20th April 2021 (1.0)
Version: 2.0

Follow:
 Insatgram: elsker_elvish.py
 Twitter: ElskerElvish
Join Telegram Channel for Source code:
 Tkinter GUI Python

Created with\u2764\uFE0Fby @ElskerElvish.py
For Education Purose only.
"""

def myYouTube(link):
	yt = YouTube(link)
	return (yt, yt.streams)

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
		self.title=""

		self.info = Label(self,text="Downloading: ... ", anchor='nw')
		self.info.pack(side='top', fill='x')
		
		self.pb = Progressbar(self, length=180)
		self.pb.pack(fill='x', expand=1)

		self.status = Label(self,text= "Status: ", anchor='nw')
		self.status.pack(side='bottom',fill='x')

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
			self.title = newYT[0].title[0:41]
			self.info['text']=f"Downloading: {self.title}..."
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
			
			file_saving_location = to_download.download()
		
			self.status.configure(fg='green', text='Status : Finished')
			self.finished = True
			self.play_button.pack(side='bottom')
			self.play_button["command"] = lambda: startfile(file_saving_location)
			self.finished = True
			
		except Exception as e:
			print(e)
			self.finished = True

class MainApp( Tk ):
	
	PACKED_FRAMES = []
	FILTER = ""
	LISTED_RESULTS = ''
	IN_PROGRESS = []
	RECENTS = []

	def __init__(self, title):
		Tk.__init__(self)
		self.title(title)
		self.resizable(0,0)

		self.dFrame = ext.ScrollingFrame(self,(540,400))
		self.right_frame = ext.ScrollingFrame(self,(540,400))
		self.recentsFrame = ext.ScrollingFrame(self,(540,400))
		self.filterFrame = LabelFrame(self,text="Filter",font=("",13),padx=20,pady=20)
		self.aboutFrame = Label(self,text=about_str,relief="groove",font=("",13),padx=20,pady=20)

		self.ScreenLoader()

	def window_packer(self, window):
		if not len(self.PACKED_FRAMES) == 0:
			self.PACKED_FRAMES.pop().pack_forget()

		window.pack(side="right",fill="both", expand=1)
		self.PACKED_FRAMES.append(window)


	def pytube_updater(self,loader):
		ret = system("pip install --upgrade pytube")
		loader.destroy()
		self.UI()

	def ScreenLoader(self):
		self.resizable(0,0)
		loader = ext.ElskerButton(self, "Checking for updates please wait...","media/gif-from-youtube.gif", auto=True, duration=0.256)
		loader.ll.configure(compound="top", fg='red', bg='white', font=("",14))
		loader.pack()
		#check to update pytube library...
		self.after(5000, lambda: self.pytube_updater(loader)) #starts updating after 5 seconds

	def update_thumbnail(self, imgBin, lbl, ttle):

		with open("res/thumbnail.dat","wb") as f:
			#save the image. Image format is jpg but saving with unknown (.dat) extension
			f.write(imgBin)

		self.thumbnail = ImageTk.PhotoImage(Image.open("res/thumbnail.dat").resize((250,250)))
		lbl.configure(image=self.thumbnail, text=ttle)
		self.update()

	def pack_recents_frame(self):
		self.window_packer(self.recentsFrame)

		window = Frame(self.recentsFrame.container)
		if not len(self.RECENTS) == 0:
			self.RECENTS.pop().pack_forget()

		window.pack(side="right",fill="both", expand=1)
		self.RECENTS.append(window)

		for i in self.IN_PROGRESS:

			Label(window, text=i.title, font=("",13)).pack(fill="x",pady=5)
			Button(window,fg="blue", text="Click to copy link to clipboard\n:"+i.link, command=lambda l =i.link:pcopy(l), font=("",13)).pack(fill="x",pady=5)
			Label(window, text="-"*10, font=("",13)).pack(fill="x",pady=5)

	def UI(self):
		self.geometry("890x550+250+50")

		lframe = Frame(self, bg="white")
		lframe.pack(side="left",fill='y')

		#lframe components..
		kw = {"bg":"white","font":("arial",15),"pady":"5","padx":"5","anchor":"w"}
		home_btn =  ext.ElskerButton(lframe, " Home","media/home.gif",command=lambda:self.window_packer(self.right_frame),infinite=False, **kw)
		home_btn.grid(row=0, column=0,sticky ="ew",pady=5)

		dload_btn =  ext.ElskerButton(lframe, " Downloads ","media/dload.gif", command=lambda:self.window_packer(self.dFrame),infinite=False, **kw)
		dload_btn.grid(row=1, column=0,sticky ="ew",pady=5)

		rcnts_btn =  ext.ElskerButton(lframe, " Recents","media/clock.gif",command= self.pack_recents_frame,infinite=False, **kw)
		rcnts_btn.grid(row=2, column=0,sticky ="ew",pady=5)

		filter_btn =  ext.ElskerButton(lframe, " Filter","media/filter.gif",command=lambda:self.window_packer(self.filterFrame),infinite=False, **kw)
		filter_btn.grid(row=3, column=0,sticky ="ew",pady=5)

		about_btn =  ext.ElskerButton(lframe, " About","media/user.gif",command=lambda:self.window_packer(self.aboutFrame),infinite=False, **kw)
		about_btn.grid(row=4, column=0,sticky ="ew",pady=5)
		self.window_packer(self.aboutFrame)

		Label(lframe,text="Powered by: ", bd=0).grid(row=5, column=0,pady=(100,0))
		self.pytube = PhotoImage(file="media/pytube.png").subsample(3)
		Label(lframe,image=self.pytube, bd=0).grid(row=6, column=0)

		#middle frame
		midframe = Frame(self)
		midframe.pack(side="left",fill="y", padx=20)

		self.img = PhotoImage(file="media/youtube.png")
		thumb_lbl =  Label(midframe, image=self.img, compound='top')
		thumb_lbl.pack()

		link = ext.LabeledEntry(midframe,"Enter TouTube video link","media/link.png")
		link.pack(fill="x",pady=10)
		# link.err("Getting video info...")
		
		self.views_img = PhotoImage(file="media/views.png")
		self.likes_img = PhotoImage(file="media/likes.png")
		self.duration_img = PhotoImage(file="media/duration.png")

		vdo_author = Label(midframe, compound='left',text=" Author : ", image = self.likes_img, anchor="w")
		vdo_views = Label(midframe, compound='left',text="  Views", image = self.views_img, anchor="w")
		vdo_duration = Label(midframe, compound='left',text=" Length", image = self.duration_img, anchor="w")

		submit_btn = ttkButton(midframe, text="Submit",command=lambda: self.get_info(link, thumb_lbl,vdo_views,vdo_author,vdo_duration) )
		submit_btn.pack(fill="x", padx=30, ipady=4, pady=5)

		vdo_author.pack(fill="x",pady=5)
		vdo_views.pack(fill="x",pady=5)
		vdo_duration.pack(fill="x",pady=5)

		#filter frame components
		FILTER = StringVar()
		v = Radiobutton(self.filterFrame,font=("",15),anchor="nw", text="Audio Only",variable = FILTER, value = "audio", command=lambda: self.add_filter(FILTER.get()))
		v.pack(fill="x", pady=5)
		m = Radiobutton(self.filterFrame,font=("",15),anchor="nw", text="Video Only",variable = FILTER, value = "video", command=lambda: self.add_filter(FILTER.get()))
		m.pack(fill="x", pady=5)
		b = Radiobutton(self.filterFrame,font=("",15),anchor="nw", text="Both",variable = FILTER, value = "both", command=lambda: self.add_filter(FILTER.get()))
		b.pack(fill="x", pady=5)
		b.invoke()


	def add_filter(self,v):
		self.FILTER = v
	
	def start_download(self, link , index,fltr):
		new_progress_frame = DownloadProgress(self.dFrame.container,link, index,fltr, bd=1, relief='groove')
		new_progress_frame.pack(padx=20, pady=20, fill="x")
		self.IN_PROGRESS.append(new_progress_frame)


	def get_info(self,link_entry,thumb_lbl,vdo_views , vdo_author ,vdo_duration):
		link_entry.err("Getting info...")
		yt,streams =  myYouTube(link_entry.get())
		thumbnail_image_data = get(yt.thumbnail_url).content
		self.update_thumbnail(thumbnail_image_data, thumb_lbl, (yt.title[0:40]+"..."))

		vdo_views['text'] = str(yt.views)+" Views"
		vdo_author['text'] = "Author: "+yt.author
		vdo_duration['text'] = "Length: {:.2f}".format(yt.length /60)

		self.window_packer(self.right_frame)

		filterd = []
		for i in streams:
			if self.FILTER =="both": filterd = streams
			elif i.type == self.FILTER: filterd.append(i)

		temp = Frame(self.right_frame.container)
		
		if not self.LISTED_RESULTS == '':
			self.LISTED_RESULTS.destroy()	
		self.LISTED_RESULTS = temp
		temp.pack()

		for i in range(len(filterd)):

			if filterd[i].type =="audio": img = "media/audio.png"
			else: img = "media/video.png"

			l = ext.StreamView(temp, filterd[i],img)
			l.pack(pady=5, fill="x")
			l.dload_btn['command'] = lambda a=i: self.start_download(link_entry.get(),a,self.FILTER)
			self.update()
		link_entry.err(f"Found {len(filterd)} results")

def main():
	app =  MainApp("Elvishaa Youtube Video Downloader ")
	app.mainloop()

if __name__ == '__main__':
	main()