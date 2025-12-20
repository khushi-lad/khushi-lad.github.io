"""
******************************
Air Travel
******************************
This file is used to create a MaintenanceRecord class with instance variables for the flight,
maintenance airport, maintenance duration, and maintenance cost per hour. There are functions
defined to return a string and check if two MaintenanceRecord objects are or are not the same.
There are comparison methods defined for less than, less than or equal, greater than, and
greater than or equal to compare the total cost. The getters can be used to get the total cost
and the duration.
"""

# Creates a MaintenanceRecord class and defines function for MaintenanceRecord objects
class MaintenanceRecord:
    # Initializes instance variables for MaintenanceRecord
    def __init__(self, input_line, all_flights, all_airports): # Takes parameters for self, input line, all_flights dictionary, and all_airports list
        parts = input_line.strip().split("-")
        if len(parts) != 5:
            raise ValueError("Invalid data string") # If the line does not have 5 parts raise ValueError
        f_code = parts[0].strip()
        f_num = parts[1].strip()
        a_code = parts[2].strip()
        duration = parts[3].strip()
        cost = parts[4].strip()
        flight_number = f_code + "-" + f_num
        self._flight = None # Set flight to None
        for flights in all_flights.values():
            for flight in flights:
                if flight.get_number() == flight_number:
                    self._flight = flight # If the flight number is the same as the given flight, then the flight is the given flight
        if self._flight is None:
            raise ValueError("Flight not found") # If flight is still None raise ValueError
        self._maintenance_airport = None # Set maintenance airport to None
        for airport in all_airports:
            if airport.get_code() == a_code:
                self._maintenance_airport = airport # If the airport is the same as the maintenance airport, then the airport is the maintenance airport
        if self._maintenance_airport is None:
            raise ValueError("Airport not found") # If maintenance airport is still None raise ValueError
        self._maintenance_duration = int(duration) # Make duration into int type
        self._maintenance_cost_per_hour = float(cost) # Make maintenance cost per hour into float type

    # Get the total cost
    def get_total_cost(self): # Takes parameters for self
        total_cost = self._maintenance_cost_per_hour * self._maintenance_duration
        return total_cost # Calculate and return total cost

    # Get the duration
    def get_duration(self): # Takes parameters for self
        return self._maintenance_duration # Return maintenance duration

    # Returns a string representation of the MaintenanceRecord
    def __str__(self): # Takes parameters for self
        return f"{self._flight._flight_number} ({self._flight}) from {self._flight._origin} to be maintained at {self._maintenance_airport} for {self._maintenance_duration} hours @ ${self._maintenance_cost_per_hour}/hour (${self.get_total_cost()})" # Returns a string with flight number, flight code, flight origin, maintenance airport, maintenance duration, and maintenance cost per hour

    # Check if the parameters for other are the given parameters
    def __eq__(self, other): # Takes parameters for self and other
        if isinstance(other, MaintenanceRecord): # Check if other is instance of MaintenanceRecord
            if (self._flight == other._flight) and (self._maintenance_airport == other._maintenance_airport) and (self._maintenance_duration == other._maintenance_duration) and (self._maintenance_cost_per_hour == other._maintenance_cost_per_hour):
                return True # Return True if other parameters for flight, maintenance airport, maintenance duration, and maintenance cost per hour are the same as the given parameters
            else:
                return False # Return False if other parameters for flight, maintenance airport, maintenance duration, and maintenance cost per hour are not the same as the given parameters
        else:
            return False # Return False if other is not an instance of MaintenanceRecord

    # Check if the parameters for other are not the given parameters
    def __ne__(self, other): # Takes parameters for self and other
        if isinstance(other, MaintenanceRecord): # Check if other is instance of MaintenanceRecord
            if (self._flight != other._flight) or (self._maintenance_airport != other._maintenance_airport) or (self._maintenance_duration != other._maintenance_duration) or (self._maintenance_cost_per_hour != other._maintenance_cost_per_hour):
                return True # Return True if at least one of the other parameters for flight, maintenance airport, maintenance duration, or maintenance cost per hour are not the same as the given parameters
            else:
                return False # Return False if all the other parameters for flight, maintenance airport, maintenance duration, and maintenance cost per hour are the same as the given parameters
        else:
            return True # Return True if other is not an instance of MaintenanceRecord

    # Check if the other total cost is less than the given total cost
    def __lt__(self, other): # Takes parameters for self and other
        if self.get_total_cost() < other.get_total_cost():
            return True # Return True if other total cost is less than the given total cost
        else:
            return False # Return True if other total cost is not less than the given total cost

    # Check if the other total cost is less than or equal to the given total cost
    def __le__(self, other): # Takes parameters for self and other
        if self.get_total_cost() <= other.get_total_cost():
            return True # Return True if other total cost is less than or equal to the given total cost
        else:
            return False # Return False of other total cost is not less than or equal to the given total cost

    # Check if the other total cost is greater than the given total cost
    def __gt__(self, other): # Takes parameters for self and other
        if self.get_total_cost() > other.get_total_cost():
            return True # Return True if the other total cost is greater than the given total cost
        else:
            return False # Return False if the other total cost is not greater than the given total cost

    # Check if the other total cost is greater than or equal to the given total cost
    def __ge__(self, other): # Takes parameters for self and other
        if self.get_total_cost() >= other.get_total_cost():
            return True # Return True if the other total cost is greater than or equal to the given total cost
        else:
            return False # Return False if the other total cost is not greater than or equal to the given total cost