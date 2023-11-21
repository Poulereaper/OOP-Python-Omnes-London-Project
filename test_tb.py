import tkinter as tk
import ttkbootstrap as tb
from PIL import Image, ImageTk

class Home_Page():
    def __init__(self, main_window):
        self.top_frame = tb.LabelFrame(main_window)
        self.second_top_frame = tb.LabelFrame(main_window)

        #Title
        self.title = tb.Label(self.top_frame, text="Welcome to our store!", bg="#ffffff", font=("Arial", 20))
        self.Hello = tb.Label(self.second_top_frametop_frame, text="Hello, ", bg="#ffffff", font=("Arial", 20))

        #Buttons
        self.Login = tb.Button(self.top_frame, text="Login", bg="#ffffff", font=("Arial", 20))
        self.Menu = tb.Button(self.top_frame, text="Menu", bg="#ffffff", font=("Arial", 20))

        #Display
        self.top_frame.pack(fill="both", expand=True)
        self.second_top_frame.pack(fill="both", expand=True)
        self.title.pack(pady=10)
        self.Login.pack(pady=10, side="left")
        self.Menu.pack(pady=10, side="right")
        self.Hello.pack(pady=10)


# Create the main window
main_window = tb.Window()
main_window.title("Home Page")
main_window.geometry("800x600")
main_window.resizable(False, False)
main_window.configure(bg="#ffffff")
mybutton = tb.Button(main_window, text="Click Me!")
mybutton.pack(pady=10)
#Home_Page(main_window)
main_window.mainloop()