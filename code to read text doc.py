import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            content = file.read()

        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

root = tk.Tk()
root.title("Text File Reader")
root.geometry("500x400")

btn = tk.Button(root, text="Open Text File", command=open_file)
btn.pack(pady=10)

text_area = tk.Text(root)
text_area.pack(expand=True, fill="both")

root.mainloop()