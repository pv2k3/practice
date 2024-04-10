# Convertor app

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
def calculate():
    try:
        val = entry_val.get()
        convert_to_meter = val * 1.61
        output_var.set(str(convert_to_meter))

    except:
        output_var.set("Invalid input")

root = ttk.Window(themename="journal")                                                                # Create Window
root.title("DISTANCE CONVERTOR")
root.geometry("350x150")

label = ttk.Label(root, text="Convertor miles to meter", font="Calibre 18 bold", foreground="green")
label.pack(pady=5)

frame = ttk.Frame(root, padding=10)

entry_val = ttk.IntVar()
entry = ttk.Entry(frame, textvariable=entry_val)


button = ttk.Button(frame, text="Convert", command=calculate)

frame.pack(pady=5)
entry.pack(side="left", padx=15)
button.pack(side="left")

output_var = ttk.StringVar()

result_label = ttk.Label(root, font="Calibre 18", textvariable=output_var)
result_label.pack()

button1 = ttk.Button(root, text="Button")
button1.pack()
radio = ttk.Radiobutton(root, text="Button")
radio.pack()
check = ttk.Checkbutton(root, text="Button")
check.pack()

root.mainloop()                                                             # Run
