#First Page of the Project test repository
import pymysql
import tkinter as tk
import tkinter.messagebox
#import Classes_Screen as CS

#---------------------## ALL THE CLASSES ##---------------------#
class Home_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.left_frame = tk.Frame(main_window)
        self.right_frame = tk.Frame(main_window)

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))

        # Create buttons
        self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Lunch_LogIn_Page)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Lunch_Menu_Page)
        self.Buy_Now_Button = tk.Button(self.left_frame, text='Buy Now', command=Lunch_LogIn_Page)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.left_frame.pack(side=tk.LEFT, fill=tk.X)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Buy Now Button
        self.Buy_Now_Button.pack(ipadx=5, ipady=5, padx=200, pady=10)
        #Display the tex

class LogIn_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.SignIn_Title = tk.Label(self.middle_frame, text="Sign In", font=("Arial", 15))
        self.Email_Title = tk.Label(self.middle_frame, text="Email", font=("Arial", 10))
        self.Password_Title = tk.Label(self.middle_frame, text="Password", font=("Arial", 10))

        #Input

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Lunch_Menu_Page)
        self.Log_Button = tk.Button(self.middle_frame, text='Log In', command=Lunch_LogIn_Page)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        
        # Pack the 'Menu' button to the right
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.SignIn_Title.pack(ipadx=5, ipady=5, padx=200, pady=35)
        #Display the Email Title
        self.Email_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Password Title
        self.Password_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        # Pack the 'Log' button 
        self.Log_Button.pack(ipadx=5, ipady=5, padx=10, pady=10)

class Menu_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.Menu_Title = tk.Label(self.middle_frame, text="Menu", font=("Arial", 15))

        # Create buttons
        self.Home_Button = tk.Button(self.middle_frame, text='    Home     ', command=Lunch_Home_Page)
        self.My_Account = tk.Button(self.middle_frame, text='My Account', command=Lunch_LogIn_Page)
        self.Purchase = tk.Button(self.middle_frame, text='   Purchase   ', command=Lunch_LogIn_Page)
        self.CLose = tk.Button(self.middle_frame, text='      Close       ', command=Lunch_LogIn_Page)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.Menu_Title.pack(ipadx=5, ipady=5, padx=200, pady=35)
        #Display the Home Button
        self.Home_Button.pack(ipadx=15, ipady=7, padx=10, pady=10)
        #Display the My Account Button
        self.My_Account.pack(ipadx=15, ipady=7, padx=10, pady=10)
        #Display the Purchase Button
        self.Purchase.pack(ipadx=15, ipady=7, padx=10, pady=10)
        #Display the Close Button
        self.CLose.pack(ipadx=15, ipady=7, padx=10, pady=10)

#---------------------## ALL THE FUNCTIONS ##---------------------#

## Opennig Pages ##
def Lunch_LogIn_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    LogIn_Page(main_window)

def Lunch_Home_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Home_Page(main_window)

def Lunch_Menu_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Menu_Page(main_window)


main_window = tk.Tk()
main_window.title("Home Page")
main_window.geometry("900x500")
Home_Page(main_window)
tk.mainloop()