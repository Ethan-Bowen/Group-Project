import tkinter as tk
from tkinter import messagebox
from tkinter import *
from passwordBank import HashMap

listbox = None


def viewPasswords():
    viewWindow = tk.Toplevel()
    viewWindow.title("View Passwords")
    viewWindow.geometry("500x300")

    # Widgets
    listbox = tk.Listbox(viewWindow)
    listbox.pack(pady=10, padx=10, expand=False)
    #This currently destroys the window as placeholder logic.
    button = tk.Button(viewWindow, text="Remove Password", command=viewWindow.destroy)
    button.pack(pady=10)

    # Displays the contents of the hash map on the list box
    hashMap = HashMap()
    try:
        hashMap.readSavedPasswords("passwords.txt")
    except FileNotFoundError:
        messagebox.showerror("Password File not Found", "Password File Missing!")
        return ()
    for key in hashMap.map:
        listbox.insert(tk.END, key + "    " + hashMap.getValue(key))
    return ()
