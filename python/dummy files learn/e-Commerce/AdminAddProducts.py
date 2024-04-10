from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
import sqlite3
from tkinter.messagebox import showinfo
from res.database import dbsys
from res.pages import ScrollingFrame
from threading import Thread
from PIL import Image, ImageTk

DBFP = "./res/database/database.db"

class LabeledEntry(LabelFrame):
	def __init__(self,parent, lbltext, *args, **kwargs):
		LabelFrame.__init__(self,parent, *args, **kwargs)
		self.config(text=lbltext,bd=0)
		self.entryVar=StringVar()
		self.entry = Entry(self,textvariable=self.entryVar,highlightthickness=1,relief='flat',width=18)
		self.entry.pack(fill='both',side='top',anchor="nw", expand=True)
	def get(self):
		return self.entryVar.get()
	def set(self,d):
		self.entryVar.set(d)


class DBLabeledEntry(LabeledEntry):
	def __init__(self,parent, lbltext,dbinfo,*args, **kwargs):
		LabeledEntry.__init__(self,parent,lbltext,*args, **kwargs)

		self.dbinfo=dbinfo
		self.entryVar.trace("w",lambda a,b,c:self.set_buttons())
		self.btnF=Frame(self,**kwargs)
		#images
		self.tick = PhotoImage(file="./res/media/icons/tick.png")
		self.ccl = PhotoImage(file="./res/media/icons/cancel.png")

		Button(self.btnF,image=self.tick,command=self.update, bd=0, **kwargs).pack(side='left')
		self.cnclbtn = Button(self.btnF,image=self.ccl,bd=0,command=lambda :self.btnF.pack_forget(), **kwargs)
		self.cnclbtn.pack()
	def set_buttons(self):
		self.btnF.pack(side="bottom", anchor="nw")
	def update(self):
		
		# {DBfp:'',tablename:'',columnName,fieldname:'',wherecol:''}
		qry = """ UPDATE %s SET %s = ? WHERE %s = ? """%( self.dbinfo['tablename'], self.dbinfo['columnName'], self.dbinfo["wehereCol"])
		db  = dbsys.DBrowser(self.dbinfo['dbfp'])
		db.action(qry,(self.entryVar.get().strip(), self.dbinfo['wehereColVal'] ),'updt')
		self.btnF.pack_forget()
		showinfo(title="Info",message="Update Was Completed Succesfully")


class ProductView(Frame):
	COUNT = 0
	def __init__(self, parent, data):
		Frame.__init__(self, parent)
		self.ID = data[0]
		self.data = data
		self["bd"] = 2
		self["relief"] = "ridge"

		self.img = Label(self)
		self.img.pack(side="left", fill="both")

		self.container = Frame(self, bg="red")

		Label(self.container, text="Name: " +data[1], anchor="nw", width=75).pack(fill="x")
		Label(self.container, text="Price : "+str(data[2]), anchor="nw", width=75).pack(fill="x")
		Label(self.container, text="Sold by: " + data[5], anchor="nw", width=75).pack(fill="x")
		Label(self.container, text="Available: " +data[7], anchor="nw", width=75).pack(fill="x")
		Label(self.container, text="Discounts: " +str(data[6]), anchor="nw", width=75).pack(fill="x")
		Label(self.container, text="Description: " +data[3], anchor="nw", width=75).pack(fill="x")

		self.i = PhotoImage(file="./res/media/icons/edit.png")
		self.closeIcon = PhotoImage(file="./res/media/icons/cancel.png")
		btn = Button(self, text="Edit", image=self.i, relief="flat", command=self.EDIT)
		btn.pack(side="right",fill="y")

		self.container.pack(side="top", fill="both")

		self.setImg(data[4],self.img)

	def EDIT(self):
		if self.COUNT == 0:
			new = Frame(self.master.master, bg="#2390d6", pady=10, padx=10, height=555)

			kw = {"bg":"#2390d6"}
			# update tablename set columnname = ?{Nm} where wherecol = wherecol[id] = ?{wherecolVal}

			Button(new,image=self.closeIcon, bd=0, command=lambda:self.unplace(new),**kw).place(x=342, y=0)

			name=DBLabeledEntry(new, "Enter New Name:",{"dbfp":DBFP, "tablename":"Products","columnName":"Name","wehereCol":"id","wehereColVal":self.ID},**kw)
			name.place(x=10, y=30)
			name.set(self.data[1])
			name.entry["width"] = 50
			
			pr=DBLabeledEntry(new, "Enter New Price:",{"dbfp":DBFP, "tablename":"Products","columnName":"price","wehereCol":"id","wehereColVal":self.ID}, **kw)
			pr.place(x=10, y=100)
			pr.set(self.data[2])
			pr.entry["width"] = 50
			
			d = DBLabeledEntry(new, "Enter New Discount:",{"dbfp":DBFP, "tablename":"Products","columnName":"discount","wehereCol":"id","wehereColVal":self.ID}, **kw)
			d.place(x=10, y=170)
			d.set(self.data[6])
			d.entry["width"] = 50

			des = DBLabeledEntry(new, "Enter New Description:",{"dbfp":DBFP, "tablename":"Products","columnName":"description","wehereCol":"id","wehereColVal":self.ID}, **kw)
			des.place(x=10, y=240)
			des.set(self.data[3])
			des.entry["width"] = 50
			
			avlvar = BooleanVar()
			def updtAval():
				db = dbsys.DBrowser(DBFP)
				q = """UPDATE Products SET availability = ? WHERE id = ? """
				db.action(q, (avlvar.get(),self.ID), "updt")

			avl = Checkbutton(new,text="Available", variable=avlvar, **kw, command=updtAval)
			avl.place(x=10, y=310)

			img = Label(new)
			img.place(x=10, y =360)	

			def updtImg():
				fp = askopenfilename(filetypes= [("Image files", "*.jpg *.png *.jpeg"), ("All File","*.*")] )
				db = dbsys.DBrowser(DBFP)
				
				with open(fp, "rb") as f:
					imgBin = f.read()

				q = """UPDATE Products SET image = ? WHERE id = ? """
				db.action(q,(imgBin,self.ID), "updt")
				self.setImg(imgBin, img)

			Button(new, text="Change", command=updtImg).place(x=10,y=490)
			self.setImg(self.data[4], img)

			Button(new, text="Remove", fg="white", bg="red", bd=0,pady=5, padx=10, command=self.remove).place(x=280, y=500)
			self.animate(frame=new,width=380,x=320, y=0)
			self.COUNT = 1

	def remove(self):
		db = dbsys.DBrowser(DBFP)
		qry = """ DELETE FROM Products WHERE id = ? """
		db.action(qry, (self.ID, ), "updt")
		showinfo(title="Deleted", message="Product Was Deleted Succesfully!!")
	def unplace(self,f):
		self.COUNT = 0
		f.place_forget()

	def animate(self,frame, width, x,y):
		frame.place(x = 320,y=0)
		def increase():
			for i in range(0,width+5,10):
				frame["width"] = i
				self.update()
			self.update()

		t = Thread(target=increase, daemon=True)
		t.start()

	def setImg(self, imgBin, lbl):
		with open("./res/media/dump.dat", "wb") as f:
			f.write(imgBin)
			f.close()

		img = Image.open("./res/media/dump.dat")
		img = img.resize((120,120))
		img = ImageTk.PhotoImage(img)
		lbl["image"] = img
		lbl.image = img
		self.update()

class Application(Tk):
	PACKED_FRAME = []
	def __init__(self):
		Tk.__init__(self)

		self.side_frame = Frame(self, bg="#2390d6",)
		self.side_frame.pack(side="left", fill="y")

		self.mid_frame = Frame(self, bg="red")
		self.mid_frame.pack(side="right",fill="both", expand=True)

		#========================== END ==================================

		self.view_all = Button(self.side_frame,bg="#2390d6",text="View All Products", width=25, relief="flat",anchor="nw", font=("",15), command = lambda:self.ViewAllProductPage( self.view_all ))
		self.view_all.pack(pady=(0,10))

		self.add_btn = Button(self.side_frame,bg="#2390d6",text="Add New Product", width=25, relief="flat",anchor="nw", font=("",15), command = lambda:self.AddNewProductPage(self.add_btn ))
		self.add_btn.pack(pady=(0,10))

		Label(self.side_frame, text="Created By:Elsker Elvish" ,bg="#2390d6", relief="flat").pack(side="bottom", fill="x")
		#pack Add Products Automatically....
		self.add_btn.invoke()


	def ViewAllProductPage(self, btn):
		frame = Frame(self.mid_frame)
		self.packer([frame, btn])

		top = Frame(frame, bg="#ddd",pady=2, padx=2)
		top.pack(side="top", fill="x")

		search_entry = Entry(top, font=("", 15), relief="flat")
		search_entry.pack(side="left",fill="both",expand=True,  anchor="nw")

		ico = PhotoImage(file="./res/media/icons/search.png")
		search_btn = Button(top, image=ico, relief="flat")
		search_btn.image = ico
		search_btn.pack(side="right", fill="both")

		mid = ScrollingFrame(frame, (700,550))
		mid.pack(anchor="nw", fill="x", expand=True)

		db = dbsys.DBrowser(DBFP)
		qry = """ SELECT * from Products """
		res = db.action(qry,"", "fetch")
		
		def pack_items():
			for product in res:
				new = ProductView(mid.container, product)
				new.pack(fill="x", expand=True)

		t = Thread(target=pack_items, daemon=True)
		t.start()


	def AddNewProductPage(self, btn):
		# =================================== contents to Add new Products  ===================
		add_product_frame = Frame(self.mid_frame, padx=50, pady=20 )
		kw = {"font":('',12)}
		name =  LabeledEntry(add_product_frame,"Product Name: ", **kw)
		name.pack(fill="x", anchor="nw", pady=(0,15))

		price =  LabeledEntry(add_product_frame,"Product Price: ", **kw)
		price.pack(fill="x", anchor="nw", pady=(0,15))

		Label(add_product_frame, text="Description: ",**kw).pack(anchor="nw")
		descp = ScrolledText(add_product_frame, width=100, font=("",10), relief="flat", height=5)
		descp.pack(anchor="nw", pady=(0,15))

		soldBy =  LabeledEntry(add_product_frame,"Product Sold By:: ", **kw)
		soldBy.pack(fill="x", anchor="nw", pady=(0,15))

		discount =  LabeledEntry(add_product_frame,"Discount Amount: ", **kw)
		discount.pack(fill="x", anchor="nw", pady=(0,15))

		Label(add_product_frame, text="Image: ").pack(anchor="nw")
		ImageLocation = StringVar()
		product_image = Label(add_product_frame, text="No file selected...", **kw) 
		product_image.pack(anchor="nw")
		Button(add_product_frame, text="Choose File",fg="blue", command = lambda: self.selectImg(ImageLocation, product_image)).pack(anchor="nw", pady=(0,12))

		available = BooleanVar()
		is_available = Checkbutton(add_product_frame, text="Available",relief="flat", width=100, font=("",12), anchor="nw", variable =  available)
		is_available.pack(anchor="nw", pady=(0,20))

		def Adddata():
			Pname = name.get()
			Pprice = price.get()
			Pdescp = descp.get(1.0,END)
			PsoldBy = soldBy.get()
			Pdiscount = discount.get()
			with open(ImageLocation.get(),"rb") as f:
				PimgBin = f.read()
				f.close()
			Pavailable =  available.get()

			db = dbsys.DBrowser(DBFP)
			qry = """INSERT INTO Products(Name, price, description, image, soldBy, discount, availability) VALUES(?,?,?,?,?,?,?) """
			values = (Pname, int(Pprice),Pdescp, PimgBin, PsoldBy, int(Pdiscount),str(Pavailable))
			res = db.action(qry, values, "updt")
			if res:
				showinfo(title="Success!!", message=f"{Pname} was added succesfully...")


		Button(add_product_frame, text="Add Product", width=100,font=("",15), relief="flat", bg="#06f866", command=Adddata).pack(anchor="nw")
		
		self.packer([add_product_frame,btn])

	def packer(self, page):
		if not self.PACKED_FRAME == []:
			rem = self.PACKED_FRAME.pop()
			rem[0].destroy()
			rem[1]["bg"] = "#2390d6"

		self.PACKED_FRAME.append(page)
		page[0].pack(fill="both", expand=True, anchor="nw")
		page[1]["bg"] = "#f0f0ed"

	def selectImg(self, var,lbl):
		fp = askopenfilename(filetypes= [("Image files", "*.jpg *.png *.jpeg"), ("All File","*.*")])
		lbl["text"] = fp
		var.set(fp)


if __name__ == "__main__":
	app = Application()
	app.title("Adminitrator:  Add Products")
	app.geometry("1000x600")
	app.resizable(0,0)
	app.mainloop()
