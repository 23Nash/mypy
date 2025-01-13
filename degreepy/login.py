import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, root):
        self.root = root    #root is defined
        self.root.title("Login Page")
        self.root.geometry("400x300")
        self.root.config(bg="#2c3e50")

        self.main_frame = tk.Frame(self.root, bg="#34495e", bd=2, relief=tk.RIDGE)  #setting the attributes of window
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.main_frame, text="Login", font=("Arial", 24, "bold"), fg="#ecf0f1", bg="#34495e")
        self.title_label.pack(pady=20)

        self.username_label = tk.Label(self.main_frame, text="Username:", font=("Arial", 14), fg="#ecf0f1", bg="#34495e")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame, font=("Arial", 14), width=30, bg="#ecf0f1", fg="#2c3e50")
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.main_frame, text="Password:", font=("Arial", 14), fg="#ecf0f1", bg="#34495e")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, font=("Arial", 14), width=30, show="*", bg="#ecf0f1", fg="#2c3e50")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.main_frame, text="Login", font=("Arial", 14, "bold"), bg="#1abc9c", fg="#ecf0f1", command=self.login)    #login function called on button press
        self.login_button.pack(pady=20)

        self.register_button = tk.Button(self.main_frame, text="Register", font=("Arial", 14, "bold"), bg="#3498db", fg="#ecf0f1", command=self.register)    #register function called on button press
        self.register_button.pack(pady=5)

    def login(self):    #define login function
        username = "admin"
        password = "password"
        if username and password:
            messagebox.showinfo("Login Success", "Welcome, " + username)
        else:
            messagebox.showerror("Login Error", "Please enter both username and password")

    def register(self): #define register function
        messagebox.showinfo("Register", "Register page will be opened soon")

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()