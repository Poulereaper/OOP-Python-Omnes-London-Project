#Imports
import pymysql
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import dbconnect
import Actual_Customer as AC
import Actual_Search as AS
import Actual_Flight as AF
import My_Basket as AB
import Mail as M
#import LogInPage as LP
import re
from PIL import Image, ImageTk, ImageDraw
import datetime
import base64
from io import BytesIO
import uuid
import base64
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#---------------------## ALL THE CLASSES ##---------------------#

##------------------------------------------------------------------------------------------------------##
##----------------------------------------------Home Page-----------------------------------------------##
##------------------------------------------------------------------------------------------------------##

class Home_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.left_frame = tk.Frame(main_window, bg=main_color)
        self.right_frame = tk.Frame(main_window, bg=main_color)
        bg_image_one = Image.open("./images/degrado.jpg")
        bg_photo_one = ImageTk.PhotoImage(bg_image_one)
        #Créer un canevas pour afficher l'image de fond
        canvas_one = tk.Canvas(self.right_frame, width=bg_image_one.width, height=bg_image_one.height, bg=main_color, highlightthickness=0, borderwidth=0)
        canvas_one.config(bg=main_color)
        canvas_one.pack()
        canvas_one.create_image(0, 0, anchor=tk.NW, image=bg_photo_one)
        canvas_one.image = bg_photo_one


        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=150,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass 

        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Pres_OOPAirLine = tk.Label(self.right_frame, text="Welcome to OOP Air Line", font=("Arial", 15))

        # Create 
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
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
        self.Home_Page_Title.pack(ipadx=0, ipady=5, padx=10, pady=10)
        #Display the Buy Now Button
        self.Buy_Now_Button.pack(ipadx=5, ipady=5, padx=200, pady=10)
        #Display the text
        self.Pres_OOPAirLine.pack(ipadx=5, ipady=5, padx=20, pady=10)

    def Hide_Button_1(self, empty):
        Launch_Basket_Page()

##------------------------------------------------------------------------------------------------------##
##-----------------------------------------------LogIn Page---------------------------------------------##
##------------------------------------------------------------------------------------------------------##

class LogIn_Page():
    def __init__(self, main_window):
        self.db=dbconnect.DBHelper()
        self.See=False
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)
        self.bottom_frame = tk.Frame(main_window, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=0,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=980,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=998,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=998,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass 

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
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=95, pady=10)
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
            sql = "SELECT * FROM customer WHERE Email = '{}' AND Password = '{}'".format(self.Email, self.Password) 
            result=self.db.fetch(sql)
            if result:
                # Copy the result to the Actual_Customer
                Actual_Customer.Copy_To_Actual_Customer(result)
                # Login successful, show the home page
                Launch_My_Account()
            else:
                # Login failed, show an error message
                tk.messagebox.showinfo('Error', 'Invalid email or password')

    def Hide_Button_1(self, empty):
        Launch_Basket_Page()
    
    def Hide_Button(self, empty):
        Launch_Home_Page()

##------------------------------------------------------------------------------------------------------##
##----------------------------------------------SignUp Page---------------------------------------------##
##------------------------------------------------------------------------------------------------------##

class SignUp_First_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)
        self.bottom_frame = tk.Frame(main_window, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=0,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two
        
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
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=95, pady=10)
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


##------------------------------------------------------------------------------------------------------##
##------------------------------------------SignUp_Second_Page------------------------------------------##
##------------------------------------------------------------------------------------------------------##

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

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=0,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two
        
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
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=95, pady=10)
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
        elif len(self.Phone)!=10:
            # Invalid phone format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid phone format')
        elif len(self.UserName)>25 or len(self.UserName)<2:
            # Invalid UserName format, show an error message
            tk.messagebox.showinfo('Error', 'UserName must be between 2 and 25 characters')
        elif len(self.FirstName)>25 or len(self.FirstName)<2:
            # Invalid FirstName format, show an error message
            tk.messagebox.showinfo('Error', 'FirstName must be between 2 and 25 characters')
        elif len(self.LastName)>25 or len(self.LastName)<2:
            # Invalid LastName format, show an error message
            tk.messagebox.showinfo('Error', 'LastName must be between 2 and 25 characters')
        else :
            Actual_Customer.Complet_Actual_Customer(self.Email, self.Password, self.FirstName, self.LastName, self.UserName, self.Phone, None)
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

##------------------------------------------------------------------------------------------------------##
##------------------------------------------------Menu Page---------------------------------------------##
##------------------------------------------------------------------------------------------------------##

class Menu_Page():
    def __init__(self, main_window):
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=0,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=980,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=998,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=998,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass 

        #theme
        if main_color==main_color_light:
            bg_image_five = Image.open("./images/light-mode.png")
        else:
            bg_image_five = Image.open("./images/dark-mode.png")
        bg_photo_five = ImageTk.PhotoImage(bg_image_five)
        # Créer un canevas pour afficher l'image du logo
        canvas_five = tk.Canvas(self.middle_frame, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_five.place(x=1020,y=20)
        canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
        canvas_five.image = bg_photo_five
        canvas_five.bind("<Button-1>", self.Change_Theme)

        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        self.Menu_Title = tk.Label(self.middle_frame, text="Menu", font=("Arial", 15), bg=main_color, fg=fourth_color)

        # Create buttons
        self.Home_Button = tk.Button(self.middle_frame, text='    Home     ', command=Launch_Home_Page, bg=second_color, fg=main_color)
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.middle_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
        else :
            self.LogIn_Button = tk.Button(self.middle_frame, text='My Account', command=Launch_My_Account, bg=second_color, fg=main_color)
        self.Purchase = tk.Button(self.middle_frame, text='   Purchase   ', command=Launch_Purchase_Page, bg=second_color, fg=main_color)
        self.CLose = tk.Button(self.middle_frame, text='      Close       ', command=self.Close, bg=second_color, fg=main_color)

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
        self.Home_Page_Title.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=95, pady=10)
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

    def Close(self):
        main_window.destroy()

    def Hide_Button(self, empty):
        Launch_Home_Page()
    
    def Hide_Button_1(self, empty):
        Launch_Basket_Page()
    
    def Change_Theme(self, empty):
        Change_Theme()

##------------------------------------------------------------------------------------------------------##
##---------------------------------------------My Account Page------------------------------------------##
##------------------------------------------------------------------------------------------------------##

class My_Account_Page():
    def __init__(self, main_window):
         # Create a frame at the top for buttons
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.left_frame = tk.Frame(main_window,  width=290, bg=main_color)
        self.right_frame = tk.Frame(main_window, bg=main_color)
        self.top_right_frame = tk.Frame(self.right_frame, height=70, bg=main_color)
        self.rest_right_frame = tk.Frame(self.right_frame, bg=main_color)

        self.scroll_canva = tk.Canvas(self.rest_right_frame, bg=main_color)
        self.scroll_canva.config(highlightthickness=0, borderwidth=0)
        self.display_frame = tk.Frame(self.scroll_canva, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=50,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=68,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=68,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass
        #Profile Picture 
        if (Actual_Customer.ProfilePicture==None) or (Actual_Customer.ProfilePicture=="") :
            bg_image_five = Image.open("./pp/user.png")
        else:
            # Open the image file and convert it to a Tkinter image object
            # Decode the base64 image
            decoded_image = base64.b64decode(Actual_Customer.ProfilePicture)
            # Create a PIL image object from the decoded image data
            image = Image.open(BytesIO(decoded_image))

            bg_image_five = image
            bg_photo_five = ImageTk.PhotoImage(bg_image_five)
            canvas_five = tk.Canvas(self.left_frame, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_five.place(x=45,y=30)
            canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
            canvas_five.image = bg_photo_five

        #Title and Text
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        self.Name_Title = tk.Label(self.left_frame, text=Actual_Customer.FirstName+" "+Actual_Customer.LastName, font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.UserName_Title = tk.Label(self.left_frame, text=Actual_Customer.UserName, font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Email_Title = tk.Label(self.left_frame, text=Actual_Customer.Email, font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Phone_Title = tk.Label(self.left_frame, text=Actual_Customer.Phone, font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Employment_Title = tk.Label(self.left_frame, text="Employee ID :"+str(Actual_Customer.CustomerID), font=("Arial", 10), bg=main_color, fg=fourth_color)

        # Button
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        if Actual_Customer.AdminOrNot == True:
            self.Admin_Button = tk.Button(self.left_frame, text='Employee Space', command=self.Admin_Page, bg=second_color, fg=main_color, width=15, height=2)
        self.Purchase_Button = tk.Button(self.left_frame, text=' Go Purchase', command=Launch_Purchase_Page, bg=second_color, fg=main_color, width=15, height=2)
        self.Profile_Picture_Button = tk.Button(self.left_frame, text='Change Profile Picture', command=self.Change_Profile_Picture, bg=third_color, fg=main_color, width=18, height=1)
        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.top_right_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.place(x=580, y=10)
        #Display Profile Picture Button
        self.Profile_Picture_Button.place(x=50, y=180)
        #Display the Name Title
        self.Name_Title.place(x=50, y=230)
        #Display the UserName Title
        self.UserName_Title.place(x=50, y=255)
        #Display the Email Title
        self.Email_Title.place(x=50, y=290)
        #Display the Phone Title
        self.Phone_Title.place(x=50, y=330)
        #Display the Purchase Button
        self.Purchase_Button.place(x=50, y=420)
        #Display the Admin Button
        if Actual_Customer.AdminOrNot == True:
            self.Employment_Title.place(x=50, y=360)
            self.Admin_Button.place(x=50, y=480)
                #draw Line right of left frame
        self.line_canvas_right = tk.Canvas(self.left_frame, width=3, height=self.left_frame.winfo_screenheight()-220, bg=second_color)
        self.line_canvas_right.config(highlightthickness=0, borderwidth=0)
        self.line_canvas_right.place(x=270, y=20)
        # Create a line on right of top_frame
        self.line_canvas_right.create_line(2, 0, 2, self.left_frame.winfo_screenheight(), fill=second_color)

        self.rest_right_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #Display Stuff in right frame
        if Actual_Customer.AdminPage==False:
            #Right Titles 
            self.Upcoming_Flights_Title = tk.Label(self.top_right_frame, text="Upcoming Flights", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Upcoming_Flights_Title.bind("<Button-1>", self.UpComFlights)
            self.Past_Flights_Title = tk.Label(self.top_right_frame, text="Past Flights", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Past_Flights_Title.bind("<Button-1>", self.PastFlights)
            self.Settings_Title = tk.Label(self.top_right_frame, text="Settings", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Settings_Title.bind("<Button-1>", self.Settings)
            self.Cards_Title = tk.Label(self.top_right_frame, text="Cards", font=("Arial", 13), bg=main_color, fg=fourth_color)
            if Actual_Customer.Page==0:self.Upcoming_Flights_Title.config( fg=third_color)
            elif Actual_Customer.Page==1:self.Past_Flights_Title.config( fg=third_color)
            elif Actual_Customer.Page==2:self.Settings_Title.config( fg=third_color)
            elif Actual_Customer.Page==3:self.Cards_Title.config( fg=third_color)
            self.Cards_Title.bind("<Button-1>", self.Cards)
            #Display the Upcoming Flights Title
            self.Upcoming_Flights_Title.place(x=40, y=15)
            #Display the Past Flights Title
            self.Past_Flights_Title.place(x=260, y=15)
            #Display the Settings Title
            self.Settings_Title.place(x=470, y=15)
            #Display the Cards Title
            self.Cards_Title.place(x=650, y=15)
            if Actual_Customer.Page==0 or Actual_Customer.Page==1:
                self.scroll_canva.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                self.yscrollbar = tk.Scrollbar(self.rest_right_frame, orient="vertical", command=self.scroll_canva.yview)
                self.yscrollbar.pack(side=tk.RIGHT, fill='y')
                self.scroll_canva.configure(yscrollcommand=self.yscrollbar.set)
                self.scroll_canva.bind('<Configure>', lambda e: self.scroll_canva.configure(scrollregion = self.scroll_canva.bbox("all")))
                self.display_frame.pack(fill=tk.BOTH, expand=True)
                self.scroll_canva.create_window((0,0), window=self.display_frame, anchor="nw")
                rep=Actual_Customer.HowMany_Orders()
                if (rep==0) or (rep==None) or ((Actual_Search.ReturnOrNot==True) & (rep==0)):
                    if Actual_Customer.Page==0:
                        self.No_Flight_Title = tk.Label(self.display_frame, text="No Flight Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
                        self.Info_Noo_Flight = tk.Label(self.display_frame, text="Unfortunately it seems that you have no Upcoming Flights.", font=("Arial", 10), bg=main_color, fg=fourth_color)
                    elif Actual_Customer.Page==1:
                        self.No_Flight_Title = tk.Label(self.display_frame, text="No Flight Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
                        self.Info_Noo_Flight = tk.Label(self.display_frame, text="Unfortunately it seems that you have no Past Flights.", font=("Arial", 10), bg=main_color, fg=fourth_color)
                    self.No_Flight_Title.pack(ipadx=5, ipady=5, padx=190, pady=40)
                    self.Info_Noo_Flight.pack(ipadx=5, ipady=5, padx=190, pady=30)
                else:
                    print(rep)
                    for i in range(rep):
                        self.Price_display=0
                        self.Total_Price_display=0
                        if Actual_Customer.Page==0: self.Search_Results = Actual_Customer.Select_UpComing_Flight()
                        elif Actual_Customer.Page==1: self.Search_Results = Actual_Customer.Select_Past_Flight()

                        try:
                            # Create a canvas widget
                            self.canvas = tk.Canvas(self.display_frame, width=700, height=200, highlightthickness=0 ,borderwidth=0, bg=main_color)
                            self.canvas.bind("<Button-1>", lambda event, param=self.Search_Results: self.FLight_Select(event, param))
                            self.canvas.pack(padx=65, pady=5, side=tk.TOP, fill=tk.X)
                            # Draw a rectangle on the canvas
                            self.canvas.create_rectangle(0, 0, 700, 200, outline='black', width=2)
                            # Print information in the rectangle
                            self.canvas.create_text(380, 40, anchor='nw', text="Flight Number: "+str(self.Search_Results[i]['FlightNumber']), font=("Arial", 10))
                            self.canvas.create_text(380, 60, anchor='nw', text="Departure: "+str(self.Search_Results[i]['Departure']), font=("Arial", 10))
                            self.canvas.create_text(380, 80, anchor='nw', text="Arrival: "+str(self.Search_Results[i]['Arrival']), font=("Arial", 10))
                            self.canvas.create_text(630, 40, anchor='nw', text="£"+str(self.Search_Results[i]['SommeDesPrix']), font=("Arial", 15))
                            self.canvas.create_text(380, 120, anchor='nw', text="Departure Time: "+str(self.Search_Results[i]['DepartureTime']), font=("Arial", 10))
                            self.canvas.create_text(380, 150, anchor='nw', text="Arrival Time: "+str(self.Search_Results[i]['ArrivalTime']), font=("Arial", 10))
                            self.canvas.create_text(640, 120, anchor='nw', text="x "+str(self.Search_Results[i]['NombreDeReservations']), font=("Arial", 10))
                            image_name = "./images/Flights_Images/"+(str(self.Search_Results[i]['Arrival']).replace(' ', '_'))+".png"
                            bg_image_rep = Image.open(image_name)
                            bg_photo_rep = ImageTk.PhotoImage(bg_image_rep)
                            # Créer un canevas pour afficher l'image du logo
                            canvas_rep = tk.Canvas(self.canvas, width=bg_image_rep.width, height=bg_image_rep.height, highlightthickness=0,borderwidth=0)
                            canvas_rep.place(x=10,y=10)
                            canvas_rep.create_image(0, 0, anchor=tk.NW, image=bg_photo_rep)
                            canvas_rep.image = bg_photo_rep
                            bg_image_rep.close()
                            bg_image_height = Image.open("./images/passenger.png")
                            bg_photo_height = ImageTk.PhotoImage(bg_image_height)
                            # Créer un canevas pour afficher l'image du logo
                            canvas_height = tk.Canvas(self.canvas, width=bg_image_height.width, height=bg_image_height.height, bg=main_color,highlightthickness=0,borderwidth=0)
                            canvas_height.place(x=625, y=120)
                            canvas_height.create_image(0, 0, anchor=tk.NW, image=bg_photo_height)
                            canvas_height.image = bg_photo_height
                            bg_image_height.close()
                        except IndexError:
                            if i==0:
                                self.canvas.destroy()
                                if Actual_Customer.Page==0:
                                    self.No_Flight_Title = tk.Label(self.display_frame, text="No Flight Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
                                    self.Info_Noo_Flight = tk.Label(self.display_frame, text="Unfortunately it seems that you have no Upcoming Flights.", font=("Arial", 10), bg=main_color, fg=fourth_color)
                                elif Actual_Customer.Page==1:
                                    self.No_Flight_Title = tk.Label(self.display_frame, text="No Flight Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
                                    self.Info_Noo_Flight = tk.Label(self.display_frame, text="Unfortunately it seems that you have no Past Flights.", font=("Arial", 10), bg=main_color, fg=fourth_color)
                                self.No_Flight_Title.pack(ipadx=5, ipady=5, padx=190, pady=40)
                                self.Info_Noo_Flight.pack(ipadx=5, ipady=5, padx=190, pady=30)
                                break
                            self.canvas.destroy()
                            break
            elif Actual_Customer.Page==2:
                #Titles 
                self.Personal_Info_Title = tk.Label(self.rest_right_frame, text="Personal Information", font=("Arial", 13), bg=main_color, fg=fourth_color)
                self.First_Name_Title = tk.Label(self.rest_right_frame, text=" First Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Last_Name_Title = tk.Label(self.rest_right_frame, text=" Last Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.User_Name_Title = tk.Label(self.rest_right_frame, text=" User Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Email_Title = tk.Label(self.rest_right_frame, text=" Email", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Phone_Title = tk.Label(self.rest_right_frame, text=" Phone", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Change_Password_Title = tk.Label(self.rest_right_frame, text="Change Password", font=("Arial", 13), bg=main_color, fg=fourth_color)
                self.Old_Password_Title = tk.Label(self.rest_right_frame, text=" Old Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.New_Password_Title = tk.Label(self.rest_right_frame, text=" New Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Confirm_Password_Title = tk.Label(self.rest_right_frame, text=" Confirm Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Info_Privacy_Title = tk.Label(self.rest_right_frame, text="Your information is private and secure", font=("Arial", 8), bg=main_color, fg=fourth_color)
                self.Info_Delete_Title = tk.Label(self.rest_right_frame, text="You can delete your account at any time and all your informations will be deleted", font=("Arial", 8), bg=main_color, fg=fourth_color)
                #Entries
                self.First_Name_Input = tk.Entry(self.rest_right_frame)
                self.First_Name_Input.insert(0, Actual_Customer.FirstName)
                self.Last_Name_Input = tk.Entry(self.rest_right_frame)
                self.Last_Name_Input.insert(0, Actual_Customer.LastName)
                self.User_Name_Input = tk.Entry(self.rest_right_frame)
                self.User_Name_Input.insert(0, Actual_Customer.UserName)
                self.Email_Input = tk.Entry(self.rest_right_frame)
                self.Email_Input.insert(0, Actual_Customer.Email)
                self.Phone_Input = tk.Entry(self.rest_right_frame)
                self.Phone_Input.insert(0, Actual_Customer.Phone)
                self.Old_Password_Input = tk.Entry(self.rest_right_frame, show="*")
                self.New_Password_Input = tk.Entry(self.rest_right_frame)
                self.Confirm_Password_Input = tk.Entry(self.rest_right_frame, show="*")
                #Button
                self.Save_Button = tk.Button(self.rest_right_frame, text='Save', command=self.Save, bg=third_color, fg=main_color, width=15, height=2)
                self.Disconnect_Button = tk.Button(self.rest_right_frame, text='Disconnect', command=self.Disconnect, bg=second_color, fg=main_color, width=15, height=2)
                self.Delete_Button = tk.Button(self.rest_right_frame, text='Delete Account', command=self.Delete_Account, bg=second_color, fg=main_color, width=15, height=2)
                #Display Stuff
                self.Personal_Info_Title.place(x=50, y=40)
                self.First_Name_Title.place(x=50, y=100)
                self.First_Name_Input.place(x=50, y=130)
                self.Last_Name_Title.place(x=50, y=170)
                self.Last_Name_Input.place(x=50, y=200)
                self.User_Name_Title.place(x=50, y=240)
                self.User_Name_Input.place(x=50, y=270)
                self.Email_Title.place(x=50, y=310)
                self.Email_Input.place(x=50, y=340)
                self.Phone_Title.place(x=50, y=380)
                self.Phone_Input.place(x=50, y=410)
                self.Change_Password_Title.place(x=350, y=40)
                self.Old_Password_Title.place(x=350, y=120)
                self.Old_Password_Input.place(x=350, y=150)
                self.New_Password_Title.place(x=350, y=190)
                self.New_Password_Input.place(x=350, y=220)
                self.Confirm_Password_Title.place(x=350, y=260)
                self.Confirm_Password_Input.place(x=350, y=290)
                self.Save_Button.place(x=600, y=130)
                self.Disconnect_Button.place(x=600, y=200)
                self.Delete_Button.place(x=600, y=270)
                self.Info_Privacy_Title.place(x=400, y=420)
                self.Info_Delete_Title.place(x=400, y=440)

            elif Actual_Customer.Page==3:
                self.canvas_card = tk.Canvas(self.rest_right_frame, width=550, height=300, highlightthickness=0 ,borderwidth=0, bg=main_color)
                self.canvas_card.pack(padx=65, pady=80)
                #Inputs
                self.Card_Number_Title = tk.Label(self.canvas_card, text="Card Number", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Card_Number = tk.Entry(self.canvas_card, width=30, bg=main_color, fg=fourth_color, font=("Arial", 12))
                self.Card_Date_Title = tk.Label(self.canvas_card, text="Expierd Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Card_Date = DateEntry(self.canvas_card, date_pattern='y-mm-dd', width=10, bg=main_color, fg=fourth_color, font=("Arial", 12))
                self.Card_Code_Title = tk.Label(self.canvas_card, text="Card Code", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Card_Code = tk.Entry(self.canvas_card, width=10, bg=main_color, fg=fourth_color, font=("Arial", 12))
                self.Card_Name_Title = tk.Label(self.canvas_card, text="Card Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Card_Name = tk.Entry(self.canvas_card, width=30, bg=main_color, fg=fourth_color, font=("Arial", 12))
                if Actual_Customer.CardNumber==0:
                    self.Card_Number.insert(0, "0000 0000 0000 0000")
                    self.Card_Code.delete(0, tk.END)
                    self.Card_Name.insert(0, Actual_Customer.FirstName+" "+Actual_Customer.LastName)
                else:
                    self.Card_Number.insert(0, Actual_Customer.CardNumber)
                    self.Card_Date.delete(0, tk.END)
                    self.Card_Date.insert(0, Actual_Customer.CardDate)
                    self.Card_Name.insert(0, Actual_Customer.CardName)

                #Button 
                self.Save_Button = tk.Button(self.canvas_card, text='Save', command=self.Save_Card, bg=third_color, fg=main_color, width=15, height=2)
                # Draw a rectangle on the canvas
                self.canvas_card.create_rectangle(0, 0, 550, 300, outline='black', width=2)
                #Card Number
                self.Card_Number_Title.place(x=35, y=30)
                self.Card_Number.place(x=35, y=55)
                #Card Date
                self.Card_Date_Title.place(x=35, y=90)
                self.Card_Date.place(x=35, y=115)
                #Card Code
                self.Card_Code_Title.place(x=250, y=90)
                self.Card_Code.place(x=250, y=115)
                #Card Name
                self.Card_Name_Title.place(x=35, y=150)
                self.Card_Name.place(x=35, y=175)
                #Pay-pro
                bg_image_four = Image.open("./images/pay-pro.png")
                bg_photo_four = ImageTk.PhotoImage(bg_image_four)
                # Créer un canevas pour afficher l'image du logo
                canvas_four = tk.Canvas(self.canvas_card, width=bg_image_four.width, height=bg_image_four.height, bg=main_color,highlightthickness=0,borderwidth=0)
                canvas_four.place(x=500,y=10)
                canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
                canvas_four.image = bg_photo_four
                #master Card
                bg_image_five = Image.open("./images/mastercard.png")
                bg_photo_five = ImageTk.PhotoImage(bg_image_five)
                # Créer un canevas pour afficher l'image du logo
                canvas_five = tk.Canvas(self.canvas_card, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
                canvas_five.place(x=40,y=220)
                canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
                canvas_five.image = bg_photo_five
                #Visa Card
                bg_image_six = Image.open("./images/visa.png")
                bg_photo_six = ImageTk.PhotoImage(bg_image_six)
                # Créer un canevas pour afficher l'image du logo
                canvas_six = tk.Canvas(self.canvas_card, width=bg_image_six.width, height=bg_image_six.height, bg=main_color,highlightthickness=0,borderwidth=0)
                canvas_six.place(x=120,y=210)
                canvas_six.create_image(0, 0, anchor=tk.NW, image=bg_photo_six)
                canvas_six.image = bg_photo_six
                #if Actual_Customer.CardNumber!=None:
                    #if isinstance(Actual_Customer.CardNumber, str):
                        #if Actual_Customer.CardNumber[0] == "4":
                            #canvas_six.place(x=40, y=210)
                        #elif Actual_Customer.CardNumber[0] == "5":
                            #canvas_five.place(x=40, y=220)
                        #else:
                            #canvas_five.place(x=40, y=220)
                            #canvas_six.place(x=120, y=210)
                self.Save_Button.place(x=400, y=220)
        else:
             #Right Titles 
            self.Cerate_Flights_Title = tk.Label(self.top_right_frame, text="Cerate Flights", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Cerate_Flights_Title.bind("<Button-1>", self.UpComFlights)
            self.Manage_Flights_Title = tk.Label(self.top_right_frame, text="Manage Flights", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Manage_Flights_Title.bind("<Button-1>", self.PastFlights)
            self.Create_Customer_Title = tk.Label(self.top_right_frame, text="Create Customer", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Create_Customer_Title.bind("<Button-1>", self.Settings)
            self.Manage_Customer_Title = tk.Label(self.top_right_frame, text="Manage Customer", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Manage_Customer_Title.bind("<Button-1>", self.Cards)
            self.Statistics_Title = tk.Label(self.top_right_frame, text="Statistics", font=("Arial", 13), bg=main_color, fg=fourth_color)
            self.Statistics_Title.bind("<Button-1>", self.Statistics)
            if Actual_Customer.Page==0:self.Cerate_Flights_Title.config( fg=third_color)
            elif Actual_Customer.Page==1:self.Manage_Flights_Title.config( fg=third_color)
            elif Actual_Customer.Page==2:self.Create_Customer_Title.config( fg=third_color)
            elif Actual_Customer.Page==3:self.Manage_Customer_Title.config( fg=third_color)
            elif Actual_Customer.Page==4:self.Statistics_Title.config( fg=third_color)
            #Display the Create Flights Title
            self.Cerate_Flights_Title.place(x=30, y=15)
            #Display the Manage Flights Title
            self.Manage_Flights_Title.place(x=190, y=15)
            #Display the Create Customer Title
            self.Create_Customer_Title.place(x=350, y=15)
            #Display the Manage Customer Title
            self.Manage_Customer_Title.place(x=510, y=15)
            #Display the Statistics Title
            self.Statistics_Title.place(x=690, y=15)
            if Actual_Customer.Page==0:
                #Titles
                self.Create_Flight_Title = tk.Label(self.rest_right_frame, text="Create Flight", font=("Arial", 13), bg=main_color, fg=fourth_color)
                self.Departure_Title = tk.Label(self.rest_right_frame, text=" Departure", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Departure_Date_Title = tk.Label(self.rest_right_frame, text=" Departure Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Departure_Time_Title = tk.Label(self.rest_right_frame, text=" Departure Time", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Arrival_Title = tk.Label(self.rest_right_frame, text=" Arrival", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Arrival_Date_Title = tk.Label(self.rest_right_frame, text=" Arrival Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Arrival_Time_Title = tk.Label(self.rest_right_frame, text=" Arrival Time", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Price_Title = tk.Label(self.rest_right_frame, text=" Price (Adulte)", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Discount_Title = tk.Label(self.rest_right_frame, text=" Discount", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Seats_Title = tk.Label(self.rest_right_frame, text=" Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Economy_Title = tk.Label(self.rest_right_frame, text=" Economy Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Business_Title = tk.Label(self.rest_right_frame, text=" Business Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.First_Title = tk.Label(self.rest_right_frame, text=" First Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Info_Title = tk.Label(self.rest_right_frame, text="Please fill all the fields", font=("Arial", 8), bg=main_color, fg=fourth_color)
                self.Info_Discount = tk.Label(self.rest_right_frame, text="Discount is in %", font=("Arial", 8), bg=main_color, fg=fourth_color)
                #Entries
                self.Departure_Input = tk.Entry(self.rest_right_frame)
                self.Departure_Date_Input = DateEntry(self.rest_right_frame, date_pattern='y-mm-dd')
                self.Departure_Time_Input = ttk.Combobox(self.rest_right_frame, values=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00","07:00", "08:00", "09:00", "10:00", "11:00", "12:00","13:00", "14:00", "15:00", "16:00", "17:00", "18:00","19:00", "20:00", "21:00", "22:00", "23:00"])
                #self.Departure_Time_Input = DateEntry(self.rest_right_frame, time_pattern='HH:mm')
                self.Arrival_Input = tk.Entry(self.rest_right_frame)
                self.Arrival_Date_Input = DateEntry(self.rest_right_frame, date_pattern='y-mm-dd')
                self.Arrival_Time_Input = ttk.Combobox(self.rest_right_frame, values=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00","07:00", "08:00", "09:00", "10:00", "11:00", "12:00","13:00", "14:00", "15:00", "16:00", "17:00", "18:00","19:00", "20:00", "21:00", "22:00", "23:00"])
                #self.Arrival_Time_Input = DateEntry(self.rest_right_frame, time_pattern='HH:mm')
                self.Price_Input = tk.Entry(self.rest_right_frame)
                self.Price_Input.insert(0, "0")
                self.Seats_Input = tk.Entry(self.rest_right_frame)
                self.Seats_Input.insert(0, "0")
                self.Discount_Input = tk.Entry(self.rest_right_frame)
                self.Discount_Input.insert(0, "0")
                self.Economy_Input = tk.Entry(self.rest_right_frame)
                self.Economy_Input.insert(0, "0")
                self.Business_Input = tk.Entry(self.rest_right_frame)
                self.Business_Input.insert(0, "0")
                self.First_Input = tk.Entry(self.rest_right_frame)
                self.First_Input.insert(0, "0")
                self.Image_Flight_Check = False
                #Button
                self.Create_Button = tk.Button(self.rest_right_frame, text='Create', command=self.Create_Flight, bg=third_color, fg=main_color, width=15, height=2)
                self.Add_Image_Flight_Button = tk.Button(self.rest_right_frame, text='Add Image', command=self.Add_Image_Flight, bg=third_color, fg=main_color, width=15, height=1)
                #Display Stuff
                self.Create_Flight_Title.place(x=50, y=20)
                self.Departure_Title.place(x=50, y=80)
                self.Departure_Input.place(x=50, y=110)
                self.Departure_Date_Title.place(x=50, y=150)
                self.Departure_Date_Input.place(x=50, y=180)
                self.Departure_Time_Title.place(x=50, y=220)
                self.Departure_Time_Input.place(x=50, y=250)
                self.Arrival_Title.place(x=350, y=80)
                self.Arrival_Input.place(x=350, y=110)
                self.Arrival_Date_Title.place(x=350, y=150)
                self.Arrival_Date_Input.place(x=350, y=180)
                self.Arrival_Time_Title.place(x=350, y=220)
                self.Arrival_Time_Input.place(x=350, y=250)
                self.Seats_Title.place(x=600, y=80)
                self.Seats_Input.place(x=600, y=110)
                self.Economy_Title.place(x=600, y=150)
                self.Economy_Input.place(x=600, y=180)
                self.Business_Title.place(x=600, y=220)
                self.Business_Input.place(x=600, y=250)
                self.First_Title.place(x=600, y=290)
                self.First_Input.place(x=600, y=320)
                self.Add_Image_Flight_Button.place(x=50, y=310)
                self.Price_Title.place(x=50, y=360)
                self.Price_Input.place(x=50, y=390)
                self.Discount_Title.place(x=350, y=360)
                self.Discount_Input.place(x=350, y=390)
                self.Create_Button.place(x=600, y=380)
                #self.Info_Title.place(x=600, y=440)
                self.Info_Discount.place(x=350, y=440)

            elif Actual_Customer.Page==1:
                if Actual_Customer.AdminFlight=="":
                    #Titles 
                    self.Serach_Flight_Title = tk.Label(self.rest_right_frame, text="Search Flight", font=("Arial", 13), bg=main_color, fg=fourth_color)
                    self.FLight_Number_Title = tk.Label(self.rest_right_frame, text=" Flight Number", font=("Arial", 10), bg=main_color, fg=fourth_color)
                    #Entry
                    self.Search_Flight_Input = tk.Entry(self.rest_right_frame)
                    #Button
                    self.Search_Flight_Button = tk.Button(self.rest_right_frame, text='Search', command=self.Search_Flight, bg=third_color, fg=main_color, width=15, height=2)
                    #Display Stuff
                    self.Serach_Flight_Title.place(x=50, y=40)
                    self.FLight_Number_Title.place(x=50, y=140)
                    self.Search_Flight_Input.place(x=50, y=170)
                    self.Search_Flight_Button.place(x=350, y=150)
                else :
                    sql = "SELECT * FROM Flight WHERE FlightNumber = '{}';".format(Actual_Customer.AdminFlight)
                    self.Search_Flight_Result =dbconnect.DBHelper().fetch(sql)
                    if self.Search_Flight_Result==None:
                        self.No_Flight_Title = tk.Label(self.rest_right_frame, text="No Flight Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
                        self.Info_Noo_Flight = tk.Label(self.rest_right_frame, text="Unfortunately it seems that you have no Flights.", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.No_Flight_Title.place(x=50, y=40)
                        self.Info_Noo_Flight.place(x=50, y=80)
                    else:
                        #Titles 
                        self.Create_Flight_Title = tk.Label(self.rest_right_frame, text="Manage Flight "+str(self.Search_Flight_Result[0]['FlightNumber']), font=("Arial", 13), bg=main_color, fg=fourth_color)
                        self.Departure_Title = tk.Label(self.rest_right_frame, text=" Departure", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Departure_Date_Title = tk.Label(self.rest_right_frame, text=" Departure Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Departure_Time_Title = tk.Label(self.rest_right_frame, text=" Departure Time", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Arrival_Title = tk.Label(self.rest_right_frame, text=" Arrival", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Arrival_Date_Title = tk.Label(self.rest_right_frame, text=" Arrival Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Arrival_Time_Title = tk.Label(self.rest_right_frame, text=" Arrival Time", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Price_Title = tk.Label(self.rest_right_frame, text=" Price (Adulte)", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Discount_Title = tk.Label(self.rest_right_frame, text=" Discount", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Seats_Title = tk.Label(self.rest_right_frame, text=" Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Economy_Title = tk.Label(self.rest_right_frame, text=" Economy Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Business_Title = tk.Label(self.rest_right_frame, text=" Business Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.First_Title = tk.Label(self.rest_right_frame, text=" First Seats", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Info_Title = tk.Label(self.rest_right_frame, text="Please fill all the fields", font=("Arial", 8), bg=main_color, fg=fourth_color)
                        self.Image_Flight_Title = tk.Label(self.rest_right_frame, text="Flight's Image", font=("Arial", 13), bg=main_color, fg=fourth_color)
                        #Entries
                        self.Departure_Input = tk.Entry(self.rest_right_frame)
                        self.Departure_Input.insert(0, self.Search_Flight_Result[0]['Departure'])
                        self.Departure_Date_Input = DateEntry(self.rest_right_frame, date_pattern='y-mm-dd')
                        self.Departure_Date_Input.delete(0, tk.END)
                        self.Departure_Date_Input.insert(0, self.Search_Flight_Result[0]['DepartureDate'])
                        self.Departure_Time_Input = ttk.Combobox(self.rest_right_frame, values=["00:00:00", "01:00:00", "02:00:00", "03:00:00", "04:00:00", "05:00:00", "06:00:00","07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00", "12:00:00","13:00:00", "14:00:00", "15:00:00", "16:00:00", "17:00:00", "18:00:00","19:00:00", "20:00:00", "21:00:00", "22:00:00", "23:00:00"])
                        self.Departure_Time_Input.delete(0, tk.END)
                        self.Departure_Time_Input.insert(0, self.Search_Flight_Result[0]['DepartureTime'])
                        #self.Departure_Time_Input = DateEntry(self.rest_right_frame, time_pattern='HH:mm')
                        self.Arrival_Input = tk.Entry(self.rest_right_frame)
                        self.Arrival_Input.insert(0, self.Search_Flight_Result[0]['Arrival'])
                        self.Arrival_Date_Input = DateEntry(self.rest_right_frame, date_pattern='y-mm-dd')
                        self.Arrival_Date_Input.delete(0, tk.END)
                        self.Arrival_Date_Input.insert(0, self.Search_Flight_Result[0]['ArrivalDate'])
                        self.Arrival_Time_Input = ttk.Combobox(self.rest_right_frame, values=["00:00:00, 01:00:00", "02:00:00", "03:00:00", "04:00:00", "05:00:00", "06:00:00","07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00", "12:00:00","13:00:00", "14:00:00", "15:00:00", "16:00:00", "17:00:00", "18:00:00","19:00:00", "20:00:00", "21:00:00", "22:00:00", "23:00:00"])
                        self.Arrival_Time_Input.delete(0, tk.END)
                        self.Arrival_Time_Input.insert(0, self.Search_Flight_Result[0]['ArrivalTime'])
                        #self.Arrival_Time_Input = DateEntry(self.rest_right_frame, time_pattern='HH:mm')
                        self.Price_Input = tk.Entry(self.rest_right_frame)
                        self.Price_Input.insert(0, int(self.Search_Flight_Result[0]['Price']))
                        self.Seats_Input = tk.Entry(self.rest_right_frame)
                        self.Seats_Input.insert(0, self.Search_Flight_Result[0]['Seats'])
                        self.Discount_Input = tk.Entry(self.rest_right_frame)
                        self.Discount_Input.insert(0, int(self.Search_Flight_Result[0]['Discount']))
                        self.Economy_Input = tk.Entry(self.rest_right_frame)
                        self.Economy_Input.insert(0, int(self.Search_Flight_Result[0]['Eco']))
                        self.Business_Input = tk.Entry(self.rest_right_frame)
                        self.Business_Input.insert(0, int(self.Search_Flight_Result[0]['Business']))
                        self.First_Input = tk.Entry(self.rest_right_frame)
                        self.First_Input.insert(0, int(self.Search_Flight_Result[0]['First']))
                        self.Image_Flight_Input = tk.Entry(self.rest_right_frame)
                        #Button
                        self.Save_Button = tk.Button(self.rest_right_frame, text='Save', command=self.Save_Flight, bg=third_color, fg=main_color, width=15, height=2)
                        self.Delete_Button = tk.Button(self.rest_right_frame, text='Delete', command=self.Delete_Flight, bg=second_color, fg=main_color, width=15, height=2)
                        self.Add_Image_Flight_Button = tk.Button(self.rest_right_frame, text='Add Image', command=self.Add_Image_Flight, bg=third_color, fg=main_color, width=15, height=1)
                        #Usless var here
                        self.Image_Flight_Check = False
                        #Display Stuff
                        self.Create_Flight_Title.place(x=50, y=20)
                        self.Departure_Title.place(x=50, y=80)
                        self.Departure_Input.place(x=50, y=110)
                        self.Departure_Date_Title.place(x=50, y=150)
                        self.Departure_Date_Input.place(x=50, y=180)
                        self.Departure_Time_Title.place(x=50, y=220)
                        self.Departure_Time_Input.place(x=50, y=250)
                        self.Arrival_Title.place(x=350, y=80)
                        self.Arrival_Input.place(x=350, y=110)
                        self.Arrival_Date_Title.place(x=350, y=150)
                        self.Arrival_Date_Input.place(x=350, y=180)
                        self.Arrival_Time_Title.place(x=350, y=220)
                        self.Arrival_Time_Input.place(x=350, y=250)
                        self.Seats_Title.place(x=600, y=80)
                        self.Seats_Input.place(x=600, y=110)
                        self.Economy_Title.place(x=600, y=150)
                        self.Economy_Input.place(x=600, y=180)
                        self.Business_Title.place(x=600, y=220)
                        self.Business_Input.place(x=600, y=250)
                        self.First_Title.place(x=600, y=290)
                        self.First_Input.place(x=600, y=320)
                        self.Add_Image_Flight_Button.place(x=50, y=310)
                        self.Price_Title.place(x=50, y=360)
                        self.Price_Input.place(x=50, y=390)
                        self.Discount_Title.place(x=350, y=360)
                        self.Discount_Input.place(x=350, y=390)
                        self.Save_Button.place(x=600, y=380)
                        self.Delete_Button.place(x=600, y=20)
                        
            
            elif Actual_Customer.Page==2:
                #Titles 
                self.Personal_Info_Title = tk.Label(self.rest_right_frame, text="Personal Information", font=("Arial", 13), bg=main_color, fg=fourth_color)
                self.First_Name_Title = tk.Label(self.rest_right_frame, text=" First Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Last_Name_Title = tk.Label(self.rest_right_frame, text=" Last Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.User_Name_Title = tk.Label(self.rest_right_frame, text=" User Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Email_Title = tk.Label(self.rest_right_frame, text=" Email", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Phone_Title = tk.Label(self.rest_right_frame, text=" Phone", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Password_Title = tk.Label(self.rest_right_frame, text="Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Confirm_Password_Title = tk.Label(self.rest_right_frame, text=" Confirm Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Admin_Title = tk.Label(self.rest_right_frame, text="Admin", font=("Arial", 10), bg=main_color, fg=fourth_color)
                #Entries
                self.First_Name_Input = tk.Entry(self.rest_right_frame)
                self.Last_Name_Input = tk.Entry(self.rest_right_frame)
                self.User_Name_Input = tk.Entry(self.rest_right_frame)
                self.Email_Input = tk.Entry(self.rest_right_frame)
                self.Phone_Input = tk.Entry(self.rest_right_frame)
                self.Password_Input = tk.Entry(self.rest_right_frame)
                self.Confirm_Password_Input = tk.Entry(self.rest_right_frame, show="*")
                self.Admin_Input = ttk.Combobox(self.rest_right_frame, values=["Yes", "No"])
                #Button
                self.Create_Button = tk.Button(self.rest_right_frame, text='Create', command=self.Create_Customer, bg=third_color, fg=main_color, width=15, height=2)
                
                #Display Stuff
                self.Personal_Info_Title.place(x=50, y=40)
                self.First_Name_Title.place(x=50, y=100)
                self.First_Name_Input.place(x=50, y=130)
                self.Last_Name_Title.place(x=50, y=170)
                self.Last_Name_Input.place(x=50, y=200)
                self.User_Name_Title.place(x=50, y=240)
                self.User_Name_Input.place(x=50, y=270)
                self.Email_Title.place(x=50, y=310)
                self.Email_Input.place(x=50, y=340)
                self.Phone_Title.place(x=50, y=380)
                self.Phone_Input.place(x=50, y=410)
                self.Password_Title.place(x=350, y=100)
                self.Password_Input.place(x=350, y=130)
                self.Confirm_Password_Title.place(x=350, y=170)
                self.Confirm_Password_Input.place(x=350, y=200)
                self.Admin_Title.place(x=350, y=260)
                self.Admin_Input.place(x=350, y=290)
                self.Create_Button.place(x=600, y=130)

            elif Actual_Customer.Page==3:
                if Actual_Customer.AdminCustomer==0:
                    #Titles
                    self.Serach_Customer_Title = tk.Label(self.rest_right_frame, text="Search Customer", font=("Arial", 13), bg=main_color, fg=fourth_color)
                    self.Customer_ID_Title = tk.Label(self.rest_right_frame, text=" Customer ID", font=("Arial", 10), bg=main_color, fg=fourth_color)
                    #Entry
                    self.Search_Customer_Input = tk.Entry(self.rest_right_frame)
                    #Button
                    self.Search_Customer_Button = tk.Button(self.rest_right_frame, text='Search', command=self.Search_Customer, bg=third_color, fg=main_color, width=15, height=2)
                    #Display Stuff
                    self.Serach_Customer_Title.place(x=50, y=40)
                    self.Customer_ID_Title.place(x=50, y=140)
                    self.Search_Customer_Input.place(x=50, y=170)
                    self.Search_Customer_Button.place(x=350, y=150)
                else :
                    sql = "SELECT * FROM Customer WHERE CustomerID = '{}';".format(Actual_Customer.AdminCustomer)
                    self.Search_Customer_Result =dbconnect.DBHelper().fetch(sql)
                    if self.Search_Customer_Result==None:
                        self.No_Customer_Title = tk.Label(self.rest_right_frame, text="No Customer Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
                        self.Info_Noo_Customer = tk.Label(self.rest_right_frame, text="Unfortunately it seems that you have no Customers.", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.No_Customer_Title.place(x=50, y=40)
                        self.Info_Noo_Customer.place(x=50, y=80)
                    else:
                        #Titles 
                        self.Personal_Info_Title = tk.Label(self.rest_right_frame, text=str(self.Search_Customer_Result[0]['FirstName'])+"Information", font=("Arial", 13), bg=main_color, fg=fourth_color)
                        self.First_Name_Title = tk.Label(self.rest_right_frame, text=" First Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Last_Name_Title = tk.Label(self.rest_right_frame, text=" Last Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.User_Name_Title = tk.Label(self.rest_right_frame, text=" User Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Email_Title = tk.Label(self.rest_right_frame, text=" Email", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Phone_Title = tk.Label(self.rest_right_frame, text=" Phone", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Old_Password_Title = tk.Label(self.rest_right_frame, text="Old Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Password_Title = tk.Label(self.rest_right_frame, text="Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Confirm_Password_Title = tk.Label(self.rest_right_frame, text=" Confirm Password", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.Admin_Title = tk.Label(self.rest_right_frame, text="Admin", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        #Entries
                        self.First_Name_Input = tk.Entry(self.rest_right_frame)
                        self.First_Name_Input.insert(0, self.Search_Customer_Result[0]['FirstName'])
                        self.Last_Name_Input = tk.Entry(self.rest_right_frame)
                        self.Last_Name_Input.insert(0, self.Search_Customer_Result[0]['LastName'])
                        self.User_Name_Input = tk.Entry(self.rest_right_frame)
                        self.User_Name_Input.insert(0,  self.Search_Customer_Result[0]['UserName'])
                        self.Email_Input = tk.Entry(self.rest_right_frame)
                        self.Email_Input.insert(0, self.Search_Customer_Result[0]['Email'])
                        self.Phone_Input = tk.Entry(self.rest_right_frame)
                        self.Phone_Input.insert(0, int(self.Search_Customer_Result[0]['Phone']))
                        self.Old_Password_Input = tk.Entry(self.rest_right_frame, show="*")
                        self.Old_Password_Input.insert(0, self.Search_Customer_Result[0]['Password'])
                        self.Password_Input = tk.Entry(self.rest_right_frame)
                        self.Confirm_Password_Input = tk.Entry(self.rest_right_frame, show="*")
                        self.Admin_Input = ttk.Combobox(self.rest_right_frame, values=["Yes", "No"])
                        if self.Search_Customer_Result[0]['AdminOrNot']==1:
                            self.Admin_Input.insert(0, "Yes")
                        else:
                            self.Admin_Input.insert(0, "No")
                        #Button
                        self.Save_Button = tk.Button(self.rest_right_frame, text='Save', command=self.Save_Customer, bg=third_color, fg=main_color, width=15, height=2)
                        self.Delete_Button = tk.Button(self.rest_right_frame, text='Delete Account', command=self.Delete_Customer, bg=second_color, fg=main_color, width=15, height=2)
                        
                        #Display Stuff
                        self.Personal_Info_Title.place(x=50, y=40)
                        self.First_Name_Title.place(x=50, y=100)
                        self.First_Name_Input.place(x=50, y=130)
                        self.Last_Name_Title.place(x=50, y=170)
                        self.Last_Name_Input.place(x=50, y=200)
                        self.User_Name_Title.place(x=50, y=240)
                        self.User_Name_Input.place(x=50, y=270)
                        self.Email_Title.place(x=50, y=310)
                        self.Email_Input.place(x=50, y=340)
                        self.Phone_Title.place(x=50, y=380)
                        self.Phone_Input.place(x=50, y=410)
                        self.Old_Password_Title.place(x=350, y=100)
                        self.Old_Password_Input.place(x=350, y=130)
                        self.Password_Title.place(x=350, y=170)
                        self.Password_Input.place(x=350, y=200)
                        self.Confirm_Password_Title.place(x=350, y=240)
                        self.Confirm_Password_Input.place(x=350, y=270)
                        self.Admin_Title.place(x=350, y=310)
                        self.Admin_Input.place(x=350, y=340)
                        self.Save_Button.place(x=600, y=130)
                        self.Delete_Button.place(x=600, y=200)


            elif Actual_Customer.Page==4:
                self.scroll_canva = tk.Canvas(self.rest_right_frame, bd=0, highlightthickness=0, bg=main_color)
                self.yscrollbar = tk.Scrollbar(self.rest_right_frame, orient="vertical", command=self.scroll_canva.yview)
                self.yscrollbar.pack(side=tk.RIGHT, fill='y')
                self.scroll_canva.configure(yscrollcommand=self.yscrollbar.set)

                self.display_frame = tk.Frame(self.scroll_canva, bg=main_color)
                self.display_frame.bind("<Configure>", lambda e: self.scroll_canva.configure(scrollregion=self.scroll_canva.bbox("all")))
                self.scroll_canva.create_window((0, 0), window=self.display_frame, anchor="nw")

                self.top_display_frame = tk.Frame(self.display_frame, bg=main_color, height=100)
                self.top_display_frame.columnconfigure(0, weight=1)
                self.top_display_frame.columnconfigure(1, weight=1)
                self.top_display_frame.columnconfigure(2, weight=1)
                self.top_display_frame.columnconfigure(3, weight=1)
                self.bottom_display_frame = tk.Frame(self.display_frame, bg=main_color)
                self.top_display_frame.pack(side=tk.TOP, fill=tk.X)
                self.bottom_display_frame.pack(side=tk.TOP, fill=tk.X)

                #self.scroll_canva.create_window((0,0), window=self.display_frame, anchor="nw")
                self.scroll_canva.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                
                self.Begin_Date_Title = tk.Label(self.top_display_frame, text="Begin Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.End_Date_Title = tk.Label(self.top_display_frame, text="End Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
                #Inputs
                self.Begin_Date_Input = DateEntry(self.top_display_frame, date_pattern='y-mm-dd')
                self.End_Date_Input = DateEntry(self.top_display_frame, date_pattern='y-mm-dd')
                if Actual_Customer.AdminDateBegin==None:
                    self.Begin_Date_Input.delete(0, tk.END)
                    self.Begin_Date_Input.insert(0, datetime.date.today())
                    self.End_Date_Input.delete(0, tk.END)
                    self.End_Date_Input.insert(0, datetime.date.today() + datetime.timedelta(days=1))
                else:
                    self.Begin_Date_Input.delete(0, tk.END)
                    self.Begin_Date_Input.insert(0, Actual_Customer.AdminDateBegin)
                    self.End_Date_Input.delete(0, tk.END)
                    self.End_Date_Input.insert(0, Actual_Customer.AdminDateEnd)
                #Button 
                self.Analyse_Button = tk.Button(self.top_display_frame, text='Analyse', command=self.Analyse, bg=third_color, fg=main_color, width=15, height=2)
                #Display Stuff
                self.Begin_Date_Title.grid(row=0, column=0, padx=10, pady=5)
                self.Begin_Date_Input.grid(row=1, column=0, padx=10, pady=5)
                self.End_Date_Title.grid(row=0, column=1, padx=10, pady=5)
                self.End_Date_Input.grid(row=1, column=1, padx=10, pady=5)
                self.Analyse_Button.grid(row=1, column=3, padx=10, pady=5)
                #Space after the plot
                self.Space=tk.Label(self.bottom_display_frame, text=" ", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Space.pack(side=tk.TOP)
                if Actual_Customer.AdminDateBegin==None:
                    self.Analyse()
                sqlHCity="SELECT Arrival, COUNT(*) FROM flight WHERE ArrivalDate>'{}' AND ArrivalDate<'{}' GROUP BY Arrival;".format(Actual_Customer.AdminDateBegin, Actual_Customer.AdminDateEnd)
                HCity=dbconnect.DBHelper().fetch(sqlHCity)
                Arrive=[]
                NumberArrive=[]
                for i in HCity:
                    Arrive.append(i['Arrival'])  # Use the key 'Arrival'
                    NumberArrive.append(i['COUNT(*)'])  # Use the key 'COUNT(*)'
                #maxNumberHC = max(NumberArrive + [0]) + 5
                # Create and display the first plot
                title = "Arrival Statistics"
                xlabel = "Arrival"
                ylabel = "Number of Flights"
                self.create_plot(Arrive, NumberArrive, title, xlabel, ylabel, 'histogram', (700, 450))
    
                sqlDCity="SELECT Departure, COUNT(*) FROM flight WHERE DepartureDate>'{}' AND DepartureDate<'{}' GROUP BY Departure;".format(Actual_Customer.AdminDateBegin, Actual_Customer.AdminDateEnd)
                DCity=dbconnect.DBHelper().fetch(sqlDCity)
                Depart=[]
                NumberDepart=[]
                for i in DCity:
                    Depart.append(i['Departure'])
                    NumberDepart.append(i['COUNT(*)'])
                #maxNumberDC = max(NumberDepart)+5
                title = "Departure Statistics"
                xlabel = "Departure"
                ylabel = "Number of Flights"
                self.create_plot(Depart, NumberDepart, title, xlabel, ylabel, 'histogram', (700, 450))

                sqlLON = """SELECT CASE WHEN CustomerID = 0 THEN 'Without Account' ELSE 'With Account' END AS GroupedCustomerID,
                        COUNT(*) 
                    FROM 
                        Reservations 
                    WHERE 
                        ReservationDate > '{}' AND ReservationDate < '{}' 
                    GROUP BY 
                        GroupedCustomerID;""".format(Actual_Customer.AdminDateBegin, Actual_Customer.AdminDateEnd)
                LON=dbconnect.DBHelper().fetch(sqlLON)
                LONCategory=[]
                LONNumber=[]
                for i in LON:
                    LONCategory.append(i['GroupedCustomerID'])
                    LONNumber.append(i['COUNT(*)'])
                title = "Reservation Statistics"
                xlabel = "Reservation"
                ylabel = "Number of Reservations"
                self.create_plot(LONCategory, LONNumber, title, xlabel, ylabel, 'histogram', (700, 450))
                #Stat Flight per day 
                sqlFPD = """SELECT DepartureDate, COUNT(*)
                        FROM Flight
                        WHERE DepartureDate > '{}' AND DepartureDate < '{}'
                        GROUP BY DepartureDate;""".format(Actual_Customer.AdminDateBegin, Actual_Customer.AdminDateEnd)
                FPD=dbconnect.DBHelper().fetch(sqlFPD)
                FPDDate=[]
                FPDNumber=[]
                for i in FPD:
                    FPDDate.append(i['DepartureDate'])
                    FPDNumber.append(i['COUNT(*)'])
                title = "Flight per day"
                xlabel = "Date"
                ylabel = "Number of Flights"
                self.create_plot(FPDDate, FPDNumber, title, xlabel, ylabel, 'line', (700, 450))
                #Stat Reservation per day
                sqlRPD = """SELECT ReservationDate, COUNT(*)
                        FROM Reservations
                        WHERE ReservationDate > '{}' AND ReservationDate < '{}'
                        GROUP BY ReservationDate;""".format(Actual_Customer.AdminDateBegin, Actual_Customer.AdminDateEnd)
                RPD=dbconnect.DBHelper().fetch(sqlRPD)
                RPDDate=[]
                RPDNumber=[]
                for i in RPD:
                    RPDDate.append(i['ReservationDate'])
                    RPDNumber.append(i['COUNT(*)'])
                title = "Reservation per day"
                xlabel = "Date"
                ylabel = "Number of Reservations"
                self.create_plot(RPDDate, RPDNumber, title, xlabel, ylabel, 'line', (700, 450))
                #Money Eared per day
                sqlMPD = """SELECT ReservationDate, SUM(Price)
                        FROM Reservations
                        WHERE ReservationDate > '{}' AND ReservationDate < '{}'
                        GROUP BY ReservationDate;""".format(Actual_Customer.AdminDateBegin, Actual_Customer.AdminDateEnd)
                MPD=dbconnect.DBHelper().fetch(sqlMPD)
                MPDDate=[]
                MPDNumber=[]
                for i in MPD:
                    MPDDate.append(i['ReservationDate'])
                    MPDNumber.append(i['SUM(Price)'])
                title = "Money Earned per day"
                xlabel = "Date"
                ylabel = "Money Earned"
                self.create_plot(MPDDate, MPDNumber, title, xlabel, ylabel, 'line', (700, 450))

    def Hide_Button(self, empty):
        plt.close('all')
        Launch_Home_Page()

    def Hide_Button_1(self, empty):
        plt.close('all')
        Launch_Basket_Page()

    def UpComFlights(self, empty):
        Actual_Customer.Page=0
        plt.close('all')
        Launch_My_Account()
    
    def PastFlights(self, empty):
        Actual_Customer.Page=1
        plt.close('all')
        Launch_My_Account()
    
    def Settings(self, empty):
        Actual_Customer.Page=2
        plt.close('all')
        Launch_My_Account()
    
    def Cards(self, empty):
        Actual_Customer.Page=3
        plt.close('all')
        Launch_My_Account()
    
    def Statistics(self, empty):
        Actual_Customer.Page=4
        plt.close('all')
        Launch_My_Account()

    #--------Customer---------#
    def Save(self):
        self.FirstName=self.First_Name_Input.get()
        self.LastName=self.Last_Name_Input.get()
        self.UserName=self.User_Name_Input.get()
        self.Email=self.Email_Input.get()
        self.Phone=self.Phone_Input.get()
        self.Old_Password=self.Old_Password_Input.get()
        self.New_Password=self.New_Password_Input.get()
        self.Confirm_Password=self.Confirm_Password_Input.get()
        if (self.FirstName=='') or (self.LastName=='') or (self.UserName=='') or (self.Email=='') or (self.Phone=='') :
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif not re.match(r'^[0-9]*$', self.Phone):
            # Invalid phone format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid phone format')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', self.Email):
            # Invalid email format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid email format')
        if (self.Old_Password!='') or ((self.New_Password!='') or (self.Confirm_Password!='')):
            if (self.Old_Password=='') or (self.New_Password=='') or (self.Confirm_Password==''):
                tk.messagebox.showinfo('Error', 'Please fill in all the information for the password')
            elif self.New_Password!=self.Confirm_Password:
                tk.messagebox.showinfo('Error', 'The new password and the confirmation password are not the same')
            elif self.Old_Password!=Actual_Customer.Password:
                tk.messagebox.showinfo('Error', 'The old password is incorrect')
            else : 
                Actual_Customer.Change_Actual_Customer(self.Email, self.New_Password, self.FirstName, self.LastName, self.UserName,  self.Phone, Actual_Customer.ProfilePicture)
                Launch_My_Account()
        else :
            Actual_Customer.Change_Actual_Customer(self.Email, Actual_Customer.Password, self.FirstName, self.LastName, self.UserName,  self.Phone, Actual_Customer.ProfilePicture)
            Launch_My_Account()
    
    def Delete_Account(self):
        response = tk.messagebox.askquestion('Warning', 'Are you sure you want to delete your account?', icon='warning')
        if response == 'yes':
            Actual_Customer.Delete_Customer(Actual_Customer.CustomerID)
            Launch_Home_Page()
            print("Delete Account")
        else:
            print("Account deletion canceled")

    def Disconnect(self):
        Actual_Customer.Disconnect()
        Launch_Home_Page()

    def Save_Card(self):
        self.CardNumber=self.Card_Number.get()
        self.CardDate=self.Card_Date.get()
        self.CardCode=self.Card_Code.get()
        self.CardName=self.Card_Name.get()
        if (self.CardNumber=='') or (self.CardDate=='') or (self.CardCode=='') or (self.CardName=='') :
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        else:
            if (self.CardNumber!="")&(self.CardDate!="")&(self.CardCode!="")&(self.CardName!=""):
                if(int(self.CardNumber)>999999999999999)&(int(self.CardNumber)<10000000000000000):
                    if(int(self.CardCode)>99)&(int(self.CardCode)<1000):
                        Actual_Customer.Add_Card(self.CardNumber, self.CardName, self.CardDate, self.CardCode)
                        Launch_My_Account()
                    else :
                        #message box 
                        tk.messagebox.showerror("Error", "Please enter a valid card code")
                else :
                    #message box 
                    tk.messagebox.showerror("Error", "Please enter a valid Card Number")
            else :
                #message box 
                tk.messagebox.showerror("Error", "Please fill all the inputs")

    def Change_Profile_Picture(self):
        chemin_image = filedialog.askopenfilename(title="Open your file", filetypes=[('image files', '.png'), ('image files', '.jpg'), ('image files', '.jpeg')])
        image = Image.open(chemin_image)
        image = image.resize((128, 128))

        # Crop the image into a circular shape
        mask = Image.new("L", (128, 128), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (128, 128), fill=255)
        image = Image.composite(image, Image.new('RGB', image.size, main_color), mask)

        # Generate a random name for the image file
        random_name = str(uuid.uuid4())
        image_path = f"./pp/{random_name}.png"
        #save it
        image.save(image_path)  # Save the resized image with the random name
        image = ImageTk.PhotoImage(image)
        #encode the image
        encode_image = base64.b64encode(open(image_path, 'rb').read())
        #send to the database
        #sqlPP = "UPDATE Customer SET ProfilePicture = '{}' WHERE CustomerID = '{}';".format(encode_image, Actual_Customer.CustomerID)
        sqlPP = "UPDATE Customer SET ProfilePicture = %s WHERE CustomerID = %s" 
        values = (encode_image, Actual_Customer.CustomerID)
        dbconnect.DBHelper().execute_row(sqlPP, values)
        Actual_Customer.ProfilePicture = encode_image
        Launch_My_Account()
        

    # Inclure l'image dans la base de données (exemple pour MySQL)

    #--------Admin---------#
    def Admin_Page(self):
        if Actual_Customer.AdminOrNot == True:
            if Actual_Customer.AdminPage==False: Actual_Customer.AdminPage=True
            elif Actual_Customer.AdminPage==True: Actual_Customer.AdminPage=False
            Actual_Customer.Page=0
            Launch_My_Account()

    def Create_Flight(self):
        self.Departure=self.Departure_Input.get()
        self.Departure_Date=self.Departure_Date_Input.get()
        self.Departure_Time=datetime.datetime.strptime(self.Departure_Time_Input.get(), '%H:%M').time()
        self.Arrival=self.Arrival_Input.get()
        self.Arrival_Date=self.Arrival_Date_Input.get()
        self.Arrival_Time=datetime.datetime.strptime(self.Arrival_Time_Input.get(), '%H:%M').time()
        self.Price_F=int(self.Price_Input.get())
        self.Discount=int(self.Discount_Input.get())
        self.Seats=int(self.Seats_Input.get())
        self.Economy=int(self.Economy_Input.get())
        self.Business=int(self.Business_Input.get())
        self.First=int(self.First_Input.get())
        # Duration
        departure_datetime = datetime.datetime.strptime(f"{self.Departure_Date} {self.Departure_Time}", '%Y-%m-%d %H:%M:%S')
        arrival_datetime = datetime.datetime.strptime(f"{self.Arrival_Date} {self.Arrival_Time}", '%Y-%m-%d %H:%M:%S')
        self.Duration = arrival_datetime - departure_datetime
    
        if (self.Departure=='') or (self.Departure_Date=='') or (self.Departure_Time=='') or (self.Arrival=='') or (self.Arrival_Date=='') or (self.Arrival_Time=='') or (self.Price_F==0) or (self.Seats==0) or ((self.Economy==0) and (self.Business==0) and (self.First==0)):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif self.Departure_Date>self.Arrival_Date:
            tk.messagebox.showinfo('Error', 'The arrival date must be after the departure date')
        elif datetime.datetime.strptime(self.Departure_Date, '%Y-%m-%d') < datetime.datetime.now() or datetime.datetime.strptime(self.Arrival_Date, '%Y-%m-%d') < datetime.datetime.now():
            tk.messagebox.showinfo('Error', 'The departure or Arrival date must be after or today')
        elif self.Price_F<=0:
            tk.messagebox.showinfo('Error', 'The price must be positive')
        elif self.Discount<0 or self.Discount>100:
            tk.messagebox.showinfo('Error', 'The discount must be between 0 and 100')
        elif self.Economy+self.Business+self.First<=0 or self.Economy+self.Business+self.First!=self.Seats:
            tk.messagebox.showinfo('Error', 'The number of seats for classes must be positive and equal to the total number of seats')
        elif self.Economy<0 or self.Business<0 or self.First<0:
            tk.messagebox.showinfo('Error', 'The number of seats for classes must be positive')
        elif len(self.Departure) <2 or len(self.Departure) >30 or not self.Departure.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid Departure format')
        elif len(self.Arrival) <2 or len(self.Arrival) >30 or not self.Arrival.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid Arrival format')
        elif self.Image_Flight_Check==False:
            tk.messagebox.showinfo('Error', 'Please add an image for the flight')
        else:
            self.Discount=self.Discount/100
            Actual_Outbound_Flight.Create_Flight(self.Departure, self.Departure_Date, self.Departure_Time, self.Arrival, self.Arrival_Date, self.Arrival_Time, self.Duration, self.Price_F, self.Discount, self.Seats, self.Economy, self.Business, self.First)
            tk.messagebox.showinfo('Succeed', 'Flight has been created')
            self.Image_Flight_Check=False
            Launch_My_Account()

    def Create_Customer(self):
        self.FirstName=self.First_Name_Input.get()
        self.LastName=self.Last_Name_Input.get()
        self.UserName=self.User_Name_Input.get()
        self.Email=self.Email_Input.get()
        self.Phone=self.Phone_Input.get()
        self.Password=self.Password_Input.get()
        self.Confirm_Password=self.Confirm_Password_Input.get()
        self.Admin=self.Admin_Input.get()
        if self.Admin=="Yes": self.Admin=1
        else: self.Admin=0
        if (self.FirstName=='') or (self.LastName=='') or (self.UserName=='') or (self.Email=='') or (self.Phone=='') or (self.Password=='') or (self.Confirm_Password==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif not re.match(r'^[0-9]*$', self.Phone):
            # Invalid phone format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid phone format')
        elif not re.match(r'^[\w\.-]+@[\w\.-]+$', self.Email):
            # Invalid email format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid email format')
        elif self.Password!=self.Confirm_Password:
            tk.messagebox.showinfo('Error', 'The password and the confirmation password are not the same')
        elif self.Admin!=1 and self.Admin!=0:
            tk.messagebox.showinfo('Error', 'Please choose if the customer is an admin or not')
        elif len(self.FirstName) <2 or len(self.FirstName) >30 or not self.FirstName.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid First Name format')
        elif len(self.LastName) <2 or len(self.LastName) >30 or not self.LastName.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid Last Name format')
        elif len(self.UserName) <2 or len(self.UserName) >30 or not self.UserName.isalnum():
            tk.messagebox.showinfo('Error', 'Invalid User Name format')
        else:
            res=Actual_Customer.Create_Customer(self.Email, self.Password, self.FirstName, self.LastName, self.UserName,  self.Phone, self.Admin)
            if res=="Email":
                tk.messagebox.showinfo('Error', 'The email already exist')
            elif res=="UserName":
                tk.messagebox.showinfo('Error', 'The username already exist')
            elif res=="Phone":
                tk.messagebox.showinfo('Error', 'The phone already exist')
            elif res=="Succeed":
                tk.messagebox.showinfo('Succeed', 'Customer has been created')
                Launch_My_Account()
            else : 
                tk.messagebox.showinfo('Error', 'Sorry, an error occured')
    
    def Add_Image_Flight(self):
        Arrival=self.Arrival_Input.get().replace(" ", "_")
        if Arrival=='':
            tk.messagebox.showinfo('Error', 'Please enter first the arrival')
        else :
            chemin_image = filedialog.askopenfilename(title="Open your file", filetypes=[('image files', '.png'), ('image files', '.jpg'), ('image files', '.jpeg')])
            image = Image.open(chemin_image)
            image = image.resize((320, 180))
            # Generate a random name for the image file
            image_path = f"./images/Flights_Images/{Arrival}.png"
            #save it
            image.save(image_path)
            self.Image_Flight_Check=True

    def Search_Flight(self):
        self.Search=self.Search_Flight_Input.get()
        if self.Search=='':
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif len(self.Search) != 6 or not self.Search[:3].isalpha() or not self.Search[3:].isdigit():
            tk.messagebox.showinfo('Error', 'Invalid Search format')
        else:
            sql = "SELECT COUNT(*) AS Here FROM Flight WHERE FlightNumber = '{}';".format(self.Search)
            Here = dbconnect.DBHelper().fetch(sql)[0]['Here']
            if Here == 0:
                tk.messagebox.showinfo('Error', 'The flight does not exist')
            else:
                Actual_Customer.AdminFlight=self.Search
                Launch_My_Account()
    
    def Save_Flight(self):
        self.Departure=self.Departure_Input.get()
        self.Departure_Date=self.Departure_Date_Input.get()
        self.Departure_Time=datetime.datetime.strptime(self.Departure_Time_Input.get(), '%H:%M:%S').time()
        self.Arrival=self.Arrival_Input.get()
        self.Arrival_Date=self.Arrival_Date_Input.get()
        self.Arrival_Time=datetime.datetime.strptime(self.Arrival_Time_Input.get(), '%H:%M:%S').time()
        self.Price_F=int(self.Price_Input.get())
        print("Price_F : ", self.Price_F)
        self.Discount=int(self.Discount_Input.get())
        self.Seats=int(self.Seats_Input.get())
        self.Economy=int(self.Economy_Input.get())
        self.Business=int(self.Business_Input.get())
        self.First=int(self.First_Input.get())
        # Duration
        departure_datetime = datetime.datetime.strptime(f"{self.Departure_Date} {self.Departure_Time}", '%Y-%m-%d %H:%M:%S')
        arrival_datetime = datetime.datetime.strptime(f"{self.Arrival_Date} {self.Arrival_Time}", '%Y-%m-%d %H:%M:%S')
        self.Duration = arrival_datetime - departure_datetime
    
        if (self.Departure=='') or (self.Departure_Date=='') or (self.Departure_Time=='') or (self.Arrival=='') or (self.Arrival_Date=='') or (self.Arrival_Time=='') or (self.Price_F=='') or (self.Discount=='') or (self.Economy=='') or (self.Business=='') or (self.First==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif self.Departure_Date>self.Arrival_Date:
            tk.messagebox.showinfo('Error', 'The arrival date must be after the departure date')
        elif datetime.datetime.strptime(self.Departure_Date, '%Y-%m-%d') < datetime.datetime.now() or datetime.datetime.strptime(self.Arrival_Date, '%Y-%m-%d') < datetime.datetime.now():
            tk.messagebox.showinfo('Error', 'The departure or Arrival date must be after or today')
        elif self.Price_F<=0:
            tk.messagebox.showinfo('Error', 'The price must be positive')
        elif self.Discount<0 or self.Discount>100:
            tk.messagebox.showinfo('Error', 'The discount must be between 0 and 100')
        elif self.Economy+self.Business+self.First<=0 or self.Economy+self.Business+self.First!=self.Seats:
            tk.messagebox.showinfo('Error', 'The number of seats for classes must be positive and equal to the total number of seats')
        elif self.Economy<0 or self.Business<0 or self.First<0:
            tk.messagebox.showinfo('Error', 'The number of seats for classes must be positive')
        elif len(self.Departure) <2 or len(self.Departure) >30 or not self.Departure.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid Departure format')
        elif len(self.Arrival) <2 or len(self.Arrival) >30 or not self.Arrival.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid Arrival format')
        elif self.Arrival==self.Departure:
            tk.messagebox.showinfo('Error', 'The arrival and the departure must be different')
        elif self.Arrival!=self.Search_Flight_Result[0]['Arrival'] and self.Image_Flight_Check==False:
            tk.messagebox.showinfo('Error', 'Please after changing the arrival, chnage the flight image')
        else:
            self.Discount=self.Discount/100
            if self.Arrival!=self.Search_Flight_Result[0]['Arrival'] and self.Image_Flight_Check==True:
                Arrival=self.Search_Flight_Result[0]['Arrival'].replace(" ", "_")
                image_path = f"./images/Flights_Images/{Arrival}.png"
                os.remove(image_path)
            Actual_Outbound_Flight.Update_Flight(Actual_Customer.AdminFlight, self.Departure, self.Departure_Date, self.Departure_Time, self.Arrival, self.Arrival_Date, self.Arrival_Time, self.Duration, self.Price_F, self.Discount, self.Seats, self.Economy, self.Business, self.First)
            Actual_Customer.AdminFlight = ""
            tk.messagebox.showinfo('Succeed', 'Flight has been updated')
            Launch_My_Account()

    def Delete_Flight(self):
        response = tk.messagebox.askquestion('Warning', 'Are you sure you want to delete this Flight?', icon='warning')
        if response == 'yes':
            Actual_Outbound_Flight.Delete_Flight(Actual_Customer.AdminFlight)
            Actual_Customer.AdminFlight = ""
            print("Delete Flight")
            Launch_My_Account()
        else:
            print("Flight deletion canceled")

    def Search_Customer(self):
        self.Search_Customer=self.Search_Customer_Input.get()
        if self.Search_Customer=='':
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif not self.Search_Customer.isdigit():
            tk.messagebox.showinfo('Error', 'Invalid ID format')
        else:
            sql = "SELECT COUNT(*) AS Here FROM Customer WHERE CustomerID = '{}';".format(self.Search_Customer)
            Here = dbconnect.DBHelper().fetch(sql)[0]['Here']
            if Here == 0:
                tk.messagebox.showinfo('Error', 'The customer does not exist')
            else:
                Actual_Customer.AdminCustomer=self.Search_Customer
                Launch_My_Account()

    def Save_Customer(self):
        self.FirstName=self.First_Name_Input.get()
        self.LastName=self.Last_Name_Input.get()
        self.UserName=self.User_Name_Input.get()
        self.Email=self.Email_Input.get()
        self.Phone=self.Phone_Input.get()
        self.Old_Password=self.Old_Password_Input.get()
        self.Password=self.Password_Input.get()
        self.Confirm_Password=self.Confirm_Password_Input.get()
        self.Admin=self.Admin_Input.get()
        if self.Admin=="Yes": self.Admin=1
        else: self.Admin=0
        if (self.FirstName=='') or (self.LastName=='') or (self.UserName=='') or (self.Email=='') or (self.Phone==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif not re.match(r'^[0-9]*$', self.Phone):
            # Invalid phone format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid phone format')
        elif not re.match(r'^[\w\.-]+@[\w\.-]+$', self.Email):
            # Invalid email format, show an error message
            tk.messagebox.showinfo('Error', 'Invalid email format')
        elif self.Password!=self.Confirm_Password:
            tk.messagebox.showinfo('Error', 'The password and the confirmation password are not the same')
        elif self.Admin!=1 and self.Admin!=0:
            tk.messagebox.showinfo('Error', 'Please choose if the customer is an admin or not')
        elif len(self.FirstName) <2 or len(self.FirstName) >30 or not self.FirstName.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid First Name format')
        elif len(self.LastName) <2 or len(self.LastName) >30 or not self.LastName.isalpha():
            tk.messagebox.showinfo('Error', 'Invalid Last Name format')
        elif len(self.UserName) <2 or len(self.UserName) >30 or not self.UserName.isalnum():
            tk.messagebox.showinfo('Error', 'Invalid User Name format')
        sqlMDP = "SELECT Password FROM Customer WHERE CustomerID = '{}';".format(Actual_Customer.AdminCustomer)
        MDP = dbconnect.DBHelper().fetch(sqlMDP)[0]['Password']
        if (self.Password!='') or (self.Confirm_Password!=''):
            if (self.Old_Password=='') or (self.Password=='') or (self.Confirm_Password==''):
                tk.messagebox.showinfo('Error', 'Please fill in all the information for the password')
            elif self.Password!=self.Confirm_Password:
                tk.messagebox.showinfo('Error', 'The new password and the confirmation password are not the same')
            elif self.Old_Password!=MDP:
                tk.messagebox.showinfo('Error', 'The old password is incorrect')
            else : 
                res=Actual_Customer.Update_Customer(Actual_Customer.AdminCustomer, self.Email, self.Password, self.FirstName, self.LastName, self.UserName,  self.Phone, self.Admin)
                M.send_email_password(self.Email, self.Password, self.FirstName)
                Launch_My_Account()
        else:
            res=Actual_Customer.Update_Customer(Actual_Customer.AdminCustomer, self.Email, MDP, self.FirstName, self.LastName, self.UserName,  self.Phone, self.Admin)
        if res=="Email":
            tk.messagebox.showinfo('Error', 'The email already exist')
        elif res=="UserName":
            tk.messagebox.showinfo('Error', 'The username already exist')
        elif res=="Phone":
            tk.messagebox.showinfo('Error', 'The phone already exist')
        elif res=="Succeed":
            tk.messagebox.showinfo('Succeed', 'Customer has been modified')
            Actual_Customer.AdminCustomer = 0
            Launch_My_Account()
        else : 
            tk.messagebox.showinfo('Error', 'Sorry, an error occured')

    def Delete_Customer(self):
        response = tk.messagebox.askquestion('Warning', 'Are you sure you want to delete your account?', icon='warning')
        if response == 'yes':
            Actual_Customer.Delete_Customer(self.Search_Customer_Result[0]['CustomerID'])
            Actual_Customer.AdminCustomer = 0
            Launch_My_Account()
            print("Delete Account")
        else:
            print("Account deletion canceled")

    
    def Analyse(self):
        self.Begin_Date=self.Begin_Date_Input.get()
        self.End_Date=self.End_Date_Input.get()
        if (self.Begin_Date=='') or (self.End_Date==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        elif self.Begin_Date>self.End_Date:
            tk.messagebox.showinfo('Error', 'The end date must be after the begin date')
        #elif self.Begin_Date<datetime.datetime.now() or self.End_Date<datetime.datetime.now():
            #tk.messagebox.showinfo('Error', 'The begin or end date must be after or today')
        else:
            Actual_Customer.AdminDateBegin=self.Begin_Date_Input.get()
            Actual_Customer.AdminDateEnd=self.End_Date_Input.get()
            Launch_My_Account()


    def create_plot(self, x_data, y_data, title, xlabel, ylabel, plot_type, image_size):
        fig, ax = plt.subplots(figsize=(image_size[0]/100, image_size[1]/100))  # Convert pixels to inches
        if plot_type == 'line':
            ax.plot(x_data, y_data, marker='o', linestyle=' ', color=second_color)
            plt.xticks(rotation=70)
            plt.subplots_adjust(bottom=0.3)
            #, linestyle='-'
        elif plot_type == 'histogram':
            ax.bar(x_data, y_data, color=second_color)
            plt.xticks(rotation=70)
            plt.subplots_adjust(bottom=0.3)
            #ax.xaxis.set_label_coords(0.5, -0.50)
            #ax.yaxis.set_label_coords(-0.055, 0.5)
        else:
            raise ValueError("Invalid plot_type. Supported values: 'line' or 'histogram'.")

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        canvas = FigureCanvasTkAgg(fig, master=self.bottom_display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP)
        #Space after the plot
        self.Space=tk.Label(self.bottom_display_frame, text=" ", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Space.pack(side=tk.TOP)

##------------------------------------------------------------------------------------------------------##
##----------------------------------------------Purchase Page-------------------------------------------##
##------------------------------------------------------------------------------------------------------##

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

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=150,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass 

        #AddOrNot
        if Actual_Search.Need_Return==False:
            bg_image_five = Image.open("./images/add.png")
            bg_photo_five = ImageTk.PhotoImage(bg_image_five)
            # Créer un canevas pour afficher l'image du logo
            canvas_five = tk.Canvas(self.second_top_frame, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_five.place(x=935,y=108)
            canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
            canvas_five.image = bg_photo_five
            canvas_five.bind("<Button-1>", self.Hide_Button_2)
        else:
            bg_image_five = Image.open("./images/no_add.png")
            bg_photo_five = ImageTk.PhotoImage(bg_image_five)
            # Créer un canevas pour afficher l'image du logo
            canvas_five = tk.Canvas(self.second_top_frame, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_five.place(x=920,y=108)
            canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
            canvas_five.image = bg_photo_five
            canvas_five.bind("<Button-1>", self.Hide_Button_2)

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
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Search_Button = tk.Button(self.fourth_top_frame, text='Search', command=self.Search_Flight, font=("Arial", 15), bg=third_color, fg=main_color)
        self.Search_Button.config(height=1, width=10)

        #Input
        self.From_Input = tk.Entry(self.second_top_frame)
        self.To_Input = tk.Entry(self.second_top_frame)
        self.Departure_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        self.Return_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        self.Passengers_Input = tk.Spinbox(self.third_top_frame, from_=1, to=10)
        self.Class_Input = ttk.Combobox(self.third_top_frame, values=["Economy", "Business", "First Class"])
        if Actual_Search.ReturnOrNot==False:
            self.From_Input.insert(0, "Paris")
            self.To_Input.insert(0, "New York")
            #Remove for final version
            self.Class_Input.delete(0, tk.END)
            self.Class_Input.insert(0, "Economy")
        else :
            self.From_Input.insert(1, Actual_Search.From)
            self.To_Input.insert(0, Actual_Search.To)
            self.Departure_Input.delete(0, tk.END)
            self.Departure_Input.insert(0, Actual_Search.Departure_Date)
            self.Return_Input.delete(0, tk.END)
            self.Return_Input.insert(0, Actual_Search.Return_Date)
            self.Passengers_Input.delete(0, tk.END)
            self.Passengers_Input.insert(0, Actual_Search.Passengers)
            self.Class_Input.delete(0, tk.END)
            self.Class_Input.insert(0, Actual_Search.Class)
            Launch_Purchase_Results_Page()


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
        #Display the Return Input
        if Actual_Search.Need_Return==True: self.Return_Input.grid(row=2, column=3, padx=10, pady=3, ipadx=5, ipady=5)
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
            if self.Departure < datetime.datetime.now().strftime("%Y-%m-%d"):
                tk.messagebox.showinfo('Error', 'Invalid Departure Date')
            elif (self.Return != '') & (self.Return < datetime.datetime.now().strftime("%Y-%m-%d"))&(Actual_Search.Need_Return==True):
                tk.messagebox.showinfo('Error', 'Invalid Return Date')
            elif (self.Return != '') & (self.Return < self.Departure)&(Actual_Search.Need_Return==True):
                tk.messagebox.showinfo('Error', 'Invalid Return Date')
            elif (self.Return == '') & (Actual_Search.Need_Return==True):
                tk.messagebox.showinfo('Error', 'Invalid Return Date')
            else:
                try :
                    if (self.Passengers == int(self.Passengers)) & (self.Passengers > 1) & (self.Passengers < 11):
                        if (self.Class == "Economy") or (self.Class == "Business") or (self.Class =="First Class"):
                            if (self.From == str(self.From)) & (self.To == str(self.To)):
                                print("Search Flight")
                                if Actual_Search.CompleteAccept():
                                        Actual_Search.Complet_Actual_Search(self.From, self.To, self.Departure, self.Return, self.Class, self.Passengers)
                                        Launch_Info_Passengers()
                                else :
                                    Actual_Search.Change_Actual_Search(self.From, self.To, self.Departure, self.Return, self.Class, self.Passengers)
                                    Launch_Info_Passengers()

                        else:
                            tk.messagebox.showinfo('Error', 'Invalid Class')
                    elif self.Passengers == 1 :
                        print("Search Flight")
                        # Dates are valid
                        if Actual_Search.CompleteAccept():
                                Actual_Search.Complet_Actual_Search(self.From, self.To, self.Departure, self.Return, self.Class, self.Passengers)
                                Launch_Purchase_Results_Page()
                        else : 
                            Actual_Search.Change_Actual_Search(self.From, self.To, self.Departure, self.Return, self.Class, self.Passengers)
                            Launch_Purchase_Results_Page()
                    else:
                        tk.messagebox.showinfo('Error', 'Invalid Number of Passengers')
                except ValueError:
                    # Invalid date format
                    tk.messagebox.showinfo('Error', 'Invalid date format or Number of Passengers or Class')

    def Hide_Button(self, empty):
        Launch_Home_Page()

    def Hide_Button_1(self, empty):
        Launch_Basket_Page()
    
    def Hide_Button_2(self, empty):
        if Actual_Search.Need_Return==False:
            Actual_Search.Need_Return=True
            Launch_Purchase_Page()
        else:
            Actual_Search.Need_Return=False
            Actual_Search.Return_Date=''
            Launch_Purchase_Page()


##------------------------------------------------------------------------------------------------------##
##---------------------------------------------Info Passengers------------------------------------------##
##------------------------------------------------------------------------------------------------------##

class Info_Passengers():
    # Create a frame at the top for buttons
    def __init__(self, main_window):
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.middle_frame = tk.Frame(main_window, bg=main_color)

        self.scroll_canva = tk.Canvas(self.middle_frame, bg=main_color)
        self.scroll_canva.config(highlightthickness=0, borderwidth=0)
        self.display_frame = tk.Frame(self.scroll_canva, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=150,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass 

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        self.Page_Title= tk.Label(self.display_frame, text=" Your Passengers", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.Info_passengers = tk.Label(self.display_frame, text="Please enter your information", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.GoBack_Title = tk.Label(self.middle_frame, text="<", font=("Arial", 20), bg=main_color)
        self.GoBack_Title.bind("<Button-1>", self.Hide_Button_2)
        self.Space_Title_1 = tk.Label(self.display_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_2 = tk.Label(self.display_frame, text=" ", font=("Arial", 10), bg=main_color)

        # Create 
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Submit_Button = tk.Button(self.display_frame, text='Submit', command=self.Submit, font=("Arial", 15), bg=third_color, fg=main_color)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        self.scroll_canva.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.yscrollbar = tk.Scrollbar(self.middle_frame, orient="vertical", command=self.scroll_canva.yview)
        self.yscrollbar.pack(side=tk.RIGHT, fill='y')
        self.scroll_canva.configure(yscrollcommand=self.yscrollbar.set)
        self.scroll_canva.bind('<Configure>', lambda e: self.scroll_canva.configure(scrollregion = self.scroll_canva.bbox("all")))
        self.display_frame.pack(fill=tk.BOTH, expand=True)
        self.scroll_canva.create_window((0,0), window=self.display_frame, anchor="nw")
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=0, ipady=5, padx=10, pady=10)
        #Display the Page Title
        self.Page_Title.pack(ipadx=5, ipady=5, padx=490, pady=30)
        #Display the Go Back Title
        self.GoBack_Title.place(x=22, y=15)
        #Display the Info Title
        self.Info_passengers.pack(ipadx=5, ipady=5, padx=490, pady=0)
        #Display the Space Title
        self.Space_Title_1.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Number of Passengers
        self.p=Actual_Search.Passengers
        self.pass_type = [None] * self.p
            
        for i in range(self.p):
            self.pass_type[i] = tk.StringVar()  # Create a StringVar for each Combobox
            self.Passsenger_Title = tk.Label(self.display_frame, text="Passenger "+str(i+1), font=("Arial", 10), bg=main_color)
            self.Passsenger_Title.pack(ipadx=5, ipady=5, padx=490, pady=3)
            self.Passenger_Type = ttk.Combobox(self.display_frame, values=["Adult", "Child", "Senior", "Student"], textvariable=self.pass_type[i])
            if Actual_Search.Passengers_Type[i] != None:
                self.Passenger_Type.insert(0, Actual_Search.Passengers_Type[i])
            self.Passenger_Type.pack(ipadx=5, ipady=5, padx=490, pady=3)
        self.Space_Title_2.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Buy Now Button
        self.Submit_Button.pack(ipadx=5, ipady=5, padx=490, pady=10)

    def Submit(self):
        good=True
        for i in range(self.p):
            if self.pass_type[i].get() == "":
                tk.messagebox.showinfo('Error', 'Please fill in all the information')
                good=False
                break
        if good:
            for i in range(self.p):
                Actual_Search.Passengers_Type[i]=self.pass_type[i].get()
                if self.pass_type[i].get() == "Adult":
                    Actual_Search.Passengers_Type_Number[i]=1
                elif self.pass_type[i].get() == "Child":
                    Actual_Search.Passengers_Type_Number[i]=0.60
                elif self.pass_type[i].get() == "Senior":
                    Actual_Search.Passengers_Type_Number[i]=0.80
                elif self.pass_type[i].get() == "Student":
                    Actual_Search.Passengers_Type_Number[i]=0.75
            Launch_Purchase_Results_Page()

    def Hide_Button(self, empty):
        Launch_Home_Page()
    
    def Hide_Button_1(self, empty):
        Launch_Basket_Page()

    def Hide_Button_2(self, empty):
        Launch_Purchase_Page()

##------------------------------------------------------------------------------------------------------##
##------------------------------------------Purchase Results Page---------------------------------------##
##------------------------------------------------------------------------------------------------------##

class Purchase_Results_Page():
    def __init__(self, main_window):
        self.Price_display=0
        self.Total_Price_display=0

        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame.columnconfigure(0, weight=1)
        self.second_top_frame.columnconfigure(1, weight=1)
        self.second_top_frame.columnconfigure(2, weight=1)
        self.second_top_frame.columnconfigure(3, weight=1)
        self.second_top_frame.columnconfigure(4, weight=1)
        self.second_top_frame.columnconfigure(5, weight=1)
        self.second_top_frame.columnconfigure(6, weight=1)
        self.second_top_frame.columnconfigure(7, weight=1)
        self.middle_frame = tk.Frame(main_window, bg=main_color)

        self.scroll_canva = tk.Canvas(self.middle_frame, bg=main_color)
        self.scroll_canva.config(highlightthickness=0, borderwidth=0)
        self.display_frame = tk.Frame(self.scroll_canva, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=150,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass 

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        if Actual_Search.ReturnOrNot==False:
            self.Page_Title= tk.Label(self.display_frame, text=" Choose your Outbound Hour", font=("Arial", 15), bg=main_color, fg=fourth_color)
        else:
            self.Page_Title= tk.Label(self.display_frame, text=" Choose your Inbound Hours", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.GoBack_Title = tk.Label(self.second_top_frame, text="<", font=("Arial", 20), bg=main_color)
        self.GoBack_Title.bind("<Button-1>", self.Hide_Button_2)
        self.Space_Title_1 = tk.Label(self.second_top_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_2 = tk.Label(self.second_top_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.From_Title = tk.Label(self.second_top_frame, text="From", font=("Arial", 10), bg=main_color)
        self.To_Title = tk.Label(self.second_top_frame, text="To", font=("Arial", 10), bg=main_color)
        self.Departure_Title = tk.Label(self.second_top_frame, text="Departure", font=("Arial", 10), bg=main_color)
        self.Return_Title = tk.Label(self.second_top_frame, text="Return *", font=("Arial", 10), bg=main_color)
        self.Class_Title = tk.Label(self.second_top_frame, text="Class", font=("Arial", 10), bg=main_color)

        #Input
        self.From_Input = tk.Entry(self.second_top_frame)
        self.To_Input = tk.Entry(self.second_top_frame)
        if Actual_Search.ReturnOrNot==False:
            self.From_Input.insert(0, Actual_Search.From)
            self.To_Input.insert(0, Actual_Search.To)
        else :
            self.From_Input.insert(0, Actual_Search.To)
            self.To_Input.insert(0, Actual_Search.From)
        self.Departure_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        self.Departure_Input.delete(0, tk.END)
        self.Departure_Input.insert(0, Actual_Search.Departure_Date)
        self.Return_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        self.Return_Input.delete(0, tk.END)
        self.Return_Input.insert(0, Actual_Search.Return_Date)
        self.Class_Input = ttk.Combobox(self.second_top_frame, values=["Economy", "Business", "First Class"])
        self.Class_Input.insert(0, Actual_Search.Class)

        # Button
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.ReSearch_Button = tk.Button(self.second_top_frame, text='Re-Search', command=self.ReSearch_Flight, font=("Arial", 10), bg=third_color, fg=main_color)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=0, ipady=5, padx=10, pady=10)

        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under second_top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        #Display the Space Title
        self.Space_Title_1.grid(row=0, column=0, padx=10, pady=0, ipadx=5, ipady=0)
        #From Title
        self.From_Title.grid(row=1, column=1, padx=10, pady=3, ipadx=5, ipady=0)
        #From Input
        self.From_Input.grid(row=2, column=1, padx=10, pady=0, ipadx=5, ipady=5)
        #To Title
        self.To_Title.grid(row=1, column=2, padx=10, pady=3, ipadx=5, ipady=0)
        #To Input
        self.To_Input.grid(row=2, column=2, padx=10, pady=0, ipadx=5, ipady=5)
        #Departure Title
        self.Departure_Title.grid(row=1, column=3, padx=10, pady=3, ipadx=5, ipady=0)
        #Departure Input
        if Actual_Search.ReturnOrNot==False: self.Departure_Input.grid(row=2, column=3, padx=10, pady=0, ipadx=5, ipady=5)
        #Return Title
        self.Return_Title.grid(row=1, column=4, padx=10, pady=3, ipadx=5, ipady=0)
        #Return Input
        if Actual_Search.Need_Return==True: self.Return_Input.grid(row=2, column=4, padx=10, pady=0, ipadx=5, ipady=5)
        #Class Title
        self.Class_Title.grid(row=1, column=5, padx=10, pady=3, ipadx=5, ipady=0)
        #Class Input
        self.Class_Input.grid(row=2, column=5, padx=10, pady=0, ipadx=5, ipady=5)
        #Re-Search Button
        self.ReSearch_Button.grid(row=2, column=6, padx=5, pady=0, ipadx=5, ipady=5)
        #Display the Space Title
        self.Space_Title_2.grid(row=3, column=0, padx=10, pady=0, ipadx=5, ipady=0)

        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        self.scroll_canva.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.yscrollbar = tk.Scrollbar(self.middle_frame, orient="vertical", command=self.scroll_canva.yview)
        self.yscrollbar.pack(side=tk.RIGHT, fill='y')
        self.scroll_canva.configure(yscrollcommand=self.yscrollbar.set)
        self.scroll_canva.bind('<Configure>', lambda e: self.scroll_canva.configure(scrollregion = self.scroll_canva.bbox("all")))
        self.display_frame.pack(fill=tk.BOTH, expand=True)
        self.scroll_canva.create_window((0,0), window=self.display_frame, anchor="nw")

        #Display the Page Title
        self.Page_Title.pack(ipadx=5, ipady=5, padx=400, pady=30)
        #Display the Go Back Title
        self.GoBack_Title.place(x=22, y=47)

        #Make search
        rep=Actual_Search.Search_HowMany()
        if (rep==0) or (rep==None) or ((Actual_Search.ReturnOrNot==True) & (rep==0)):
            self.No_Flight_Title = tk.Label(self.display_frame, text="No Flight Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
            self.Info_Noo_Flight = tk.Label(self.display_frame, text="Unfortunately it seems that no flight corresponds to your dates.\nTry with different dates please", font=("Arial", 10), bg=main_color, fg=fourth_color)
            self.No_Flight_Title.pack(ipadx=5, ipady=5, padx=370, pady=30)
            self.Info_Noo_Flight.pack(ipadx=5, ipady=5, padx=370, pady=30)
        else:
            for i in range(rep):
                self.Price_display=0
                self.Total_Price_display=0
                if Actual_Search.ReturnOrNot == True:
                    self.Search_Results_Outbound = Actual_Search.Search_Inbound()
                else:
                    self.Search_Results_Outbound = Actual_Search.Search_Outbound()
                try:
                    # Create a canvas widget
                    self.canvas = tk.Canvas(self.display_frame, width=850, height=200, highlightthickness=0 ,borderwidth=0, bg=main_color)
                    self.canvas.bind("<Button-1>", lambda event, param=self.Search_Results_Outbound: self.FLight_Select(event, param))
                    self.canvas.pack(padx=65, pady=15, side=tk.TOP, fill=tk.X)
                    # Draw a rectangle on the canvas
                    self.canvas.create_rectangle(0, 0, 930, 200, outline='black', width=2)
                    # Print information in the rectangle
                    self.canvas.create_text(380, 40, anchor='nw', text="Flight Number: "+str(self.Search_Results_Outbound[i]['FlightNumber']), font=("Arial", 10))
                    self.canvas.create_text(380, 60, anchor='nw', text="Departure: "+str(self.Search_Results_Outbound[i]['Departure']), font=("Arial", 10))
                    self.canvas.create_text(380, 80, anchor='nw', text="Arrival: "+str(self.Search_Results_Outbound[i]['Arrival']), font=("Arial", 10))
                    if Actual_Search.Passengers == 1:
                        self.Total_Price_display=float(self.Search_Results_Outbound[i]['Price'])*Actual_Search.Class_Type
                    else :
                        for j in range(Actual_Search.Passengers):
                            self.Total_Price_display+=(float(self.Search_Results_Outbound[i]['Price'])*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type
                    self.Price_display=round(self.Price_display, 2)
                    self.canvas.create_text(760, 40, anchor='ne', text=str(self.Total_Price_display)+"£", font=("Arial", 15))
                    self.Price_display=round(float(self.Search_Results_Outbound[i]['Price'])*Actual_Search.Class_Type,2)
        
                    self.canvas.create_text(380, 120, anchor='nw', text="Departure Time: "+str(self.Search_Results_Outbound[i]['DepartureTime']), font=("Arial", 10))
                    self.canvas.create_text(580, 120, anchor='nw', text="Arrival Time: "+str(self.Search_Results_Outbound[i]['ArrivalTime']), font=("Arial", 10))
                    if (self.Search_Results_Outbound[i]['Discount'] != 0) & Actual_Customer.LogOrNot==True:
                        if Actual_Search.Passengers == 1:
                            self.Total_Price_display=float(self.Search_Results_Outbound[i]['Price'])*Actual_Search.Class_Type*(1-(self.Search_Results_Outbound[i]['Discount']))
                        else :
                            for j in range(Actual_Search.Passengers):
                                self.Total_Price_display+=(float(self.Search_Results_Outbound[i]['Price'])*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-(self.Search_Results_Outbound[i]['Discount']))
                        #Draw red Line on the first Total Price
                        self.canvas.create_line(690, 40, 760, 65, fill='red', width=2)
                        self.canvas.create_text(840, 40, anchor='ne', text=str(self.Total_Price_display)+"£", font=("Arial", 15), fill='red')
                        self.Price_display=round(float(self.Search_Results_Outbound[i]['Price'])*Actual_Search.Class_Type*(1-(self.Search_Results_Outbound[i]['Discount'])),2)
                    self.canvas.create_text(760, 70, anchor='ne', text="Adult Price: "+str(self.Price_display)+"£", font=("Arial", 10))
                    image_name = "./images/Flights_Images/"+(str(self.Search_Results_Outbound[i]['Arrival']).replace(' ', '_'))+".png"
                    bg_image_rep = Image.open(image_name)
                    bg_photo_rep = ImageTk.PhotoImage(bg_image_rep)
                    # Créer un canevas pour afficher l'image du logo
                    canvas_rep = tk.Canvas(self.canvas, width=bg_image_rep.width, height=bg_image_rep.height, highlightthickness=0,borderwidth=0)
                    canvas_rep.place(x=10,y=10)
                    canvas_rep.create_image(0, 0, anchor=tk.NW, image=bg_photo_rep)
                    canvas_rep.image = bg_photo_rep
                    bg_image_rep.close()
                except IndexError:
                    if i==0:
                        self.canvas.destroy()
                        self.No_Flight_Title = tk.Label(self.display_frame, text="No Flight Found", font=("Arial", 15), bg=main_color, fg=fourth_color)
                        self.Info_Noo_Flight = tk.Label(self.display_frame, text="Unfortunately it seems that no flight corresponds to your dates.\nTry with different dates please", font=("Arial", 10), bg=main_color, fg=fourth_color)
                        self.No_Flight_Title.pack(ipadx=5, ipady=5, padx=370, pady=30)
                        self.Info_Noo_Flight.pack(ipadx=5, ipady=5, padx=370, pady=30)
                        break
                    self.canvas.destroy()
                    break
                
    def Hide_Button(self, empty):
        Launch_Home_Page()
    
    def Hide_Button_1(self, empty):
        Launch_Basket_Page()

    def Hide_Button_2(self, empty):
        Launch_Purchase_Page()
    
    def FLight_Select(self, event, param):
        if Actual_Outbound_Flight.Flight_Number==None:
            Actual_Outbound_Flight.Complete_Outbound_Flight(param[0]['FlightID'], param[0]['Airline'], param[0]['FlightNumber'], param[0]['Departure'], param[0]['DepartureDate'], param[0]['DepartureTime'], param[0]['Arrival'], param[0]['ArrivalDate'], param[0]['ArrivalTime'], param[0]['Duration'], param[0]['Price'], param[0]['Discount'], param[0]['Seats'], param[0]['SeatsAvailable'], Actual_Search.Class_Type, Actual_Search.Passengers, Actual_Search.Passengers_Type_Number)
        else:
            Actual_Inbound_Flight.Complete_Inbound_Flight(param[0]['FlightID'], param[0]['Airline'], param[0]['FlightNumber'], param[0]['Departure'], param[0]['DepartureDate'], param[0]['DepartureTime'], param[0]['Arrival'], param[0]['ArrivalDate'], param[0]['ArrivalTime'], param[0]['Duration'], param[0]['Price'], param[0]['Discount'], param[0]['Seats'], param[0]['SeatsAvailable'], Actual_Search.Class_Type, Actual_Search.Passengers, Actual_Search.Passengers_Type_Number)
        Launch_Flight_Results_Page()

    def ReSearch_Flight(self):
        #get the input
        self.From=self.From_Input.get()
        self.To=self.To_Input.get()
        self.Departure=self.Departure_Input.get()
        if Actual_Search.ReturnOrNot==True: self.Return=self.Return_Input.get()
        else : self.Return=''
        self.Passengers=Actual_Search.Passengers
        self.Class=self.Class_Input.get()
        print(self.From)
        print(self.To)
        # Check if the email is a valid
        if (self.From=='') or (self.To=='') or (self.Departure=='') or (self.Passengers=='') or (self.Class==''):
            tk.messagebox.showinfo('Error', 'Please fill in all the information')
        else :
            if self.Departure < datetime.datetime.now().strftime("%Y-%m-%d"):
                tk.messagebox.showinfo('Error', 'Invalid Departure Date')
            elif (self.Return != '') & (self.Return < datetime.datetime.now().strftime("%Y-%m-%d"))&(Actual_Search.Need_Return==True)&(Actual_Search.ReturnOrNot==True):
                tk.messagebox.showinfo('Error', 'Invalid Return Date')
            elif (self.Return != '') & (self.Return < self.Departure)&(Actual_Search.Need_Return==True)&(Actual_Search.ReturnOrNot==True):
                tk.messagebox.showinfo('Error', 'Invalid Return Date')
            elif (self.Return == '') & (Actual_Search.Need_Return==True)&(Actual_Search.ReturnOrNot==True):
                tk.messagebox.showinfo('Error', 'Invalid Return Date')
            else:
                try :
                    if (self.Passengers == int(self.Passengers)) & (self.Passengers > 1) & (self.Passengers < 11):
                        if (self.Class == "Economy") or (self.Class == "Business") or (self.Class =="First Class"):
                            if (self.From == str(self.From)) & (self.To == str(self.To)):
                                print("Search Flight")
                                # Dates are valid
                                if (Actual_Search.ReturnOrNot == False) or (Actual_Search.Need_Return==False):
                                    Actual_Search.Change_Actual_Search(self.From, self.To, self.Departure, self.Return, self.Class, self.Passengers)
                                    Launch_Purchase_Results_Page()
                                else:
                                    Actual_Search.Change_Actual_Search(Actual_Search.From, Actual_Search.To, Actual_Search.Departure_Date, self.Return, self.Class, self.Passengers)
                                    Launch_Purchase_Results_Page()
                        else:
                            tk.messagebox.showinfo('Error', 'Invalid Class')
                    elif self.Passengers == 1 :
                        print("Search Flight")
                        # Dates are valid
                        if (Actual_Search.ReturnOrNot == False) or (Actual_Search.Need_Return==False):
                            Actual_Search.Change_Actual_Search(self.From, self.To, self.Departure, self.Return, self.Class, self.Passengers)
                            Launch_Purchase_Results_Page()
                        else:
                            Actual_Search.Change_Actual_Search(Actual_Search.From, Actual_Search.To, Actual_Search.Departure_Date, self.Return, self.Class, self.Passengers)
                            Launch_Purchase_Results_Page()
                    else:
                        tk.messagebox.showinfo('Error', 'Invalid Number of Passengers')
                except ValueError:
                    # Invalid date format
                    tk.messagebox.showinfo('Error', 'Invalid date format or Number of Passengers or Class')

##------------------------------------------------------------------------------------------------------##
##-------------------------------------------Flight Results Page----------------------------------------##
##------------------------------------------------------------------------------------------------------##

class Flight_Results_Page():
    def __init__(self, main_window):
        if Actual_Inbound_Flight.Flight_Number==None:
            Flight_Result=Actual_Outbound_Flight
        else:
            Flight_Result=Actual_Inbound_Flight
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.left_frame = tk.Frame(main_window, bg=main_color)
        self.right_frame = tk.Frame(main_window, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Basket
        bg_image_three = Image.open("./images/shopping-cart-res.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(self.top_frame, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=150,y=20)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three
        canvas_three.bind("<Button-1>", self.Hide_Button_1)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            notif_image = Image.open("./images/number-1.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            notif_image = Image.open("./images/number-2.png")
            bg_photo_four = ImageTk.PhotoImage(notif_image)
            canvas_four = tk.Canvas(self.top_frame, width=notif_image.width, height=notif_image.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_four.place(x=168,y=18)
            canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
            canvas_four.image = bg_photo_four
        else : pass 
        #plane
        bg_image_five = Image.open("./images/black-planeres.png")
        bg_photo_five = ImageTk.PhotoImage(bg_image_five)
        # Créer un canevas pour afficher l'image du logo
        canvas_five = tk.Canvas(self.right_frame, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_five.place(x=142,y=10)
        canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
        canvas_five.image = bg_photo_five

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button)
        self.Page_Title= tk.Label(self.second_top_frame, text=" Your Outbound Flight Recap", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.Info_passengers = tk.Label(self.second_top_frame, text="Add To basket and pay after", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.GoBack_Title = tk.Label(self.second_top_frame, text="<", font=("Arial", 20), bg=main_color)
        self.GoBack_Title.bind("<Button-1>", self.Hide_Button_2)
        self.Space_Title_1 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_2 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)

        # Buttons
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.AddBasket_Button = tk.Button(self.right_frame, text='Add to Basket', command=self.AddBasket, font=("Arial", 15), bg=third_color, fg=main_color)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None)&(Actual_Search.Need_Return==True):
            self.Chose_Return_Button = tk.Button(self.left_frame, text='Choose Return', command=Launch_Purchase_Results_Page, font=("Arial", 15), bg=third_color, fg=main_color)
        else:
            self.Chose_Return_Button = tk.Button(self.left_frame, text='Go to Basket', command=Launch_Basket_Page, font=("Arial", 15), bg=third_color, fg=main_color)
        #Info
        self.Flight_Title = tk.Label(self.right_frame, text="Flight Number: "+str(Flight_Result.Flight_Number), font=("Arial", 11), bg=main_color)
        self.Departure_Title = tk.Label(self.right_frame, text="Departure: "+str(Flight_Result.Departure_Airport), font=("Arial", 11), bg=main_color)
        self.Arrival_Title = tk.Label(self.right_frame, text="Arrival: "+str(Flight_Result.Arrival_Airport), font=("Arial", 11), bg=main_color)
        self.DepartureTime_Title = tk.Label(self.right_frame, text=str(Flight_Result.Departure_Time), font=("Arial", 15), bg=main_color)
        self.ArrivalTime_Title = tk.Label(self.right_frame, text=str(Flight_Result.Arrival_Time), font=("Arial", 15), bg=main_color)
        self.Duration_Title = tk.Label(self.right_frame, text="Duration: "+str(Flight_Result.Flight_Duration), font=("Arial", 11), bg=main_color)
        self.Price_Title = tk.Label(self.right_frame, text="Adult Price: "+str(Flight_Result.Price)+"£", font=("Arial", 11), bg=main_color)
        self.City = tk.Label(self.left_frame, text=str(Flight_Result.Arrival_Airport), font=("Arial", 15), bg=main_color)
        self.Total_Price=0

        if Actual_Search.Passengers == 1:
            self.Total_Price=float(Flight_Result.Price*Actual_Search.Class_Type)
        else :
            for j in range(Actual_Search.Passengers):
                self.Total_Price+=(float(Flight_Result.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type
        self.Total_Price_Title = tk.Label(self.right_frame, text="Total Price: "+str(self.Total_Price)+"£", font=("Arial", 15), bg=main_color)
        #Discount 
        if (Flight_Result.Discount != 0) & Actual_Customer.LogOrNot==True:
            if Actual_Search.Passengers == 1:
                self.Total_Price=float(Flight_Result.Price*Actual_Search.Class_Type*(1-Flight_Result.Discount))
            else :
                for j in range(Actual_Search.Passengers):
                    self.Total_Price+=(float(Flight_Result.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Flight_Result.Discount)
            self.Total_Price_Title = tk.Label(self.right_frame, text="Total Price: "+str(self.Total_Price)+"£", font=("Arial", 15), bg=main_color, fg='red')
            self.Price_Title = tk.Label(self.right_frame, text="Adult Price: "+str(round(float(Flight_Result.Price)*Actual_Search.Class_Type*(1-Flight_Result.Discount),2))+"£", font=("Arial", 11), bg=main_color)
            self.Total_Price_Title.place(x=40, y=220)
            self.Price_Title.place(x=40, y=170)
        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=10)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #Display the title
        #Display the Page Title
        self.Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=20)
        #Display the Go Back Title
        self.GoBack_Title.place(x=22, y=15)
        #Display the Info Title
        self.Info_passengers.pack(ipadx=5, ipady=5, padx=0, pady=10)
        #Display City
        self.City.pack(ipadx=5, ipady=5, padx=0, pady=10)
        image_name = "./images/Flights_Images/"+(str(Flight_Result.Arrival_Airport).replace(' ', '_'))+".png"
        bg_image_one = Image.open(image_name)
        bg_photo_one = ImageTk.PhotoImage(bg_image_one)
        # Créer un canevas pour afficher l'image de fond
        canvas = tk.Canvas(self.left_frame, width=bg_image_one.width, height=bg_image_one.height, bg=main_color, highlightthickness=0, borderwidth=0)
        canvas.pack(pady=10)
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo_one)
        canvas.image = bg_photo_one
        #Display the Departure Time Title
        self.DepartureTime_Title.place(x=40, y=10)
        #Display the Arrival Time Title
        self.ArrivalTime_Title.place(x=200, y=10)
        #Display the Flight Title
        self.Flight_Title.place(x=40, y=70)
        #Display the Departure Title
        self.Departure_Title.place(x=40, y=110)
        #Display the Arrival Title
        self.Arrival_Title.place(x=40, y=130)
        #Display the Duration Title
        self.Duration_Title.place(x=40, y=150)
        #Display the Price Title
        self.Price_Title.place(x=40, y=170)
        #Display the Total Price Title
        self.Total_Price_Title.place(x=40, y=220)
        #Display the Add to basket Button
        self.AddBasket_Button.place(x=43, y=280)
        #Display the Choose Return Button
        if Actual_Basket.Outbound_Flight_B!=None:
            self.Chose_Return_Button.pack(ipadx=5, ipady=5, padx=0, pady=20)
    
    def Hide_Button(self, empty):
        Launch_Home_Page()

    def Hide_Button_1(self, empty):
        Launch_Basket_Page()
    
    def Hide_Button_2(self, empty):
        Launch_Purchase_Results_Page()

    def AddBasket(self):
        Actual_Basket.Complete_Basket(Actual_Outbound_Flight, Actual_Inbound_Flight, Actual_Search.ReturnOrNot)
        Actual_Search.ReturnOrNot=True
        Launch_Flight_Results_Page()


##------------------------------------------------------------------------------------------------------##
##-----------------------------------------------Basket Page--------------------------------------------##
##------------------------------------------------------------------------------------------------------##

class Basket_Page():
    def __init__(self, main_window):
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.left_frame = tk.Frame(main_window, bg=main_color)
        self.right_frame = tk.Frame(main_window, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button_1)
        self.Page_Title= tk.Label(self.second_top_frame, text=" Your Basket", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.Space_Title_1 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_2 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_3 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_4 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_5 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)

        # Buttons
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Pay_Button = tk.Button(self.right_frame, text='Pay', command=Launch_Payment_Page, font=("Arial", 15), bg=third_color, fg=main_color)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=10)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #Display the title
        #Display the Page Title
        self.Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=20, side=tk.LEFT)
        self.Total_Price_display=0
        self.Price_display=0

        if (Actual_Basket.Outbound_Flight_B==None)&(Actual_Basket.Inbound_Flight_B==None):
            for i in range(2):  
                # Create a canvas widget
                self.canvas = tk.Canvas(self.left_frame, width=750, height=200, bg=main_color, highlightthickness=0, borderwidth=0)
                #self.canvas.bind("<Button-1>", lambda event, param=Display_Flight.Flight_ID : self.FLight_Select(event, param))
                self.canvas.pack(padx=25, pady=10, side=tk.TOP, fill=tk.X)
                # Draw a rectangle on the canvas
                self.canvas.create_rectangle(0, 0, 750, 200, outline='black', width=2)
                
                # Print information in the rectangle
                self.canvas.create_text(300, 80, anchor='nw', text="It looks pretty empty here! ", font=("Arial", 13))
                #images
                if main_color == main_color_light:
                    bg_image_rep_one = Image.open("./images/Where_L_res.png")
                else:
                    bg_image_rep_one = Image.open("./images/Where_D_res.png")
                bg_photo_rep_one = ImageTk.PhotoImage(bg_image_rep_one)
                # Créer un canevas pour afficher l'image du logo
                canvas_rep_one = tk.Canvas(self.canvas, width=261, height=bg_image_rep_one.height, highlightthickness=0,borderwidth=0)
                canvas_rep_one.place(x=10,y=10)
                canvas_rep_one.create_image(0, 0, anchor=tk.NW, image=bg_photo_rep_one)
                canvas_rep_one.image = bg_photo_rep_one
                bg_image_rep_one.close()
                if i==0:
                    self.Time_To_Shop_Button = tk.Button(self.canvas, text='Fly to shop!', command=Launch_Purchase_Page, font=("Arial", 11), bg=third_color, fg=main_color)
                    self.Time_To_Shop_Button.place(x=590, y=75)
                    #Plane
                    bg_image_five = Image.open("./images/black-planeres.png")
                    bg_photo_five = ImageTk.PhotoImage(bg_image_five)
                    # Créer un canevas pour afficher l'image du logo
                    canvas_five = tk.Canvas(self.canvas, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
                    canvas_five.place(x=520,y=75)
                    canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
                    canvas_five.image = bg_photo_five
            if Actual_Customer.LogOrNot == False:
                self.SignInfo = tk.Label(self.right_frame, text="Sign In or Sign Up for faster order", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Sign_Button = tk.Button(self.right_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
                self.SignInfo.pack(ipadx=5, ipady=5, padx=0, pady=20)
                self.Sign_Button.pack(ipadx=5, ipady=5, padx=0, pady=0)
            else :
                self.SignInfo = tk.Label(self.right_frame, text="Already Loged In ! \n What a smart customer ;)", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.SignInfo.pack(ipadx=5, ipady=5, padx=0, pady=20)
        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None):
            for i in range(2):  
                self.Total_Price_display=0
                self.Price_display=0
                # Create a canvas widget
                self.canvas = tk.Canvas(self.left_frame, width=750, height=200, bg=main_color, highlightthickness=0, borderwidth=0)
                self.canvas.pack(padx=25, pady=10, side=tk.TOP, fill=tk.X)
                # Draw a rectangle on the canvas
                self.canvas.create_rectangle(0, 0, 750, 200, outline='black', width=2)
                
                # Print information in the rectangle
                if i==0: 
                    self.Display_Flight = Actual_Basket.Outbound_Flight_B
                    self.canvas.create_text(280, 30, anchor='nw', text="Flight Number: "+str(self.Display_Flight.Flight_Number), font=("Arial", 10))
                    self.canvas.create_text(280, 50, anchor='nw', text="Departure: "+str(self.Display_Flight.Departure_Airport), font=("Arial", 10))
                    self.canvas.create_text(280, 70, anchor='nw', text="Arrival: "+str(self.Display_Flight.Arrival_Airport), font=("Arial", 10))
                    if Actual_Search.Passengers == 1:
                        self.Total_Price_display=float(self.Display_Flight.Price)*Actual_Search.Class_Type
                    else :
                        for j in range(Actual_Search.Passengers):
                            self.Total_Price_display+=(float(self.Display_Flight.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type
                    self.Price_display=round(float(self.Display_Flight.Price)*Actual_Search.Class_Type,2)
                    if (self.Display_Flight.Discount != 0) & Actual_Customer.LogOrNot==True:
                        if Actual_Search.Passengers == 1:
                            self.Total_Price_display=float(self.Display_Flight.Price)*Actual_Search.Class_Type*(1-self.Display_Flight.Discount)
                        else :
                            for j in range(Actual_Search.Passengers):
                                self.Total_Price_display+=(float(self.Display_Flight.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-self.Display_Flight.Discount)
                        self.Price_display=round(float(self.Display_Flight.Price)*Actual_Search.Class_Type*(1-self.Display_Flight.Discount),2)
                    self.canvas.create_text(660, 30, anchor='ne', text=str(self.Total_Price_display)+"£", font=("Arial", 15))
                    self.canvas.create_text(660, 60, anchor='ne', text="Adult Price: "+str(self.Price_display)+"£", font=("Arial", 10))
                    self.canvas.create_text(280, 110, anchor='nw', text="Departure Time: "+str(self.Display_Flight.Departure_Time), font=("Arial", 10))
                    self.canvas.create_text(480, 110, anchor='nw', text="Arrival Time: "+str(self.Display_Flight.Arrival_Time), font=("Arial", 10))
                    bg_image_two = Image.open("./images/bin.png")
                    bg_photo_two = ImageTk.PhotoImage(bg_image_two)
                    canvas_two = tk.Canvas(self.canvas, width=bg_image_two.width, height=bg_image_two.height, highlightthickness=0,borderwidth=0)
                    canvas_two.place(x=720,y=170)
                    canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
                    canvas_two.image = bg_photo_two
                    bg_image_two.close()
                    canvas_two.bind("<Button-1>", lambda event, param=i: self.Delete(event, param))
                    image_name = "./images/Flights_Images/"+(str(self.Display_Flight.Arrival_Airport).replace(' ', '_'))+".png"
                    bg_image_rep_one = Image.open(image_name)
                else : 
                    self.Display_Flight = Actual_Basket.Outbound_Flight_B
                    self.canvas.create_text(640, 30, anchor='ne', text="Need to return from "+str(self.Display_Flight.Arrival_Airport)+"?", font=("Arial", 15))
                    self.Book_Return_Button = tk.Button(self.canvas, text='Book Return', command=self.Book_Return, font=("Arial", 11), bg=third_color, fg=main_color)
                    self.Book_Return_Button.place(x=460, y=100)
                    if main_color == main_color_light:
                        bg_image_rep_one = Image.open("./images/Where_L_res.png")
                    else:
                        bg_image_rep_one = Image.open("./images/Where_D_res.png")
                #images 
                bg_photo_rep_one = ImageTk.PhotoImage(bg_image_rep_one)
                # Créer un canevas pour afficher l'image du logo
                canvas_rep_one = tk.Canvas(self.canvas, width=261, height=bg_image_rep_one.height, highlightthickness=0,borderwidth=0)
                canvas_rep_one.place(x=10,y=10)
                canvas_rep_one.create_image(0, 0, anchor=tk.NW, image=bg_photo_rep_one)
                canvas_rep_one.image = bg_photo_rep_one
                bg_image_rep_one.close()

            self.Total_Price_display=0
            if Actual_Search.Passengers == 1:
                if Actual_Basket.Inbound_Flight_B==None: self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type)
                else : self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type+(Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Class_Type)
            else :
                if Actual_Basket.Inbound_Flight_B==None:
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type)
                else : 
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type+((Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type)
            if (Actual_Basket.Outbound_Flight_B.Discount != 0) & Actual_Customer.LogOrNot==True:
                if Actual_Search.Passengers == 1:
                    if Actual_Basket.Inbound_Flight_B==None: self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount))
                    else : self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount)+(Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Inbound_Flight_B.Discount))
                else :
                    if Actual_Basket.Inbound_Flight_B==None:
                        for j in range(Actual_Search.Passengers):
                            self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount))
                    else : 
                        for j in range(Actual_Search.Passengers):
                            self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount)+((Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Inbound_Flight_B.Discount))
                
            self.Total_Price_B = round(self.Total_Price_display,2)
            self.Total_Price_B_Label = tk.Label(self.right_frame, text=str(self.Total_Price_B)+"£", font=("Arial", 15), bg=main_color, fg=fourth_color)
            self.Total_Basket_Price = tk.Label(self.right_frame, text="Total Basket Price :", font=("Arial", 11), bg=main_color, fg=fourth_color)
            self.Total_Basket_Price.pack(ipadx=5, ipady=5, padx=10, pady=0)
            self.Total_Price_B_Label.pack(ipadx=5, ipady=5, padx=10, pady=10)
            if Actual_Customer.LogOrNot == False:
                self.SignInfo = tk.Label(self.right_frame, text="Sign In or Sign Up for faster order", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Sign_Button = tk.Button(self.right_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
                self.SignInfo.pack(ipadx=5, ipady=5, padx=0, pady=20)
                self.Sign_Button.pack(ipadx=5, ipady=5, padx=0, pady=0)
                self.Delet_All_Basket_Button = tk.Button(self.right_frame, text='Delete My Basket', command=self.Delete_All, font=("Arial", 11), bg=second_color, fg=main_color)
                self.Delet_All_Basket_Button.pack(ipadx=5, ipady=5, padx=0, pady=60)
                self.Pay_Button.pack(ipadx=5, ipady=0, padx=0, pady=0)
            else :
                self.SignInfo = tk.Label(self.right_frame, text="Already Loged In ! \n What a smart customer ;)", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.SignInfo.pack(ipadx=5, ipady=5, padx=0, pady=20)
                self.Delet_All_Basket_Button = tk.Button(self.right_frame, text='Delete My Basket', command=self.Delete_All, font=("Arial", 11), bg=second_color, fg=main_color)
                self.Delet_All_Basket_Button.pack(ipadx=5, ipady=5, padx=0, pady=60)
                self.Pay_Button.pack(ipadx=5, ipady=0, padx=0, pady=0)

        elif (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B!=None):
            for i in range(2):  
                self.Total_Price_display=0
                self.Price_display=0
                if i==0: self.Display_Flight = Actual_Basket.Outbound_Flight_B
                else : self.Display_Flight = Actual_Basket.Inbound_Flight_B
                # Create a canvas widget
                self.canvas = tk.Canvas(self.left_frame, width=750, height=200, bg=main_color, highlightthickness=0, borderwidth=0)
                self.canvas.pack(padx=25, pady=10, side=tk.TOP, fill=tk.X)
                # Draw a rectangle on the canvas
                self.canvas.create_rectangle(0, 0, 750, 200, outline='black', width=2)
                
                # Print information in the rectangle
                self.canvas.create_text(280, 30, anchor='nw', text="Flight Number: "+str(self.Display_Flight.Flight_Number), font=("Arial", 10))
                self.canvas.create_text(280, 50, anchor='nw', text="Departure: "+str(self.Display_Flight.Departure_Airport), font=("Arial", 10))
                self.canvas.create_text(280, 70, anchor='nw', text="Arrival: "+str(self.Display_Flight.Arrival_Airport), font=("Arial", 10))
                if Actual_Search.Passengers == 1:
                    self.Total_Price_display=float(self.Display_Flight.Price)*Actual_Search.Class_Type
                else :
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=(float(self.Display_Flight.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type
                self.Price_display=round(float(self.Display_Flight.Price)*Actual_Search.Class_Type,2)
                if (self.Display_Flight.Discount != 0) & Actual_Customer.LogOrNot==True:
                    if Actual_Search.Passengers == 1:
                        self.Total_Price_display=float(self.Display_Flight.Price)*Actual_Search.Class_Type*(1-self.Display_Flight.Discount)
                    else :
                        for j in range(Actual_Search.Passengers):
                            self.Total_Price_display+=(float(self.Display_Flight.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-self.Display_Flight.Discount)
                    self.Price_display=round(float(self.Display_Flight.Price)*Actual_Search.Class_Type*(1-self.Display_Flight.Discount),2)
                self.canvas.create_text(660, 30, anchor='ne', text=str(self.Total_Price_display)+"£", font=("Arial", 15))
                self.canvas.create_text(660, 60, anchor='ne', text="Adult Price: "+str(self.Price_display)+"£", font=("Arial", 10))
                self.canvas.create_text(280, 110, anchor='nw', text="Departure Time: "+str(self.Display_Flight.Departure_Time), font=("Arial", 10))
                self.canvas.create_text(480, 110, anchor='nw', text="Arrival Time: "+str(self.Display_Flight.Arrival_Time), font=("Arial", 10))
                #images
                image_name = "./images/Flights_Images/"+(str(self.Display_Flight.Arrival_Airport).replace(' ', '_'))+".png"
                bg_image_rep_one = Image.open(image_name)
                bg_photo_rep_one = ImageTk.PhotoImage(bg_image_rep_one)
                # Créer un canevas pour afficher l'image du logo
                canvas_rep_one = tk.Canvas(self.canvas, width=261, height=bg_image_rep_one.height, highlightthickness=0,borderwidth=0)
                canvas_rep_one.place(x=10,y=10)
                canvas_rep_one.create_image(0, 0, anchor=tk.NW, image=bg_photo_rep_one)
                canvas_rep_one.image = bg_photo_rep_one
                bg_image_rep_one.close()
                bg_image_two = Image.open("./images/bin.png")
                bg_photo_two = ImageTk.PhotoImage(bg_image_two)
                # Créer un canevas pour afficher l'image du logo
                canvas_two = tk.Canvas(self.canvas, width=bg_image_two.width, height=bg_image_two.height, highlightthickness=0,borderwidth=0)
                canvas_two.place(x=720,y=170)
                canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
                canvas_two.image = bg_photo_two
                bg_image_two.close()
                canvas_two.bind("<Button-1>", lambda event, param=i+1: self.Delete(event, param))

            self.Total_Price_display=0
            if Actual_Search.Passengers == 1:
                if Actual_Basket.Inbound_Flight_B==None: self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type)
                else : self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type+(Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Class_Type)
            else :
                if Actual_Basket.Inbound_Flight_B==None:
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type)
                else : 
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type+((Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type)
            if (Actual_Basket.Outbound_Flight_B.Discount != 0) & Actual_Customer.LogOrNot==True:
                if Actual_Search.Passengers == 1:
                    if Actual_Basket.Inbound_Flight_B==None: self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount))
                    else : self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount)+(Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Inbound_Flight_B.Discount))
                else :
                    if Actual_Basket.Inbound_Flight_B==None:
                        for j in range(Actual_Search.Passengers):
                            self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount))
                    else : 
                        for j in range(Actual_Search.Passengers):
                            self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount)+((Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Inbound_Flight_B.Discount))
            self.Total_Price_B = round(self.Total_Price_display,2)
            self.Total_Price_B_Label = tk.Label(self.right_frame, text=str(self.Total_Price_B)+"£", font=("Arial", 15), bg=main_color, fg=fourth_color)
            self.Total_Basket_Price = tk.Label(self.right_frame, text="Total Basket Price :", font=("Arial", 11), bg=main_color, fg=fourth_color)
            self.Total_Basket_Price.pack(ipadx=5, ipady=5, padx=10, pady=0)
            self.Total_Price_B_Label.pack(ipadx=5, ipady=5, padx=10, pady=10)

            if Actual_Customer.LogOrNot == False:
                self.SignInfo = tk.Label(self.right_frame, text="Sign In or Sign Up for faster order", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.Sign_Button = tk.Button(self.right_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
                self.SignInfo.pack(ipadx=5, ipady=5, padx=0, pady=20)
                self.Sign_Button.pack(ipadx=5, ipady=5, padx=0, pady=0)
                self.Delet_All_Basket_Button = tk.Button(self.right_frame, text='Delete My Basket', command=self.Delete_All, font=("Arial", 11), bg=second_color, fg=main_color)
                self.Delet_All_Basket_Button.pack(ipadx=5, ipady=5, padx=0, pady=60)
                self.Pay_Button.pack(ipadx=5, ipady=0, padx=0, pady=0)
            else :
                self.SignInfo = tk.Label(self.right_frame, text="Already Loged In ! \n What a smart customer ;)", font=("Arial", 10), bg=main_color, fg=fourth_color)
                self.SignInfo.pack(ipadx=5, ipady=5, padx=0, pady=20)
                self.Delet_All_Basket_Button = tk.Button(self.right_frame, text='Delete My Basket', command=self.Delete_All, font=("Arial", 11), bg=second_color, fg=main_color)
                self.Delet_All_Basket_Button.pack(ipadx=5, ipady=5, padx=0, pady=60)
                self.Pay_Button.pack(ipadx=5, ipady=0, padx=0, pady=0)
        else : pass 


    def Hide_Button_1(self, empty):
        Launch_Home_Page()
    
    def Delete(self, event, param):
        print("Delete")
        if param==0:
            Actual_Search.ReturnOrNot=False
            Actual_Basket.Delete_Outbound()
            Actual_Outbound_Flight.Reset_Outbound_Flight()
            print(Actual_Outbound_Flight.Flight_Number)
            Actual_Inbound_Flight.Reset_Inbound_Flight()
            Actual_Search.Reset_Search()
        elif param==1:
            print(Actual_Inbound_Flight.Price)
            Actual_Basket.Complete_Basket(Actual_Inbound_Flight, None, False)
            Actual_Outbound_Flight.Complete_Outbound_Flight(Actual_Basket.Outbound_Flight_B.Flight_ID, Actual_Basket.Outbound_Flight_B.Airline_Name, Actual_Basket.Outbound_Flight_B.Flight_Number, Actual_Basket.Outbound_Flight_B.Departure_Airport, Actual_Basket.Outbound_Flight_B.Departure_Date, Actual_Basket.Outbound_Flight_B.Departure_Time, Actual_Basket.Outbound_Flight_B.Arrival_Airport, Actual_Basket.Outbound_Flight_B.Arrival_Date, Actual_Basket.Outbound_Flight_B.Arrival_Time, Actual_Basket.Outbound_Flight_B.Flight_Duration, Actual_Basket.Outbound_Flight_B.Price, Actual_Basket.Outbound_Flight_B.Discount, Actual_Basket.Outbound_Flight_B.Seats_Left, Actual_Basket.Outbound_Flight_B.Seats_Capacity, Actual_Basket.Outbound_Flight_B.Class_Type, Actual_Basket.Outbound_Flight_B.Passengers, Actual_Basket.Outbound_Flight_B.Passengers_Type_Number)
            print(Actual_Outbound_Flight.Flight_Number)
            print(Actual_Basket.Outbound_Flight_B.Flight_Number)
            #Actual_Inbound_Flight.Reset_Inbound_Flight()
            Actual_Search.ReturnOrNot=True
            Actual_Search.From=Actual_Outbound_Flight.Departure_Airport
            Actual_Search.To=Actual_Outbound_Flight.Arrival_Airport
            Actual_Search.Departure_Date=Actual_Search.Return_Date
        else:
            Actual_Search.ReturnOrNot=True
            Actual_Inbound_Flight.Reset_Inbound_Flight()
            Actual_Basket.Delete_Inbound()
        Launch_Basket_Page()

    def Delete_All(self):
        print("Delete All")
        Actual_Basket.Clear_Basket()
        Actual_Outbound_Flight.Reset_Outbound_Flight()
        Actual_Inbound_Flight.Reset_Inbound_Flight()
        Actual_Search.Reset_Search()
        Launch_Basket_Page()

    def Book_Return(self):
        Actual_Search.Need_Return=True
        Actual_Search.ReturnOrNot=True
        Launch_Purchase_Results_Page()

##------------------------------------------------------------------------------------------------------##
##----------------------------------------------Payment Page--------------------------------------------##
##------------------------------------------------------------------------------------------------------##


class Payment_Page():
    def __init__(self, main_window):
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.third_top_frame = tk.Frame(main_window, bg=main_color)
        self.fourth_top_frame = tk.Frame(main_window, bg=main_color)
        self.left_frame = tk.Frame(main_window, bg=main_color)
        self.right_frame = tk.Frame(main_window, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two
        #Money
        bg_image_three = Image.open("./images/debit-card.png")
        bg_photo_three = ImageTk.PhotoImage(bg_image_three)
        # Créer un canevas pour afficher l'image du logo
        canvas_three = tk.Canvas(main_window, width=bg_image_three.width, height=bg_image_three.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_three.place(x=675,y=85)
        canvas_three.create_image(0, 0, anchor=tk.NW, image=bg_photo_three)
        canvas_three.image = bg_photo_three

        
        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button_1)
        self.Page_Title= tk.Label(self.second_top_frame, text=" Time to Pay!", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.Info_Payment= tk.Label(self.third_top_frame, text="Please enter your payment information", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Info_Payment_2= tk.Label(self.fourth_top_frame, text="You will recieve an e-mail with your recap order and your Tickets", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Space_Title_1 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_2 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_3 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_4 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)
        self.Space_Title_5 = tk.Label(self.right_frame, text=" ", font=("Arial", 10), bg=main_color)

        # Buttons
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=10)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.third_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.fourth_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #Display the title
        #Display the Page Title
        self.Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=5, side=tk.LEFT)
        #Display the Info Title
        self.Info_Payment.pack(ipadx=5, ipady=5, padx=0, pady=0, side=tk.LEFT)
        self.Info_Payment_2.pack(ipadx=5, ipady=5, padx=0, pady=0, side=tk.LEFT)
        self.Total_Price_display=0
        # Create a canvas widget
        self.canvas_left = tk.Canvas(self.left_frame, width=550, height=300, bg=main_color, highlightthickness=0, borderwidth=0)
        #self.canvas.bind("<Button-1>", lambda event, param=Display_Flight.Flight_ID : self.FLight_Select(event, param))
        self.canvas_left.pack(padx=25, pady=30, side=tk.TOP, fill=tk.X)
         # Create a canvas widget
        self.canvas_right = tk.Canvas(self.right_frame, width=300, height=400, bg=main_color, highlightthickness=0, borderwidth=0)
        #self.canvas.bind("<Button-1>", lambda event, param=Display_Flight.Flight_ID : self.FLight_Select(event, param))
        self.canvas_right.pack(padx=25, pady=0, side=tk.TOP, fill=tk.X)

        #Inputs
        self.Card_Number_Title = tk.Label(self.canvas_left, text="Card Number", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Card_Number = tk.Entry(self.canvas_left, width=30, bg=main_color, fg=fourth_color, font=("Arial", 12))
        self.Card_Date_Title = tk.Label(self.canvas_left, text="Expierd Date", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Card_Date = DateEntry(self.canvas_left, date_pattern='y-mm-dd', width=10, bg=main_color, fg=fourth_color, font=("Arial", 12))
        self.Card_Code_Title = tk.Label(self.canvas_left, text="Card Code", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Card_Code = tk.Entry(self.canvas_left, width=10, bg=main_color, fg=fourth_color, font=("Arial", 12))
        self.Card_Name_Title = tk.Label(self.canvas_left, text="Card Name", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Card_Name = tk.Entry(self.canvas_left, width=30, bg=main_color, fg=fourth_color, font=("Arial", 12))
        self.New_Email_Info = tk.Label(self.canvas_right, text="You will recieve your bill and your tickets on this email", font=("Arial", 8), bg=main_color, fg=fourth_color)
        self.New_Email_Title = tk.Label(self.canvas_right, text="E-mail", font=("Arial", 10), bg=main_color, fg=fourth_color)
        self.Email = tk.Entry(self.canvas_right, width=30, bg=main_color, fg=fourth_color, font=("Arial", 10))
        if Actual_Customer.LogOrNot == True:
            self.Card_Name.insert(0, Actual_Customer.CardName)
            self.Card_Number.insert(0, Actual_Customer.CardNumber)
            self.Card_Date.delete(0, tk.END)
            self.Card_Date.insert(0, Actual_Customer.CardDate)
            self.Email.insert(0, Actual_Customer.Email)
            self.SignInfo = tk.Label(self.canvas_right, text="Already Loged In !    \n What a smart customer ;)", font=("Arial", 8), bg=main_color, fg=fourth_color)
        else :
            self.Card_Number.insert(0, "0000 0000 0000 0000")
            self.SignInfo = tk.Label(self.canvas_right, text="Sign In or Sign Up for faster order", font=("Arial", 8), bg=main_color, fg=fourth_color)
            self.Sign_Button = tk.Button(self.canvas_right, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
        #Basket Info 
        self.OutB_From = tk.Label(self.canvas_right, text=Actual_Basket.Outbound_Flight_B.Departure_Airport, font=("Arial", 11), bg=main_color, fg=fourth_color)
        self.OutB_To = tk.Label(self.canvas_right, text=Actual_Basket.Outbound_Flight_B.Arrival_Airport, font=("Arial", 11), bg=main_color, fg=fourth_color)
        self.OutB_Date = tk.Label(self.canvas_right, text=Actual_Basket.Outbound_Flight_B.Departure_Date, font=("Arial", 11), bg=main_color, fg=fourth_color)
        self.OutB_Passengers = tk.Label(self.canvas_right, text="x"+str(Actual_Basket.Outbound_Flight_B.Passengers), font=("Arial", 11), bg=main_color, fg=fourth_color)
        if Actual_Basket.Inbound_Flight_B!=None:
            self.InB_From = tk.Label(self.canvas_right, text=Actual_Basket.Inbound_Flight_B.Departure_Airport, font=("Arial", 11), bg=main_color, fg=fourth_color)
            self.InB_To = tk.Label(self.canvas_right, text=Actual_Basket.Inbound_Flight_B.Arrival_Airport, font=("Arial", 11), bg=main_color, fg=fourth_color)
            self.InB_Date = tk.Label(self.canvas_right, text=Actual_Basket.Inbound_Flight_B.Departure_Date, font=("Arial", 11), bg=main_color, fg=fourth_color)
            self.InB_Passengers = tk.Label(self.canvas_right, text="x"+str(Actual_Basket.Inbound_Flight_B.Passengers), font=("Arial", 11), bg=main_color, fg=fourth_color)
        if Actual_Search.Passengers == 1:
            if Actual_Basket.Inbound_Flight_B==None: self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type)
            else : self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type+(Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Class_Type)
        else :
            if Actual_Basket.Inbound_Flight_B==None:
                for j in range(Actual_Search.Passengers):
                    self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type)
            else : 
                for j in range(Actual_Search.Passengers):
                    self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type+((Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type)
        if (Actual_Basket.Outbound_Flight_B.Discount != 0) & Actual_Customer.LogOrNot==True:
            if Actual_Search.Passengers == 1:
                if Actual_Basket.Inbound_Flight_B==None: self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount))
                else : self.Total_Price_display=float((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount)+(Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Class_Type*(1-Actual_Basket.Inbound_Flight_B.Discount))
            else :
                if Actual_Basket.Inbound_Flight_B==None:
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount))
                else : 
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=float(((Actual_Basket.Outbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Outbound_Flight_B.Discount)+((Actual_Basket.Inbound_Flight_B.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type*(1-Actual_Basket.Inbound_Flight_B.Discount))
        self.Total_Price = round(self.Total_Price_display,2)
        self.Total_Price_Label = tk.Label(self.canvas_right, text=str(self.Total_Price)+"£", font=("Arial", 15), bg=main_color, fg=fourth_color)
        self.Total_Basket_Price = tk.Label(self.canvas_right, text="Total Basket Price", font=("Arial", 11), bg=main_color, fg=fourth_color)
        
        self.Pay_Button = tk.Button(self.canvas_left, text='Proced Payment', command=self.Pay, font=("Arial", 15), bg=third_color, fg=main_color)

        # Draw a rectangle on the canvas
        self.canvas_left.create_rectangle(0, 0, 550, 300, outline='black', width=2)
        # Draw a rectangle on the canvas
        self.canvas_right.create_rectangle(0, 0, 300, 380, outline='black', width=2)
        #Card Number
        self.Card_Number_Title.place(x=35, y=30)
        self.Card_Number.place(x=35, y=55)
        #Card Date
        self.Card_Date_Title.place(x=35, y=90)
        self.Card_Date.place(x=35, y=115)
        #Card Code
        self.Card_Code_Title.place(x=250, y=90)
        self.Card_Code.place(x=250, y=115)
        #Card Name
        self.Card_Name_Title.place(x=35, y=150)
        self.Card_Name.place(x=35, y=175)
        #Pay-pro
        bg_image_four = Image.open("./images/pay-pro.png")
        bg_photo_four = ImageTk.PhotoImage(bg_image_four)
        # Créer un canevas pour afficher l'image du logo
        canvas_four = tk.Canvas(self.canvas_left, width=bg_image_four.width, height=bg_image_four.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_four.place(x=500,y=10)
        canvas_four.create_image(0, 0, anchor=tk.NW, image=bg_photo_four)
        canvas_four.image = bg_photo_four
        #master Card
        bg_image_five = Image.open("./images/mastercard.png")
        bg_photo_five = ImageTk.PhotoImage(bg_image_five)
        # Créer un canevas pour afficher l'image du logo
        canvas_five = tk.Canvas(self.canvas_left, width=bg_image_five.width, height=bg_image_five.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_five.place(x=40,y=220)
        canvas_five.create_image(0, 0, anchor=tk.NW, image=bg_photo_five)
        canvas_five.image = bg_photo_five
        #Visa Card
        bg_image_six = Image.open("./images/visa.png")
        bg_photo_six = ImageTk.PhotoImage(bg_image_six)
        # Créer un canevas pour afficher l'image du logo
        canvas_six = tk.Canvas(self.canvas_left, width=bg_image_six.width, height=bg_image_six.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_six.place(x=120,y=210)
        canvas_six.create_image(0, 0, anchor=tk.NW, image=bg_photo_six)
        canvas_six.image = bg_photo_six
        
        self.Pay_Button.place(x=360, y=220)

        #Right Canvas
        #Email
        self.New_Email_Info.place(x=10, y=10)
        self.New_Email_Title.place(x=10, y=40)
        self.Email.place(x=10, y=65)
        self.SignInfo.place(x=10, y=95)
        if Actual_Customer.LogOrNot == False: self.Sign_Button.place(x=10, y=120)
        # Add a Canvas widget for drawing the line
        self.line_canvas_two = tk.Canvas(self.canvas_right, height=3, bg=second_color)
        self.line_canvas_two.config(highlightthickness=0, borderwidth=0)
        self.line_canvas_two.place(x=12, y=155, width=275)
        # Create a line under top_frame
        self.line_canvas_two.create_line(5, 2, 150, 2, fill=second_color)
        #Basket Info
        self.OutB_From.place(x=10, y=180)
        #plane
        bg_image_seven = Image.open("./images/black-planeress.png")
        bg_photo_seven = ImageTk.PhotoImage(bg_image_seven)
        # Créer un canevas pour afficher l'image du logo
        canvas_seven = tk.Canvas(self.canvas_right, width=bg_image_seven.width, height=bg_image_seven.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_seven.place(x=97,y=182)
        canvas_seven.create_image(0, 0, anchor=tk.NW, image=bg_photo_seven)
        canvas_seven.image = bg_photo_seven
        self.OutB_To.place(x=130, y=180)
        self.OutB_Date.place(x=10, y=210)
        bg_image_height = Image.open("./images/passenger.png")
        bg_photo_height = ImageTk.PhotoImage(bg_image_height)
        # Créer un canevas pour afficher l'image du logo
        canvas_height = tk.Canvas(self.canvas_right, width=bg_image_height.width, height=bg_image_height.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_height.place(x=130,y=212)
        canvas_height.create_image(0, 0, anchor=tk.NW, image=bg_photo_height)
        canvas_height.image = bg_photo_height
        self.OutB_Passengers.place(x=150, y=210)
        if Actual_Basket.Inbound_Flight_B!=None:
            self.InB_From.place(x=10, y=250)
            bg_image_nine = Image.open("./images/black-planeress.png")
            bg_photo_nine = ImageTk.PhotoImage(bg_image_nine)
            # Créer un canevas pour afficher l'image du logo
            canvas_nine = tk.Canvas(self.canvas_right, width=bg_image_nine.width, height=bg_image_nine.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_nine.place(x=97,y=252)
            canvas_nine.create_image(0, 0, anchor=tk.NW, image=bg_photo_nine)
            canvas_nine.image = bg_photo_nine
            self.InB_To.place(x=130, y=250)
            self.InB_Date.place(x=10, y=280)
            bg_image_ten = Image.open("./images/passenger.png")
            bg_photo_ten = ImageTk.PhotoImage(bg_image_ten)
            # Créer un canevas pour afficher l'image du logo
            canvas_ten = tk.Canvas(self.canvas_right, width=bg_image_ten.width, height=bg_image_ten.height, bg=main_color,highlightthickness=0,borderwidth=0)
            canvas_ten.place(x=130,y=282)
            canvas_ten.create_image(0, 0, anchor=tk.NW, image=bg_photo_ten)
            canvas_ten.image = bg_photo_ten
            self.InB_Passengers.place(x=150, y=280)
        self.Total_Basket_Price.place(x=10, y=320)
        self.Total_Price_Label.place(x=10, y=340)
                

        #Buttons

    def Hide_Button_1(self, empty):
        Launch_Home_Page()
    
    def Pay(self):
        # Verify all inputs
        if (self.Card_Number.get()!="")&(self.Card_Date.get()!="")&(self.Card_Code.get()!="")&(self.Card_Name.get()!="")&(self.Email.get()!=""):
            if(int(self.Card_Number.get())>999999999999999)&(int(self.Card_Number.get())<10000000000000000):
                if(int(self.Card_Code.get())>99)&(int(self.Card_Code.get())<1000):
                    # Check if the email is a valid email address using a regular expression
                    if not re.match(r'^[\w\.-]+@[\w\.-]+$', self.Email.get()):
                        # Invalid email format, show an error message
                        tk.messagebox.showinfo('Error', 'Invalid email format')
                    else: 
                        #if(self.Card_Date.get()<str(datetime.date.today())):
                            #message box 
                            #tk.messagebox.showerror("Error", "Please enter a valid date")
                        #else :
                        if (int(self.Card_Code.get())!=int(Actual_Customer.CardCode)) & (Actual_Customer.CardCode != 0):
                            #message box
                            print("ACtual : "+str(Actual_Customer.CardCode)+"\nInput : "+self.Card_Code.get()+"\n")
                            tk.messagebox.showerror("Error", "WRONG card code")
                        else :
                            print("Pay")
                            print(Actual_Customer.CustomerID)
                            Actual_Basket.Create_Res(self.Email.get(), Actual_Customer.CustomerID, self.Card_Name.get())
                            Actual_Basket.Clear_Basket()
                            Actual_Outbound_Flight.Reset_Outbound_Flight()
                            Actual_Inbound_Flight.Reset_Inbound_Flight()
                            Actual_Search.Reset_Search()
                            Launch_Thanks_Page()
                else :
                    #message box 
                    tk.messagebox.showerror("Error", "Please enter a valid card code")
            else :
                #message box 
                tk.messagebox.showerror("Error", "Please enter a valid Card Number")
        else :
            #message box 
            tk.messagebox.showerror("Error", "Please fill all the inputs")


##------------------------------------------------------------------------------------------------------##
##----------------------------------------------Thanks Page-----------------------------------------##
##------------------------------------------------------------------------------------------------------##

class Thanks_Page():
    def __init__(self, main_window):
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.third_top_frame = tk.Frame(main_window, bg=main_color)
        self.fourth_top_frame = tk.Frame(main_window, bg=main_color)

        #Logo
        bg_image_two = Image.open("./images/photologo_re.png")
        bg_photo_two = ImageTk.PhotoImage(bg_image_two)
        # Créer un canevas pour afficher l'image du logo
        canvas_two = tk.Canvas(self.top_frame, width=bg_image_two.width, height=bg_image_two.height, bg=main_color,highlightthickness=0,borderwidth=0)
        canvas_two.place(x=410,y=-5)
        canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
        canvas_two.image = bg_photo_two

        #Title
        self.Home_Page_Title = tk.Label(self.top_frame, text="OOP Air Line", font=("Arial", 20), bg=main_color, fg=fourth_color)
        self.Home_Page_Title.bind("<Button-1>", self.Hide_Button_1)
        self.Page_Title= tk.Label(self.second_top_frame, text=" Thanks for your order!", font=("Arial", 18), bg=main_color, fg=third_color)
        self.Info_Payment= tk.Label(self.third_top_frame, text="You will recieve an e-mail with your recap order and your Tickets", font=("Arial", 13), bg=main_color, fg=fourth_color)
        self.Info_Payment_2= tk.Label(self.fourth_top_frame, text="We hope to see you again soon", font=("Arial", 13), bg=main_color, fg=fourth_color)

        # Buttons
        if Actual_Customer.LogOrNot == False:
            self.LogIn_Button = tk.Button(self.top_frame, text='Sign In or Sign Up', command=Launch_LogIn_Page, bg=second_color)
        else :
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_My_Account, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Home_Button = tk.Button(self.fourth_top_frame, text='Home', command=Launch_Home_Page, bg=third_color)

        # Pack all wigets
        #Frame
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.LogIn_Button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=15, pady=12)
        # Pack the 'Advanced Search' button to the right (east)
        self.Menu_Button.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=15, pady=12)
        #Display the title
        self.Home_Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=10)
        # Add a Canvas widget for drawing the line
        self.line_canvas = tk.Canvas(main_window, height=3, bg=second_color)
        self.line_canvas.config(highlightthickness=0, borderwidth=0)
        self.line_canvas.pack(fill=tk.X)
        # Create a line under top_frame
        self.line_canvas.create_line(5, 2, main_window.winfo_screenwidth(), 2, fill=second_color)
        self.second_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.third_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.fourth_top_frame.pack(side=tk.TOP, fill=tk.X)
        #Display the title
        #Display the Page Title
        self.Page_Title.pack(ipadx=5, ipady=5, padx=0, pady=50)
        #Display the Info Title
        self.Info_Payment.pack(ipadx=5, ipady=5, padx=0, pady=10)
        self.Info_Payment_2.pack(ipadx=5, ipady=5, padx=0, pady=10)
        self.Total_Price_display=0
        # Home Button
        self.Home_Button.pack(ipadx=5, ipady=5, padx=0, pady=10)

    def Hide_Button_1(self, empty):
        Launch_Home_Page()

##------------------------------------------------------------------------------------------------------##
##---------------------------------------------End Of Class Part----------------------------------------##
##------------------------------------------------------------------------------------------------------##

#---------------------## ALL THE FUNCTIONS ##---------------------#


def Launch_Home_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Home_Page(main_window)

def Launch_LogIn_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
        plt.close('all')
    LogIn_Page(main_window)

def Launch_SignUp_First_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    SignUp_First_Page(main_window)

def Launch_SignUp_Second_Page(Email, Password):
    for widget in main_window.winfo_children():
        widget.destroy()
    SignUp_Second_Page(main_window, Email, Password)

def Launch_Menu_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
        plt.close('all')
    Menu_Page(main_window)

def Launch_Purchase_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
        plt.close('all')
    Purchase_Page(main_window)

def Launch_Info_Passengers():
    for widget in main_window.winfo_children():
        widget.destroy()
    Info_Passengers(main_window)

def Launch_Purchase_Results_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
        plt.close('all')
    Purchase_Results_Page(main_window)

def Launch_Flight_Results_Page():
    print(Actual_Outbound_Flight.Flight_Number)
    for widget in main_window.winfo_children():
        widget.destroy()
    Flight_Results_Page(main_window)

def Launch_Basket_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
        plt.close('all')
    Basket_Page(main_window)

def Launch_Payment_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Payment_Page(main_window)

def Launch_My_Account():
    for widget in main_window.winfo_children():
        widget.destroy()
        plt.close('all')
    My_Account_Page(main_window)

def Launch_Thanks_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Thanks_Page(main_window)

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
Actual_Outbound_Flight = AF.Outbound_Flight()
Actual_Inbound_Flight = AF.Inbound_Flight()
Actual_Basket = AB.Basket()

#Light Theme
main_color_light="#fff7ea"
second_color_light="#722a39"
third_color_light="#375c4f"
fourth_color_light="#3f171f"
def_color_light="#252525"
#Dark Theme
main_color_dark='#292929'
second_color_dark="#9c4c5b"
third_color_dark="#017368"
fourth_color_dark="#cf6679"
def_color_drak="#fff9ea"

#Theme
main_color=main_color_light
second_color=second_color_light
third_color=third_color_light
fourth_color=fourth_color_light
def_color=def_color_light
main_window.configure(bg=main_color, highlightthickness=0, borderwidth=0, relief='ridge')
main_window.fg=def_color

Home_Page(main_window)
tk.mainloop()
