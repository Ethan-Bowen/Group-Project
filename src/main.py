from passwordBank import HashMap
from user import User
import os
import cryption
from login import UserCreatorGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = UserCreatorGUI(root)
    app.root.mainloop()