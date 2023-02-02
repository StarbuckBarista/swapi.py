import swapi
from swapi.types import *

def test_films():
    film_one: Film = swapi.getObjectByID("films", 6)
    film_two: Film = swapi.getObjectByName("films", "Revenge")[0]

    film_one_character: Character = swapi.castToType(Character, film_one.characters[0])
    film_two_character: Character = swapi.castToType(Character, film_two.characters[0])

    assert film_one.data == film_two.data
    assert film_one_character.data == film_two_character.data
    print("Films Passed! (1/7)")

def test_characters():
    character_one: Character = swapi.getObjectByID("people", 10)
    character_two: Character = swapi.getObjectByName("people", "Obi")[0]

    character_one_film: Film = swapi.castToType(Film, character_one.films[0])
    character_two_film: Film = swapi.castToType(Film, character_two.films[0])

    assert character_one.data == character_two.data
    assert character_one_film.data == character_two_film.data
    print("Characters Passed! (2/7)")

def test_planets():
    planet_one: Planet = swapi.getObjectByID("planets", 14)
    planet_two: Planet = swapi.getObjectByName("planets", "Kash")[0]

    planet_one_film: Film = swapi.castToType(Film, planet_one.films[0])
    planet_two_film: Film = swapi.castToType(Film, planet_two.films[0])

    assert planet_one.data == planet_two.data
    assert planet_one_film.data == planet_two_film.data
    print("Planets Passed! (3/7)")

def test_species():
    species_one: Species = swapi.getObjectByID("species", 3)
    species_two: Species = swapi.getObjectByName("species", "Wookie")[0]

    species_one_film: Film = swapi.castToType(Film, species_one.films[0])
    species_two_film: Film = swapi.castToType(Film, species_two.films[0])

    assert species_one.data == species_two.data
    assert species_one_film.data == species_two_film.data
    print("Species Passed! (4/7)")

def test_starships():
    starship_one: Starship = swapi.getObjectByID("starships", 3)
    starship_two: Starship = swapi.getObjectByName("starships", "Star")[0]

    starship_one_film: Film = swapi.castToType(Film, starship_one.films[0])
    starship_two_film: Film = swapi.castToType(Film, starship_two.films[0])

    assert starship_one.data == starship_two.data
    assert starship_one_film.data == starship_two_film.data
    print("Starships Passed! (5/7)")

def test_vehicles():
    vehicle_one: Vehicle = swapi.getObjectByID("vehicles", 4)
    vehicle_two: Vehicle = swapi.getObjectByName("vehicles", "Sand")[0]

    vehicle_one_film: Film = swapi.castToType(Film, vehicle_one.films[0])
    vehicle_two_film: Film = swapi.castToType(Film, vehicle_two.films[0])

    assert vehicle_one.data == vehicle_two.data
    assert vehicle_one_film.data == vehicle_two_film.data
    print("Vehicles Passed! (6/7)")

def test_relationships():
    object_one: Character = swapi.getObjectByID("people", 10)
    object_two: Film = swapi.getObjectByID("films", 6)

    assert swapi.areRelated(object_one, object_two) == True
    print("Relationships Passed! (7/7)")

if __name__ == "__main__":
    test_films()
    test_characters()
    test_planets()
    test_species()
    test_starships()
    test_vehicles()
    test_relationships()

    print("Tests Passed!")
