import tkinter as tk

def display_greeting():
    name = name_entry.get()
    greeting_label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.geometry("300x150")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

submit_button = tk.Button(root, text="Submit", command=display_greeting)
submit_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

root.mainloop()
