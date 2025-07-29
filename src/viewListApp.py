import tkinter as tk
from tkinter import messagebox
from passwordBank import HashMap

class viewPasswords:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel()
        self.window.title("View Passwords")
        self.window.geometry("300x200")

        #The loadList function should go here. Be sure to include an except
        #function if the file isn't found
        def loadList():

            listbox = tk.Listbox(root, height=15, width=50)
            listbox.pack(pady=10, padx=10)
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

        listButton = tk.Button(root, text="Show List", command=loadList)
        listButton.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = viewPasswords(root)
    app.root.mainloop()
