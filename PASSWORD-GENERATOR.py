import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_var = tk.IntVar(value=8)
        tk.Entry(root, textvariable=self.length_var).grid(row=0, column=1, padx=10, pady=10)
        self.include_uppercase = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Uppercase", variable=self.include_uppercase).grid(row=1, column=0, padx=10, pady=5)
        self.include_lowercase = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Lowercase", variable=self.include_lowercase).grid(row=1, column=1, padx=10, pady=5)
        self.include_digits = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits).grid(row=2, column=0, padx=10, pady=5)
        # self.include_special = tk.BooleanVar(value=True)
        # tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special).grid(row=2, column=1, padx=10, pady=5)
        tk.Button(root, text="Generate Password", command=self.generate_password).grid(row=3, column=0, columnspan=2, pady=20)
        self.password_var = tk.StringVar()
        tk.Entry(root, textvariable=self.password_var, state='readonly', width=50).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    def generate_password(self):
        length = self.length_var.get()
        if length < 8 or length > 50:
            messagebox.showerror("Error", "Password length must be between 8 and 50 characters.")
            return

        characters = ""
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
        if self.include_digits.get():
            characters += string.digits
        if not characters:
            messagebox.showerror("Error", "At least one character type must be selected.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
