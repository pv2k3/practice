from tkinter import *

def calc():
    try:
        a = entry.get()
        b = str(eval(a))
        result_Label.config(text="Result :"+b)
    except:
        result_Label.config(text="Invalid Input")

root=Tk()

entry = Entry(root)
entry.grid(row=0, column=0)

entry.insert(0, "Enter your operation : like 123+123")

button = Button(root, text="Calculate", command=calc, fg="blue")
button.grid(row=0, column=1)

result_Label = Label(root, text="Result")
result_Label.grid(row=1)



root.mainloop()