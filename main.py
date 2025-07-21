import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "bmi_history.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Weight(kg)", "Height(cm)", "BMI", "Category"])

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        if weight <= 0 or height_cm <= 0:
            raise ValueError

        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)
        category = get_bmi_category(bmi)

        result_label.config(text=f"Your BMI: {bmi} ({category})")

        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), weight, height_cm, bmi, category])

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for weight and height.")


def show_graph():
    dates, bmis = [], []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dates.append(row["Date"])
                bmis.append(float(row["BMI"]))

        if not dates:
            messagebox.showinfo("No Data", "No BMI history available.")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(dates, bmis, marker='o', linestyle='-', color='blue')
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.title("BMI Trend Over Time")
        plt.tight_layout()
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't load data: {e}")

root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x350")
root.config(padx=20, pady=20)

tk.Label(root, text="Weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (cm):").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

tk.Button(root, text="Show BMI Graph", command=show_graph).pack(pady=10)

tk.Label(root, text="BMI Calculator - Oasis Project 2").pack(side="bottom", pady=10)

root.mainloop()