import tkinter as tk

def press(num):
    current = equation.get()
    equation.set(current + str(num))

def equalpress(event=None):
    try:
        expr = equation.get()
        result = str(eval(expr))
        result_var.set(result)
        history_listbox.insert(tk.END, f"{expr} = {result}")
    except:
        result_var.set("Error")

def clear(event=None):
    equation.set("")
    result_var.set("")

def key_press(event):
    if event.char.isdigit() or event.char in "+-*/.()":
        press(event.char)
    elif event.keysym == "Return":
        equalpress()
    elif event.keysym == "BackSpace":
        equation.set(equation.get()[:-1])
    elif event.char.lower() == 'c':
        clear()

# Main window
root = tk.Tk()
root.title("Wide Format Calculator")
root.geometry("700x500")
root.configure(bg='white')

equation = tk.StringVar()
result_var = tk.StringVar()

# Input Entry
entry = tk.Entry(root, textvariable=equation, font=('Arial', 24), bd=5, insertwidth=2, width=30, justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=20, pady=10, sticky='ew')

# Output Label
result_label = tk.Label(root, textvariable=result_var, font=('Arial', 22), fg='darkblue', bg='lightyellow', height=2, anchor='e', bd=5, relief='sunken')
result_label.grid(row=1, column=0, columnspan=5, padx=20, pady=(0, 10), sticky='ew')

# Buttons layout
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('(', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), (')', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('^', 4, 4),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3), ('C', 5, 4),
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = equalpress
    elif text == 'C':
        cmd = clear
    elif text == '^':
        cmd = lambda: press('**')
    else:
        cmd = lambda t=text: press(t)

    btn = tk.Button(root, text=text, padx=10, pady=20, font=('Arial', 16), width=6, command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5)

# History Listbox
history_frame = tk.Frame(root)
history_frame.grid(row=0, column=5, rowspan=6, padx=10, pady=10, sticky="ns")

history_label = tk.Label(history_frame, text="History", font=('Arial', 14, 'bold'))
history_label.pack(pady=(0, 5))

history_listbox = tk.Listbox(history_frame, width=30, height=20, font=('Arial', 12))
history_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

history_scrollbar = tk.Scrollbar(history_frame)
history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
history_listbox.config(yscrollcommand=history_scrollbar.set)
history_scrollbar.config(command=history_listbox.yview)

# Keyboard bindings
root.bind("<Key>", key_press)
root.bind("<Return>", equalpress)
root.bind("<c>", clear)

root.mainloop()
