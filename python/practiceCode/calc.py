import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        result_label.config(text="Result: " + result)
    except:
        result_label.config(text="Invalid Input")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an input entry field
entry = tk.Entry(window)
entry.pack()

# Create a Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Run the main loop
window.mainloop()