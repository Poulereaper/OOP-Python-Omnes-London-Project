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

