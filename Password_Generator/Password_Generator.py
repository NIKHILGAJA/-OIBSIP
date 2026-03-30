import tkinter as tk
from tkinter import messagebox
import random
import string

#  GENERATE PASSWORD 
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter valid length")
            return

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one option")
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except:
        messagebox.showerror("Error", "Enter valid number")

#  COPY TO CLIPBOARD 
def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showerror("Error", "Generate password first")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")

#  CLEAR 
def clear_fields():
    password_entry.delete(0, tk.END)

# UI 
root = tk.Tk()
root.title("Password Generator - Gaja")
root.geometry("400x350")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=20)

# Title
tk.Label(frame, text="Password Generator", font=("Arial", 18, "bold"))\
    .grid(row=0, column=0, columnspan=2, pady=10)

# Length
tk.Label(frame, text="Password Length").grid(row=1, column=0, pady=5)
length_entry = tk.Entry(frame, justify="center")
length_entry.grid(row=1, column=1, pady=5)

# Options
var_letters = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(frame, text="Include Letters", variable=var_letters)\
    .grid(row=2, column=0, columnspan=2, sticky="w")

tk.Checkbutton(frame, text="Include Numbers", variable=var_numbers)\
    .grid(row=3, column=0, columnspan=2, sticky="w")

tk.Checkbutton(frame, text="Include Symbols", variable=var_symbols)\
    .grid(row=4, column=0, columnspan=2, sticky="w")

# Generate button
tk.Button(frame, text="Generate Password", command=generate_password,
          bg="green", fg="white", width=20)\
    .grid(row=5, column=0, columnspan=2, pady=10)

# Output
password_entry = tk.Entry(frame, justify="center", width=25, font=("Arial", 12))
password_entry.grid(row=6, column=0, columnspan=2, pady=5)

# Buttons
tk.Button(frame, text="Copy", command=copy_password, width=10)\
    .grid(row=7, column=0, pady=5)

tk.Button(frame, text="Clear", command=clear_fields, width=10)\
    .grid(row=7, column=1, pady=5)

# Run
root.mainloop()