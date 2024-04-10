from tkinter import *
from time import sleep
from threading import Thread
from PIL import Image, ImageTk #install by >> pip install pillow


class ElskerButton( Frame ):
	""" 
	A Button class created by Button and Frame widget.
	
	parent   >>  root, 
	label    >>  text (to be displayed on the button),
	file     >>  gif (A gif file path),
	command  >>  command (command for button default None)
	duration >>  ( default=0.0299 ,sleep time in changing a simple frame), *args, **kwargs.
	"""

	def __init__(self,parent, text, gif ,command=None,infinite=True, duration=0.0299,*args,**kwargs):
		Frame.__init__(self, parent)
		self.gif_fp = gif
		self.duration = duration
		self.infinite = infinite
		
		self.new_frame = Image.open(self.gif_fp)
		self.no_of_frames = self.new_frame.n_frames

		self.ll = Button(self,text=text,compound='left', command=command, *args, **kwargs)
		self.ll.pack()

		self.bind("<Enter>", self.__hover_in)
		self.bind("<Leave>", self.__hover_out)
		self.__default_image()
		
	def __hover_in(self, event):
		self.animate_thread =  Thread(target=self.__animate)
		self.animate_thread.start()

	def __default_image(self):
		self.img = ImageTk.PhotoImage(file=self.gif_fp)
		self.ll['image']=self.img
		self.ll.image = self.img

	def __animate(self):
		#lets display the gif !
		j = 0
		while j <= self.no_of_frames:

			if j >= self.no_of_frames:
				if self.infinite:
					j = 0 #run infinitly
				else:
					break
			elif not self.animate_thread.isAlive(): break  #closes as button loses focus!
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
				print("frame number", j)
		self.__default_image()

	def __hover_out(self, e):
		print("hover out")
		if self.animate_thread.isAlive():
			self.animate_thread._tstate_lock.release()
			self.animate_thread._stop()




class Application( Tk ):
	def __init__(self):
		Tk.__init__(self)
		self.lframe = Frame(self, bg='black')
		self.lframe.pack(side='left',fill='y')

		b1 = ElskerButton(parent=self.lframe,text="Loading",gif="loader.gif", command=lambda:print("hello world!"),fg='#8ff', bd=0,bg='black', font=("", 15))
		b1.pack()

		b = ElskerButton(self.lframe, "","6.gif", command=lambda:print("hello world!"), bd=0, bg='black', fg='#8ff', font=("", 15))
		b.pack(fill='both')

		b2 = ElskerButton(self,"","sp3.gif", command=lambda:print("sdsd"), bd=0, fg='#8ff', font=("Kruti Dev 010", 15))
		b2.pack()


if __name__ == "__main__":
	app = Application()
	app.mainloop()