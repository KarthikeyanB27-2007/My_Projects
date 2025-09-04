import tkinter as tk
from tkinter import messagebox
import random

class Car:
    def __init__(self, model, reg_no, owner, fuel):
        self.model = model
        self.reg_no = reg_no
        self.owner = owner
        self.fuel = fuel

    def __str__(self):
        return f"{self.model} ({self.reg_no}) - Owner: {self.owner}"

class CarResaleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car/Bike Resale Application (OLX Style)")
        self.root.geometry("1000x600")  # Make window wider

        self.cars = []

        # Car Creation Section
        tk.Label(root, text="Model:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.model_entry = tk.Entry(root, width=40)
        self.model_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Reg No:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.reg_entry = tk.Entry(root, width=40)
        self.reg_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Owner:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.owner_entry = tk.Entry(root, width=40)
        self.owner_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Fuel:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.fuel_entry = tk.Entry(root, width=40)
        self.fuel_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(root, text="Add Car/Bike", command=self.add_car, width=30).grid(row=4, column=0, columnspan=2, pady=10)

        # Car Listings
        tk.Label(root, text="Car/Bike Listings").grid(row=5, column=0, columnspan=2, pady=5)
        self.car_listbox = tk.Listbox(root, width=100, height=8)
        self.car_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        # Resale Section
        tk.Label(root, text="New Owner:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.new_owner_entry = tk.Entry(root, width=40)
        self.new_owner_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(root, text="Sale Price ($):").grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = tk.Entry(root, width=40)
        self.price_entry.grid(row=8, column=1, padx=10, pady=5)

        tk.Button(root, text="Resale Car/Bike", command=self.resale_car, width=30).grid(row=9, column=0, columnspan=2, pady=10)

        # Transaction History
        tk.Label(root, text="Transaction History").grid(row=10, column=0, columnspan=2, pady=5)
        self.history_listbox = tk.Listbox(root, width=120, height=10)
        self.history_listbox.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

        # AI-generated reasons
        self.reasons = [
            "Needed for daily commute",
            "Wanted to upgrade from old model",
            "For family use",
            "For long road trips",
            "Affordable deal, couldn’t miss it",
            "Collector’s choice",
            "Starting a business with this vehicle"
        ]

    def add_car(self):
        model = self.model_entry.get()
        reg_no = self.reg_entry.get()
        owner = self.owner_entry.get()
        fuel = self.fuel_entry.get()

        if model and reg_no and owner and fuel:
            car = Car(model, reg_no, owner, fuel)
            self.cars.append(car)
            self.car_listbox.insert(tk.END, str(car))
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def resale_car(self):
        selected = self.car_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a car to resale")
            return

        new_owner = self.new_owner_entry.get()
        price = self.price_entry.get()

        if not new_owner or not price.isdigit():
            messagebox.showwarning("Input Error", "Enter valid new owner and sale price")
            return

        car_index = selected[0]
        car = self.cars[car_index]
        old_owner = car.owner

        # Update owner
        car.owner = new_owner
        self.car_listbox.delete(car_index)
        self.car_listbox.insert(car_index, str(car))

        # AI-generated reason
        reason = random.choice(self.reasons)

        # Log transaction
        transaction = f"{car.model} ({car.reg_no}) sold from {old_owner} to {new_owner} for ${price} | Reason: {reason}"
        self.history_listbox.insert(tk.END, transaction)

        # Clear inputs
        self.new_owner_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def clear_entries(self):
        self.model_entry.delete(0, tk.END)
        self.reg_entry.delete(0, tk.END)
        self.owner_entry.delete(0, tk.END)
        self.fuel_entry.delete(0, tk.END)

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CarResaleApp(root)
    root.mainloop()