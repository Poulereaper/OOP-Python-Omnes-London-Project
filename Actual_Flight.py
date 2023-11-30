import pymysql
import dbconnect
import datetime
import Actual_Search as AS

class Outbound_Flight():
    def __init__(self):
        self.Flight_ID = None
        self.Airline_Name = None
        self.Flight_Number = None
        self.Departure_Airport = None
        self.Departure_Date = None
        self.Departure_Time = None
        self.Arrival_Airport = None
        self.Arrival_Date = None
        self.Arrival_Time = None
        self.Flight_Duration = None
        self.Price = None
        self.Discount = None
        self.Seats_Left = None
        self.Seats_Capacity = None
        self.Class_Type = 0
        self.Passengers=0
        self.Passengers_Type_Number=[None]*11

    def Complete_Outbound_Flight(self, Flight_ID, Airline_Name, Flight_Number, Departure_Airport, Departure_Date, Departure_Time, Arrival_Airport, Arrival_Date, Arrival_Time, Flight_Duration, Price, Discount, Seats_Left, Seats_Capacity, Class_Type, Passengers, Passengers_Type_Number):
        self.Flight_ID = Flight_ID
        self.Airline_Name = Airline_Name
        self.Flight_Number = Flight_Number
        self.Departure_Airport = Departure_Airport
        self.Departure_Date = Departure_Date
        self.Departure_Time = Departure_Time
        self.Arrival_Airport = Arrival_Airport
        self.Arrival_Date = Arrival_Date
        self.Arrival_Time = Arrival_Time
        self.Flight_Duration = Flight_Duration
        self.Price = Price
        self.Discount = Discount
        self.Seats_Left = Seats_Left
        self.Seats_Capacity = Seats_Capacity
        self.Class_Type = Class_Type
        self.Passengers=Passengers
        self.Passengers_Type_Number=Passengers_Type_Number

    def Create_Flight(self, Departure_Airport, Departure_Date, Departure_Time, Arrival_Airport, Arrival_Date, Arrival_Time, Flight_Duration, Price, Discount, Seats, Economy_Class_Price, Business_Class_Price, First_Class_Price):
        #Create Flight ID
        sql1 = "SELECT MAX(FlightID) AS MaxFlightID FROM Flight"
        result1=dbconnect.DBHelper().fetch(sql3)
        Flight_ID = result1[0]['MaxFlightID']+1
        #Create Flight Number
        sql2 = "SELECT DISTINCT FlightNumber FROM Flight;"
        result2=dbconnect.DBHelper().fetch(sql2)
        ListNumVols = [d['FlightNumber'] for d in result2]
        Flight_Number = self.generer_numero_vol(ListNumVols)
        #Create Flight in the database
        sql3="INSERT INTO Flight (FlightID, FlightNumber, Departure, DepartureDate, DepartureTime, Arrival, ArrivalDate, ArrivalTime, Duration, Eco, Business, First, SeatsAvaible, Seats, Discount) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(Flight_ID, Flight_Number, Departure_Airport, Departure_Date, Departure_Time, Arrival_Airport, Arrival_Date, Arrival_Time, Flight_Duration, Economy_Class_Price, Business_Class_Price, First_Class_Price, Seats_Left, Seats_Capacity, Discount)
        dbconnect.DBHelper().execute(sql3)
        print("Create Flight", Flight_Number," Succeed")

    def Update_Flight(self, Flight_Number, Departure_Airport, Departure_Date, Departure_Time, Arrival_Airport, Arrival_Date, Arrival_Time, Flight_Duration, Price, Discount, Seats, Economy_Class_Price, Business_Class_Price, First_Class_Price):
        #Update Flight in the database
        sql3="UPDATE Flight SET Departure = '{}', DepartureDate = '{}', DepartureTime = '{}', Arrival = '{}', ArrivalDate = '{}', ArrivalTime = '{}', Duration = '{}', Eco = '{}', Business = '{}', First = '{}', SeatsAvaible = '{}', Seats = '{}', Discount = '{}' WHERE FlightNumber = '{}';".format(Departure_Airport, Departure_Date, Departure_Time, Arrival_Airport, Arrival_Date, Arrival_Time, Flight_Duration, Economy_Class_Price, Business_Class_Price, First_Class_Price, Seats_Left, Seats_Capacity, Discount, Flight_Number)
        dbconnect.DBHelper().execute(sql3)
        print("Update Flight", Flight_Number," Succeed")

    def Delete_Flight(self, Flight_Number):
        #Delete Flight in the database
        sql3="DELETE FROM Flight WHERE FlightNumber = '{}';".format(Flight_Number)
        dbconnect.DBHelper().execute(sql3)
        print("Delete Flight", Flight_Number," Succeed")


    def generer_numero_vol(self, ListNumVols):
        while True:
            # Générer 5 lettres majuscules aléatoires
            lettres = ''.join(random.choices(string.ascii_uppercase, k=3))
            # Générer 5 chiffres aléatoires
            chiffres = ''.join(random.choices(string.digits, k=3))
            # Concaténer les lettres et les chiffres pour former le numéro de billet
            numero_vol = lettres + chiffres
            # Vérifier si le numéro de vol existe déjà dans la liste
            if (numero_vol not in ListNumVols):
                break  # Sortir de la boucle si le numéro est unique
        return numero_vol


    def Reset_Outbound_Flight(self):
        self.Flight_ID = None
        self.Airline_Name = None
        self.Flight_Number = None
        self.Departure_Airport = None
        self.Departure_Date = None
        self.Departure_Time = None
        self.Arrival_Airport = None
        self.Arrival_Date = None
        self.Arrival_Time = None
        self.Flight_Duration = None
        self.Price = None
        self.Discount = None
        self.Seats_Left = None
        self.Seats_Capacity = None
        self.Class_Type = 0
        self.Passengers=0
        self.Passengers_Type_Number=[None]*11

   

class Inbound_Flight():
    def __init__(self):
        self.Flight_ID = None
        self.Airline_Name = None
        self.Flight_Number = None
        self.Departure_Airport = None
        self.Departure_Date = None
        self.Departure_Time = None
        self.Arrival_Airport = None
        self.Arrival_Date = None
        self.Arrival_Time = None
        self.Flight_Duration = None
        self.Price = None
        self.Discount = None
        self.Seats_Left = None
        self.Seats_Capacity = None
        self.Class_Type = 0
        self.Passengers=0
        self.Passengers_Type_Number=[None]*11

    def Complete_Inbound_Flight(self, Flight_ID, Airline_Name, Flight_Number, Departure_Airport, Departure_Date, Departure_Time, Arrival_Airport, Arrival_Date, Arrival_Time, Flight_Duration, Price, Discount, Seats_Left, Seats_Capacity, Class_Type, Passengers, Passengers_Type_Number):
        self.Flight_ID = Flight_ID
        self.Airline_Name = Airline_Name
        self.Flight_Number = Flight_Number
        self.Departure_Airport = Departure_Airport
        self.Departure_Date = Departure_Date
        self.Departure_Time = Departure_Time
        self.Arrival_Airport = Arrival_Airport
        self.Arrival_Date = Arrival_Date
        self.Arrival_Time = Arrival_Time
        self.Flight_Duration = Flight_Duration
        self.Price = Price
        self.Discount = Discount
        self.Seats_Left = Seats_Left
        self.Seats_Capacity = Seats_Capacity
        self.Class_Type = Class_Type
        self.Passengers=Passengers
        self.Passengers_Type_Number=Passengers_Type_Number

    def Reset_Inbound_Flight(self):
        self.Flight_ID = None
        self.Airline_Name = None
        self.Flight_Number = None
        self.Departure_Airport = None
        self.Departure_Date = None
        self.Departure_Time = None
        self.Arrival_Airport = None
        self.Arrival_Date = None
        self.Arrival_Time = None
        self.Flight_Duration = None
        self.Price = None
        self.Discount = None
        self.Seats_Left = None
        self.Seats_Capacity = None
        self.Class_Type = 0
        self.Passengers=0
        self.Passengers_Type_Number=[None]*11

