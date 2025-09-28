from tkinter import *
from tkinter import ttk

# Fixed conversion rates (base: 1 USD)
rates = {
    'USD': 1.0,
    'INR': 83.0,
    'EUR': 0.93,
    'GBP': 0.79,
    'JPY': 149.0,
    'AUD': 55.06,
    'CAD': 61.02,
    'SGD': 61.67,
    'CNY': 11.56,
}

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()

        # Convert via USD
        amount_in_usd = amount / rates[from_currency]
        converted = amount_in_usd * rates[to_currency]

        label_result.config(text=f"{amount} {from_currency} = {round(converted, 2)} {to_currency}")
    except:
        label_result.config(text="⚠ Error! Check input.")

def clear_fields():
    entry_amount.delete(0, END)
    combo_from.set('')
    combo_to.set('')
    label_result.config(text="")

# Tkinter Window
root = Tk()
root.title("Simple Currency Converter")
root.geometry("420x300")
root.config(bg="#528dc1")

currency_list = list(rates.keys())

# Heading
Label(root, text="💱 Welcome to Currency Converter", font=("Times New Roman", 16, "bold"), bg="#f0f8ff", fg="darkblue").pack(pady=10)

# Amount input
frame1 = Frame(root, bg="#f0f8ff")
frame1.pack(pady=5)
Label(frame1, text="Enter Amount:", font=("Copperplate Gothic Bold", 12), bg="#f0f8ff").grid(row=0, column=0, padx=5)
entry_amount = Entry(frame1, font=("Copperplate Gothic Bold", 12))
entry_amount.grid(row=0, column=1)

# From currency
frame2 = Frame(root, bg="#f0f8ff")
frame2.pack(pady=5)
Label(frame2, text="From Currency:", font=("Copperplate Gothic Bold", 12), bg="#f0f8ff").grid(row=0, column=0, padx=5)
combo_from = ttk.Combobox(frame2, values=currency_list, font=("Copperplate Gothic Bold", 12), state="readonly")
combo_from.grid(row=0, column=1)

# To currency
frame3 = Frame(root, bg="#f0f8ff")
frame3.pack(pady=5)
Label(frame3, text="To Currency:", font=("Copperplate Gothic Bold", 12), bg="#f0f8ff").grid(row=0, column=0, padx=5)
combo_to = ttk.Combobox(frame3, values=currency_list, font=("Copperplate Gothic Bold", 12), state="readonly")
combo_to.grid(row=0, column=1)

# Buttons
frame4 = Frame(root, bg="#f0f8ff")
frame4.pack(pady=10)
Button(frame4, text="Convert", font=("Times New Roman", 12, "bold"), bg="green", fg="white", command=convert_currency).grid(row=0, column=0, padx=10)
Button(frame4, text="Clear", font=("Times New Roman", 12, "bold"), bg="red", fg="white", command=clear_fields).grid(row=0, column=1, padx=10)

# Result label
label_result = Label(root, text="", font=("Arial", 14, "bold"), bg="#759dc0", fg="red")
label_result.pack(pady=15)

root.mainloop()
