class Flight:
    def __init__(self, flight_number, origin, destination, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger.name} added to flight {self.flight_number}.")
            return True
        else:
            print("Flight is full!")
            return False

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"Passenger {passenger.name} removed from flight {self.flight_number}.")
            return True
        else:
            print(f"Passenger {passenger.name} not found on flight {self.flight_number}.")
            return False

    def get_passenger_list(self):
        return [passenger.name for passenger in self.passengers]

    def __str__(self):
        return f"Flight {self.flight_number}: {self.origin} to {self.destination}, Capacity: {self.capacity}, Passengers: {len(self.passengers)}"

class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"Passenger {self.name}, Passport No: {self.passport_number}"

class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_number} added to airline {self.name}.")

    def remove_flight(self, flight):
        if flight in self.flights:
            self.flights.remove(flight)
            print(f"Flight {flight.flight_number} removed from airline {self.name}.")
            return True
        else:
            print(f"Flight {flight.flight_number} not found in airline {self.name}.")
            return False

    def find_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        print(f"Flight {flight_number} not found.")
        return None

    def __str__(self):
        return f"Airline: {self.name}, Total Flights: {len(self.flights)}"

# Example usage:

def main():
    # Create airline
    airline = Airline("OpenAI Airlines")

    # Create flights
    flight1 = Flight("OA123", "New York", "Los Angeles", 2)
    flight2 = Flight("OA456", "San Francisco", "Chicago", 3)

    # Add flights to airline
    airline.add_flight(flight1)
    airline.add_flight(flight2)

    # Create passengers
    passenger1 = Passenger("Ali", "A12345678")
    passenger2 = Passenger("Omer", "B98765432")
    passenger3 = Passenger("Ahmed", "C12398745")

    # Add passengers to flight
    flight1.add_passenger(passenger1)
    flight1.add_passenger(passenger2)
    # This should fail since flight1's capacity is 2
    flight1.add_passenger(passenger3)

    # Check passenger list for flight1
    print(f"Passengers on flight {flight1.flight_number}: {flight1.get_passenger_list()}")

    # Remove a passenger and check the list again
    flight1.remove_passenger(passenger1)
    print(f"Passengers on flight {flight1.flight_number}: {flight1.get_passenger_list()}")

    # Find a flight in the airline
    found_flight = airline.find_flight("OA456")
    if found_flight:
        print(f"Flight {found_flight.flight_number} found from {found_flight.origin} to {found_flight.destination}.")

    # Display information about the airline
    print(airline)

    # Display flight information
    print(flight1)
    print(flight2)

if __name__ == "__main__":
    main()
