import pymysql
import dbconnect
import datetime
from PIL import Image, ImageTk, ImageDraw
import base64
from io import BytesIO
import uuid
import base64

class Actual_Customer():
    def __init__(self):
        self.CustomerID=0
        self.LoginOrNot = False
        self.Email = ""
        self.Password = ""
        self.FirstName = ""
        self.LastName = ""
        self.UserName = ""
        self.Phone = 0
        self.AdminOrNot = False
        self.AdminPage=False
        self.AdminFlight=""
        self.AdminCustomer=0
        self.AdminDateBegin=None
        self.AdminDateEnd=None
        self.ProfilePicture = None
        self.CardNumber = 0
        self.CardName = ""
        self.CardDate = 0
        self.CardCode = 0
        self.Page = 0
    # Check if we can Complet the Actual Customer
    def CompleteAccept(self):
        if (self.Email != "") & (self.Password != "") & (self.FirstName != "") & (self.LastName != "") & (self.UserName != "") & (self.Phone != 0):
            return True
        else:
            return False
    # Complet Actual Customer
    def Complet_Actual_Customer(self, Email, Password, FirstName, LastName, UserName, Phone, ProfilePicture):
        self.Email = Email
        self.Password = Password
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Phone = Phone
        self.ProfilePicture = ProfilePicture

    def Change_Actual_Customer(self, Email, Password, FirstName, LastName, UserName, Phone, ProfilePicture):
        self.Email = Email
        self.Password = Password
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Phone = Phone
        self.ProfilePicture = ProfilePicture
        #sql
        sql = "UPDATE Customer SET Email='{}', Password='{}', FirstName='{}', LastName='{}', UserName='{}', Phone='{}', ProfilePicture='{}' WHERE CustomerID='{}'".format(self.Email, self.Password, self.FirstName, self.LastName, self.UserName, self.Phone, self.ProfilePicture, self.CustomerID)
        dbconnect.DBHelper().execute(sql)
        print("Change Actual Customer Succeed")

    # Creat the Actual Customer in the DB
    def Creat_Actual_Customer(self):
        if self.CompleteAccept():
            if self.LogOrNot:
                print("PLease Unlogin First")
            else:
                sql1 = "SELECT * FROM Customer WHERE Email='{}'".format(self.Email)
                result1 = dbconnect.DBHelper().fetch(sql1)
                sql2 = "SELECT * FROM Customer WHERE Phone='{}'".format(self.Phone)
                result2 = dbconnect.DBHelper().fetch(sql2)
                sql3 = "SELECT * FROM Customer WHERE UserName='{}'".format(self.UserName)
                result3 = dbconnect.DBHelper().fetch(sql3)
                if (len(result1)==0) & (len(result2)==0) & (len(result3)==0):
                    sql4 = "SELECT MAX(CustomerID) AS MaxCustomerID FROM Customer"
                    result4=dbconnect.DBHelper().fetch(sql4)
                    print("result4 : ")
                    print(result4)
                    self.CustomerID=result4[0]['MaxCustomerID']+1
                    #self.CustomerID = (dbconnect.DBHelper().fetch(sql3))+1
                    sql5 = "INSERT INTO `customer` (`CustomerID`, `Email`, `Password`, `FirstName`, `LastName`, `UserName`, `Phone`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(self.CustomerID, self.Email, self.Password, self.FirstName, self.LastName, self.UserName, self.Phone)
                    dbconnect.DBHelper().execute(sql5)
                    image = Image.open("./pp/user.png")
                    image = image.resize((128, 128))

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
                    values = (encode_image, self.CustomerID)
                    dbconnect.DBHelper().execute_row(sqlPP, values)
                    print("Creat Actual Customer Succeed")
                    return "Succeed"
                elif len(result1) != 0:
                    print("This Email has already been used")
                    return "Email"
                elif len(result2) != 0:
                    print("This Phone has already been used")
                    return "Phone"
                elif len(result3) != 0:
                    print("This UserName has already been used")
                    return "UserName"
                else:
                    print("Creat Actual Customer Failed")
        else:
            print("Creat Actual Customer Failed")
    
    def Copy_To_Actual_Customer(self, result):
        self.LogOrNot = True
        self.CustomerID = result[0]['CustomerID']
        self.Email = result[0]['Email']
        self.Password = result[0]['Password']
        self.FirstName = result[0]['FirstName']
        self.LastName = result[0]['LastName']
        self.UserName = result[0]['UserName']
        self.Phone = result[0]['Phone']
        self.AdminOrNot = result[0]['AdminOrNot']
        self.ProfilePicture = result[0]['ProfilePicture']
        self.CardNumber = result[0]['CardNumber']
        self.CardName = result[0]['CardName']
        self.CardDate = result[0]['CardDate']
        self.CardCode = result[0]['CardCode']

    def Disconnect(self):
        self.LogOrNot = False
        self.CustomerID = 0
        self.Email = ""
        self.Password = ""
        self.FirstName = ""
        self.LastName = ""
        self.UserName = ""
        self.Phone = 0
        self.AdminOrNot = False
        self.AdminPage=False
        self.AdminFlight=""
        self.AdminCustomer=0
        self.ProfilePicture = None
        self.CardNumber = 0
        self.CardName = ""
        self.CardDate = 0
        self.CardCode = 0
        self.Page = 0

    def Delete_Customer(self, CustomerID):
        sql = "DELETE FROM Customer WHERE CustomerID='{}'".format(CustomerID)
        dbconnect.DBHelper().execute(sql)
        print("Delete Customer Succeed")
        self.AdminCustomer=0

    def Add_Card(self, CardNumber, CardName, CardDate, CardCode):
        sql = "UPDATE Customer SET CardNumber='{}', CardDate='{}', CardName='{}', CardCode='{}' WHERE CustomerID='{}'".format(CardNumber, CardDate, CardName, CardCode, self.CustomerID)
        dbconnect.DBHelper().execute(sql)
        self.CardNumber = CardNumber
        self.CardName = CardName
        self.CardDate = CardDate
        self.CardCode = CardCode
        print("Change Actual Customer Card Succeed")

    def HowMany_Orders(self):
        sql = "SELECT COUNT(DISTINCT ReservationGrpID) FROM Reservations WHERE CustomerID = '{}'".format(self.CustomerID)
        result = dbconnect.DBHelper().fetch(sql)
        return result[0]['COUNT(DISTINCT ReservationGrpID)']
    
    def Select_UpComing_Flight(self):
        sql = """SELECT
        r.FlightID,
        r.ReservationGrpID,
        COUNT(r.ReservationID) AS NombreDeReservations,
        SUM(r.Price) AS SommeDesPrix,
        f.FlightNumber,
        f.Departure,
        f.DepartureDate,
        f.Arrival,
        f.ArrivalDate,
        f.DepartureTime,
        f.ArrivalTime,
        f.Airline,
        f.Duration
        FROM
            Reservations r
            INNER JOIN flight f ON r.FlightID = f.FlightID
        WHERE
            r.CustomerID = '{}'
            AND f.DepartureDate > '{}'
        GROUP BY
            r.FlightID, r.ReservationGrpID, r.Price, f.FlightNumber, f.Departure, f.DepartureDate, f.Arrival, f.ArrivalDate, f.DepartureTime, f.ArrivalTime, f.Airline, f.Duration;
        """.format(self.CustomerID, datetime.datetime.now())
        result = dbconnect.DBHelper().fetch(sql)
        return result
        
    def Select_Past_Flight(self):
        sql = """SELECT
        r.FlightID,
        r.ReservationGrpID,
        COUNT(r.ReservationID) AS NombreDeReservations,
        SUM(r.Price) AS SommeDesPrix,
        f.FlightNumber,
        f.Departure,
        f.DepartureDate,
        f.Arrival,
        f.ArrivalDate,
        f.DepartureTime,
        f.ArrivalTime,
        f.Airline,
        f.Duration
        FROM
            Reservations r
            INNER JOIN flight f ON r.FlightID = f.FlightID
        WHERE
            r.CustomerID = '{}'
            AND f.DepartureDate < '{}'
        GROUP BY
            r.FlightID, r.ReservationGrpID, r.Price, f.FlightNumber, f.Departure, f.DepartureDate, f.Arrival, f.ArrivalDate, f.DepartureTime, f.ArrivalTime, f.Airline, f.Duration;
        """.format(self.CustomerID, datetime.datetime.now())
        result = dbconnect.DBHelper().fetch(sql)
        return result

    # Creat the Actual Customer in the DB
    def Create_Customer(self, Email, Password, FirstName, LastName, UserName, Phone, AdminOrNot):
        sql1 = "SELECT * FROM Customer WHERE Email='{}'".format(Email)
        result1 = dbconnect.DBHelper().fetch(sql1)
        sql2 = "SELECT * FROM Customer WHERE Phone='{}'".format(Phone)
        result2 = dbconnect.DBHelper().fetch(sql2)
        sql3 = "SELECT * FROM Customer WHERE UserName='{}'".format(UserName)
        result3 = dbconnect.DBHelper().fetch(sql3)
        if (len(result1)==0) & (len(result2)==0) & (len(result3)==0):
            sql4 = "SELECT MAX(CustomerID) AS MaxCustomerID FROM Customer"
            result4=dbconnect.DBHelper().fetch(sql4)
            CustomerID=result4[0]['MaxCustomerID']+1
            sql5 = "INSERT INTO `customer` (`CustomerID`, `Email`, `Password`, `FirstName`, `LastName`, `UserName`, `Phone`, `AdminOrNot`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(CustomerID, Email, Password, FirstName, LastName, UserName, Phone, AdminOrNot)
            dbconnect.DBHelper().execute(sql5)
            print("Creat Customer Succeed")
            return "Succeed"
        elif len(result1) != 0:
            print("This Email has already been used")
            return "Email"
        elif len(result2) != 0:
            print("This Phone has already been used")
            return "Phone"
        elif len(result3) != 0:
            print("This UserName has already been used")
            return "UserName"
        else:
            print("Creat Customer Failed")

    def Update_Customer(self, CustomerID, Email, Password, FirstName, LastName, UserName, Phone, AdminOrNot):
        sql1 = "SELECT * FROM Customer WHERE Email='{}' AND CustomerID!= '{}'".format(Email, CustomerID)
        result1 = dbconnect.DBHelper().fetch(sql1)
        sql2 = "SELECT * FROM Customer WHERE Phone='{}' AND CustomerID!= '{}'".format(Phone, CustomerID)
        result2 = dbconnect.DBHelper().fetch(sql2)
        sql3 = "SELECT * FROM Customer WHERE UserName='{}' AND CustomerID!= '{}'".format(UserName, CustomerID)
        result3 = dbconnect.DBHelper().fetch(sql3)
        if (len(result1)==0) & (len(result2)==0) & (len(result3)==0):
            sql = "UPDATE Customer SET Email='{}', Password='{}', FirstName='{}', LastName='{}', UserName='{}', Phone='{}', AdminOrNot='{}' WHERE CustomerID='{}'".format(Email, Password, FirstName, LastName, UserName, Phone, AdminOrNot, CustomerID)
            dbconnect.DBHelper().execute(sql)
            print("Update Customer Succeed")
            return "Succeed"
        elif len(result1) != 0:
            print("This Email has already been used")
            return "Email"
        elif len(result2) != 0:
            print("This Phone has already been used")
            return "Phone"
        elif len(result3) != 0:
            print("This UserName has already been used")
            return "UserName"
        else:
            print("Creat Customer Failed")
        

