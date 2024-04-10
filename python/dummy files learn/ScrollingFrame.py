from tkinter import *

class ScrollingFrame( Frame ):
	""" Frame with x and y scrollbars add contents  using  <object-name>.container
		
		Required parameters - parent_window , scroll_region = (width, height)
		Default parameters -  X_scroll (by default True) pass False to hide bottom scroll bar
							  Y_scroll (by default True) pass False to hide left scroll bar
							 [,*args, **kwargs] and configurations. 
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
		#by using create_window((pos x, pos y), window=window_name) created a frame inside and bounded the frams in a limited region
		#if region exceeded scrollbars will be active

		if Y_scroll:
			self.canvas.configure(yscrollcommand=self.set_scrollbary)
			self.y_scroll.configure( command=self.canvas.yview )
		
		if X_scroll:
			self.canvas.configure(xscrollcommand=self.set_scrollbarx)
			self.x_scroll.configure( command=self.canvas.xview )

		self.container=Frame(self.canvas, height=self.region[0], width=self.region[1]) #wideget continer...
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


root = Tk()
root.geometry("500x500")

Label(root, text="Y_scroll and X_scroll both are True",bg="#88f" ,width=50).pack()

v = ScrollingFrame(root, (200,200),X_scroll=True,**{"bg":"#222"})
v.place(x=100,y=30)

for i in range(600):
	Label(v.container, text=f"Label Numeber: {i}",bg="#88f" ,width=50).pack()


Label(root, text='Only Y_scroll is \nTrue').place(x=10, y=350)
n = ScrollingFrame(root, (100,100),**{"bg":"#222"})
n.place(x=100,y=300)
import string

for i in string.ascii_letters:
	Label(n.container, text=i,bg="#88f").pack()



Label(root, text='Only X_scroll is True').place(x=240, y=350)
kk = ScrollingFrame(root, (100,100),X_scroll=True,Y_scroll=False,**{"bg":"#222"})
kk.place(x=370,y=300)
import string

for i in string.ascii_letters:
	Label(kk.container, text=i,bg="#88f").pack(side='left')

root.mainloop()