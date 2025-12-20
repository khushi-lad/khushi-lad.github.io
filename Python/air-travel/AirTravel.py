"""
******************************
Air Travel
******************************
This file is used to load files, get an airport using a code, find all flights with a specific city
or country, check if there is a flight with a specific origin and destination, find the shortest
flight from a specific origin, and find a return flight that goes back from the destination to the
origin. There are also functions defined to find the total cost of all maintenance records, the
total duration of all maintenance records, and sort the maintenance records from lowest to highest cost.
"""

from Flight import *
from Airport import *
from MaintenanceRecord import *

all_airports = []
all_flights = {}
maintenance_records = []

# Load airport files and add to all_airports list, load flight files and add to all_flights dictionary
def load_flight_files(airport_file, flight_file): # Takes parameters of the airport file and flight file
    try:
        airport_text = open(airport_file, "r")
        airport_lines = airport_text.readlines() # Open the airport file and read the lines
        for airport_line in airport_lines:
            airport_parts = airport_line.strip().split("-")
            airport_parts = [part.strip() for part in airport_parts]
            if len(airport_parts) == 3:
                code, country, city = airport_parts
                airport = Airport(country, city, code) # Create Airport object with the necessary parameters
                all_airports.append(airport) # Append the airport to the all_airports list
        flight_text = open(flight_file, "r")
        flight_lines = flight_text.readlines() # Open the flight file and read the lines
        for flight_line in flight_lines:
            flight_parts = flight_line.strip().split("-")
            flight_parts = [part.strip() for part in flight_parts]
            if len(flight_parts) == 5:
                flight_letters, flight_numbers, origin, destination, duration = flight_parts
                flight_code = flight_letters + "-" + flight_numbers
                flight = Flight(get_airport_using_code(origin), get_airport_using_code(destination), flight_code, float(duration)) # Create Flight object with the necessary parameters
                if origin not in all_flights:
                    all_flights[origin] = [] # If the origin key is not in all_flights, add the origin key
                all_flights[origin].append(flight) # Append the flight to the specific origin key
        airport_text.close()
        flight_text.close() # Close all files
        return True # Returns True if there are no errors
    except Exception:
        return False # Returns False if an error is found

# Get the airport using the given code
def get_airport_using_code(code): # Takes parameters of the given code
    for airport in all_airports:
        if code == airport.get_code(): # Check if the code of the airport is the given code
            return airport # Returns the airport if it has the given code
    raise ValueError(f"No airport with the given code: {code}") # Raises a ValueError if no airport is found with the given code

# Find all the flights with the given city as the origin or destination
def find_all_flights_city(city): # Takes parameters of the given city
    flight_city_list = [] # Create an empty list
    for flights in all_flights.values():
        for flight in flights:
            if (flight.get_origin().get_city() == city) or (flight.get_destination().get_city() == city):
                flight_city_list.append(flight) # If the origin or destination of the flight is the given city, append it to the list
    return flight_city_list # Returns the list of flights that have that city

# Find all the flights with the given country as the origin and/or destination
def find_all_flights_country(country): # Takes parameters of the given country
    flight_country_list = [] # Create an empty list
    for flights in all_flights.values():
        for flight in flights:
            if (flight.get_origin().get_country() == country) or (flight.get_destination().get_country() == country):
                flight_country_list.append(flight) # If the origin or destination of the flight is the given country, append it to the list
            elif (flight.get_origin().get_country() == country) and (flight.get_destination().get_country() == country):
                flight_country_list.append(flight) # If the origin and the destination of the flight is the given country, append it to the list
    return flight_country_list # Returns the list of flights that have that country

# Check if there is a flight going from a specific origin to a specific destination
def has_flight_between(orig_airport, dest_airport): # Takes parameters of the origin airport and the destination airport
    for flights in all_flights.values():
        for flight in flights:
            if (flight.get_origin() == orig_airport) and (flight.get_destination() == dest_airport): # Check if the origin is the given origin and check if the destination is the given destination
                return True # Returns True if the flight has the given origin and destination
    return False # Returns False if there is no flight with the given origin and destination

# Find the shortest flight from the origin
def shortest_flight_from(orig_airport): # Takes parameters of the origin airport
    shortest_flight = None # Set the shortest flight to None
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin() == orig_airport: # Check if the origin is the given origin
                if shortest_flight is None or (flight.get_duration() <= shortest_flight.get_duration()):
                    shortest_flight = flight # If the shortest flight is None or the duration of the flight is less than or equal to the shortest flight, the flight is the new shortest flight
    return shortest_flight # Returns the shortest flight from the origin

# Find the flight that goes from the destination back to the origin
def find_return_flight(first_flight): # Takes parameters of the first flight
    for flights in all_flights.values():
        for flight in flights:
            if first_flight.get_destination() == flight.get_origin() and first_flight.get_origin() == flight.get_destination():
                return_flight = flight # If the destination of the first flight is the origin of the flight, and the origin of the first flight is the destination of the flight, then the return flight is the flight
                return return_flight # Returns the return flight that goes from the destination back to the origin
    raise ValueError(f"There is no flight from {first_flight.get_destination().get_code()} to {first_flight.get_origin().get_code()}") # Raises a ValueError if there is no return flight

# Load the maintenance file and add it to the maintenance records list
def create_maintenance_records(maintenance_file, flights_dict, airports_list): # Takes parameters of the maintenance file, the flight dictionary, and the airport list
        try:
            maintenance_text = open(maintenance_file, "r")
            maintenance_lines = maintenance_text.readlines() # Open the maintenance file and read the lines
            for maintenance_line in maintenance_lines:
                maintenance_parts = maintenance_line.strip().split("-")
                if len(maintenance_parts) == 5:
                    maintenance_record = MaintenanceRecord(maintenance_line, flights_dict, airports_list) # Create MaintenanceRecord object with the necessary parameters
                    if maintenance_record not in maintenance_records:
                        maintenance_records.append(maintenance_record) # If the maintenance record is not already in the maintenance records list, then append the maintenance record
            return True # Returns True if the maintenance record is added to the maintenance records list
        except ValueError:
            return False # Returns False if a ValueError occurs

# Find the total cost of all the records
def find_total_cost(records): # Takes parameters of the records
    total_cost = 0 # Set total cost to 0
    for maintenance_record in records:
        total_cost += maintenance_record.get_total_cost() # Add the total cost for each maintenance record to the total cost
    return total_cost # Returns the total cost

# Find the total duration of all the records
def find_total_duration(records): # Takes parameters of the records
    total_duration = 0 # Set total duration to 0
    for maintenance_record in records:
        total_duration += maintenance_record.get_duration() # Add the total duration for each maintenance record to the total duration
    return total_duration # Returns the total duration

# Sort the maintenance records list
def sort_maintenance_records(records): # Takes parameters of the records
    sorted_records_list = sorted(records)
    return sorted_records_list # Returns the sorted records list

# Put code to test your functions and classes inside of this if statement.
# Having code outside of these functions, your classes, or this if statement may cause the autograder to fail.
if __name__ == "__main__":
    # These examples are from the assignment document.
    # Note that you will need to implement the required classes, methods, and functions before these tests will work.
    # Remove the pass keyword above and uncomment these when you are ready to test.

    print("Example 1: load_files(airport_file, flight_file)")
    data = load_flight_files("airports.txt", "flights.txt")
    print(data, len(all_airports), len(all_flights))

    print("\nExample 2: get_airport_by_code(code)")
    print(get_airport_using_code("ORD"))
    # print(get_airport_using_code("ABC"))  # Should cause an Exception

    print("\nExample 3: find_all_flights_city(city)")
    res = find_all_flights_city("Dallas")
    for r in res:
        print(r)

    print("\nExample 4: find_all_flights_country(country)")
    res = find_all_flights_country("China")
    for r in res:
        print(r)

    print("\nExample 5: find_flight_between(orig_airport, dest_airport)")
    pearson = get_airport_using_code("YYZ")
    ohare = get_airport_using_code("ORD")
    edm = get_airport_using_code("YEG")
    print(has_flight_between(edm, ohare))
    print(has_flight_between(edm, pearson))
    print(has_flight_between(pearson, ohare))

    print("\nExample 6: shortest_flight_from(orig_airport)")
    jfk = get_airport_using_code("JFK")
    print(shortest_flight_from(jfk))

    print("\nExample 7: find_return_flight(flight)")
    sf_to_sp = all_flights["SFO"][0]
    print(find_return_flight(sf_to_sp))

    print("\nExample 8: __add__(self, conn_flight) [in Flight.py]")
    f1 = all_flights["YEG"][0]
    f2 = all_flights["ORD"][0]
    print(f1 + f2)
    # print(f2 + f1)  # Should cause an Exception

    print("\nExample 9: create_maintenance_records(“maintenance.txt”, all_flights, all_airports)")
    create_maintenance_records("file.txt", all_flights, all_airports)
    print(len(maintenance_records))
    print(maintenance_records[0])
    print(maintenance_records[1])

    print("\nExample 10: find_total_cost(records)")
    m1 = MaintenanceRecord("YOI-104-ATL-1-2", all_flights, all_airports)
    m2 = MaintenanceRecord("RTK-498-ATL-15-5", all_flights, all_airports)
    m3 = MaintenanceRecord("ADJ-602-ATL-100-10", all_flights, all_airports)
    print(find_total_cost([m1, m2, m3]))

    print("\nExample 12: find_total_duration(records)")
    print(find_total_duration([m1, m2, m3]))

    print("\nExample 13: sort_maintenance_records(records)")
    recs = [m3, m2, m1]
    print(recs[0].get_total_cost(),
          recs[1].get_total_cost(),
          recs[2].get_total_cost())
    sorted_recs = sort_maintenance_records(recs)

    print(sorted_recs[0].get_total_cost(),
          sorted_recs[1].get_total_cost(),
          sorted_recs[2].get_total_cost())