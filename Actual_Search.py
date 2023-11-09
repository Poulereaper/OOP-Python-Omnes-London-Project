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
        if (self.From!="") & (self.To!="") & (self.Departure_Date!="") & (self.Return_Date!="") & (self.Class!=0) & (self.Passengers!=0):
            return True
        else:
            return False
    
    def Complet_Actual_Search(self,From,To,Departure_Date,Return_Date,Class,Passengers):
        if self.CompleteAccept():
            self.From=From
            self.To=To
            self.Departure_Date=Departure_Date
            self.Return_Date=Return_Date
            self.Class=Class
            self.Passengers=Passengers
        else :
            print("Complet Actual Search Failed")

    def Search(self):
        sql="SELECT * FROM flight WHERE Departure='{}' AND Arrival='{}' AND DepartureTime='{}' AND ArriveTime='{}' AND Class='{}' AND SeatsAvaible>='{}'".format(self.From,self.To,self.Departure_Date,self.Return_Date, self.Class,self.Passengers)
        result = dbconnect.DBHelper().fetch(sql)
        print(result)
        return result