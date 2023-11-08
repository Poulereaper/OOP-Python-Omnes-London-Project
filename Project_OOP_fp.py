#First Page of the Project test repository
import pymysql
import tkinter as tk
import tkinter.messagebox
from tkcalendar import DateEntry
import dbconnect
import Actual_Customer as AC
import re
from PIL import Image, ImageTk
import datetime
#import Classes_Screen as CS

#---------------------## ALL THE CLASSES ##---------------------#

class Home_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.left_frame = tk.Frame(main_window)
        self.right_frame = tk.Frame(main_window, bg='#14539a')

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.Pres_OOPAirLine = tk.Label(self.right_frame, text="Welcome to OOP Air Line", font=("Arial", 15), bg='#14539a')

        # Create 
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg='#0d3562')
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg='#0d3562')
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg='#0d3562')
        self.Buy_Now_Button = tk.Button(self.left_frame, text='Buy Now', command=Launch_Purchase_Page, font=("Arial", 17), bg='#14539a')
        self.Buy_Now_Button.config(height=1, width=10)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg='black')
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill='black')
        self.left_frame.pack(side=tk.LEFT, fill=tk.X)
        #self.right_frame.pack(side=tk.RIGHT, fill=tk.X)
        self.right_frame.place(x=535, y=220, relwidth=0.35, relheight=0.45)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Buy Now Button
        self.Buy_Now_Button.pack(ipadx=5, ipady=5, padx=200, pady=10)
        #Display the text
        self.Pres_OOPAirLine.pack(ipadx=5, ipady=5, padx=20, pady=10)

class LogIn_Page():
    def __init__(self, main_window):
        self.db=dbconnect.DBHelper()
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        self.bottom_frame = tk.Frame(main_window)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.SignIn_Title = tk.Label(self.middle_frame, text="Sign In", font=("Arial", 15))
        self.Email_Title = tk.Label(self.middle_frame, text="Email", font=("Arial", 10))
        self.Password_Title = tk.Label(self.middle_frame, text="Password", font=("Arial", 10))
        self.Space_Title1 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10))
        self.NewAccount_Title = tk.Label(self.bottom_frame, text="Don't have an account?", font=("Arial", 10))

        #Input
        self.Email_Input = tk.Entry(self.middle_frame)
        self.Password_Input = tk.Entry(self.middle_frame)
        self.Password_Input.config(show="*")

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page)
        self.Log_Button = tk.Button(self.middle_frame, text='Log In', command=self.Log_check)
        self.NewAccount_Button = tk.Button(self.bottom_frame, text='Sign Up', command=Launch_SignUp_First_Page)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg='black')
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill='black')
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)               
        
        # Pack the 'Menu' button to the right
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.SignIn_Title.pack(ipadx=5, ipady=5, padx=200, pady=35)
        #Display the Email Title
        self.Email_Title.pack(ipadx=5, ipady=5, padx=10, pady=3)
        #Display the Email Input
        self.Email_Input.pack(ipadx=20, ipady=5, padx=10, pady=3)
        self.Space_Title1.pack(ipadx=5, ipady=0, padx=10, pady=15)
        #Display the Password Title
        self.Password_Title.pack(ipadx=5, ipady=0, padx=10, pady=3)
        #Display the Password Input
        self.Password_Input.pack(ipadx=20, ipady=5, padx=10, pady=3)
        # Pack the 'Log' button 
        self.Log_Button.pack(ipadx=20, ipady=5, padx=10, pady=40)
        #Display the New Account Title
        self.NewAccount_Title.grid(row=0, column=1, padx=10, pady=20, ipadx=5, ipady=5)
        # Pack the 'New Account' button
        self.NewAccount_Button.grid(row=0, column=2, padx=10, pady=20, ipadx=20, ipady=5)
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.columnconfigure(2, weight=1)
        self.bottom_frame.columnconfigure(3, weight=1)

    
    def Log_check(self):
        #get the input
        self.Email=self.Email_Input.get()
        self.Password=self.Password_Input.get()
        # Check if the email is a valid email address using a regular expression
        if not re.match(r'^[\w\.-]+@[\w\.-]+$', self.Email):
            # Invalid email format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid email format')
        else :
            query = "SELECT * FROM customer WHERE Email = '{}' AND Password = '{}'".format(self.Email, self.Password) 
            result=self.db.fetch(query)
            if result:
                # Copy the result to the Actual_Customer
                Actual_Customer.Copy_To_Actual_Customer(result)
                # Login successful, show the home page
                Launch_Home_Page()
            else:
                # Login failed, show an error message
                # You can display an error message using a messagebox or a label
                tk.messagebox.showinfo('Error', 'Invalid email or password')
                #error_label = tk.Label(self.middle_frame, text="Invalid email or password", font=("Arial", 10), fg="red")
                #error_label.pack()

class SignUp_First_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        self.bottom_frame = tk.Frame(main_window)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.SignUp_Title = tk.Label(self.middle_frame, text="Sign Up", font=("Arial", 15))
        self.information_Title = tk.Label(self.middle_frame, text="Please enter your information to creat a new account", font=("Arial", 10))
        self.Email_Title = tk.Label(self.middle_frame, text="Email", font=("Arial", 10))
        self.Password_Title = tk.Label(self.middle_frame, text="Password", font=("Arial", 10))
        self.Password_Confirm_Title = tk.Label(self.middle_frame, text="Confirm Password", font=("Arial", 10))
        self.Space_Title1 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10))
        self.Space_Title2 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10))
        self.Space_Title3 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10))

        #Input
        self.Email_Input = tk.Entry(self.middle_frame)
        self.Password_Input = tk.Entry(self.middle_frame)
        self.Password_Confirm_Input = tk.Entry(self.middle_frame)
        self.Password_Input.config(show="*")
        #self.Password_Input.config(show="*")

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page)
        self.Continue_Button = tk.Button(self.middle_frame, text='Continue', command=self.Continue_test)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg='black')
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill='black')
        self.middle_frame.pack(fill=tk.BOTH, expand=True)              
        
        # Pack the 'Menu' button to the right
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.SignUp_Title.pack(ipadx=5, ipady=5, padx=200, pady=20)
        #Display the information Title
        self.information_Title.pack(ipadx=5, ipady=0, padx=10, pady=0)
        self.Space_Title1.pack(ipadx=5, ipady=0, padx=10, pady=5)
        #Display the Email Title
        self.Email_Title.pack(ipadx=5, ipady=5, padx=10, pady=3)
        #Display the Email Input
        self.Email_Input.pack(ipadx=20, ipady=5, padx=10, pady=3)
        self.Space_Title2.pack(ipadx=5, ipady=0, padx=10, pady=10)
        #Display the Password Title
        self.Password_Title.pack(ipadx=5, ipady=0, padx=10, pady=3)
        #Display the Password Input
        self.Password_Input.pack(ipadx=20, ipady=5, padx=10, pady=3)
        self.Space_Title3.pack(ipadx=5, ipady=0, padx=10, pady=10)
        #Display the Password Confirm Title
        self.Password_Confirm_Title.pack(ipadx=5, ipady=0, padx=10, pady=3)
        #Display the Password Confirm Input
        self.Password_Confirm_Input.pack(ipadx=20, ipady=5, padx=10, pady=3)
        # Pack the 'Continue' button 
        self.Continue_Button.pack(ipadx=20, ipady=5, padx=10, pady=40)

    def Continue_test(self):
        #get the input
        self.Email=self.Email_Input.get()
        self.Password=self.Password_Input.get()
        self.Password_Confirm=self.Password_Confirm_Input.get()
        # Check if the email is a valid
        if not re.match(r'^[\w\.-]+@[\w\.-]+$', self.Email):
            # Invalid email format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid email format')
        else :
            if (self.Password==self.Password_Confirm) & (self.Email!='') & (self.Password!='') & (self.Password_Confirm!=''):
                Launch_SignUp_Second_Page(self.Email, self.Password)
            elif (self.Email=='') or (self.Password=='') or (self.Password_Confirm==''):
                tk.messagebox.showinfo('Error', 'Please fill in all the information')
            else:
                tk.messagebox.showinfo('Error', 'Password does not match')

class SignUp_Second_Page():
    def __init__(self, main_window, Email, Password):
        # Create a frame at the top for buttons
        self.Email = Email
        self.Password = Password
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        self.second_top_frame = tk.Frame(main_window)
        self.third_top_frame = tk.Frame(main_window)
        self.third_top_frame.columnconfigure(0, weight=1)
        self.third_top_frame.columnconfigure(1, weight=1)
        self.third_top_frame.columnconfigure(2, weight=1)
        self.third_top_frame.columnconfigure(3, weight=1)
        self.third_top_frame.columnconfigure(4, weight=1)
        self.bottom_frame = tk.Frame(main_window)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.SignUp_Title = tk.Label(self.second_top_frame, text="Sign Up", font=("Arial", 15))
        self.FirstName_Title = tk.Label(self.third_top_frame, text="First Name", font=("Arial", 10))
        self.LastName_Title = tk.Label(self.third_top_frame, text="Last Name *", font=("Arial", 10))
        self.UserName_Title = tk.Label(self.third_top_frame, text="User Name", font=("Arial", 10))
        self.Space_Title = tk.Label(self.middle_frame, text=" ", font=("Arial", 10))
        self.Phone_Title = tk.Label(self.middle_frame, text="Phone *", font=("Arial", 10))
        self.information_Optional_Title = tk.Label(self.bottom_frame, text="* Optional", font=("Arial", 10))
        self.information_Data_Title = tk.Label(self.bottom_frame, text="We'll only use your phone number to notify you about your flight", font=("Arial", 10))

        #Input
        self.FirstName_Input = tk.Entry(self.third_top_frame)
        self.LastName_Input = tk.Entry(self.third_top_frame)
        self.UserName_Input = tk.Entry(self.third_top_frame)
        self.Phone_Input = tk.Entry(self.middle_frame)
        print(Email)

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page)
        self.SignUp_Button = tk.Button(self.middle_frame, text='Sign Up', command=self.Sign_Up)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg='black')
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill='black')
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.third_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)        
        
        # Pack the 'Menu' button to the right
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.SignUp_Title.pack(ipadx=5, ipady=5, padx=200, pady=35)
        #Display the First Name Title
        self.FirstName_Title.grid(row=0, column=1, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the First Name Input
        self.FirstName_Input.grid(row=1, column=1, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the Last Name Title
        self.LastName_Title.grid(row=0, column=2, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the Last Name Input
        self.LastName_Input.grid(row=1, column=2, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the User Name Title
        self.UserName_Title.grid(row=0, column=3, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the User Name Input
        self.UserName_Input.grid(row=1, column=3, padx=10, pady=3, ipadx=5, ipady=5)
        self.Space_Title.pack(ipadx=5, ipady=0, padx=10, pady=15)
        #Display the Phone Title
        self.Phone_Title.pack(ipadx=5, ipady=0, padx=10, pady=3)
        #Display the Phone Input
        self.Phone_Input.pack(ipadx=20, ipady=5, padx=10, pady=3)
        # Pack the 'Sign Up' button 
        self.SignUp_Button.pack(ipadx=20, ipady=5, padx=10, pady=35)
        #Display the information Optional Title
        self.information_Optional_Title.pack(side=tk.LEFT, ipadx=5, ipady=0, padx=10, pady=3)
        #Display the information Data Title
        self.information_Data_Title.pack(side=tk.RIGHT, ipadx=5, ipady=0, padx=10, pady=3)
    
    def Sign_Up(self):
        #get the input
        self.FirstName=self.FirstName_Input.get()
        self.LastName=self.LastName_Input.get()
        self.UserName=self.UserName_Input.get()
        self.Phone=self.Phone_Input.get()
        # Check if the email is a valid
        if (self.FirstName=='') or (self.LastName=='') or (self.UserName=='') or (self.Phone==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        else :
            Actual_Customer.Complet_Actual_Customer(self.Email, self.Password, self.FirstName, self.LastName, self.UserName, self.Phone)
            Actual_Customer.Creat_Actual_Customer()
            Launch_Home_Page()


class Menu_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.middle_frame = tk.Frame(main_window)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.Menu_Title = tk.Label(self.middle_frame, text="Menu", font=("Arial", 15))

        # Create buttons
        self.Home_Button = tk.Button(self.middle_frame, text='    Home     ', command=Launch_Home_Page)
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.middle_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page)
        else :
            self.LogIn_Button = tk.Button(self.middle_frame, text='My Account', command=Launch_LogIn_Page)
        self.Purchase = tk.Button(self.middle_frame, text='   Purchase   ', command=Launch_Purchase_Page)
        self.CLose = tk.Button(self.middle_frame, text='      Close       ', command=Launch_LogIn_Page)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg='black')
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill='black')
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.Menu_Title.pack(ipadx=5, ipady=5, padx=200, pady=35)
        #Display the Home Button
        self.Home_Button.pack(ipadx=24, ipady=7, padx=10, pady=15)
        #Display the My Account Button
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button.pack(ipadx=8, ipady=7, padx=10, pady=15)
        else :
            self.LogIn_Button.pack(ipadx=24, ipady=7, padx=10, pady=15)
        #Display the Purchase Button
        self.Purchase.pack(ipadx=24, ipady=7, padx=10, pady=15)
        #Display the Close Button
        self.CLose.pack(ipadx=24, ipady=7, padx=10, pady=15)

class Purchase_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window)
        self.second_top_frame = tk.Frame(main_window)
        self.second_top_frame.columnconfigure(0, weight=1)
        self.second_top_frame.columnconfigure(1, weight=1)
        self.second_top_frame.columnconfigure(2, weight=1)
        self.second_top_frame.columnconfigure(3, weight=1)
        self.third_top_frame = tk.Frame(main_window)
        self.third_top_frame.columnconfigure(0, weight=1)
        self.third_top_frame.columnconfigure(1, weight=1)
        self.third_top_frame.columnconfigure(2, weight=1)
        self.third_top_frame.columnconfigure(3, weight=1)
        self.fourth_top_frame = tk.Frame(main_window)
        self.bottom_frame = tk.Frame(main_window)

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20))
        self.Space_Title = tk.Label(self.second_top_frame, text=" ", font=("Arial", 10))
        self.From_Title = tk.Label(self.second_top_frame, text="From", font=("Arial", 10))
        self.To_Title = tk.Label(self.second_top_frame, text="To", font=("Arial", 10))
        self.Departure_Title = tk.Label(self.second_top_frame, text="Departure", font=("Arial", 10))
        self.Return_Title = tk.Label(self.second_top_frame, text="Return *", font=("Arial", 10))
        self.Second_Space_Title = tk.Label(self.second_top_frame, text=" ", font=("Arial", 10))
        self.Passengers_Title = tk.Label(self.third_top_frame, text="Passengers", font=("Arial", 10))
        self.Class_Title = tk.Label(self.third_top_frame, text="Class", font=("Arial", 10))
        self.Third_Space_Title = tk.Label(self.third_top_frame, text=" ", font=("Arial", 10))
        self.Info = tk.Label(self.bottom_frame, text="* Optional", font=("Arial", 10))


        # Create buttons
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg='#0d3562')
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg='#0d3562')
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg='#0d3562')
        self.Search_Button = tk.Button(self.fourth_top_frame, text='Search', command=self.Search_Flight, font=("Arial", 15))
        self.Search_Button.config(height=1, width=10)

        #Input
        self.From_Input = tk.Entry(self.second_top_frame)
        self.To_Input = tk.Entry(self.second_top_frame)
        self.From_Input.insert(0, "London")
        self.To_Input.insert(0, "New York")
        self.Departure_Input = DateEntry(self.second_top_frame)
        self.Return_Input = DateEntry(self.second_top_frame)
        self.Passengers_Input = tk.Spinbox(self.third_top_frame, from_=1, to=10)
        self.Class_Input = tk.Spinbox(self.third_top_frame, from_=1, to=3)


        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg='black')
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill='black')
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.third_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.fourth_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Space Title
        self.Space_Title.grid(row=0, column=0, padx=10, pady=40, ipadx=5, ipady=0)
        #Display the From Title
        self.From_Title.grid(row=1, column=0, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the From Input
        self.From_Input.grid(row=2, column=0, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the To Title
        self.To_Title.grid(row=1, column=1, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the To Input
        self.To_Input.grid(row=2, column=1, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the Departure Title
        self.Departure_Title.grid(row=1, column=2, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the Departure Input
        self.Departure_Input.grid(row=2, column=2, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the Return Title
        self.Return_Title.grid(row=1, column=3, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the Return Input
        self.Return_Input.grid(row=2, column=3, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the Second Space Title
        self.Second_Space_Title.grid(row=3, column=0, padx=10, pady=20, ipadx=5, ipady=0)
        #Display the Passengers Title
        self.Passengers_Title.grid(row=0, column=1, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the Passengers Input
        self.Passengers_Input.grid(row=1, column=1, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the Class Title
        self.Class_Title.grid(row=0, column=2, padx=10, pady=3, ipadx=5, ipady=0)
        #Display the Class Input
        self.Class_Input.grid(row=1, column=2, padx=10, pady=3, ipadx=5, ipady=5)
        #Display the Third Space Title
        self.Third_Space_Title.grid(row=2, column=0, padx=10, pady=20, ipadx=5, ipady=0)
        #Display the Search Button
        self.Search_Button.pack(ipadx=15, ipady=5, padx=10, pady=10)
        #Display the Info
        self.Info.pack(side=tk.RIGHT, ipadx=5, ipady=0, padx=10, pady=3)

    def Search_Flight(self):
        #get the input
        self.From=self.From_Input.get()
        self.To=self.To_Input.get()
        self.Departure=self.Departure_Input.get()
        self.Return=self.Return_Input.get()
        self.Passengers=self.Passengers_Input.get()
        self.Class=self.Class_Input.get()
        # Check if the email is a valid
        if (self.From=='') or (self.To=='') or (self.Departure=='') or (self.Passengers=='') or (self.Class==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
            
        else :
            if self.Return!='':
                try :
                    departure_date = datetime.datetime.strptime(self.Departure, '%m/%d/%y')
                    return_date = datetime.datetime.strptime(self.Return, '%m/%d/%y')
                    (self.Passengers == int(self.Passengers)) & (self.Passengers > 0) & (self.Passengers < 11)
                    (self.Class == int(self.Class)) & (self.Class > 0) & (self.Class < 4)
                    self.From = str(self.From)
                    self.To = str(self.To)
                    if return_date < departure_date:
                        tk.messagebox.showinfo('Error', 'Return date must be after departure date')
                    else :
                        print("Search Flight")
                    # Dates are valid
                    # Now you can use departure_date and return_date as datetime objects
                    # for further processing.
                except ValueError:
                    # Invalid date format
                    tk.messagebox.showinfo('Error', 'Invalid date format for Departure or Return')
            else :
                try :
                    departure_date = datetime.datetime.strptime(self.Departure, '%m/%d/%y')
                    (self.Passengers == int(self.Passengers)) & (self.Passengers > 0) & (self.Passengers < 11)
                    (self.Class == int(self.Class)) & (self.Class > 0) & (self.Class < 4)
                    self.From = str(self.From)
                    self.To = str(self.To)
                    # Dates are valid
                    # Now you can use departure_date and return_date as datetime objects
                    # for further processing.
                    print("Search Flight")
                except ValueError:
                    # Invalid date format
                    tk.messagebox.showinfo('Error', 'Invalid date format for Departure')
                
            #print(self.From)
            #print(self.To)
            #print(self.Departure)
            #print(self.Return)
            #print(self.Passengers)
            #print(self.Class)

#---------------------## ALL THE FUNCTIONS ##---------------------#

## Opennig Pages ##

def Launch_Home_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    #main_window['bg']="#0d3562"
    Home_Page(main_window)

def Launch_LogIn_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    LogIn_Page(main_window)

def Launch_SignUp_First_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    SignUp_First_Page(main_window)

def Launch_SignUp_Second_Page(Email, Password):
    for widget in main_window.winfo_children():
        widget.destroy()
    SignUp_Second_Page(main_window, Email, Password)
    #print(Email)
    #print(Password)

def Launch_Menu_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Menu_Page(main_window)

def Launch_Purchase_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Purchase_Page(main_window)


main_window = tk.Tk()
main_window.title("OOP Air Line")
main_window.geometry("1100x600")
Actual_Customer = AC.Actual_Customer()
Actual_Customer.LogOrNot = False
Home_Page(main_window)
tk.mainloop()
