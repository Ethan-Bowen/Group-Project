import tkinter as tk
from tkinter import messagebox
from mainMenu import mainMenu
from user import User
import os
import cryption
import cryptography.fernet

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
        tk.Button(self.root, text="Login", command=self.login).grid(row=3, column=0, columnspan=2, pady=0)
        
    #Used for the create user button
    #Uses the create user fn in user to make a new folder, salt file, and encryption key
    def createUser(self):
        username = self.usernameEntry.get().strip() #Gets username from entry box
        password = self.passwordEntry.get().strip() #Gets password from entry box
        #if username or password is left blank
        if not username or not password:
            messagebox.showerror("Error", "Both fields are required!") #Error if fields are left blank
            return
        #If both fields are entered then It creates a new user
        else:
            User.createUser(username=username, password=password) #Creates user using the user fn and shows successful message box when finished
            messagebox.showinfo("Success", f"User '{username}' created successfully!")
            self.openMainWindow()

    #Used for the login button
    #Uses the decryption fn from cryption to login a user if they have the correct password
    def login(self):
        username = self.usernameEntry.get().strip() #Gets username from entry box
        password = self.passwordEntry.get().strip() #Gets password from entry box

        #if username or password is left blank
        if not username or not password:
            messagebox.showerror("Error", "Both fields are required!") #Error if fields are left blank
            return
        #checks if the user exists already
        elif not os.path.isdir(username):
            print()
            print(os.getcwd())
            messagebox.showerror("Error", "Invalid Username!") #Opens an error message box if the user exists already
            return
        #Decryption with correct password
        else:
            os.chdir(username)
            key = cryption.genarateKey(password, loadSalt=True) #Generates a key using the salt file and given password
            try: #Tries to decrypt the file using the generated key
                cryption.decrypt("passwords.txt", key)
            except cryptography.fernet.InvalidToken: #If the key doesn't match the saved key then it will return an error message box
                messagebox.showerror("Error", "Incorrect Password!")
                os.chdir("..")
                return()
            self.openMainWindow()
        
        # self.openMainWindow()

    # This closes the login window and opens the main window, which will be integrated more in the future
    def openMainWindow(self):
        self.root.destroy()
        mainMenu()

#Used to run the program
if __name__ == "__main__":
    root = tk.Tk()
    app = UserCreatorGUI(root)
    app.root.mainloop()
