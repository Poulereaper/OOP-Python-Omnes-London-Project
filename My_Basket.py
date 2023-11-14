import pymysql
import dbconnect
import datetime

class Basket():
    def __init__(self):
        self.Outbound_Flight_B= None
        self.Inbound_Flight_B = None
        self.Basket_Total_Price = 0
        self.Basket_date = datetime.datetime.now()

    def Complete_Basket(self, Outbound_Flight, Inbound_Flight):
        self.Outbound_Flight_B = Outbound_Flight
        self.Inbound_Flight_B = Inbound_Flight
        if self.Inbound_Flight_B.Flight_ID==None:
            if self.Outbound_Flight_B.Passengers==1:
                self.Basket_Total_Price = self.Outbound_Flight_B.Price*Outbound_Flight.Class_Type
            else:
                for j in range(Outbound_Flight.Passengers):
                    self.Basket_Total_Price += float(((self.Outbound_Flight_B.Price*Outbound_Flight.Passengers_Type_Number)*Outbound_Flight.Class_Type))
        else:
            if self.Outbound_Flight_B.Passengers==1:
                self.Basket_Total_Price = self.Outbound_Flight_B.Price*Outbound_Flight.Class_Type[0] + self.Inbound_Flight_B.Price*Inbound_Flight.Class_Type
            else:
                for j in range(Outbound_Flight.Passengers):
                    self.Basket_Total_Price += float(((self.Outbound_Flight_B.Price*Outbound_Flight.Passengers_Type_Number)*Outbound_Flight.Class_Type)) + float(((self.Inbound_Flight_B.Flight_Price*Inbound_Flight.Passenger_Type)*Inbound_Flight.Class_Type))
        self.Basket_Total_Price = round(self.Basket_Total_Price,2)
        self.Basket_date = datetime.datetime.now()
    
    def Creat_Res(self):
        #Creat a res by sql resquest
        pass

    def Clear_Basket(self):
        self.Outbound_Flight_B = None
        self.Inbound_Flight_B = None
        self.Basket_Total = 0
        self.Basket_date = None

    def Delete_Basket(self):
        #Delete a basket by sql resquest
        pass

    def Modify_Basket(self):
        #Modify a basket by sql resquest
        pass

    def Rest_Basket(self):
        Clear_Basket()

