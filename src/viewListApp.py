import tkinter as tk
from tkinter import messagebox
from tkinter import *
from passwordBank import HashMap
from passwordBank import HashMap


class viewPasswords:
    def __init__(self):
        self.viewWindow = tk.Toplevel()
        self.viewWindow.title("View Passwords")
        self.viewWindow.geometry("500x300")

        #Listbox
        self.listbox = tk.Listbox(self.viewWindow)
        self.listbox.pack(pady=10, padx=10, expand=False)
        #Button
        button = tk.Button(self.viewWindow, text="Remove Password", command=self.remove)
        button.pack(pady=10)

        # Displays the contents of the hash map on the list box
        hashMap = HashMap()
        try:
            hashMap.readSavedPasswords("passwords.txt")
        except FileNotFoundError:
            messagebox.showerror("Password File not Found", "Password File Missing!")
            return()
        for key in hashMap.map:
            self.listbox.insert(tk.END, key + "    " + hashMap.getValue(key))
        return()

    #Used for the remove button
    #Removes the saved password in the listbox, the hash map, and the passwords file
    def remove(self):
        try:
            passwordNum = self.listbox.curselection()
        except tk.TclError:
            messagebox.showerror("Error", "A Password Must be Selected!")
        password = self.listbox.get(passwordNum)
        split = password.split()
        hashMap = HashMap()
        hashMap.readSavedPasswords("passwords.txt")
        hashMap.removeValue(split[0])
        hashMap.savePasswords("passwords.txt")
        self.listbox.delete(passwordNum)
        return()