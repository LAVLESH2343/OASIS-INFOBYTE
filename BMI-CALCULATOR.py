import tkinter as tk

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / ((height / 100) ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.resizable(False,False)
tk.Label(root, text="Height (cm):").place(x=0, y=0)
tk.Label(root, text="Weight (kg):").place(x=1, y=0)
entry_height = tk.Entry(root)
entry_weight = tk.Entry(root)
entry_height.grid(row=0, column=1)
entry_weight.grid(row=1, column=1)
calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2)
result_label = tk.Label(root, text="BMI: ")
result_label.grid(row=3, column=0, columnspan=2)
root.mainloop()
