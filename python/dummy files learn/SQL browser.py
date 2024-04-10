
from tkinter import *
from tkinter.ttk import Combobox
import sqlite3
from tkinter.messagebox import showinfo

class create_columns(Frame):
	def __init__(self,parent,**kwargs):
		Frame.__init__(self,parent,**kwargs)

		self.column_created = list()

		Label(self, text = "Databse Name: ").place(x=5,y=10)

		self.db_name = Entry(self, width=55)
		self.db_name.place(x=100,y=10)

		Label(self, text = "Table Name: ").place(x=5,y=50)

		self.table_name = Entry(self, width=55)
		self.table_name.place(x=100,y=50)

		data_type = ["INTEZER", "TEXT", 'BLOB', "NUMERIC","REAL"]
		Label(self, text='Column Name: ').place(x=5,y=120)

		self.col_name = Entry(self,width=30)
		self.col_name.place(x=100,y=120)
		#when user  hits ente key
		self.col_name.bind("<Return>",self.add)

		self.col_data_type = Combobox(self, values=data_type)
		self.col_data_type.place(x=300,y=120)

		Button(self, text='Add',command=self.add).place(x=240,y=150)
		Button(self, text='Remove',command=self.rmv).place(x=230,y=180)

		self.show_queries = Text(self,width=60,height=20)
		self.show_queries.place(x=5,y=220)

		self.show_queries.insert(1.0, """Heyy Friends Subscribe in Telegram and share with everyoe! Follow on instagram elsker_elvish.py """)

		Button(self, text='Create Database', command=self.create_database).place(x=200,y=580)

	def update_text(self,char):
		#clear field first
		self.show_queries.delete(1.0,END)
		#insert content
		self.show_queries.insert(1.0, char)

	def add(self, event = None):
		col_name = self.col_name.get()
		col_data_type = self.col_data_type.get()
		#clear fields
		self.col_name.delete(0,END)
		self.column_created.append( "{} {}".format(col_name, col_data_type) )
		self.create_query()

	def rmv(self):
		#it will work only when the list will have any item
		if not self.column_created==[]:
			self.create_query()
			self.update_text(char)

	def create_query(self):
		table_name = self.table_name.get()
		cols = " ,".join(self.column_created )
		qry = """  CREATE TABLE {} ( {} )""".format( table_name  , cols)
		self.update_text(qry)
		return qry

	def create_database(self):
		#connect
		db = sqlite3.connect( self.db_name.get()+'.db' )
		#create cursor
		cur = db.cursor()
		q=self.create_query() 
		cur.execute(q)
		db.close()

		file = open('Your Query.txt','w')
		file.write(q)
		file.close()
		showinfo(message="Database was Created Sucessfully! and Query was  saved as Your Query.txt")

root = Tk()
root.geometry('500x650+200+0')
root.title("With love from Elsker Elvish.py Subscribe for more!")
root.resizable(0,0)
Label(root, text='Create SQL LITE Database', bg='yellow' , font=("",15) ).pack(side='top' ,fill='x', anchor='nw')
v = create_columns(root)
v.pack(expand=True, fill='both')
root.mainloop()