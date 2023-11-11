#First Page of the Project test repository
import pymysql
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import DateEntry
import dbconnect
import Actual_Customer as AC
import Actual_Search as AS
import re
from PIL import Image, ImageTk
import datetime
#import Classes_Screen as CS

#---------------------## ALL THE CLASSES ##---------------------#

class Home_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.left_frame = tk.Frame(main_window, bg=main_color)
        self.right_frame = tk.Frame(main_window)
        bg_image_one = Image.open("./images/degrado.jpg")
        bg_photo_one = ImageTk.PhotoImage(bg_image_one)
        # Créer un canevas pour afficher l'image de fond
        canvas = tk.Canvas(self.right_frame, width=bg_image_one.width, height=bg_image_one.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo_one)
        canvas.image = bg_photo_one

    
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Pres_OOPAirLine = tk.Label(self.right_frame, text="Welcome to OOP Air Line", font=("Arial", 15))

        # Create 
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Buy_Now_Button = tk.Button(self.left_frame, text='Buy Now', command=Launch_Purchase_Page, font=("Arial", 17), bg=third_color, fg=main_color)
        self.Buy_Now_Button.config(height=1, width=10)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.left_frame.pack(side=tk.LEFT, fill=tk.X)
        #self.right_frame.pack(side=tk.RIGHT, fill=tk.X)
        self.right_frame.place(x=520, y=200, relwidth=0.36, relheight=0.50)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
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
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)
        self.bottom_frame = tk.Frame(main_window, bg=main_color)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        self.SignIn_Title = tk.Label(self.middle_frame, text="Sign In", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.Email_Title = tk.Label(self.middle_frame, text="Email", font=("Arial", 10), bg=main_color)
        self.Password_Title = tk.Label(self.middle_frame, text="Password", font=("Arial", 10), bg=main_color)
        self.Space_Title1 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.NewAccount_Title = tk.Label(self.bottom_frame, text="Don't have an account?", font=("Arial", 10), bg=main_color)

        #Input
        self.Email_Input = tk.Entry(self.middle_frame)
        self.Password_Input = tk.Entry(self.middle_frame)
        self.Password_Input.config(show="*")

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Log_Button = tk.Button(self.middle_frame, text='Log In', command=self.Log_check, bg=third_color, fg=main_color)
        self.NewAccount_Button = tk.Button(self.bottom_frame, text='Sign Up', command=Launch_SignUp_First_Page, bg=third_color, fg=main_color)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
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

    def Hide_Button(self, empty):
        Launch_Home_Page()

    
    def Log_check(self):
        #get the input
        self.Email=self.Email_Input.get()
        self.Password=self.Password_Input.get()
        # Check if the email is a valid email address using a regular expression
        if not re.match(r'^[\w\.-]+@[\w\.-]+$', self.Email):
            # Invalid email format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid email format')
        else :
            sql = "SELECT * FROM customer WHERE Email = '{}' AND Password = '{}'".format(self.Email, self.Password) 
            result=self.db.fetch(sql)
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
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)
        self.bottom_frame = tk.Frame(main_window, bg=main_color)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button_1)
        self.SignUp_Title = tk.Label(self.middle_frame, text="Sign Up", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.GoBack_Title = tk.Label(self.middle_frame, text="<", font=("Arial", 20), bg=main_color)
        self.GoBack_Title.bind("<Button-1>", self.Hide_Button_2)
        self.information_Title = tk.Label(self.middle_frame, text="Please enter your information to creat a new account", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Email_Title = tk.Label(self.middle_frame, text="Email", font=("Arial", 10), bg=main_color)
        self.Password_Title = tk.Label(self.middle_frame, text="Password", font=("Arial", 10), bg=main_color)
        self.Password_Confirm_Title = tk.Label(self.middle_frame, text="Confirm Password", font=("Arial", 10), bg=main_color)
        self.Space_Title1 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title2 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title3 = tk.Label(self.middle_frame, text=" ", font=("Arial", 10), bg=main_color)

        #Input
        self.Email_Input = tk.Entry(self.middle_frame)
        self.Password_Input = tk.Entry(self.middle_frame)
        self.Password_Confirm_Input = tk.Entry(self.middle_frame)
        self.Password_Input.config(show="*")
        #self.Password_Input.config(show="*")

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Continue_Button = tk.Button(self.middle_frame, text='Continue', command=self.Continue_test, bg=third_color, fg=main_color)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)              
        
        # Pack the 'Menu' button to the right
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        #Display the Sign In Title
        self.SignUp_Title.pack(ipadx=5, ipady=5, padx=200, pady=20)
        #Display the Go Back Title
        self.GoBack_Title.place(x=22, y=15)
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

    def Hide_Button_1(self, empty):
        Launch_Home_Page()
    
    def Hide_Button_2(self, empty):
        Launch_LogIn_Page()

class SignUp_Second_Page():
    def __init__(self, main_window, Email, Password):
        # Create a frame at the top for buttons
        self.Email = Email
        self.Password = Password
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.third_top_frame = tk.Frame(main_window, bg=main_color)
        self.third_top_frame.columnconfigure(0, weight=1)
        self.third_top_frame.columnconfigure(1, weight=1)
        self.third_top_frame.columnconfigure(2, weight=1)
        self.third_top_frame.columnconfigure(3, weight=1)
        self.third_top_frame.columnconfigure(4, weight=1)
        self.bottom_frame = tk.Frame(main_window, bg=main_color)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button_1)
        self.GoBack_Title = tk.Label(self.second_top_frame, text="<", font=("Arial", 20), bg=main_color)
        self.GoBack_Title.bind("<Button-1>", self.Hide_Button_2)
        self.SignUp_Title = tk.Label(self.second_top_frame, text="Sign Up", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.FirstName_Title = tk.Label(self.third_top_frame, text="First Name", font=("Arial", 10), bg=main_color)
        self.LastName_Title = tk.Label(self.third_top_frame, text="Last Name *", font=("Arial", 10), bg=main_color)
        self.UserName_Title = tk.Label(self.third_top_frame, text="User Name", font=("Arial", 10), bg=main_color)
        self.Space_Title = tk.Label(self.middle_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Phone_Title = tk.Label(self.middle_frame, text="Phone *", font=("Arial", 10), bg=main_color)
        self.information_Optional_Title = tk.Label(self.bottom_frame, text="* Optional", font=("Arial", 10), bg=main_color)
        self.information_Data_Title = tk.Label(self.bottom_frame, text="We'll only use your phone number to notify you about your flight", font=("Arial", 10), bg=main_color)

        #Input
        self.FirstName_Input = tk.Entry(self.third_top_frame)
        self.LastName_Input = tk.Entry(self.third_top_frame)
        self.UserName_Input = tk.Entry(self.third_top_frame)
        self.Phone_Input = tk.Entry(self.middle_frame)
        print(Email)

        # Create buttons
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.SignUp_Button = tk.Button(self.middle_frame, text='Sign Up', command=self.Sign_Up, bg=third_color, fg=main_color)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
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
        #Display the Go Back Title
        self.GoBack_Title.place(x=22, y=15)
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
        # Check if the phone is a valid one
        if (self.FirstName=='') or (self.LastName=='') or (self.UserName=='') or (self.Phone==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif not re.match(r'^[0-9]*$', self.Phone):
            # Invalid phone format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid phone format')
        else :
            Actual_Customer.Complet_Actual_Customer(self.Email, self.Password, self.FirstName, self.LastName, self.UserName, self.Phone)
            Creat=Actual_Customer.Creat_Actual_Customer()
            if Creat=="Email":
                tk.messagebox.showinfo('Error', 'This Email has already been used')
            elif Creat=="Phone":
                tk.messagebox.showinfo('Error', 'This Phone has already been used')
            elif Creat=="UserName":
                tk.messagebox.showinfo('Error', 'This UserName has already been used')
            elif Creat=="Succeed":
                Launch_Home_Page()
            else:
                tk.messagebox.showinfo('Error', 'Creat Failed')
    
    def Hide_Button_1(self, empty):
        Launch_Home_Page()
    
    def Hide_Button_2(self, empty):
        Launch_SignUp_First_Page()

class Menu_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)
        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        self.Menu_Title = tk.Label(self.middle_frame, text="Menu", font=("Arial", 15), bg=main_color, fg=fourth_color)

        # Create buttons
        self.Home_Button = tk.Button(self.middle_frame, text='    Home     ', command=Launch_Home_Page, bg=second_color, fg=main_color)
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.middle_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
        else :
            self.LogIn_Button = tk.Button(self.middle_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
        self.Purchase = tk.Button(self.middle_frame, text='   Purchase   ', command=Launch_Purchase_Page, bg=second_color, fg=main_color)
        self.CLose = tk.Button(self.middle_frame, text='      Close       ', command=self.Close, bg=second_color, fg=main_color)
        if main_color==main_color_light:
            self.Change_Theme = tk.Button(self.middle_frame, text='Dark Theme', command=Change_Theme, bg=second_color, fg=main_color)
        else:
            self.Change_Theme = tk.Button(self.middle_frame, text='Light Theme', command=Change_Theme, bg=second_color, fg=main_color)

        # Pack all widgets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
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
        #Display the Change Theme Button
        self.Change_Theme.pack(ipadx=24, ipady=7, padx=10, pady=15)

    def Close(self):
        main_window.destroy()

    def Hide_Button(self, empty):
        Launch_Home_Page()

class Purchase_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame.columnconfigure(0, weight=1)
        self.second_top_frame.columnconfigure(1, weight=1)
        self.second_top_frame.columnconfigure(2, weight=1)
        self.second_top_frame.columnconfigure(3, weight=1)
        self.third_top_frame = tk.Frame(main_window, bg=main_color)
        self.third_top_frame.columnconfigure(0, weight=1)
        self.third_top_frame.columnconfigure(1, weight=1)
        self.third_top_frame.columnconfigure(2, weight=1)
        self.third_top_frame.columnconfigure(3, weight=1)
        self.fourth_top_frame = tk.Frame(main_window, bg=main_color)
        self.bottom_frame = tk.Frame(main_window, bg=main_color)

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        self.Space_Title = tk.Label(self.second_top_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.From_Title = tk.Label(self.second_top_frame, text="From", font=("Arial", 10), bg=main_color)
        self.To_Title = tk.Label(self.second_top_frame, text="To", font=("Arial", 10), bg=main_color)
        self.Departure_Title = tk.Label(self.second_top_frame, text="Departure", font=("Arial", 10), bg=main_color)
        self.Return_Title = tk.Label(self.second_top_frame, text="Return *", font=("Arial", 10), bg=main_color)
        self.Second_Space_Title = tk.Label(self.second_top_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Passengers_Title = tk.Label(self.third_top_frame, text="Passengers", font=("Arial", 10), bg=main_color)
        self.Class_Title = tk.Label(self.third_top_frame, text="Class", font=("Arial", 10), bg=main_color)
        self.Third_Space_Title = tk.Label(self.third_top_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Info = tk.Label(self.bottom_frame, text="* Optional", font=("Arial", 10), bg=main_color)


        # Create buttons
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Search_Button = tk.Button(self.fourth_top_frame, text='Search', command=self.Search_Flight, font=("Arial", 15), bg=third_color, fg=main_color)
        self.Search_Button.config(height=1, width=10)

        #Input
        self.From_Input = tk.Entry(self.second_top_frame)
        self.To_Input = tk.Entry(self.second_top_frame)
        self.From_Input.insert(0, "London")
        self.To_Input.insert(0, "New York")
        self.Departure_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        #self.Return_Input_Radio = tk.Radiobutton(self.second_top_frame, text="Return", value=1)
        self.Return_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        self.Passengers_Input = tk.Spinbox(self.third_top_frame, from_=1, to=10)
        self.Class_Input = ttk.Combobox(self.third_top_frame, values=["Economy", "Business", "First Class"])


        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=2, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(0, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.third_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.fourth_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
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
        #Display The Radio Button
        #self.Return_Input_Radio.grid(row=2, column=3, padx=10, pady=3, ipadx=5, ipady=0)
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
        # Pack the 'Search' button
        self.Search_Button.pack(ipadx=10, ipady=5, padx=10, pady=10)
        #Display the Info
        self.Info.pack(side=tk.RIGHT, ipadx=5, ipady=0, padx=10, pady=3)

    def Search_Flight(self):
        #get the input
        self.From=self.From_Input.get()
        self.To=self.To_Input.get()
        self.Departure=self.Departure_Input.get()
        self.Return=self.Return_Input.get()
        self.Passengers=int(self.Passengers_Input.get())
        self.Class=self.Class_Input.get()
        # Check if the email is a valid
        if (self.From=='') or (self.To=='') or (self.Departure=='') or (self.Passengers=='') or (self.Class==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
            
        else :
            if self.Return!='':
                try :
                    #departure_date = datetime.datetime.strptime(self.Departure, '%y-%m-%d')
                    #return_date = datetime.datetime.strptime(self.Return, '%y-%m-%d')
                    if self.Departure > self.Return:
                        tk.messagebox.showinfo('Error', 'Return date must be after departure date')
                    else :
                        if (self.Passengers == int(self.Passengers)) & (self.Passengers > 0) & (self.Passengers < 11):
                            if (self.Class == "Economy") or (self.Class == "Business") or (self.Class =="First Class"):
                                if (self.From == str(self.From)) & (self.To == str(self.To)):
                                    print("Search Flight")
                                    # Dates are valid
                                    Actual_Search.Complet_Actual_Search(self.From, self.To, self.Departure, self.Return, self.Class, self.Passengers)
                                    Actual_Search.Search()
                            else:
                                tk.messagebox.showinfo('Error', 'Invalid Class')
                        else:
                            tk.messagebox.showinfo('Error', 'Invalid Number of Passengers')
                except ValueError:
                    # Invalid date format
                    tk.messagebox.showinfo('Error', 'Invalid date format or Number of Passengers or Class')
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
                    tk.messagebox.showinfo('Error', 'Invalid date format or Number of Passengers or Class')
                
            #print(self.From)
            #print(self.To)
            #print(self.Departure)
            #print(self.Return)
            #print(self.Passengers)
            #print(self.Class)

    def Hide_Button(self, empty):
        Launch_Home_Page()

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

def Change_Theme():
    global main_color
    global second_color
    global third_color
    global fourth_color
    global main_color_light
    global second_color_light
    global third_color_light
    global fourth_color_light
    global main_color_dark
    global second_color_dark
    global third_color_dark
    global fourth_color_dark
    
    if main_color==main_color_light:
        main_color=main_color_dark
        second_color=second_color_dark
        third_color=third_color_dark
        fourth_color=fourth_color_dark
    else:
        main_color=main_color_light
        second_color=second_color_light
        third_color=third_color_light
        fourth_color=fourth_color_light

    main_window.configure(bg=main_color)
    for widget in main_window.winfo_children():
        widget.destroy()
    Menu_Page(main_window)


main_window = tk.Tk()
main_window.title("OOP Air Line")
main_window.geometry("1100x600")
main_window.style = tk.ttk.Style()
main_window.style.theme_use("clam")
#main_window.iconbitmap("./images/avion.ico")



Actual_Customer = AC.Actual_Customer()
Actual_Customer.LogOrNot = False
Actual_Search = AS.Actual_Search()
#Light Theme
main_color_light="#fff7ea"
second_color_light="#722a39"
third_color_light="#375c4f"
fourth_color_light="#3f171f"
#Dark Theme
main_color_dark='#292929'
second_color_dark="#9c4c5b"
third_color_dark="#017368"
fourth_color_dark="#cf6679"

#Theme
main_color=main_color_light
second_color=second_color_light
third_color=third_color_light
fourth_color=fourth_color_light
main_window.configure(bg=main_color)

Home_Page(main_window)
tk.mainloop()
