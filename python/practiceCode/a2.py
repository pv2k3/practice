import tkinter as tk

def calculate():
    try:
        num = int(entry.get())
        rev = 0
        i = abs(num)
        while i > 0:
            rev = rev*10 + (i % 10)
            i //= 10
        if num < 0:
            rev *= -1
        result_label.config(text="Reverse: " + str(rev))
    except:
        result_label.config(text="Invalid Input")


window = tk.Tk()
window.title("Reverse")
window.geometry("600x300")

entry = tk.Entry(window, width=50)
entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()
calculate_button.configure(background="#aaccff")

result_label = tk.Label(window, text="Reverse: ")
result_label.pack()

version_label = tk.Label(window, text="Version : 1.1")
version_label.pack(pady=200, anchor="se")



window.mainloop()
