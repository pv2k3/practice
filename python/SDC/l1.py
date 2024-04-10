import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("First window")
root.geometry("300x300")

label_text = ttk.Label(root, text="SDC", padding=10)
label_text.pack()

root.mainloop()



# ttk bootstrap 1.9.0