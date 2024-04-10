from custom_pages import custompages
from tkinter import *

class App(Tk):

	def __init__(self, title):
		Tk.__init__(self)
		#set title
		self.title(title)
		#set window to full zoomes
		# self.state("zoomed")

		#create a frame to contain all login register pages

		self.login_page = custompages.Login_Page( self )
		self.login_page.pack()

		self.login_page.regbtn.configure( command= self.OpenRegPage )


	def OpenRegPage(self):
		
		v = custompages.Register_Page(self)
		v.place(x=90, y=65)

#run app
ap = App('My App')
#infinite loop
ap.mainloop()
