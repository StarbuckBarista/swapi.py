import swapi

def test_films():
    film_one = swapi.getObjectByID("films", 6)
    film_two = swapi.getObjectByName("films", "Revenge")[0]

    assert film_one.data == film_two.data
    print("Films Passed!")

def test_characters():
    character_one = swapi.getObjectByID("people", 10)
    character_two = swapi.getObjectByName("people", "Obi")[0]

    assert character_one.data == character_two.data
    print("Characters Passed!")

def test_planets():
    planet_one = swapi.getObjectByID("planets", 14)
    planet_two = swapi.getObjectByName("planets", "Kash")[0]

    assert planet_one.data == planet_two.data
    print("Planets Passed!")

def test_species():
    species_one = swapi.getObjectByID("species", 3)
    species_two = swapi.getObjectByName("species", "Wookie")[0]

    assert species_one.data == species_two.data
    print("Species Passed!")

def test_starships():
    starship_one = swapi.getObjectByID("starships", 3)
    starship_two = swapi.getObjectByName("starships", "Star")[0]

    assert starship_one.data == starship_two.data
    print("Starships Passed!")

def test_vehicles():
    vehicle_one = swapi.getObjectByID("vehicles", 4)
    vehicle_two = swapi.getObjectByName("vehicles", "Sand")[0]

    assert vehicle_one.data == vehicle_two.data
    print("Vehicles Passed!")

def test_relationships():
    object_one = swapi.getObjectByID("people", 10)
    object_two = swapi.getObjectByID("films", 6)

    assert swapi.areRelated(object_one, object_two) == True
    print("Relationships Passed!")

if __name__ == "__main__":
    test_films()
    test_characters()
    test_planets()
    test_species()
    test_starships()
    test_vehicles()
    test_relationships()

    print("Tests Passed!")
