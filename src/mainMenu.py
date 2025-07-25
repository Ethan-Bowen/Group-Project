import tkinter as tk
from tkinter import messagebox
from addPassword import passwordWindow

#This creates the main application window
def mainMenu():
    mainRoot=tk.Tk()

    def placeholder_function():
        """A placeholder function for menu options."""
        messagebox.showinfo("Info", "This feature is not implemented yet!")

    def openPassWindow():
        newWindow1 = passwordWindow()

    def exit_application():
        """Exit the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            mainRoot.destroy()



    #This creates a label for the main menu
    label = tk.Label(mainRoot, text="Main Menu", font=("Arial", 16))
    label.pack(pady=20)

    #This creates a frame to hold the buttons
    button_frame = tk.Frame(mainRoot)
    button_frame.pack(pady=10)

    #This adds buttons for different functions
    btn_function2 = tk.Button(button_frame, text="Add Password", width=20, command=openPassWindow)
    btn_function2.pack(pady=5)

    btn_function2 = tk.Button(button_frame, text="Password Manager", width=20, command=placeholder_function)
    btn_function2.pack(pady=5)

    #This adds an Exit button
    btn_exit = tk.Button(button_frame, text="Exit", width=20, command=exit_application)
    btn_exit.pack(pady=5)

    #This runs the application
    mainRoot.mainloop()
