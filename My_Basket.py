import pymysql
import dbconnect
import datetime
import random
import string
import Mail as M
import PDF_Create as PDF

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
    
    def Create_Res(self, Email, CustomerID, Name):
        #Creat a res by sql resquest
        #nasket date = now
        self.Basket_date = datetime.datetime.now()
        #creat a res in the database
        #Request to the database to see the last res ID anable to creat a new one
        sql_1="SELECT MAX(ReservationID) AS PlusGrandReservationID FROM Reservations;"
        Last_ID = dbconnect.DBHelper().fetch(sql_1)
        Last_ID = Last_ID[0]['PlusGrandReservationID'] + 1
        sql_2="SELECT MAX(ReservationgrpID) AS PlusGrandReservationGrpID FROM Reservations;"
        Res_ID = dbconnect.DBHelper().fetch(sql_2)
        Res_ID = Res_ID[0]['PlusGrandReservationGrpID'] + 1
        #Request to the database to get all the existing TicketsNum
        sql_3="SELECT DISTINCT NumTicket FROM Reservations;"
        ListNumTickets = dbconnect.DBHelper().fetch(sql_3)
        ListNumTickets = [d['NumTicket'] for d in ListNumTickets]
        ListNumTicketsNew = [None]*self.Outbound_Flight_B.Passengers*2
        Flight_Total = 0
        Out_Price=0
        In_Price=0
        if self.Inbound_Flight_B != None:
            for j in range(2):
                if j==0:
                    Flight_ID=self.Outbound_Flight_B.Flight_ID
                    Price = self.Outbound_Flight_B.Price
                    Class=self.Outbound_Flight_B.Class_Type
                else:
                    Flight_ID=self.Inbound_Flight_B.Flight_ID
                    Price = self.Inbound_Flight_B.Price
                    Class=self.Inbound_Flight_B.Class_Type
                for i in range(self.Outbound_Flight_B.Passengers):
                    Number=self.generer_numero_billet(ListNumTickets, ListNumTicketsNew)
                    ListNumTicketsNew.append(Number)
                    Ticket_Price = float(((Price*self.Outbound_Flight_B.Passengers_Type_Number[i])*self.Outbound_Flight_B.Class_Type)**(1-(self.Outbound_Flight_B.Discount/100)))
                    Flight_Total += Ticket_Price
                    sql_4="INSERT INTO `reservations` (`ReservationID`, `ReservationGrpID`, `ReservationDate`, `NumTicket`, `FlightID`, `CustomerID`, `Price`, `Class`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(Last_ID, Res_ID, self.Basket_date, Number, Flight_ID, CustomerID, Ticket_Price, Class)
                    dbconnect.DBHelper().execute(sql_4)
                    Last_ID+=1
                sql_5="UPDATE flight SET SeatsAvailable = SeatsAvailable - '{}' WHERE FlightID = '{}';".format(self.Outbound_Flight_B.Passengers, Flight_ID)
                dbconnect.DBHelper().execute(sql_5)
                if j==0:
                    Out_Price=Flight_Total
                else:
                    In_Price=Flight_Total
                Flight_Total=0
        else:
            Flight_ID=self.Outbound_Flight_B.Flight_ID
            Price = self.Outbound_Flight_B.Price
            if self.Outbound_Flight_B.Passengers==1:
                Number=self.generer_numero_billet(ListNumTickets, None)
                Ticket_Price = float((Price*self.Outbound_Flight_B.Class_Type)*(1-(self.Outbound_Flight_B.Discount/100)))
                Class=self.Outbound_Flight_B.Class_Type
                sql_3="INSERT INTO `reservations` (`ReservationID`, `ReservationGrpID`, `ReservationDate`, `NumTicket`, `FlightID`, `CustomerID`, `Price`, `Class`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(Last_ID, Res_ID, self.Basket_date, Number, Flight_ID, CustomerID, Ticket_Price, Class)
                dbconnect.DBHelper().execute(sql_3)
                #Remove one from the booked flight*
                sql_5="UPDATE flight SET SeatsAvailable = SeatsAvailable - '{}' WHERE FlightID = '{}';".format(self.Outbound_Flight_B.Passengers, Flight_ID)
                dbconnect.DBHelper().execute(sql_5)
                Out_Price=Ticket_Price
            else:
                for i in range(self.Outbound_Flight_B.Passengers):
                    Number=self.generer_numero_billet(ListNumTickets, ListNumTicketsNew)
                    ListNumTicketsNew.append(Number)
                    Ticket_Price = float(((Price*self.Outbound_Flight_B.Passengers_Type_Number[i])*self.Outbound_Flight_B.Class_Type)*(1-(self.Outbound_Flight_B.Discount/100)))
                    Flight_Total += Ticket_Price
                    Class=self.Outbound_Flight_B.Class_Type
                    sql_3="INSERT INTO `reservations` (`ReservationID`, `ReservationGrpID`, `ReservationDate`, `NumTicket`, `FlightID`, `CustomerID`, `Price`, `Class`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(Last_ID, Res_ID, self.Basket_date, Number, Flight_ID, CustomerID, Ticket_Price, Class)
                    dbconnect.DBHelper().execute(sql_3)
                    Last_ID+=1
                    #Remove one from the booked flight*
                sql_5="UPDATE flight SET SeatsAvailable = SeatsAvailable - '{}' WHERE FlightID = '{}';".format(self.Outbound_Flight_B.Passengers, Flight_ID)
                dbconnect.DBHelper().execute(sql_5)
                Out_Price=Flight_Total
        #M.send_email(Email, Name, self.Outbound_Flight_B, self.Inbound_Flight_B, self.Basket_Total_Price)
        #PDF.bill_pdf(Name, Email, self.Outbound_Flight_B, self.Inbound_Flight_B, Out_Price, In_Price, Res_ID)
        print("Create Res Succeed")

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

    def generer_numero_billet(self, ListNumTickets, ListNumTicketsNew):
        while True:
            # Générer 5 lettres majuscules aléatoires
            lettres = ''.join(random.choices(string.ascii_uppercase, k=5))
            # Générer 5 chiffres aléatoires
            chiffres = ''.join(random.choices(string.digits, k=5))
            # Concaténer les lettres et les chiffres pour former le numéro de billet
            numero_billet = lettres + chiffres
            # Vérifier si le numéro de billet existe déjà dans la liste
            if (numero_billet not in ListNumTickets) or (numero_billet not in ListNumTicketsNew):
                break  # Sortir de la boucle si le numéro est unique
        return numero_billet


