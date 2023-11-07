import pymysql
import dbconnect

class Actual_Customer():
    def __init__(self):
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
            sql = "INSERT INTO `customer` (`Email`, `Password`, `FirstName`, `LastName`, `UserName`, `Phone`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(self.Email, self.Password, self.FirstName, self.LastName, self.UserName, self.Phone)
            dbconnect.DBHelper().execute(sql)
            print("Creat Actual Customer Succeed")
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