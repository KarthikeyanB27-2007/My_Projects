import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Data Models
# -----------------------------
class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        return f"ID={self.pid}, Name={self.name}, Age={self.age}, Disease={self.disease}"

class Doctor:
    def __init__(self, did, name, specialization):
        self.did = did
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"ID={self.did}, Name={self.name}, Specialization={self.specialization}"


# -----------------------------
# Searching Functions
# -----------------------------
def linear_search_patient(name):
    for p in patients:
        if p.name.lower() == name.lower():
            return p
    return None

def binary_search_patient(pid):
    patients.sort(key=lambda x: x.pid)
    low, high = 0, len(patients) - 1
    while low <= high:
        mid = (low + high) // 2
        if patients[mid].pid == pid:
            return patients[mid]
        elif patients[mid].pid < pid:
            low = mid + 1
        else:
            high = mid - 1
    return None


# -----------------------------
# GUI Functions
# -----------------------------
def add_patient():
    try:
        pid = int(entry_pid.get())
        name = entry_pname.get()
        age = int(entry_page.get())
        disease = entry_pdisease.get()

        patients.append(Patient(pid, name, age, disease))
        messagebox.showinfo("Success", "Patient added successfully!")
    except:
        messagebox.showerror("Error", "Invalid patient input!")

def add_doctor():
    try:
        did = int(entry_did.get())
        name = entry_dname.get()
        specialization = entry_dspecial.get()

        doctors[did] = Doctor(did, name, specialization)
        messagebox.showinfo("Success", "Doctor added successfully!")
    except:
        messagebox.showerror("Error", "Invalid doctor input!")

def show_patients():
    output.delete(1.0, tk.END)
    if not patients:
        output.insert(tk.END, "No patients found.\n")
    for p in patients:
        output.insert(tk.END, str(p) + "\n")

def show_doctors():
    output.delete(1.0, tk.END)
    if not doctors:
        output.insert(tk.END, "No doctors found.\n")
    for d in doctors.values():
        output.insert(tk.END, str(d) + "\n")

def search_by_name():
    name = entry_search_name.get()
    result = linear_search_patient(name)
    output.delete(1.0, tk.END)
    if result:
        output.insert(tk.END, "Found (Linear Search):\n" + str(result))
    else:
        output.insert(tk.END, "Patient not found.")

def search_by_id():
    try:
        pid = int(entry_search_id.get())
        result = binary_search_patient(pid)
        output.delete(1.0, tk.END)
        if result:
            output.insert(tk.END, "Found (Binary Search):\n" + str(result))
        else:
            output.insert(tk.END, "Patient not found.")
    except:
        messagebox.showerror("Error", "Enter valid Patient ID!")

def search_doctor_by_id():
    try:
        did = int(entry_search_did.get())
        result = doctors.get(did)
        output.delete(1.0, tk.END)
        if result:
            output.insert(tk.END, "Found Doctor:\n" + str(result))
        else:
            output.insert(tk.END, "Doctor not found.")
    except:
        messagebox.showerror("Error", "Enter valid Doctor ID!")


# -----------------------------
# Data
# -----------------------------
patients = []
doctors = {}  # dynamic now


# -----------------------------
# Tkinter GUI
# -----------------------------
root = tk.Tk()
root.title("Hospital Management System - Searching")
root.geometry("650x600")

# --- Patient Entry ---
tk.Label(root, text="Add Patient", font=("Arial", 14, "bold")).pack()
frame_add = tk.Frame(root)
frame_add.pack(pady=5)

tk.Label(frame_add, text="ID").grid(row=0, column=0)
entry_pid = tk.Entry(frame_add)
entry_pid.grid(row=0, column=1)

tk.Label(frame_add, text="Name").grid(row=1, column=0)
entry_pname = tk.Entry(frame_add)
entry_pname.grid(row=1, column=1)

tk.Label(frame_add, text="Age").grid(row=2, column=0)
entry_page = tk.Entry(frame_add)
entry_page.grid(row=2, column=1)

tk.Label(frame_add, text="Disease").grid(row=3, column=0)
entry_pdisease = tk.Entry(frame_add)
entry_pdisease.grid(row=3, column=1)

tk.Button(frame_add, text="Add Patient", command=add_patient).grid(row=4, columnspan=2, pady=5)
tk.Button(frame_add, text="Show Patients", command=show_patients).grid(row=5, columnspan=2, pady=5)

# --- Doctor Entry ---
tk.Label(root, text="Add Doctor", font=("Arial", 14, "bold")).pack()
frame_doc = tk.Frame(root)
frame_doc.pack(pady=5)

tk.Label(frame_doc, text="Doctor ID").grid(row=0, column=0)
entry_did = tk.Entry(frame_doc)
entry_did.grid(row=0, column=1)

tk.Label(frame_doc, text="Name").grid(row=1, column=0)
entry_dname = tk.Entry(frame_doc)
entry_dname.grid(row=1, column=1)

tk.Label(frame_doc, text="Specialization").grid(row=2, column=0)
entry_dspecial = tk.Entry(frame_doc)
entry_dspecial.grid(row=2, column=1)

tk.Button(frame_doc, text="Add Doctor", command=add_doctor).grid(row=3, columnspan=2, pady=5)
tk.Button(frame_doc, text="Show Doctors", command=show_doctors).grid(row=4, columnspan=2, pady=5)

# --- Search ---
tk.Label(root, text="Search", font=("Arial", 14, "bold")).pack()
frame_search = tk.Frame(root)
frame_search.pack(pady=5)

tk.Label(frame_search, text="By Patient Name").grid(row=0, column=0)
entry_search_name = tk.Entry(frame_search)
entry_search_name.grid(row=0, column=1)
tk.Button(frame_search, text="Search", command=search_by_name).grid(row=0, column=2)

tk.Label(frame_search, text="By Patient ID").grid(row=1, column=0)
entry_search_id = tk.Entry(frame_search)
entry_search_id.grid(row=1, column=1)
tk.Button(frame_search, text="Search", command=search_by_id).grid(row=1, column=2)

tk.Label(frame_search, text="By Doctor ID").grid(row=2, column=0)
entry_search_did = tk.Entry(frame_search)
entry_search_did.grid(row=2, column=1)
tk.Button(frame_search, text="Search", command=search_doctor_by_id).grid(row=2, column=2)

# --- Output ---
output = tk.Text(root, height=12, width=75)
output.pack(pady=10)

root.mainloop()
