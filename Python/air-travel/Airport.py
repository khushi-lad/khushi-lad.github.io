"""
******************************
Air Travel
******************************
This file is used to create an Airport class with instance variables for the country, city, and code.
There are functions defined to return a string and check if two airports are the same. The getters
can be used to get the code, city, or country of an airport. The setters can be used to set a new
city or country.
"""

# Creates an Airport class and defines functions for Airport objects
class Airport:
    # Initializes instance variables for Airport
    def __init__(self, country, city, code): # Takes parameters for self, code, country, and city
        self._country = country.strip()
        self._city = city.strip()
        self._code = code.strip().upper()

    # Returns a string representation of the Airport
    def __str__(self): # Takes parameters for self
        return f"{self._code} [{self._city}, {self._country}]" # Return a string with the code, city, and country

    # Check if codes are equal
    def __eq__(self, other): # Takes parameters for self and other
        if isinstance(other, Airport): # Check if other is an instance of Airport
            if self._code == other._code: # Check if code is the same as the other code
                return True # Return True if the code is the same
            else:
                return False # Return False if the code is not the same
        else:
            return False # Return False if other is not an instance of Airport

    # Get the code
    def get_code(self): # Takes parameters for self
        return self._code # Return the code

    # Get the city
    def get_city(self): # Takes parameters for self
        return self._city # Return the city

    # Get the country
    def get_country(self): # Takes parameters for self
        return self._country # Return the country

    # Set a new city
    def set_city(self, city): # Takes parameters for self and city
        self._city = city # Set city to a new city

    # Set a new country
    def set_country(self, country): # Takes parameters for self and country
        self._country = country # Set country to a new country