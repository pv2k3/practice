from tkinter import *
import sqlite3
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from res.database import dbsys
from PIL import Image, ImageTk
from threading import Thread
from tkinter.scrolledtext import ScrolledText
import json


def setImg(imgBin, lbl, imgSize=(120,120)):
	try:
		with open("./res/media/dump.dat", "wb") as f:
			f.write(imgBin)
			f.close()
		img = Image.open("./res/media/dump.dat")
		img = img.resize(imgSize)
		img = ImageTk.PhotoImage(img)
		lbl["image"] = img
		lbl.image = img
	except:
		pass

class ScrollingFrame( Frame ):
	""" Frame with x and y scrollbars add contents  using  <object-name>.container
		Required parameters - parent_window , scroll_region = (width, height)
		Default parameters -  X_scroll (by default False) pass False to hide bottom scroll bar
							  Y_scroll (by default True) pass True to hide left scroll bar
							 [,*args, **kwargs] and configurations. """
	def __init__(self,parent,scroll_region,X_scroll=False,Y_scroll=True,*args ,**kwargs):
		Frame.__init__(self,parent, *args, **kwargs)
		self.configure(bd=2, relief="groove")
		if Y_scroll: #if True
			self.y_scroll=Scrollbar(self,orient="vertical", width=13)
			self.y_scroll.pack(side="right",fill="y")
		if X_scroll:
			self.x_scroll=Scrollbar(self,orient="horizontal", width=13)
			self.x_scroll.pack(side="bottom",fill="x", anchor='nw')
		
		self.canvas=Canvas(self,relief="flat",width = scroll_region[0], height = scroll_region[1],**kwargs) 
		self.canvas.pack(fill="both", expand=True)
		
		if Y_scroll:
			self.canvas.configure(yscrollcommand=self.set_scrollbary)
			self.y_scroll.configure( command=self.canvas.yview )
		if X_scroll:
			self.canvas.configure(xscrollcommand=self.set_scrollbarx)
			self.x_scroll.configure( command=self.canvas.xview )

		self.container=Frame(self.canvas, height=self.canvas.winfo_height(),relief='flat', width=self.canvas.winfo_width()) #wideget continer...
		self.canvas.create_window((0,0),window=self.container,anchor='nw')
		self.container.bind("<Configure>",self.scroll)
		#configure is a event called when there is a change in size of a widgets
		#here <Configure> id called when size of container frame exceeded from specified scroll_region
	def scroll(self,event=None): self.canvas.configure(scrollregion=self.canvas.bbox("all"))
	def set_scrollbary(self,first, last):
		self.y_scroll.set(first, last)
		self.update()
	def set_scrollbarx(self,first, last):
		self.x_scroll.set(first, last)
		self.update()

class LoginPage(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.bg = PhotoImage(file="./res/media/bg/a.png")
		self.bg_lbl = Label(self, image=self.bg)
		self.bg_lbl.image = self.bg
		self.bg_lbl.pack()
		self.parent.resizable(0,0)

		self.id = Entry(self, bd=0,bg="white", font=("", 12),width=26 ,justify="center")
		self.id.place(x = 139,y=250)

		self.psw = Entry(self, bd=0,bg="white", font=("", 12),width=26, show="*", justify="center")
		self.psw.place(x = 139,y=318)

		self.psw.bind("<Button-3>", self.view_pass)
		self.psw.bind("<ButtonRelease-3>", self.hide_pass)

		self.forget_password = Button(self, bd="0", relief="flat",bg="#2390d6" ,text="Forgot Password?")
		self.forget_password.place(x=329, y = 365)

		self.remember_me = Checkbutton(self, bd="0", relief="flat",bg="#2390d6" ,text="Remember me")
		self.remember_me.place(x=139, y = 365)

		self.login_btn = Button(self, bd="0", relief="flat",bg="#06f866" ,fg="white",text="Login",font=("",15), width=25)
		self.login_btn.place(x=140, y=408)

		self.reg_btn = Button(self, bd="0", relief="flat",bg="#06f866" ,fg="white",text="Register",font=("",15), width=10)
		self.reg_btn.place(x=151, y=498)

	def view_pass(self, event):
		widget = event.widget
		widget["show"]= ""
	def hide_pass(self, event):
		widget = event.widget
		widget["show"]= "*"

	def verify_login(self):
		if self.id.get().strip() == "" or self.psw.get().strip() == "":
			showinfo(title="Info", detail="Fill from Correctly")
			return False
		else:
			db = dbsys.DBrowser("./res/database/database.db")
			qry = """ SELECT id,name, email, phone, profileImg, Address from Users where email= ? and password = ?"""
			res = db.action(qry, (self.id.get().strip(), self.psw.get().strip()) ,"fetch")
			if res == []:
				showinfo(title="Info", detail="User Not Found..")
				return False
			else:
				return res

class RegisterPage(Frame):
	def __init__(self, parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.img_location = ""
		self.parent.resizable(0,0)
		
		self.bg = PhotoImage(file="./res/media/bg/b.png")
		self.bg_lbl = Label(self, image=self.bg)
		self.bg_lbl.image = self.bg
		self.bg_lbl.pack()

		self.name = Entry(self, bd=0,bg="white", font=("", 12),width=15)
		self.name.place(x=99,y=235)

		self.phone = Entry(self, bd=0,bg="white", font=("", 12),width=15)
		self.phone.place(x=315,y=235)

		self.email = Entry(self, bd=0,bg="white", font=("", 12),width=33 )
		self.email.place(x=100,y=313)

		self.psw = Entry(self, bd=0,bg="white", font=("", 12),width=15 )
		self.psw.place(x=99,y=394)

		self.psw.bind("<Button-3>", self.view_pass)
		self.psw.bind("<ButtonRelease-3>", self.hide_pass)

		self.repsw = Entry(self, bd=0,bg="white", font=("", 12),width=15 )
		self.repsw.place(x=315,y=394)

		self.repsw.bind("<Button-3>", self.view_pass)
		self.repsw.bind("<ButtonRelease-3>", self.hide_pass)

		self.img_name = Label(self,bg="white", text="No file selected..", bd=0, font=("", 12))
		self.img_name.place(x=99,y=465)

		self.filebtn = Button(self, text="Select file",fg="blue", bd=0, bg="white", width=11, command=self.selectImg)
		self.filebtn.place(x=375, y=464)

		self.register_btn = Button(self, bd="0", relief="flat",bg="#06f866" ,fg="white",text="Register",font=("",12), width=25, command=self.addUser)
		self.register_btn.place(x=150, y=530)

		self.go_login = Button(self, bd="0", relief="flat",bg="#2390d6" ,fg="white",text="Login",font=("",12), width=25)
		self.go_login.place(x=575, y=530)


	def selectImg(self):
		fp = askopenfilename(filetypes= [("Image files", "*.jpg *.png *.jpeg"), ("All File","*.*")] )
		if fp:
			nm = fp.split("/")[-1]
			if len(nm)>25:nm = nm[:22]+"...."
			self.img_name["text"] = nm
			self.img_location = fp

	def view_pass(self, event):
		widget = event.widget
		widget["show"]= ""
	def hide_pass(self, event):
		widget = event.widget
		widget["show"]= "*"

	def validate(self, entries):
		message = ""
		for key, value in entries.items():
			if value.get().strip() == "":
				message=key
				break
		return message

	def check_email_if_exist(self):
		db = sqlite3.connect("./res/database/database.db")
		qry = """ SELECT name from Users where email= ?"""
		res = db.execute(qry, (self.email.get().strip(),) ).fetchall()
		db.close()
		if res != []:
			return True
		else:
			return False

	def addUser(self):
		entries = {"Name":self.name, "Phone":self.phone, "Email":self.email, "Password":self.psw, "Retype Password":self.repsw}
		val = self.validate(entries)
		if val != True and val != "":
			showinfo(title="Info", message="Fill Form Correctyly", detail=f"Please Enter Your {val}")
		
		elif len(self.phone.get().strip()) < 10 or len(self.phone.get().strip()) < 10 or self.phone.get().strip()[0] in ["0","1",'2','3','4','5']:
			showinfo(title="Info", message="Invalid Phone Number!!", detail=f"Enter a Valid phone number")
		
		elif self.psw.get().strip() != self.repsw.get().strip():
			showinfo(title="Info", message="Invalid Password!!", detail=f"Password and Retyped Password are not same.")
		
		elif self.check_email_if_exist():
			showinfo(title="Info", message="Email Already Registered", detail="Enter another email!!")

		else:
			value = (self.name.get().strip(), self.email.get().strip(), self.psw.get().strip(), int(self.phone.get().strip()) )
			
			if self.img_location == "":
				qry = """ INSERT INTO Users(name , email, password, phone) VALUES(?,?,?,?)"""
			else:
				print(self.img_location)
				qry = """ INSERT INTO Users(name , email, password, phone, profileImg) VALUES(?,?,?,?,?)"""
				with open(self.img_location, "rb") as f:
					imgBin = f.read()
					f.close()
				value += (imgBin,)

			db = sqlite3.connect("./res/database/database.db")
			res = db.execute(qry, value)
			db.commit()
			db.close()
			showinfo(title="Success", message="User added succesfully go to login page...")
class SearchBar(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self["bg"] ="#2390d6"

		self.entry = Entry(self, width=25, font=("",12), relief="flat")
		self.entry.pack(side="left", fill="both",expand=True, pady=15)

		self.search_ico = PhotoImage(file="./res/media/icons/search.png")
		self.search_btn = Button(self, bd=0, image=self.search_ico, bg ="white")
		self.search_btn.pack(side="right", fill="both",expand=True, ipadx=5, pady=15)

		self.entry.bind("<Return>", lambda e:self.search_btn.invoke()) # trigger Search Button
	def get(self):
		return self.entry.get().strip()

text ="""
\t%s

\tM.R.P : Rs. %s 

\tSold by: %s

\tDiscount Offered : %s

\tProduct Available: %s
"""

class PopUpProductDescription(ScrollingFrame):
	def __init__(self, parent, scroll_region, productId):
		ScrollingFrame.__init__(self, parent, scroll_region)
		self.p = productId

		self.imgSize = (400,400)
		if  self.p[7] == "1":
			avl= "Available"
		else:
			avl = "Not Available"
		l = Label(self.container, justify="left",font=("",18,"bold"), compound="left", text = text%(self.p[1],self.p[2], self.p[5], self.p[6],avl)   ) 
		l.pack(anchor="nw",fill="x", expand=True)

		self.pvc_cart_btn = Button(self.container,text="Add to Cart", bd=0 , font=("", 15), padx=40, pady=8,bg="yellow")
		self.pvc_cart_btn.pack(anchor="nw")
		setImg(self.p[4], l, self.imgSize)

		self.t = ScrolledText(self.container, bd=0)
		self.t.pack(fill="both",side="bottom",expand=True, pady=10)

		self.addText("Description: \n\n"+self.p[3])

	def addText(self, txt):
		self.t.insert(1.0,txt)
		self.t["state"] = "disabled"

class ProductViewConsumer(Frame):
	count = 1
	def __init__(self, parent, data):
		LabelFrame.__init__(self, parent)
		self.ID = data[0]
		self.data = data
		self.lbl = Label(self, text=data[1]+"\nRs."+str(data[2]), compound="top")
		self.lbl.pack()
		self.add_to_cart_btn = Button(self, text="Add to Cart", bd=0, bg="#06f855", pady=5)
		self.add_to_cart_btn.pack(pady=(10,2), fill="x", padx=5)
		setImg(data[4], self.lbl)

class CART_ITEM(Frame):
	count = 1
	def __init__(self, parent, d):
		Frame.__init__(self, parent)
		self.d = d
		f = font=("",15)

		self.namelbl = Label(self,width=24,text=f"{self.d[0]} x {self.d[3]}", anchor="nw", font=f)
		self.namelbl.grid(row=0,column=0, columnspan = 3)

		if d[2] == 0:
			Label(self, text=f"{d[1]} x {d[3]} = {self.d[1]*d[3]} Rs" ,width=20, font=f, anchor="nw").grid(row=0, column=4)
		else:
			Label(self, text=f"{d[1]} x {d[3]} = {self.d[1]*d[3]} Rs\nWith Discount :{(self.d[1]*d[3])-d[2]} " ,width=20, font=f, anchor="nw").grid(row=0, column=4)

class CART(Frame):
	p = []
	def __init__(self, parent, p_ids, *args, **kwargs):
		Frame.__init__(self,parent, *args, **kwargs)

		self.p_ids = p_ids
		self.AA = ScrollingFrame(self,scroll_region=(500,550), )
		self.AA.pack()
		
		self.place_ordr_btn = Button(self.AA.container, text="Place Order", width=45, bg='yellow')

		self.list_items()

	def get_price(self,pid):
		db = dbsys.DBrowser("./res/database/database.db")
		q = """SELECT Name,price,discount FROM Products WHERE id = ? """
		res = db.action(q, (pid,), "fetch")
		return res

	def list_items(self):
		total = 0
		if not self.p_ids == {}:

			for Id,quantity in self.p_ids.items():
				d = self.get_price(Id)[0]
				total += d[1]*quantity

				d += (quantity,)
				# d = Name,price,discount, quantity
				n = CART_ITEM(self.AA.container,d)
				n.pack()

			Label(self.AA.container, text=f"Amount to be paid: {total} Rs", width=45 ,anchor="nw").pack(pady=(60,10))
			self.place_ordr_btn.pack()
		else:
			Label(self.AA.container, text="Your Cart is Empty!!",bg="red", font=("", 18),pady=10,width=37).pack()


class USERVIEW(Frame):
	def __init__(self, parent,res):
		Frame.__init__(self, parent,padx=10, pady=10)
		self.res = res
		Button(self, text="Profile", bd=0, width=20, anchor="nw", compound ="left").pack()
		Button(self, text="Change Password", bd=0, width=20, anchor="nw", compound ="left").pack()
		Button(self, text="Address", bd=0, width=20, anchor="nw", compound ="left").pack()
		Button(self, text="Order History", bd=0, width=20, anchor="nw", compound ="left").pack()
		Button(self, text="Deleted Acount", bd=0, width=20, anchor="nw", compound ="left").pack()
		self.log_out_btn = Button(self, text="Log Out",fg="red", bd=0, width=20, anchor="nw", compound ="left")
		self.log_out_btn.pack()


class HomePage(Frame):
	# "productId":"quantity"
	CART = {}
	PACKED_FRAME = []
	cart_placer = []
	user_placer = 0
	def __init__(self, parent, res):
		Frame.__init__(self, parent)

		self.user_id, self.user_name , self.user_email, self.user_phone, self.profileImgBin, self.user_addres = res
		self.top = Frame(self,relief="flat", bg="#2390d6")
		self.top.pack(fill="x", anchor="nw")

		self.lbl = Label(self.top, text="Evlsihaa e-Commerce", bg="#2390d6", font=("Joker", 20), anchor="nw")

		self.search_bar = SearchBar(self.top)
		self.search_bar.search_btn["command"] =  self.serachProducts

		self.cart_ico = PhotoImage(file="./res/media/icons/cart.png")
		self.cart = Button(self.top, text="0 Items",fg="red", relief="flat", bg="#2390d6", image=self.cart_ico, compound="top", command=self.showCart)

		self.user_ico = PhotoImage(file="./res/media/icons/user.png")
		self.user = Button(self.top, text="User",image=self.user_ico,compound="top", bg="#2390d6", relief="flat", command=self.user_details)
		self.user_Frame = USERVIEW(self.master, res)

		self.home_ico = PhotoImage(file="./res/media/icons/home.png")
		self.homebtn = Button(self.top, text="Home",image=self.home_ico,compound="top", bg="#2390d6", relief="flat", command=self.defaultView)
		
		self.lbl.pack(side='left', fill="both", expand=True)
		self.cart.pack(side="right",fill="both", ipadx=10)
		self.user.pack(side="right",fill="both", ipadx=10,)
		self.homebtn.pack(side="right",fill="both", ipadx=10, padx=(50,0))
		self.search_bar.pack(side="right",fill="both")

		self.section = Frame(self, bd=0)
		self.section.pack(anchor="nw", fill="both", expand=True)
		self.defaultView()

	def defaultView(self, products=None):
		if products == None:
			#if products != None means we got serached item to pack else defualt means pack all products
			products = self.get_products()
		#packing eithter searched result or default
		self.packer(self.pack_found_products(products))
	
	def user_details(self):
		if self.user_placer % 2 == 0:self.user_Frame.place(x=760, y=60)
		else:self.user_Frame.place_forget() 
		self.user_placer += 1

	def serachProducts(self):
		v = self.get_products(by_name=self.search_bar.get())
		if v == []:
			showinfo(title="Info", message="No products found matching with the name entered!!")
		else:
			self.defaultView(products=v)
	
	def packer(self, page):
		if not self.PACKED_FRAME == []:
			self.PACKED_FRAME.pop().destroy()
		self.PACKED_FRAME.append(page)
		page.pack(fill="both", expand=True, anchor="nw")

	def AddItemCart(self, pid):
		try:
			if self.CART[pid]:
				prev_quantity =  self.CART[pid]
				self.CART[pid] =  prev_quantity + 1
		except KeyError:
			self.CART[pid] = 1
		self.cart["text"]= f"{len(self.CART.keys())} Items"

	def place_order(self):
		qry = """INSERT INTO Orders(orderedBy, 	productIdDump) VALUES (?,?) """ 
		values = (self.user_id, json.dumps(self.CART))
		db = dbsys.DBrowser("./res/database/database.db")
		res = db.action(qry, values, "updt")

		if res:
			showinfo(message="Order Placed Succesfully!!")
			self.CART.clear()
			self.cart.invoke()
			self.cart["text"]= "0 Items"
		else:
			showinfo(message="Oder Failed!!")


	def showCart(self):
		if self.cart_placer == []:
			new = CART(self.master, p_ids=self.CART, **{"bg":"white"})
			new.place_ordr_btn["command"] = self.place_order
			new.place(x = 460,y=60)
			self.update()
			self.cart_placer.append(new)
		else:
			self.cart_placer.pop().destroy()

	def viewSpecific(self, pvc):
		nSF = PopUpProductDescription(self.section,(980,602), pvc)
		nSF.pvc_cart_btn["command"] = lambda:self.AddItemCart(pvc[0])
		self.packer(nSF)

	def pack_found_products(self, products):
		SF = ScrollingFrame(self.section,(980,602))
		def p():
			row=col=0
			for product in products:
				a = ProductViewConsumer(SF.container, product)
				a.lbl.bind("<Button-1>", lambda e, p_data=product:self.viewSpecific(p_data))
				a.add_to_cart_btn["command"] = lambda pid = a.ID:self.AddItemCart(pid)
				a.grid(row=row, column=col, padx=5, pady=(0,5))
				col += 1

				if col == 7:
					row+=1
					col = 0
		t = Thread(target=p, daemon=True)
		t.start()
		return SF

	def get_products(self,by_name=None):
		db = dbsys.DBrowser("./res/database/database.db")
		if by_name == None:
			qry = """SELECT * from Products """ 
			values = ""
		else:
			qry = """SELECT * FROM Products WHERE Name=? """
			values = (by_name,)
			
		res = db.action(qry, values, "fetch")
		return res

