import tkinter as tk

allowed = "0123456789+-*/%(). "  # allowed characters for safety

def press(key):
    """Add button text to the entry field."""
    entry.insert(tk.END, key)

def clear():
    """Clear the entry field."""
    entry.delete(0, tk.END)
    result_label.config(text="")

def calculate():
    """Evaluate the expression in the entry."""
    expr = entry.get()
    if all(ch in allowed for ch in expr):
        try:
            result = eval(expr)
            result_label.config(text=str(result))
        except:
            result_label.config(text="Error")
    else:
        result_label.config(text="Invalid Input")

# GUI setup
window = tk.Tk()
window.title("Modern Calculator")
window.resizable(False, False)
window.configure(bg="#1e1e1e")  # dark background

# Entry field
entry = tk.Entry(window, width=20, font=("Consolas", 20), bd=0,
                 bg="#2d2d2d", fg="white", insertbackground="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

# Result label
result_label = tk.Label(window, text="", font=("Consolas", 16), anchor="e",
                        bg="#1e1e1e", fg="#00ffcc")
result_label.grid(row=1, column=0, columnspan=4, sticky="we", padx=10)

# Button style helper
def create_button(text, row, col, bg="#333333", fg="white", w=5, h=2, cmd=None, colspan=1):
    action = cmd if cmd else (lambda t=text: press(t))
    tk.Button(window, text=text, width=w, height=h, font=("Consolas", 14),
              command=action, bg=bg, fg=fg, activebackground="#555555",
              relief="flat").grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

# Button layout
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("%", 5, 2), ("+", 5, 3),
]

# Create number/operator buttons
for (text, row, col) in buttons:
    create_button(text, row, col)

# Special buttons
create_button("C", 6, 0, bg="#cc3333", cmd=clear)  # red
create_button("=", 6, 1, bg="#33cc33", cmd=calculate, colspan=2)  # green
create_button("(", 6, 3)
create_button(")", 7, 3)

window.mainloop()
