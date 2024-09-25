import tkinter as tk
import random
import string
import pyperclip
from tkinter import messagebox
class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Password Generator")
        master.config(bg="lightblue")
        self.length_label = tk.Label(master, text="Password Length:",height=1,width=0,font=("Georgia", 12), bg="lightblue")
        self.length_label.place(x=20,y=20)

        self.length_var = tk.IntVar(value=8)
        self.length_entry = tk.Entry(master, textvariable=self.length_var,width=10,)
        self.length_entry.place(x=155,y=22)

        self.include_uppercase = tk.BooleanVar(value=True)
        self.uppercase_check = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.include_uppercase, bg="lightblue",font=("Georgia",9))
        self.uppercase_check.place(x=20,y=50)

        self.include_lowercase = tk.BooleanVar(value=True)
        self.lowercase_check = tk.Checkbutton(master, text="Include lowercase Letters", variable=self.include_lowercase, bg="lightblue",font=("Georgia", 9))
        self.lowercase_check.place(x=220,y=50)
        
        self.include_numbers = tk.BooleanVar(value=True)
        self.numbers_check = tk.Checkbutton(master, text="Include Numbers", variable=self.include_numbers, bg="lightblue",font=("Georgia", 9))
        self.numbers_check.place(x=20,y=100)
        self.include_special = tk.BooleanVar(value=True)
        self.special_check = tk.Checkbutton(master, text="Include Special Characters", variable=self.include_special, bg="lightblue",font=("Georgia", 9))
        self.special_check.place(x=215,y=100)
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password,font=("Georgia",11),bg="yellow",fg="black")
        self.generate_button.place(x=130,y=145)
        self.password_label = tk.Label(master, text="Generated Password", height=1, width=0, bg="lightblue", font=("Georgia", 9),background="red")
        self.password_label.place(x=15, y=185)


        self.password_display = tk.Entry(master, width=40)
        self.password_display.place(x=150,y=185)

        
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard,bg="grey",fg="white",font=("Georgia",9))
        self.copy_button.place(x=180,y=220)

    def generate_password(self):
        length = self.length_var.get()
        if length < 8:
            messagebox.showerror("Error", "Password length must be at least 1.")
            return

        characters = string.ascii_uppercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
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
    root.geometry("400x250")
    app = PasswordGeneratorApp(root)
    root.mainloop()
