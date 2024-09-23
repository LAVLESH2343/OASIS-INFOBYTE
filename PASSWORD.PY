#password generator
import tkinter as tk
import random
import string
from tkinter import messagebox
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Password Generator")

        self.length_label = tk.Label(master, text="Password Length:",font="custom_font",size = 12)
        self.length_label.pack()
        root.config(bg="lightblue")
        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(master, textvariable=self.length_var)
        self.length_entry.pack()

        self.include_uppercase = tk.BooleanVar(value=True)
        self.uppercase_check = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.pack()

        self.include_numbers = tk.BooleanVar(value=True)
        self.numbers_check = tk.Checkbutton(master, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.pack()

        self.include_special = tk.BooleanVar(value=True)
        self.special_check = tk.Checkbutton(master, text="Include Special Characters", variable=self.include_special)
        self.special_check.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()

        self.password_display = tk.Entry(master, width=50)
        self.password_display.pack()

        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        length = self.length_var.get()
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1.")
            return

        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "At least one character type must be selected.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy.")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
