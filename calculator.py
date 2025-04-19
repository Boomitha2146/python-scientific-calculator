import tkinter as tk
import math

# Initialize angle_mode at the top of the script
angle_mode = "Deg"  # Default angle mode

# Function to evaluate the expression
def click(event):
    global angle_mode  # Declare global variable first
    current = entry.get()
    text = event.widget["text"]
    
    if text == "=":
        try:
            # Evaluate the expression using eval, but ensure valid function calls are complete
            if 'log10(' in current:
                # Get the number inside the parentheses
                num = float(current[6:-1])  # Extract number from log10(num)
                result = math.log10(num)
            elif 'sin(' in current:
                num = float(current[4:-1])
                result = math.sin(math.radians(num)) if angle_mode == "Deg" else math.sin(num)
            elif 'cos(' in current:
                num = float(current[4:-1])
                result = math.cos(math.radians(num)) if angle_mode == "Deg" else math.cos(num)
            elif 'tan(' in current:
                num = float(current[4:-1])
                result = math.tan(math.radians(num)) if angle_mode == "Deg" else math.tan(num)
            elif '√(' in current:
                num = float(current[2:-1])
                result = math.sqrt(num)
            elif 'log(' in current:
                num = float(current[4:-1])
                result = math.log(num)
            else:
                result = eval(current)  # For normal calculations
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            # Add to history
            history_list.insert(tk.END, current + " = " + str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "⌫":
        entry.delete(len(current)-1, tk.END)
    elif text == "π":
        entry.insert(tk.END, str(math.pi))
    elif text == "e":
        entry.insert(tk.END, str(math.e))
    elif text == "Deg":
        angle_mode = "Deg"
        entry.insert(tk.END, "Deg Mode")
    elif text == "Rad":
        angle_mode = "Rad"
        entry.insert(tk.END, "Rad Mode")
    else:
        # Insert function with parentheses
        if text == "log":
            entry.insert(tk.END, "log10(")
        elif text == "sin":
            entry.insert(tk.END, "sin(")
        elif text == "cos":
            entry.insert(tk.END, "cos(")
        elif text == "tan":
            entry.insert(tk.END, "tan(")
        elif text == "√":
            entry.insert(tk.END, "√(")
        elif text == "ln":
            entry.insert(tk.END, "log(")
        elif text == "x²":
            entry.insert(tk.END, "**2")
        elif text == "xʸ":
            entry.insert(tk.END, "**")
        else:
            entry.insert(tk.END, text)

# Function for keyboard support
def key_press(event):
    char = event.char
    if char == "=":
        click(event)
    elif char in "0123456789+-*/.()":
        entry.insert(tk.END, char)
    elif char == "BackSpace":
        current = entry.get()
        entry.delete(len(current)-1, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Realistic Scientific Calculator")
root.geometry("400x600")
root.bind("<Key>", key_press)

# Entry widget to display input and output
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=10)

# History listbox
history_list = tk.Listbox(root, height=5, font=("Arial", 10))
history_list.grid(row=1, column=0, columnspan=5, pady=5)

# Buttons layout
buttons = [
    ['C', '⌫', '(', ')', 'mod'],
    ['7', '8', '9', '/', '√'],
    ['4', '5', '6', '*', 'x²'],
    ['1', '2', '3', '-', 'xʸ'],
    ['0', '.', '=', '+', '1/x'],
    ['sin', 'cos', 'tan', 'ln', 'log'],
    ['π', 'e', 'exp', 'Deg', 'Rad']
]

# Add buttons to the grid
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        button = tk.Button(root, text=btn_text, font=("Arial", 14), padx=20, pady=20)
        button.grid(row=i+2, column=j, sticky="nsew")
        button.bind("<Button-1>", click)

# Start the main loop
root.mainloop()
