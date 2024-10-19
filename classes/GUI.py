import tkinter as tk
import threading
from classes.Game import Game
from urls.generals import *

class GUI:
    def __init__(self, game:Game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("FarmRPG Automate")

        #Defining GUI elements for Login
        # username entry
        self.username_entry = tk.Entry(self.window, width=40)
        self.username_entry.insert(0, "Username")
        self.username_entry.pack(pady=5)
        # password entry
        self.password_entry = tk.Entry(self.window, width=40)
        self.password_entry.insert(0, "Password")
        self.password_entry.pack(pady=5)
        # login button
        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        # Close button
        self.close_button = tk.Button(self.window, text="Close", command=self.close_game)
        self.close_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        url = LOGIN_URL
        threading.Thread(target=self.game.login, args=(url, username, password)).start()
    
    def close_game(self):
        threading.Thread(target=self.game.quit).start()

    def run(self):
        self.window.mainloop()