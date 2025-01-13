import tkinter as tk

# Function to update the entry widget when a button is clicked
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())  # Evaluate the expression in the entry
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Setting up the Tkinter window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying input and result
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=2, relief="solid", bg="lightgray", fg="black")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operations with colors
buttons = [
    ('7', 1, 0, "lightblue", "black"), ('8', 1, 1, "lightblue", "black"), ('9', 1, 2, "lightblue", "black"),
    ('4', 2, 0, "lightblue", "black"), ('5', 2, 1, "lightblue", "black"), ('6', 2, 2, "lightblue", "black"),
    ('1', 3, 0, "lightblue", "black"), ('2', 3, 1, "lightblue", "black"), ('3', 3, 2, "lightblue", "black"),
    ('0', 4, 1, "lightblue", "black"),
    ('+', 1, 3, "orange", "white"), ('-', 2, 3, "orange", "white"), ('*', 3, 3, "orange", "white"), ('/', 4, 3, "orange", "white"),
    ('=', 4, 2, "green", "white"), ('C', 4, 0, "red", "white")
]

# Creating buttons dynamically and adding to grid
for (text, row, col, bg_color, fg_color) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), bg=bg_color, fg=fg_color, command=evaluate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), bg=bg_color, fg=fg_color, command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), bg=bg_color, fg=fg_color, command=lambda t=text: button_click(t))
    
    button.grid(row=row, column=col)

# Start the Tkinter event loop
root.mainloop()