import pymysql
import dbconnect
import datetime
import Actual_Search as AS
import Actual_Flight as AF

class Basket():
    def __init__(self, basket_id, user_id):
        self.Outbound_Flight_B= None
        self.Inbound_Flight_B = None
        self.Basket_Total = 0
        self.Basket_date = datetime.datetime.now()

    def Complete_Basket(self):
        self.Outbound_Flight_B =  AF.Outbound_Flight
        self.Inbound_Flight_B = AF.Inbound_Flight
        if AS.Passengers==1
            self.Basket_Total = self.Outbound_Flight_B.Flight_Price + self.Inbound_Flight_B.Flight_Price
        else:
            for j in range(AS.Passengers):
                self.Basket_Total += ((self.Outbound_Flight_B.Flight_Price*AF.Passenger_Type)*AF.Class_Type) + ((self.Inbound_Flight_B.Flight_Price*AF.Passenger_Type)*AF.Class_Type)  
        self.Basket_date = datetime.datetime.now()
    
    def Creat_Res(self):
        #Creat a res by sql resquest
        pass

    def Clear_Basket(self):
        self.Outbound_Flight_B = None
        self.Inbound_Flight_B = None
        self.Basket_Total = 0
        self.Basket_date = None
