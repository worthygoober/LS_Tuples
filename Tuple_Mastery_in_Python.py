# Task 1: Formatting Flight Itineraries

def list_itinerary(itineraries):
    for itinerary in itineraries:
        name, origin, destination = itinerary
        print(f"Itinerary: {name} - From {origin} to {destination}.")

flight_itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

list_itinerary(flight_itinerary)