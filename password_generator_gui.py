import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    pwd = password_entry.get()
    if pwd:
        with open("saved_passwords.txt", "a") as f:
            f.write(pwd + "\n")
        messagebox.showinfo("Saved", "Password saved successfully!")
    else:
        messagebox.showwarning("Empty", "No password to save!")

# GUI Part
root = tk.Tk()
root.title("Advanced Password Generator")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")  # default length
length_entry.pack()

tk.Button(root, text="Generate", command=generate_password).pack(pady=5)
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=5)

tk.Button(root, text="Save Password", command=save_password).pack(pady=5)

root.mainloop()