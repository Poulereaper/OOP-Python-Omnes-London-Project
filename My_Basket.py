import pymysql
import dbconnect
import datetime
import random
import string

class Basket():
    def __init__(self):
        self.Outbound_Flight_B= None
        self.Inbound_Flight_B = None
        self.Basket_Total_Price = 0
        self.Basket_date = datetime.datetime.now()

    def Complete_Basket(self, Outbound_Flight, Inbound_Flight, Condition):
        #self.Outbound_Flight_B = Outbound_Flight
        #self.Inbound_Flight_B = Inbound_Flight
        #print("print du test : ", self.Inbound_Flight_B.Flight_Number)
        if Condition==False:
            self.Outbound_Flight_B = Outbound_Flight
            self.Inbound_Flight_B = None
            if self.Outbound_Flight_B.Passengers==1:
                self.Basket_Total_Price = float(self.Outbound_Flight_B.Price*Outbound_Flight.Class_Type)
            else:
                for j in range(Outbound_Flight.Passengers):
                    self.Basket_Total_Price += float(((self.Outbound_Flight_B.Price*Outbound_Flight.Passengers_Type_Number[j])*Outbound_Flight.Class_Type))
        else:
            self.Outbound_Flight_B = Outbound_Flight
            self.Inbound_Flight_B = Inbound_Flight
            if self.Outbound_Flight_B.Passengers==1:
                self.Basket_Total_Price = float(self.Outbound_Flight_B.Price*Outbound_Flight.Class_Type + self.Inbound_Flight_B.Price*Inbound_Flight.Class_Type)
            else:
                for j in range(Outbound_Flight.Passengers):
                    self.Basket_Total_Price += (float(((self.Outbound_Flight_B.Price*Outbound_Flight.Passengers_Type_Number[j])*Outbound_Flight.Class_Type)) + float(((self.Inbound_Flight_B.Price*Inbound_Flight.Passengers_Type_Number[j]))*Inbound_Flight.Class_Type))
        self.Basket_Total_Price = round(self.Basket_Total_Price,2)
        self.Basket_date = datetime.datetime.now()
    
    def Create_Res(self, Email):
        #Creat a res by sql resquest
        #nasket date = now
        self.Basket_date = datetime.datetime.now()
        #creat a res in the database
        #Request to the database to see the last res ID anable to creat a new one
        sql_1="SELECT MAX(ReservationID) AS PlusGrandReservationID FROM Reservations;"
        Last_ID = dbconnect.DBHelper().fetch(sql_1)
        res_ID = Last_ID[0]['PlusGrandReservationID'] + 1
        #Request to the database to get all the existing TicketsNum
        sql_2="SELECT DISTINCT NumTicket FROM Reservations;"
        ListNumTickets = dbconnect.DBHelper().fetch(sql_2)
        ListNumTickets = [d['NumTicket'] for d in ListNumTickets]
        ListNumTicketsNew = [None]*self.Outbound_Flight_B.Passengers*2
        if self.Inbound_Flight_B != None:
            for j in range(2):
                for i in range(self.Outbound_Flight_B.Passengers):
                    Number=self.generer_numero_billet(ListNumTickets)
                    ListNumTicketsNew.append(Number)
                    print(Number)
                    print(Res_ID)
                    print(Email)
                    if i==0:Flight_ID=self.Outbound_Flight_B.Flight_ID
                    else:Flight_ID=self.Inbound_Flight_B.Flight_ID
                    print(Flight_ID)
                    sql_3="INSERT INTO `reservations` (`ReservationID`, `ReservationDate`, `NumTicket`, `FlightID`, `CustomerID`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(Res_ID, self.Basket_date, Number, FlightID, None)
            #print(ListNumTickets)

    def Clear_Basket(self):
        self.Outbound_Flight_B = None
        self.Inbound_Flight_B = None
        self.Basket_Total = 0
        self.Basket_date = None

    def Delete_Outbound(self):
        self.Outbound_Flight_B = self.Inbound_Flight_B
        self.Inbound_Flight_B = None
        self.Clear_Basket()

    def Delete_Inbound(self):
        self.Inbound_Flight_B = None
        self.Complete_Basket(self.Outbound_Flight_B, self.Inbound_Flight_B, False)

    def generer_numero_billet(self, ListNumTickets):
        while True:
            # Générer 5 lettres majuscules aléatoires
            lettres = ''.join(random.choices(string.ascii_uppercase, k=5))
            # Générer 5 chiffres aléatoires
            chiffres = ''.join(random.choices(string.digits, k=5))
            # Concaténer les lettres et les chiffres pour former le numéro de billet
            numero_billet = lettres + chiffres
            # Vérifier si le numéro de billet existe déjà dans la liste
            if numero_billet not in ListNumTickets:
                break  # Sortir de la boucle si le numéro est unique
        return numero_billet


