import pymysql
import dbconnect

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
    # Check if we can Complet the Actual Customer
    def CompleteAccept(self):
        if (self.Email != "") & (self.Password != "") & (self.FirstName != "") & (self.LastName != "") & (self.UserName != "") & (self.Phone != 0):
            return True
        else:
            return False
    # Complet Actual Customer
    def Complet_Actual_Customer(self, Email, Password, FirstName, LastName, UserName, Phone):
        self.Email = Email
        self.Password = Password
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Phone = Phone

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
                    result4=dbconnect.DBHelper().fetch(sql3)
                    self.CustomerID=result4[0]['MaxCustomerID']+1
                    sql5 = "INSERT INTO `customer` (`CustomerID`, `Email`, `Password`, `FirstName`, `LastName`, `UserName`, `Phone`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(self.CustomerID, self.Email, self.Password, self.FirstName, self.LastName, self.UserName, self.Phone)
                    dbconnect.DBHelper().execute(sql5)
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
        self.Email = result[0]['Email']
        self.Password = result[0]['Password']
        self.FirstName = result[0]['FirstName']
        self.LastName = result[0]['LastName']
        self.UserName = result[0]['UserName']
        self.Phone = result[0]['Phone']
        self.AdminOrNot = result[0]['AdminOrNot']