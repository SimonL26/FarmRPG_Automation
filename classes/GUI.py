import tkinter as tk
from tkinter import ttk 
import threading
from classes.Game import Game
from urls.generals import *
from datetime import datetime
import sys

class GUI:
    def __init__(self, game:Game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("FarmRPG Automate")

        #Defining GUI elements for Login
        #username label 
        username_label = tk.Label(self.window, text="Username")
        username_label.pack(pady=3)
        # username entry
        self.username_entry = tk.Entry(self.window, width=40)
        self.username_entry.insert(0, "")
        self.username_entry.pack(pady=5)
        # password label
        password_label = tk.Label(self.window, text="Password")
        password_label.pack(pady=5)
        # password entry
        self.password_entry = tk.Entry(self.window, width=40)
        self.password_entry.insert(0, "")
        self.password_entry.pack(pady=5)
        # login button
        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        url = LOGIN_URL
        threading.Thread(target=self.process_login, args=(url, username, password)).start()
    
    def process_login(self, url:str, username:str, password:str): 
        self.game.login(url, username, password)

        #close login window and open a new window for game operation
        self.window.withdraw()
        #Open a new window for activities
        self.open_game_window()

    def open_game_window(self):
        game_window = tk.Toplevel(self.window)
        game_window.title("FarmRPG Automate")

        # Catch close event for the game window as well
        game_window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # label for explore
        explore_label = tk.Label(game_window, text="Choose a location to explore")
        explore_label.pack(pady=3)

        # dropdown for choosing a location
        locations = list(EXPLORE_AREAS.keys())
        self.explore_location = ttk.Combobox(game_window, values=locations)
        self.explore_location.current(0)
        self.explore_location.pack(pady=5)   

        # Number of times that needs to be clicked
        click_time_label = tk.Label(game_window, text="How many times to click")
        click_time_label.pack(pady=3)

        # Input for click time
        self.click_time_input = tk.Entry(game_window, width=40)
        self.click_time_input.insert(0, "1")
        self.click_time_input.pack(pady=5)

        #Explore button
        explore_button = tk.Button(game_window, text="Explore", command=self.start_explore)
        explore_button.pack(pady=5)

        # Close button
        close_button = tk.Button(game_window, text="Close", command=self.on_closing)
        close_button.pack(pady=5)

    def start_explore(self):
        selected_location = EXPLORE_AREAS[self.explore_location.get()]
        location_url = EXPLORE_URL + selected_location
        click_times = int(self.click_time_input.get())
        threading.Thread(target=self.game.explore, args=(location_url, click_times)).start()

    def on_closing(self):
        try:
            threading.Thread(target=self.game.quit).start()
        except Exception as e:
            print(f"[{datetime.now()}]: Exception occurred while closing: {e}")
        finally:
            self.window.quit()
            self.window.destroy()
            print(f"[{datetime.now()}]: Exiting...")
            sys.exit()



    def run(self):
        self.window.mainloop()