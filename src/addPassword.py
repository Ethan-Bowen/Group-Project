import tkinter as tk
from tkinter import messagebox
from passwordBank import HashMap
import os

class passwordWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Add Password")
        self.window.geometry("300x200")

        # Label and Entry for user input
        tk.Label(self.window, text="Enter the website or use case:").pack(pady=5)
        self.websiteEntry = tk.Entry(self.window)
        self.websiteEntry.pack(pady=5)

        tk.Label(self.window, text="Enter the new password:").pack(pady=5)
        self.passwordEntry = tk.Entry(self.window)
        self.passwordEntry.pack(pady=5)

        # Submit button
        submit_button = tk.Button(self.window, text="Submit", command=self.submit)
        submit_button.pack(pady=20)

    def submit(self):
        website = self.websiteEntry.get()
        password = self.passwordEntry.get()

        if not website or not password:
            messagebox.showwarning("Error", "Both fields are required!")

        # This simulates saving the inputs (like in the Login code, replace this and the saveInfo definition with the save to file logic
        # when it gets done)
        
        hashMap = HashMap()
        hashMap.readSavedPasswords("passwords.txt")
        hashMap.setValue(website, password)
        hashMap.savePasswords("passwords.txt")
        messagebox.showinfo("Success", f"New website and Password saved")


    # def saveInfo(self, website, password):
    #     # This is a placeholder for the saving logic
    #     print(f"Saving use case: {website}, Password: {password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = passwordWindow(root)
    app.root.mainloop()
