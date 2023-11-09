import pymysql
import dbconnect
import datetime

class Actual_Search():
    def __init__(self):
        self.From=""
        self.To=""
        self.Departure_Date=""
        self.Return_Date=""
        self.Class=0
        self.Passengers=0

    def CompleteAccept(self):
        if (self.From=="") & (self.To=="") & (self.Departure_Date=="") & (self.Return_Date=="") & (self.Class==0) & (self.Passengers==0):
            return True
        else:
            return False
    
    def Complet_Actual_Search(self,From,To,Departure_Date,Return_Date,Class,Passengers):
        if self.CompleteAccept():
            print("Complet Actual Search Succeed")
            self.From=From
            self.To=To
            self.Departure_Date=Departure_Date
            self.Return_Date=Return_Date
            self.Class=Class
            self.Passengers=Passengers
        else :
            print("Complet Actual Search Failed")

    def Search(self):
        if self.Return_Date=="": # One Way
            sql="SELECT * FROM flight WHERE Departure='{}' AND Arrival='{}' AND DepartureDate='{}' AND SeatsAvailable>='{}'".format(self.From,self.To,self.Departure_Date,self.Passengers)
            result = dbconnect.DBHelper().fetch(sql)
            if len(result)==0:
                print("No Flight")
            else:
                print("Search Succeed")
            return result
        else: # Round Trip
            sql1="SELECT * FROM flight WHERE Departure='{}' AND Arrival='{}' AND DepartureDate='{}' AND SeatsAvailable>='{}'".format(self.From,self.To,self.Departure_Date,self.Passengers)
            result1 = dbconnect.DBHelper().fetch(sql1)
            sql2="SELECT * FROM flight WHERE Departure='{}' AND Arrival='{}' AND DepartureDate='{}' AND SeatsAvailable>='{}'".format(self.To,self.From,self.Return_Date,self.Passengers)
            result2 = dbconnect.DBHelper().fetch(sql2)
            if (len(result1)==0) & (len(result2)==0):
                print("No Flight")
            else:
                print("Search Succeed")
            return result1,result2