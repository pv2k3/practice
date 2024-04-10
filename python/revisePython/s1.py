import tkinter as tk

def greet():
    name = entry.get()
    result_label = tk.Label(root, text=" Hello "+name)
    result_label.pack()



root = tk.Tk()
root.title("GREET")
root.geometry("300x300")

start = tk.Label(root, text="Your name\n")
start.pack()

entry = tk.Entry(root, borderwidth=5, fg="red", bg="yellow")
entry.pack()

button = tk.Button(root, text="Greet", command=greet, fg="blue", bg="yellow")
button.pack()

root.mainloop()
