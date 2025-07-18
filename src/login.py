import tkinter as tk
from tkinter import messagebox
from mainMenu import mainMenu

class UserCreatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("User login")
        self.root.geometry("300x200")

        #The labels and Entry fields
        tk.Label(self.root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.usernameEntry = tk.Entry(self.root)
        self.usernameEntry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.passwordEntry = tk.Entry(self.root, show="*")
        self.passwordEntry.grid(row=1, column=1, padx=10, pady=10)

        #The buttons
        tk.Button(self.root, text="Create User", command=self.createUser).grid(row=2, column=0, columnspan=2,
                                                                                  pady=20)
    #The logic for the main function here
    def createUser(self):
        username = self.usernameEntry.get().strip()
        password = self.passwordEntry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return

        #This simulates saving the user (replace this and the saveUser definition with the save to file logic
        #when it gets done)
        self.saveUser(username, password)
        messagebox.showinfo("Success", f"User '{username}' created successfully!")
        self.openMainWindow()

    def saveUser(self, username, password):
        #This is a placeholder for the saving user logic
        print(f"Saving user: {username}, Password: {password}")

    # This closes the login window and opens the main window, which will be integrated more in the future
    def openMainWindow(self):
        self.root.destroy()
        mainMenu()


if __name__ == "__main__":
    root = tk.Tk()
    app = UserCreatorGUI(root)
    app.root.mainloop()
