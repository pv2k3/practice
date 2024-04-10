import tkinter as tk
from res import pages

class Applicaion(tk.Tk):
	def  __init__(self):
		tk.Tk.__init__(self)
		self.login_page()

	def login_page(self, page=None):
		if page:page.destroy()
		page = pages.LoginPage(self)
		page.pack(fill="both")
		page.login_btn["command"] = lambda :self.UserVerify(page)
		page.reg_btn["command"]= lambda:self.reg_page(page)
	def logOut(self, page):
		page.destroy()
		self.login_page()
	def UserVerify(self, page):
		res = page.verify_login()
		if res:
			page.destroy()
			page = pages.HomePage(self, res[0])
			page.pack(fill="both", expand=True)
			page.user_Frame.log_out_btn["command"] = lambda: self.logOut(page)
		else:
			self.login_page()
	def reg_page(self, page):
		if page:page.destroy()
		page = pages.RegisterPage(self)
		page.pack(fill="both")
		page.go_login['command'] =  lambda:self.login_page(page)
	
if __name__ == "__main__":
	app = Applicaion()
	app.resizable(0,0)
	app.geometry("1000x667+200+50")
	app.mainloop()

