import tkinter as tk
from tkinter import ttk
c1 = "#60cdbc"
root = tk.Tk()
root.title("BMI Calculator")
root.iconbitmap("bmi.ico")  # Correct
root.geometry("295x230")
root.resizable(height=False,width=False)
root.config(bg="#60cdbc")
def calc_bmi():
    weight = weight_var.get()
    height = height_var.get()

    if height <= 0 or weight <= 0:
        result_var.set("Please enter valid values!")
        return
    height_in_meter = height / 100
    BMI = weight / (height_in_meter ** 2)
    result_var.set(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        category = "Underweight"
    elif 18.5 <= BMI < 24.9:
        category = "Normal weight"
    elif 25 <= BMI < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
        
    result_var.set(f"Your BMI is {BMI:.2f} you are {category}")


appname = tk.Label(root,text="BMI CALCULATOR 🧮",anchor="center",font=("Georgia",15),bg="red",width=50)
appname.pack()
weight = tk.Label(root,text="Enter Weight in (KG):",bg="white",fg="brown",font=("Georgia",9))
weight.place(x=10,y=45)
weight_var = tk.IntVar(value=0)
entry_weight=tk.Entry(root,textvariable=weight_var,width=15)
entry_weight.place(x=150,y=50)

height = tk.Label(root,text="Enter Height in (CM):",bg="white",fg="brown",font=("Georgia",9))
height.place(x=10,y=80)
height_var = tk.IntVar(value=0)
entry_height=tk.Entry(root,textvariable=height_var,width=15)
entry_height.place(x=150,y=80)
button = tk.Button(root, text="CALCULATE BMI",command=calc_bmi,bg="grey",fg="white",font=("Georgia",9))
button.place(x=80,y=125)
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, bg="#60cdbc", font=("Georgia", 10))
result_label.place(x=60, y=160)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, bg="#60cdbc", font=("Georgia", 10))
result_label.place(x=20, y=160)


root.mainloop()