from swapi.types.api import APIObject

class Film(APIObject):
    """Wrapper for the film object in the Star Wars API."
    
    Represents a film in the Star Wars universe, denoted <Film - ID>.
    """

    def __repr__(self) -> str:
        return f"<Film - {APIObject.getObjectID(self.data['url'])}>"

    @property
    def title(self) -> str: return self.data["title"]

    @property
    def episode_id(self) -> int: return self.data["episode_id"]

    @property
    def opening_crawl(self) -> str: return self.data["opening_crawl"]

    @property
    def director(self) -> str: return self.data["director"]

    @property
    def producer(self) -> str: return self.data["producer"]

    @property
    def release_date(self) -> str: return self.data["release_date"]

    @property
    def characters(self) -> list[int]: return [APIObject.getObjectID(character) for character in self.data["characters"]]

    @property
    def planets(self) -> list[int]: return [APIObject.getObjectID(planet) for planet in self.data["planets"]]

    @property
    def starships(self) -> list[int]: return [APIObject.getObjectID(starship) for starship in self.data["starships"]]

    @property
    def vehicles(self) -> list[int]: return [APIObject.getObjectID(vehicle) for vehicle in self.data["vehicles"]]

    @property
    def species(self) -> list[int]: return  [APIObject.getObjectID(species) for species in self.data["species"]]
