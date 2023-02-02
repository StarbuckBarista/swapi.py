from requests import get
from swapi.types import *

def getObjectByID(type: str, id: int) -> APIObject:
    """Returns an object of the specified type and ID.
    
    Parameters:
        type: The type of object to return.
        id: The ID of the object to return.

    Raises:
        InvalidURL: The URL provided is not found in the Star Wars API.
        JSONDecodeError: The URL provided is not in the correct format.
    """

    base_url = f"https://swapi.dev/api/{type}/{id}/"
    class_types = {
        "people": Character,
        "planets": Planet,
        "films": Film,
        "species": Species,
        "vehicles": Vehicle,
        "starships": Starship
    }

    return class_types[type](base_url)

def getObjectByName(type: str, name: str) -> list[APIObject]:
    """Returns a list of objects of the specified type and name.
    
    Parameters:
        type: The type of object to return.
        name: The name of the object to return.

    Raises:
        InvalidURL: The URL provided is not found in the Star Wars API.
        JSONDecodeError: The URL provided is not in the correct format.
    """

    base_url = f"https://swapi.dev/api/{type}/?search={name}"
    class_types = {
        "people": Character,
        "planets": Planet,
        "films": Film,
        "species": Species,
        "vehicles": Vehicle,
        "starships": Starship
    }

    request = get(base_url)
    data = request.json()
    results = [result["url"] for result in data["results"]]

    return [class_types[type](result_url) for result_url in results]

def areRelated(objectOne: APIObject, objectTwo: APIObject) -> bool:
    """Returns whether or not two objects are related.

    Parameters:
        objectOne: The first object to check.
        objectTwo: The second object to check.
    """
    
    related = False
    filteredID = APIObject.getObjectID(objectTwo.data["url"])

    if isinstance(objectOne, Film):
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.characters]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.planets]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.starships]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.vehicles]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.species]: related = True
    elif isinstance(objectOne, Character):
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.films]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.species]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.starships]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.vehicles]: related = True
        if filteredID is APIObject.getObjectID(objectOne.homeworld.url): related = True
    elif isinstance(objectOne, Planet):
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.films]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.residents]: related = True
    elif isinstance(objectOne, Species):
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.films]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.people]: related = True
        if filteredID is APIObject.getObjectID(objectOne.homeworld.url): related = True
    elif isinstance(objectOne, Vehicle):
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.films]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.pilots]: related = True
    elif isinstance(objectOne, Starship):
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.films]: related = True
        if filteredID in [APIObject.getObjectID(type_pointer.url) for type_pointer in objectOne.pilots]: related = True
    
    return related

def castToType(type: APIObject, object: APIObject) -> APIObject:
        """Returns an object of the specified type.

        Arguments:
            type: The type of object to return.
            object: The object to cast to the specified type.
        
        Raises:
            InvalidURL: The URL provided is not found in the Star Wars API.
            InvalidFormat: The URL provided is not in the correct format.
        """

        return type(object.url)
