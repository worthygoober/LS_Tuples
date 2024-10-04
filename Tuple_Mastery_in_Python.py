# Task 1: Formatting Flight Itineraries

def list_itinerary(itineraries):
    counter = 0
    for itinerary in itineraries:
        name, origin, destination = itinerary
        counter += 1
        print(f"Itinerary {counter}: {name} - From {origin} to {destination}.")

flight_itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

list_itinerary(flight_itinerary)