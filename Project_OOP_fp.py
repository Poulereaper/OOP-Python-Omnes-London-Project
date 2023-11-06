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
        self.Buy_Now_Button = tk.Button(self.left_frame, text='Buy Now', command=Lunch_Purchase_Page)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.left_frame.pack(side=tk.LEFT, fill=tk.X)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Buy Now Button
        self.Buy_Now_Button.pack(ipadx=5, ipady=5, padx=200, pady=10)
        #Display the text

class LogIn_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        self.bottom_frame = tk.Frame(main_window)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.SignIn_Title = tk.Label(self.middle_frame, text="Sign In", font=("Arial", 15))
        self.Email_Title = tk.Label(self.middle_frame, text="Email", font=("Arial", 10))
        self.Password_Title = tk.Label(self.middle_frame, text="Password", font=("Arial", 10))
        self.NewAccount_Title = tk.Label(self.bottom_frame, text="Don't have an account?", font=("Arial", 10))

        #Input
        self.Email_Input = tk.Entry(self.middle_frame)
        self.Password_Input = tk.Entry(self.middle_frame)

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Lunch_Menu_Page)
        self.Log_Button = tk.Button(self.middle_frame, text='Log In', command=Lunch_LogIn_Page)
        self.NewAccount_Button = tk.Button(self.bottom_frame, text='Sign Up', command=Lunch_SignUp_Page)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)               
        
        # Pack the 'Menu' button to the right
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.SignIn_Title.pack(ipadx=5, ipady=5, padx=200, pady=35)
        #Display the Email Title
        self.Email_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Email Input
        self.Email_Input.pack(ipadx=20, ipady=0, padx=10, pady=10)
        #Display the Password Title
        self.Password_Title.pack(ipadx=5, ipady=0, padx=10, pady=10)
        #Display the Password Input
        self.Password_Input.pack(ipadx=20, ipady=5, padx=10, pady=10)
        # Pack the 'Log' button 
        self.Log_Button.pack(ipadx=20, ipady=5, padx=10, pady=35)
        #Display the New Account Title
        self.NewAccount_Title.grid(row=0, column=1, padx=10, pady=20, ipadx=5, ipady=5)
        # Pack the 'New Account' button
        self.NewAccount_Button.grid(row=0, column=2, padx=10, pady=20, ipadx=20, ipady=5)
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.columnconfigure(2, weight=1)
        self.bottom_frame.columnconfigure(3, weight=1)


class SignUp_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        self.second_top_frame = tk.Frame(main_window)
        self.third_top_frame = tk.Frame(main_window)
        self.third_top_frame.columnconfigure(0, weight=1)
        self.third_top_frame.columnconfigure(1, weight=1)
        self.third_top_frame.columnconfigure(2, weight=1)
        self.third_top_frame.columnconfigure(3, weight=1)
        self.third_top_frame.columnconfigure(4, weight=1)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.SignUp_Title = tk.Label(self.second_top_frame, text="Sign Up", font=("Arial", 15))
        self.FirstName_Title = tk.Label(self.third_top_frame, text="First Name", font=("Arial", 10))
        self.LastName_Title = tk.Label(self.third_top_frame, text="Last Name", font=("Arial", 10))
        self.UserName_Title = tk.Label(self.third_top_frame, text="User Name", font=("Arial", 10))
        self.Email_Title = tk.Label(self.middle_frame, text="Email", font=("Arial", 10))
        self.Phone_Title = tk.Label(self.middle_frame, text="Phone", font=("Arial", 10))
        self.Password_Title = tk.Label(self.middle_frame, text="Password", font=("Arial", 10))

        #Input
        self.FirstName_Input = tk.Entry(self.third_top_frame)
        self.LastName_Input = tk.Entry(self.third_top_frame)
        self.UserName_Input = tk.Entry(self.third_top_frame)
        self.Email_Input = tk.Entry(self.middle_frame)
        self.Phone_Input = tk.Entry(self.middle_frame)
        self.Password_Input = tk.Entry(self.middle_frame)

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Lunch_Menu_Page)
        self.SignUp_Button = tk.Button(self.middle_frame, text='Sign Up', command=Lunch_Home_Page)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.third_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)              
        
        # Pack the 'Menu' button to the right
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.SignUp_Title.pack(ipadx=5, ipady=5, padx=200, pady=35)
        #Display the First Name Title
        self.FirstName_Title.grid(row=0, column=1, padx=10, pady=0, ipadx=5, ipady=0)
        #Display the First Name Input
        self.FirstName_Input.grid(row=1, column=1, padx=10, pady=0, ipadx=5, ipady=5)
        #Display the Last Name Title
        self.LastName_Title.grid(row=0, column=2, padx=10, pady=20, ipadx=5, ipady=0)
        #Display the Last Name Input
        self.LastName_Input.grid(row=0, column=2, padx=10, pady=20, ipadx=5, ipady=5)
        #Display the User Name Title
        self.UserName_Title.grid(row=0, column=3, padx=10, pady=20, ipadx=5, ipady=0)
        #Display the User Name Input
        self.UserName_Input.grid(row=0, column=3, padx=10, pady=20, ipadx=5, ipady=5)
        #Display the Email Title
        self.Email_Title.pack(ipadx=5, ipady=0, padx=10, pady=0)
        #Display the Email Input
        self.Email_Input.pack(ipadx=20, ipady=5, padx=10, pady=10)
        #Display the Phone Title
        self.Phone_Title.pack(ipadx=5, ipady=0, padx=10, pady=10)
        #Display the Phone Input
        self.Phone_Input.pack(ipadx=20, ipady=5, padx=10, pady=10)
        #Display the Password Title
        self.Password_Title.pack(ipadx=5, ipady=0, padx=10, pady=10)
        #Display the Password Input
        self.Password_Input.pack(ipadx=20, ipady=5, padx=10, pady=10)
        # Pack the 'Log' button 
        self.SignUp_Button.pack(ipadx=20, ipady=5, padx=10, pady=35)
        #Display the New Account Title

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

class Purchase_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.second_top_frame = tk.Frame(main_window)

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))

        # Create buttons
        self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Lunch_LogIn_Page)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Lunch_Menu_Page)
        self.Search_Button = tk.Button(self.second_top_frame, text='Search', command=Lunch_LogIn_Page)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Buy Now Button
        self.Search_Button.pack(ipadx=5, ipady=5, padx=200, pady=10)
        #Display the text

#---------------------## ALL THE FUNCTIONS ##---------------------#

## Opennig Pages ##

def Lunch_Home_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Home_Page(main_window)

def Lunch_LogIn_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    LogIn_Page(main_window)

def Lunch_SignUp_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    SignUp_Page(main_window)

def Lunch_Menu_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Menu_Page(main_window)

def Lunch_Purchase_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Purchase_Page(main_window)


main_window = tk.Tk()
main_window.title("OOP Air Line")
main_window.geometry("1100x600")
Home_Page(main_window)
tk.mainloop()
