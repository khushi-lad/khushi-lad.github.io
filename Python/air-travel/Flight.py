"""
******************************
Air Travel
******************************
This file is used to create a Flight class with instance variables for the origin, destination,
flight number, and duration. There are functions defined to return a string, check if two
flights are the same, and add the duration of a connecting flight to a flight. The getters
can be used to get the flight number, origin, destination, and duration. The setters can be
used to set a new origin or destination. There is also a function defined to check if a
flight is domestic or international.
"""

from Airport import *

# Creates a Flight class and defines functions for Flight objects
class Flight:
    # Initializes instance variables for Flight
    def __init__(self, origin, destination, flight_number, duration): # Takes parameters for self, flight number, origin, destination, and duration
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._origin = origin
            self._destination = destination
            self._flight_number = flight_number
            self._duration = duration
        else:
            raise TypeError("The origin and destination must be Airport objects") # If origin and destination are not instances of Airport, raise a TypeError

    # Returns a string representation of the Flight
    def __str__(self): # Takes parameters for self
        if self.is_domestic():
            flight_type = "domestic"
        else:
            flight_type = "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({flight_type}) [{self._duration:.0f}h]" # Returns a string with origin city, destination city, domestic or international flight type, and duration

    # Check if origin and destination are the same
    def __eq__(self, other): # Takes parameters for self and other
        if isinstance(other, Flight): # Check if other is instance of Flight
            if self._origin == other._origin and self._destination == other._destination:
                return True # Return True if the other origin is the same as the given origin and the other destination is the same as the given destination
            else:
                return False # Return False if other origin is not the same as the given origin and the other destination is not the same as the given destination
        else:
            return False # Return False if other is not an instance of Flight

    # Add duration of connecting flight and flight
    def __add__(self, conn_flight): # Takes parameters for self and connecting flight
        if isinstance(conn_flight, Flight): # Check if connecting flight is instance of Flight
            if self._destination == conn_flight._origin: # Check if destination of flight is origin of connecting flight
                return Flight(self._origin, conn_flight._destination, self._flight_number, (float(self._duration) + float(conn_flight._duration))) # Create new Flight object with flight number, origin of flight, destination of connecting flight, and sum of the duration of flight and connecting flight
            else:
                raise ValueError("These flights cannot be combined") # If destination of flight is not origin of connecting flight raise ValueError
        else:
            raise TypeError("The conn_flight must be a Flight object") # If connecting flight is not an instance of Flight raise TypeError

    # Get the flight number
    def get_number(self): # Takes parameters for self
        return self._flight_number # Return flight number

    # Get the origin
    def get_origin(self): # Takes parameters for self
        return self._origin # Return origin

    # Get the destination
    def get_destination(self): # Takes parameters for self
        return self._destination # Return destination

    # Get the duration
    def get_duration(self): # Takes parameters for self
        return self._duration # Return duration

    # Check if the flight is domestic or international
    def is_domestic(self): # Takes parameters for self
        origin_country = self._origin.get_country() # Get the origin country
        destination_country = self._destination.get_country() # Get the destination country
        if origin_country == destination_country:
            return True # Return True if destination country is the origin country
        else:
            return False # Return False if destination country is not the origin country

    # Set a new origin
    def set_origin(self, origin): # Takes parameters for self and origin
        self._origin = origin # Set origin to a new origin

    # Set a new destination
    def set_destination(self, destination): # Takes parameters for self and destination
        self._destination = destination # Set destination to a new destination