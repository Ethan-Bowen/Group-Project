import tkinter as tk
from tkinter import messagebox
from passwordBank import HashMap

def viewPasswords():
    viewWindow = tk.Toplevel()
    viewWindow.title("View Passwords")
    viewWindow.geometry("300x200")

    listbox = tk.Listbox(viewWindow)
    listbox.pack(pady=10, padx=10)
        #The loadList function should go here. Be sure to include an except
        #function if the file isn't found
    def loadList():


        hashMap = HashMap()
        try:
            hashMap.readSavedPasswords("passwords.txt")
        except FileNotFoundError:
            messagebox.showerror("Password File not Found", "Password File Missing!")
            return()
        counter = 1
        for key in hashMap.map():
            listbox.insert(tk.END, counter, key, hashMap.getValue(key))
            counter += 1
            return()

    loadList()
