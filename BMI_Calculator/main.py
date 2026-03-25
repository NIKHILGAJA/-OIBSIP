import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

# ---------------- SAVE DATA ----------------
def save_data(weight, height, bmi, category):
    with open("bmi_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([weight, height, bmi, category])

# ---------------- VIEW HISTORY ----------------
def view_history():
    try:
        with open("bmi_data.csv", "r") as file:
            data = file.read()
            messagebox.showinfo("BMI History", data)
    except:
        messagebox.showinfo("BMI History", "No data found")

# ---------------- SHOW GRAPH ----------------
def show_graph():
    bmis = []

    try:
        with open("bmi_data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                bmis.append(float(row[2]))

        if not bmis:
            messagebox.showinfo("Graph", "No data to display")
            return

        plt.figure()
        plt.plot(bmis, marker='o')
        plt.title("BMI Trend")
        plt.xlabel("Entries")
        plt.ylabel("BMI")
        plt.grid()
        plt.show()

    except:
        messagebox.showerror("Error", "No data found")

# ---------------- BMI CALCULATION ----------------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Enter valid values")
            return

        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")

        save_data(weight, height_cm, bmi, category)

    except:
        messagebox.showerror("Error", "Enter numeric values")

# ---------------- CLEAR ----------------
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# ---------------- UI ----------------
root = tk.Tk()
root.title("BMI Calculator - Gaja")
root.geometry("400x450")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="BMI Calculator", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Weight (kg)").grid(row=1, column=0, pady=5)
weight_entry = tk.Entry(frame, justify="center")
weight_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Height (cm)").grid(row=2, column=0, pady=5)
height_entry = tk.Entry(frame, justify="center")
height_entry.grid(row=2, column=1, pady=5)

tk.Button(frame, text="Calculate BMI", command=calculate_bmi,
          bg="green", fg="white", width=20).grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(frame, text="Clear", command=clear_fields, width=15)\
    .grid(row=4, column=0, columnspan=2, pady=5)

tk.Button(frame, text="View History", command=view_history, width=15)\
    .grid(row=5, column=0, columnspan=2, pady=5)

tk.Button(frame, text="Show Graph", command=show_graph, width=15)\
    .grid(row=6, column=0, columnspan=2, pady=5)

result_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), justify="center")
result_label.grid(row=7, column=0, columnspan=2, pady=20)

root.mainloop()