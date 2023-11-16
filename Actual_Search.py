import pymysql
import dbconnect
import datetime

class Actual_Search():
    def __init__(self):
        self.From=""
        self.To=""
        self.Departure_Date=""
        self.Return_Date=""
        self.Class=""
        self.Class_Type = 0
        self.Passengers=0
        self.Passengers_Type = [None]*11
        self.Passengers_Type_Number=[None]*11
        self.ReturnOrNot=False

    def CompleteAccept(self):
        if (self.From=="") & (self.To=="") & (self.Departure_Date=="") & (self.Return_Date=="") & (self.Class=="") & (self.Passengers==0):
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
            if Class=="Economy":
                self.Class_Type=1
            elif Class=="Business":
                self.Class_Type=1.3
            elif Class=="First Class":
                self.Class_Type=2.5
            self.Passengers=Passengers
        else :
            print("Complet Actual Search Failed")
    
    def Change_Actual_Search(self,From,To,Departure_Date,Return_Date,Class,Passengers):
        if self.CompleteAccept():
            print("Actual Search is empty for the moment")
        else :
            self.From=From
            self.To=To
            self.Departure_Date=Departure_Date
            self.Return_Date=Return_Date
            self.Class=Class
            if Class=="Economy":
                self.Class_Type=1
            elif Class=="Business":
                self.Class_Type=1.3
            elif Class=="First Class":
                self.Class_Type=2.5
            self.Passengers=Passengers

    def Search_Outbound(self):

        sql="SELECT * FROM flight WHERE Departure='{}' AND Arrival='{}' AND DepartureDate='{}' AND SeatsAvailable>='{}'".format(self.From,self.To,self.Departure_Date,self.Passengers)
        result = dbconnect.DBHelper().fetch(sql)
        if len(result)==0:
            print("No Flight")
        else:
            print("Search Outbound Succeed")
            print(result[0]['FlightID'])
        return result

    def Search_Inbound(self):
        sql="SELECT * FROM flight WHERE Departure='{}' AND Arrival='{}' AND DepartureDate='{}' AND SeatsAvailable>='{}'".format(self.To,self.From,self.Return_Date,self.Passengers)
        result = dbconnect.DBHelper().fetch(sql)
        if len(result)==0:
            print("No Flight")
        else:
            print("Search Return Succeed")
            print(result[0]['FlightID'])
        return result

    def Rest_Search(self):
        self.From=""
        self.To=""
        self.Departure_Date=""
        self.Return_Date=""
        self.Class=""
        self.Class_Type = 0
        self.Passengers=0
        self.Passengers_Type = [None]*11
        self.Passengers_Type_Number=[None]*11
        self.ReturnOrNot=False
