#First Page of the Project test repository
import pymysql
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import DateEntry
import dbconnect
import Actual_Customer as AC
import Actual_Search as AS
import Actual_Flight as AF
import My_Basket as AB
#import LogInPage as LP
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
        canvas_one = tk.Canvas(self.right_frame, width=bg_image_one.width, height=bg_image_one.height)
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
        self.Home_Page_Title.pack(ipadx=0, ipady=5, padx=10, pady=10)
        #Display the Buy Now Button
        self.Buy_Now_Button.pack(ipadx=5, ipady=5, padx=200, pady=10)
        #Display the text
        self.Pres_OOPAirLine.pack(ipadx=5, ipady=5, padx=20, pady=10)

    def Hide_Button_1(self, empty):
        Launch_Basket_Page()

class LogIn_Page():
    def __init__(self, main_window):
        self.db=dbconnect.DBHelper()
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
                Launch_Home_Page()
            else:
                # Login failed, show an error message
                # You can display an error message using a messagebox or a label
                tk.messagebox.showinfo('Error', 'Invalid email or password')
                #error_label = tk.Label(self.middle_frame, text="Invalid email or password", font=("Arial", 10), fg="red")
                #error_label.pack()

    def Hide_Button_1(self, empty):
        Launch_Basket_Page()
    
    def Hide_Button(self, empty):
        Launch_Home_Page()

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
            self.LogIn_Button = tk.Button(self.middle_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color, fg=main_color)
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
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Search_Button = tk.Button(self.fourth_top_frame, text='Search', command=self.Search_Flight, font=("Arial", 15), bg=third_color, fg=main_color)
        self.Search_Button.config(height=1, width=10)

        #Input
        self.From_Input = tk.Entry(self.second_top_frame)
        self.To_Input = tk.Entry(self.second_top_frame)
        self.Departure_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        #self.Return_Input_Radio = tk.Radiobutton(self.second_top_frame, text="Return", value=1)
        self.Return_Input = DateEntry(self.second_top_frame, date_pattern='y-mm-dd')
        self.Passengers_Input = tk.Spinbox(self.third_top_frame, from_=1, to=10)
        self.Class_Input = ttk.Combobox(self.third_top_frame, values=["Economy", "Business", "First Class"])
        if Actual_Search.ReturnOrNot==False:
            self.From_Input.insert(0, "Paris")
            self.To_Input.insert(0, "New York")
            #Remove for final version
            self.Class_Input.delete(0, tk.END)
            self.Class_Input.insert(0, "First Class")
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
        #Display The Radio Button
        #self.Return_Input_Radio.grid(row=2, column=3, padx=10, pady=3, ipadx=5, ipady=0)
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
            if self.Return!='':
                try :
                    if (self.Departure > self.Return)&(Actual_Search.Need_Return==True):
                        tk.messagebox.showinfo('Error', 'Return date must be after departure date')
                    else :
                        if (self.Passengers == int(self.Passengers)) & (self.Passengers > 1) & (self.Passengers < 11):
                            if (self.Class == "Economy") or (self.Class == "Business") or (self.Class =="First Class"):
                                if (self.From == str(self.From)) & (self.To == str(self.To)):
                                    print("Search Flight")
                                    # Dates are valid
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
            else :
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
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color)
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
        #for i in range(self.p):
            #self.pass_type.append(tk.StringVar())
            
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
                #print(self.pass_type[i].get())
                Actual_Search.Passengers_Type[i]=self.pass_type[i].get()
                if self.pass_type[i].get() == "Adult":
                    Actual_Search.Passengers_Type_Number[i]=1
                elif self.pass_type[i].get() == "Child":
                    Actual_Search.Passengers_Type_Number[i]=0.60
                elif self.pass_type[i].get() == "Senior":
                    Actual_Search.Passengers_Type_Number[i]=0.80
                elif self.pass_type[i].get() == "Student":
                    Actual_Search.Passengers_Type_Number[i]=0.75
            print(Actual_Search.Passengers_Type)
            print(Actual_Search.Passengers_Type_Number)
            Launch_Purchase_Results_Page()

    def Hide_Button(self, empty):
        Launch_Home_Page()
    
    def Hide_Button_1(self, empty):
        Launch_Basket_Page()

    def Hide_Button_2(self, empty):
        Launch_Purchase_Page()


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
        self.Page_Title= tk.Label(self.display_frame, text=" Choose your Flight Hour", font=("Arial", 15), bg=main_color, fg=fourth_color)
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
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color)
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
        self.Page_Title.pack(ipadx=5, ipady=5, padx=450, pady=30)
        #Display the Go Back Title
        self.GoBack_Title.place(x=22, y=47)

        #Make search
        self.Search_Results_Outbound = [None] * 5

        for i in range(5):
            self.Price_display=0
            self.Total_Price_display=0
            print(Actual_Search.ReturnOrNot)
            if Actual_Search.ReturnOrNot == True:
                self.Search_Results_Outbound[i] = Actual_Search.Search_Inbound()
            else:
                self.Search_Results_Outbound[i] = Actual_Search.Search_Outbound()
            
            # Create a canvas widget
            self.canvas = tk.Canvas(self.display_frame, width=850, height=200, highlightthickness=0 ,borderwidth=0, bg=main_color)
            self.canvas.bind("<Button-1>", lambda event, param=self.Search_Results_Outbound[i]: self.FLight_Select(event, param))
            self.canvas.pack(padx=65, pady=15, side=tk.TOP, fill=tk.X)
            # Draw a rectangle on the canvas
            self.canvas.create_rectangle(0, 0, 950, 200, outline='black', width=2)

            # Print information in the rectangle
            #self.canvas.create_text(20, 20, anchor='nw', text="Flight Number: "+str(self.Search_Results_Outbound[i]), font=("Arial", 10))
            self.canvas.create_text(380, 40, anchor='nw', text="Flight Number: "+str(self.Search_Results_Outbound[i][0]['FlightNumber']), font=("Arial", 10))
            self.canvas.create_text(380, 60, anchor='nw', text="Departure: "+str(self.Search_Results_Outbound[i][0]['Departure']), font=("Arial", 10))
            self.canvas.create_text(380, 80, anchor='nw', text="Arrival: "+str(self.Search_Results_Outbound[i][0]['Arrival']), font=("Arial", 10))
            if Actual_Search.Passengers == 1:
                self.Total_Price_display=float(self.Search_Results_Outbound[i][0]['Price'])*Actual_Search.Class_Type
            else :
                for j in range(Actual_Search.Passengers):
                    self.Total_Price_display+=(float(self.Search_Results_Outbound[i][0]['Price'])*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type
            self.Price_display=round(self.Price_display, 2)
            self.canvas.create_text(760, 40, anchor='ne', text=str(self.Total_Price_display)+"£", font=("Arial", 15))
            self.Price_display=round(float(self.Search_Results_Outbound[i][0]['Price'])*Actual_Search.Class_Type,2)
            self.canvas.create_text(760, 70, anchor='ne', text="Adult Price: "+str(self.Price_display)+"£", font=("Arial", 10))
            self.canvas.create_text(380, 120, anchor='nw', text="Departure Time: "+str(self.Search_Results_Outbound[i][0]['DepartureTime']), font=("Arial", 10))
            self.canvas.create_text(580, 120, anchor='nw', text="Arrival Time: "+str(self.Search_Results_Outbound[i][0]['ArrivalTime']), font=("Arial", 10))
            bg_image_rep = Image.open("./images/avion_res.png")
            bg_photo_rep = ImageTk.PhotoImage(bg_image_rep)
            # Créer un canevas pour afficher l'image du logo
            canvas_rep = tk.Canvas(self.canvas, width=bg_image_rep.width, height=bg_image_rep.height, highlightthickness=0,borderwidth=0)
            canvas_rep.place(x=10,y=10)
            canvas_rep.create_image(0, 0, anchor=tk.NW, image=bg_photo_rep)
            canvas_rep.image = bg_photo_rep
            bg_image_rep.close()
                

    def Hide_Button(self, empty):
        Launch_Home_Page()
    
    def Hide_Button_1(self, empty):
        Launch_Basket_Page()

    def Hide_Button_2(self, empty):
        Launch_Purchase_Page()
    
    def FLight_Select(self, event, param):
        #print("Time "+str(DepartureTime)+" Selected")
        #Actual_Search.Flight_Selected_Outbound=self.Search_Results_Outbound[param]
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


class Flight_Results_Page():
    def __init__(self, main_window):
        self.top_frame = tk.Frame(main_window, bg=main_color)
        self.second_top_frame = tk.Frame(main_window, bg=main_color)
        self.left_frame = tk.Frame(main_window, bg=main_color)
        self.right_frame = tk.Frame(main_window, bg=main_color)

        bg_image_one = Image.open("./images/avion_ress.png")
        bg_photo_one = ImageTk.PhotoImage(bg_image_one)
        # Créer un canevas pour afficher l'image de fond
        canvas = tk.Canvas(self.left_frame, width=bg_image_one.width, height=bg_image_one.height, bg=main_color, highlightthickness=0, borderwidth=0)
        canvas.pack(pady=15)
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo_one)
        canvas.image = bg_photo_one

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
        #Plane
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
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.AddBasket_Button = tk.Button(self.right_frame, text='Add to Basket', command=self.AddBasket, font=("Arial", 15), bg=third_color, fg=main_color)
        if (Actual_Basket.Outbound_Flight_B!=None)&(Actual_Basket.Inbound_Flight_B==None)&(Actual_Search.Need_Return==True):
            self.Chose_Return_Button = tk.Button(self.left_frame, text='Choose Return', command=Launch_Purchase_Results_Page, font=("Arial", 15), bg=third_color, fg=main_color)
        else:
            self.Chose_Return_Button = tk.Button(self.left_frame, text='Go to Basket', command=Launch_Basket_Page, font=("Arial", 15), bg=third_color, fg=main_color)
        #Info
        self.Flight_Title = tk.Label(self.right_frame, text="Flight Number: "+str(Actual_Outbound_Flight.Flight_Number), font=("Arial", 11), bg=main_color)
        self.Departure_Title = tk.Label(self.right_frame, text="Departure: "+str(Actual_Outbound_Flight.Departure_Airport), font=("Arial", 11), bg=main_color)
        self.Arrival_Title = tk.Label(self.right_frame, text="Arrival: "+str(Actual_Outbound_Flight.Arrival_Airport), font=("Arial", 11), bg=main_color)
        self.DepartureTime_Title = tk.Label(self.right_frame, text=str(Actual_Outbound_Flight.Departure_Time), font=("Arial", 15), bg=main_color)
        self.ArrivalTime_Title = tk.Label(self.right_frame, text=str(Actual_Outbound_Flight.Arrival_Time), font=("Arial", 15), bg=main_color)
        self.Duration_Title = tk.Label(self.right_frame, text="Duration: "+str(Actual_Outbound_Flight.Flight_Duration), font=("Arial", 11), bg=main_color)
        self.Price_Title = tk.Label(self.right_frame, text="Adult Price: "+str(Actual_Outbound_Flight.Price)+"£", font=("Arial", 11), bg=main_color)
        self.Total_Price=0

        if Actual_Search.Passengers == 1:
            self.Total_Price=float(Actual_Outbound_Flight.Price*Actual_Search.Class_Type)
        else :
            for j in range(Actual_Search.Passengers):
                self.Total_Price+=(float(Actual_Outbound_Flight.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type
        self.Total_Price_Title = tk.Label(self.right_frame, text="Total Price: "+str(self.Total_Price)+"£", font=("Arial", 15), bg=main_color)

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
        #Display the Space Title
        #self.Space_Title_1.pack(ipadx=5, ipady=5, padx=10, pady=10)
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
        #Display the Space Title
        #self.Space_Title_2.pack(ipadx=5, ipady=5, padx=10, pady=10)
        #Display the Add to basket Button
        self.AddBasket_Button.place(x=43, y=280)
        #Display the Choose Return Button
        if Actual_Basket.Outbound_Flight_B!=None:
            self.Chose_Return_Button.pack(ipadx=5, ipady=5, padx=0, pady=10)
    
    def Hide_Button(self, empty):
        Launch_Home_Page()

    def Hide_Button_1(self, empty):
        Launch_Basket_Page()
    
    def Hide_Button_2(self, empty):
        Launch_Purchase_Results_Page()

    def AddBasket(self):
        Actual_Basket.Complete_Basket(Actual_Outbound_Flight, Actual_Inbound_Flight, Actual_Search.ReturnOrNot)
        #print(Actual_Basket.Outbound_Flight_B.Flight_Number)
        #print(Actual_Basket.Inbound_Flight_B.Flight_Number)
        #print(Actual_Basket.Basket_Total_Price)
        Actual_Search.ReturnOrNot=True
        Launch_Flight_Results_Page()


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
            self.LogIn_Button = tk.Button(self.top_frame, text='My Account', command=Launch_LogIn_Page, bg=second_color)
        self.Menu_Button = tk.Button(self.top_frame, text='Menu', command=Launch_Menu_Page, bg=second_color)
        self.Pay_Button = tk.Button(self.right_frame, text='Pay', command=self.Pay, font=("Arial", 15), bg=third_color, fg=main_color)

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
                canvas_rep_one = tk.Canvas(self.canvas, width=bg_image_rep_one.width, height=bg_image_rep_one.height, highlightthickness=0,borderwidth=0)
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
                #self.canvas.bind("<Button-1>", lambda event, param=Display_Flight.Flight_ID : self.FLight_Select(event, param))
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
                    self.canvas.create_text(660, 30, anchor='ne', text=str(self.Total_Price_display)+"£", font=("Arial", 15))
                    self.Price_display=round(float(self.Display_Flight.Price)*Actual_Search.Class_Type,2)
                    self.canvas.create_text(660, 60, anchor='ne', text="Adult Price: "+str(self.Price_display)+"£", font=("Arial", 10))
                    self.canvas.create_text(280, 110, anchor='nw', text="Departure Time: "+str(self.Display_Flight.Departure_Time), font=("Arial", 10))
                    self.canvas.create_text(480, 110, anchor='nw', text="Arrival Time: "+str(self.Display_Flight.Arrival_Time), font=("Arial", 10))
                    bg_image_two = Image.open("./images/bin.png")
                    bg_photo_two = ImageTk.PhotoImage(bg_image_two)
                    # Créer un canevas pour afficher l'image du logo
                    canvas_two = tk.Canvas(self.canvas, width=bg_image_two.width, height=bg_image_two.height, highlightthickness=0,borderwidth=0)
                    canvas_two.place(x=720,y=170)
                    canvas_two.create_image(0, 0, anchor=tk.NW, image=bg_photo_two)
                    canvas_two.image = bg_photo_two
                    bg_image_two.close()
                    canvas_two.bind("<Button-1>", lambda event, param=i: self.Delete(event, param))
                    bg_image_rep_one = Image.open("./images/avion_res.png")
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
                canvas_rep_one = tk.Canvas(self.canvas, width=bg_image_rep_one.width, height=bg_image_rep_one.height, highlightthickness=0,borderwidth=0)
                canvas_rep_one.place(x=10,y=10)
                canvas_rep_one.create_image(0, 0, anchor=tk.NW, image=bg_photo_rep_one)
                canvas_rep_one.image = bg_photo_rep_one
                bg_image_rep_one.close()
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
                #self.canvas.bind("<Button-1>", lambda event, param=Display_Flight.Flight_ID : self.FLight_Select(event, param))
                self.canvas.pack(padx=25, pady=10, side=tk.TOP, fill=tk.X)
                # Draw a rectangle on the canvas
                self.canvas.create_rectangle(0, 0, 750, 200, outline='black', width=2)
                
                # Print information in the rectangle
                #self.canvas.create_text(20, 20, anchor='nw', text="Flight Number: "+str(self.Search_Results_Outbound[i]), font=("Arial", 10))
                #self.canvas.create_image(10, 10, anchor='nw', image=fly_photo[i], tags=("fly"+str(i)))
                self.canvas.create_text(280, 30, anchor='nw', text="Flight Number: "+str(self.Display_Flight.Flight_Number), font=("Arial", 10))
                self.canvas.create_text(280, 50, anchor='nw', text="Departure: "+str(self.Display_Flight.Departure_Airport), font=("Arial", 10))
                self.canvas.create_text(280, 70, anchor='nw', text="Arrival: "+str(self.Display_Flight.Arrival_Airport), font=("Arial", 10))
                if Actual_Search.Passengers == 1:
                    self.Total_Price_display=float(self.Display_Flight.Price)*Actual_Search.Class_Type
                else :
                    for j in range(Actual_Search.Passengers):
                        self.Total_Price_display+=(float(self.Display_Flight.Price)*Actual_Search.Passengers_Type_Number[j])*Actual_Search.Class_Type
                self.canvas.create_text(660, 30, anchor='ne', text=str(self.Total_Price_display)+"£", font=("Arial", 15))
                self.Price_display=round(float(self.Display_Flight.Price)*Actual_Search.Class_Type,2)
                self.canvas.create_text(660, 60, anchor='ne', text="Adult Price: "+str(self.Price_display)+"£", font=("Arial", 10))
                self.canvas.create_text(280, 110, anchor='nw', text="Departure Time: "+str(self.Display_Flight.Departure_Time), font=("Arial", 10))
                self.canvas.create_text(480, 110, anchor='nw', text="Arrival Time: "+str(self.Display_Flight.Arrival_Time), font=("Arial", 10))
                #images
                bg_image_rep_one = Image.open("./images/avion_res.png")
                bg_photo_rep_one = ImageTk.PhotoImage(bg_image_rep_one)
                # Créer un canevas pour afficher l'image du logo
                canvas_rep_one = tk.Canvas(self.canvas, width=bg_image_rep_one.width, height=bg_image_rep_one.height, highlightthickness=0,borderwidth=0)
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

        #Buttons

    def Hide_Button_1(self, empty):
        Launch_Home_Page()

    def Pay(self):
        print("Pay")
        #Launch_Home_Page()
    
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

    def Hide_Button_1(self, empty):
        Launch_Home_Page()
    
    def Pay(self):
        print("Pay")
        #Launch_Home_Page()

    def Book_Return(self):
        Actual_Search.Need_Return=True
        Actual_Search.ReturnOrNot=True
        Launch_Purchase_Results_Page()
    
    def Change_Outbound(self):
        Actual_Search.ReturnOrNot=False
        print("Change Outbound")
        Launch_Purchase_Results_Page()
    
    def Change_Inbound(self):
        Actual_Search.ReturnOrNot=True
        print("Change Inbound")
        Launch_Purchase_Results_Page()

#---------------------## ALL THE FUNCTIONS ##---------------------#

## Opennig Pages ##

def Launch_Home_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
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

def Launch_Menu_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Menu_Page(main_window)

def Launch_Purchase_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Purchase_Page(main_window)

def Launch_Info_Passengers():
    for widget in main_window.winfo_children():
        widget.destroy()
    Info_Passengers(main_window)

def Launch_Purchase_Results_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Purchase_Results_Page(main_window)

def Launch_Flight_Results_Page():
    print(Actual_Outbound_Flight.Flight_Number)
    for widget in main_window.winfo_children():
        widget.destroy()
    Flight_Results_Page(main_window)

def Launch_Basket_Page():
    for widget in main_window.winfo_children():
        widget.destroy()
    Basket_Page(main_window)

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
