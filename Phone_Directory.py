import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import subprocess

DATA_FILE = "contacts.json"

contacts = {}       # {name: phone}
favourites = set()  # favourite contact names

# Load contacts
def load_contacts():
    global contacts, favourites
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            contacts = data.get("contacts", {})
            favourites = set(data.get("favourites", []))

# Save contacts
def save_contacts():
    with open(DATA_FILE, "w") as f:
        json.dump({"contacts": contacts, "favourites": list(favourites)}, f)

# Find contact by name or phone
def find_contact():
    name_query = entry_name.get().strip()
    phone_query = entry_phone.get().strip()
    for name, phone in contacts.items():
        if name_query and name_query == name:
            return name, phone
        if phone_query and phone_query == phone:
            return name, phone
    return None, None

# Add contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone cannot be empty!")
        return
    contacts[name] = phone
    save_contacts()
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    update_contact_list()

# Edit contact
def edit_contact():
    old_name, old_phone = find_contact()
    if old_name:
        new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=old_name)
        if not new_name:
            new_name = old_name
        new_phone = simpledialog.askstring("Edit Phone", "Enter new phone:", initialvalue=old_phone)
        if not new_phone:
            new_phone = old_phone
        if new_name != old_name:
            del contacts[old_name]
            if old_name in favourites:
                favourites.remove(old_name)
                favourites.add(new_name)
        contacts[new_name] = new_phone
        save_contacts()
        messagebox.showinfo("Success", f"Contact updated to:\nName: {new_name}\nPhone: {new_phone}")
        update_contact_list()
    else:
        messagebox.showerror("Not Found", "Contact not found!")

# Search contact
def search_contact():
    name, phone = find_contact()
    if name:
        fav_status = " (Favourite)" if name in favourites else ""
        messagebox.showinfo("Contact Found", f"Name: {name}{fav_status}\nPhone: {phone}")
    else:
        messagebox.showerror("Not Found", "Contact not found!")

# Delete contact
def delete_contact():
    name, _ = find_contact()
    if name:
        del contacts[name]
        favourites.discard(name)
        save_contacts()
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted successfully!")
        update_contact_list()
    else:
        messagebox.showerror("Not Found", "Contact not found!")

# Toggle favourite
def toggle_favourite():
    name, _ = find_contact()
    if name:
        if name in favourites:
            favourites.remove(name)
            messagebox.showinfo("Favourite Removed", f"Contact '{name}' removed from favourites.")
        else:
            favourites.add(name)
            messagebox.showinfo("Favourite Added", f"Contact '{name}' marked as favourite.")
        save_contacts()
        update_contact_list()
    else:
        messagebox.showerror("Not Found", "Contact not found!")

# Share contact to Notepad
def share_contact():
    name, phone = find_contact()
    if name:
        file_name = f"{name}_contact.txt"
        with open(file_name, "w") as f:
            f.write(f"Name: {name}\nPhone: {phone}\n")
        if os.name == "nt":
            subprocess.Popen(["notepad.exe", file_name])
        else:
            subprocess.Popen(["open", file_name])
    else:
        messagebox.showerror("Not Found", "Contact not found!")

# Update listbox
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name, phone in contacts.items():
        fav = "★" if name in favourites else ""
        listbox_contacts.insert(tk.END, f"{fav} {name} : {phone}")

# On listbox select
def on_contact_select(event):
    selection = listbox_contacts.curselection()
    if selection:
        index = selection[0]
        value = listbox_contacts.get(index)
        # Remove ★ if exists
        if value.startswith("★ "):
            value = value[2:]
        # Split name and phone
        if " : " in value:
            name, phone = value.split(" : ")
            entry_name.delete(0, tk.END)
            entry_name.insert(0, name)
            entry_phone.delete(0, tk.END)
            entry_phone.insert(0, phone)

# Load contacts on startup
load_contacts()

# GUI
root = tk.Tk()
root.title("Phone Directory")
root.geometry("550x550")
root.configure(bg="#f0f4f8")  # Light pastel background

# Search area
frame_search = tk.Frame(root, bg="#f0f4f8")
frame_search.pack(pady=10)

tk.Label(frame_search, text="Name", bg="#f0f4f8", fg="#333", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_search, width=30, bg="#e6f0ff")
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_search, text="Phone", bg="#f0f4f8", fg="#333", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_search, width=30, bg="#e6f0ff")
entry_phone.grid(row=1, column=1, padx=5, pady=5)

# Buttons
frame_buttons = tk.Frame(root, bg="#69d881")
frame_buttons.pack(pady=10)

btn_style = {"width": 20, "bg": "#4da6ff", "fg": "white", "font": ("Arial", 10, "bold")}

tk.Button(frame_buttons, text="Add Contact", command=add_contact, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Edit Contact", command=edit_contact, **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Search Contact", command=search_contact, **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Delete Contact", command=delete_contact, **btn_style).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Toggle Favourite", command=toggle_favourite, **btn_style).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Share Contact (Notepad)", command=share_contact, **btn_style).grid(row=2, column=1, padx=5, pady=5)

# Listbox
listbox_contacts = tk.Listbox(root, width=65, height=15, bg="#62acd3", fg="#000", font=("Arial", 10))
listbox_contacts.pack(pady=10)
listbox_contacts.bind("<<ListboxSelect>>", on_contact_select)

update_contact_list()
root.mainloop()
