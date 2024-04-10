from tkinter import *


# from tkinter import ttk
# Show value on entry field on click


def on_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + value)


# Clear the entry field
def clear():
    entry.delete(0, END)


# To perform the operation
def calculate():
    try:
        a = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(a))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


root = Tk()
root.title("Priyanshu Verma")

entry = Entry(root, width=16, font=("Arial", 20), justify="right", fg="green", borderwidth=3)
entry.grid(row=0, column=0, columnspan=4, pady=5)

bu = [
    "C", "(", ")", "+",
    "7", "8", "9", "-",
    "6", "5", "4", "*",
    "3", "2", "1", "/",
    "0", ".", "%", "="
]

r = 1
c = 0

for button in bu:
    Button(root, text=button, width=4, height=2, background="#C1CDCD",
           command=lambda b=button: on_click(b) if (b not in ["C", "="]) else (calculate() if b == "=" else clear())
           , fg="blue").grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()
