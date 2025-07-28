import tkinter as tk
from tkinter import messagebox
from passwordBank import HashMap

class viewPasswords:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("View Passwords")
        self.window.geometry("300x200")

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
        for key in hashMap.map:
            listbox.insert(counter, key, hashMap.getValue(key))
            counter += 1

        # This is the Listbox widget
        listbox = tk.Listbox(root, height=15, width=50)
        listbox.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = viewPasswords(root)
    app.root.mainloop()
