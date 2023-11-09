import pymysql
import dbconnect
import datetime

class Outbound_Flight():
    def __init__(self):
        self.Flight_ID = None
        self.Airline_ID = None
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
   

class Inbound_Flight():
    def __init__(self):
        self.Flight_ID = None
        self.Airline_ID = None
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

