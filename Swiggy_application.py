import tkinter as tk
from tkinter import messagebox
import random


class UnavagamApp:
    menu = {
        'veg': {'margerita': 129, 'cheese_and_corn': 100, 'veg_fried_rice': 260, 'veg_biriyani': 210, 'Veg_burger': 170, 'veg_noodles': 150, 'paneer_butter_masala': 300, 'dal_makhani': 250, 'jeera_rice': 200},
        'non_veg': {'pepper_barbeque': 199, 'Mutton_biriyani': 169, 'Chicken_biriyani': 200, 'chicken_burger': 180, 'chicken_fried_rice': 250, 'chicken_noodles': 220}, 
        'snacks': {'garlic_bread': 120, 'bingo': 59, 'chicken_cheese_balls': 170, 'lays': 45, 'french_fries': 99, 'bread_bajji': 30, 'samosa': 20}, 
        'desserts': {'choco_lava': 100, 'mousse cake': 169, 'brownie': 150, 'ice_cream': 80, 'pastry': 90, 'donut': 40, 'cup_cake': 70, 'gulab_jamun': 50}, 
        'drinks': {'coke': 90, 'pepsi': 78, 'sprite': 50, 'red bull': 120, 'fanta': 70, 'tea': 20, 'coffee': 50, 'thums_up': 80}
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Unavagam App")
        self.root.geometry("500x500")
        self.root.configure(bg="#f2e9e4")  # light coloured background

        self.users = []
        self.current_user = None
        self.login_status = False
        self.cart = {}

        self.main_frame = tk.Frame(self.root, bg="#f2e9e4")  # background frame colour
        self.main_frame.pack(fill="both", expand=True)

        self.home_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def styled_button(self, parent, text, command):
        """Reusable black button with white text."""
        return tk.Button(parent, text=text, command=command,
                         bg="black", fg="white", font=("Arial", 11), padx=10, pady=5)

    def home_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Welcome to Unavagam", font=("Arial", 16),
                 bg="#f2e9e4", fg="black").pack(pady=20)

        self.styled_button(self.main_frame, "Register", self.register_screen).pack(pady=10)
        self.styled_button(self.main_frame, "Login with Phone", lambda: self.login(choice=1)).pack(pady=10)
        self.styled_button(self.main_frame, "Login with Email", lambda: self.login(choice=2)).pack(pady=10)

    def register_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Register New User", font=("Arial", 14),
                 bg="#f2e9e4").pack(pady=10)

        tk.Label(self.main_frame, text="Name:", bg="#f2e9e4").pack()
        name_entry = tk.Entry(self.main_frame)
        name_entry.pack()

        tk.Label(self.main_frame, text="Email:", bg="#f2e9e4").pack()
        email_entry = tk.Entry(self.main_frame)
        email_entry.pack()

        tk.Label(self.main_frame, text="Phone:", bg="#f2e9e4").pack()
        phone_entry = tk.Entry(self.main_frame)
        phone_entry.pack()

        def save_user():
            name = name_entry.get().strip()
            email = email_entry.get().strip()
            phone = phone_entry.get().strip()

            if not name or not email or not phone:
                messagebox.showerror("Error", "All fields are required!")
                return

            if not phone.isdigit():
                messagebox.showerror("Error", "Phone must be digits only!")
                return

            for u in self.users:
                if u["email"] == email or u["phno"] == int(phone):
                    messagebox.showerror("Error", "User already exists!")
                    return

            self.users.append({"name": name, "email": email, "phno": int(phone)})
            messagebox.showinfo("Success", "User Registered Successfully ✅")
            self.home_screen()

        self.styled_button(self.main_frame, "Register", save_user).pack(pady=10)
        self.styled_button(self.main_frame, "Back", self.home_screen).pack()

    def validate_otp(self, user):
        og_otp = random.randint(1000, 9999)
        messagebox.showinfo("OTP Sent", f"Your OTP is: {og_otp}")

        otp_window = tk.Toplevel(self.root)
        otp_window.title("Enter OTP")
        otp_window.geometry("300x150")
        otp_window.configure(bg="#dbe7e4")

        tk.Label(otp_window, text="Enter OTP:", bg="#dbe7e4").pack(pady=5)
        otp_entry = tk.Entry(otp_window)
        otp_entry.pack()

        def check_otp():
            try:
                entered = int(otp_entry.get())
                if entered == og_otp:
                    self.login_status = True
                    self.current_user = user
                    messagebox.showinfo("Success", f"Welcome {user['name']} ✅")
                    otp_window.destroy()
                    self.dashboard()
                else:
                    messagebox.showerror("Error", "Invalid OTP ❌")
            except ValueError:
                messagebox.showerror("Error", "Enter digits only!")

        self.styled_button(otp_window, "Submit", check_otp).pack(pady=10)

    def login(self, choice):
        self.clear_frame()

        if choice == 1:
            tk.Label(self.main_frame, text="Enter Phone Number", bg="#f2e9e4").pack(pady=5)
            phone_entry = tk.Entry(self.main_frame)
            phone_entry.pack()

            def submit_phone():
                ph = phone_entry.get().strip()
                if not ph.isdigit():
                    messagebox.showerror("Error", "Phone must be digits!")
                    return
                for user in self.users:
                    if user["phno"] == int(ph):
                        self.validate_otp(user)
                        return
                messagebox.showerror("Error", "Phone number not registered")

            self.styled_button(self.main_frame, "Submit", submit_phone).pack(pady=10)

        elif choice == 2:
            tk.Label(self.main_frame, text="Enter Email ID", bg="#f2e9e4").pack(pady=5)
            email_entry = tk.Entry(self.main_frame)
            email_entry.pack()

            def submit_email():
                email = email_entry.get().strip()
                for user in self.users:
                    if user["email"] == email:
                        self.validate_otp(user)
                        return
                messagebox.showerror("Error", "Email not registered")

            self.styled_button(self.main_frame, "Submit", submit_email).pack(pady=10)

        self.styled_button(self.main_frame, "Back", self.home_screen).pack(pady=10)

    def dashboard(self):
        self.clear_frame()
        tk.Label(self.main_frame, text=f"Welcome {self.current_user['name']}", font=("Arial", 16),
                 bg="#f2e9e4").pack(pady=20)
        self.styled_button(self.main_frame, "Order Food", self.order_screen).pack(pady=10)
        self.styled_button(self.main_frame, "Show Cart", self.show_cart).pack(pady=10)
        self.styled_button(self.main_frame, "Logout", self.logout).pack(pady=10)

    def order_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Choose Category", font=("Arial", 14),
                 bg="#f2e9e4").pack(pady=10)

        for cat in UnavagamApp.menu:
            self.styled_button(self.main_frame, cat.capitalize(), lambda c=cat: self.show_items(c)).pack(pady=5)

        self.styled_button(self.main_frame, "Back", self.dashboard).pack(pady=20)

    def show_items(self, category):
        self.clear_frame()
        tk.Label(self.main_frame, text=f"{category.capitalize()} Menu", font=("Arial", 14),
                 bg="#f2e9e4").pack(pady=10)

        for item, price in UnavagamApp.menu[category].items():
            self.styled_button(self.main_frame, f"{item} - Rs.{price}",
                               lambda i=item, p=price: self.add_to_cart(i, p)).pack(pady=5)

        self.styled_button(self.main_frame, "Back", self.order_screen).pack(pady=20)

    def add_to_cart(self, item, price):
        if item in self.cart:
            self.cart[item] += price
        else:
            self.cart[item] = price
        messagebox.showinfo("Cart", f"{item} added to cart!")

    def show_cart(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Your Cart", font=("Arial", 14), bg="#f2e9e4").pack(pady=10)

        if not self.cart:
            tk.Label(self.main_frame, text="Cart is empty", bg="#f2e9e4").pack()
        else:
            total = 0
            for item, price in self.cart.items():
                tk.Label(self.main_frame, text=f"{item} - Rs.{price}", bg="#f2e9e4").pack()
                total += price
            tk.Label(self.main_frame, text=f"Total: Rs.{total}", font=("Arial", 12, "bold"),
                     bg="#f2e9e4").pack(pady=10)

            self.styled_button(self.main_frame, "Place Order", self.place_order).pack(pady=5)

        self.styled_button(self.main_frame, "Back", self.dashboard).pack(pady=20)

    def place_order(self):
        messagebox.showinfo("Order Placed", f"Thank you {self.current_user['name']}! Your order will arrive soon.")
        self.cart.clear()
        self.dashboard()

    def logout(self):
        self.login_status = False
        self.current_user = None
        messagebox.showinfo("Logout", "You have been logged out.")
        self.home_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = UnavagamApp(root)
    root.mainloop()
