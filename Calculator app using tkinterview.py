import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for button in row:
        if button == "=":
            cmd = calculate
        else:
            cmd = lambda x=button: button_click(x)

        tk.Button(
            row_frame,
            text=button,
            font=("Arial", 16),
            command=cmd
        ).pack(side="left", expand=True, fill="both")

tk.Button(
    root,
    text="Clear",
    font=("Arial", 16),
    command=clear
).pack(fill="both")

root.mainloop()