import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        result_label.config(text="Result: " + result)
    except:
        result_label.config(text="Invalid Input")


window = tk.Tk()
window.title("Calculator")
window.geometry("300x150")

entry = tk.Entry(window)
entry.pack()


calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()
calculate_button.configure(background="#aaccff")

result_label = tk.Label(window, text="Result: ")
result_label.pack()

version_label = tk.Label(window, text="Version : 1")
version_label.pack()

window.mainloop()
