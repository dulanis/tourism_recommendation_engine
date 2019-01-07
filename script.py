# Tourism Recommendation Engine
destinations = ["Paris, France", "Shanghai, China",
                "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = {"name": "Erin Wilkes", "current_location": "Shanghai, China",
                 "interests": ["historical site", "art"]}


def get_destination_index(possible_destinations, destination):
    destination_index = possible_destinations.index(destination)
    return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler["current_location"]
    traveler_destination_index = get_destination_index(
        destinations, traveler_destination)
    return traveler_destination_index


traveler_destination_index = get_traveler_location(test_traveler)
attractions = [[] for place in destinations]


def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destinations, destination)
    except ValueError:
        print("That destination is not an option.")
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return


add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
