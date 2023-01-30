from swapi.types.api import APIObject

class Character(APIObject):
    """Wrapper for the character object in the Star Wars API."
    
    Represents a character in the Star Wars universe, denoted <Characted - ID>.
    """

    def __repr__(self) -> str:
        return f"<Character - {APIObject.getObjectID(self.data['url'])}>"

    @property
    def name(self) -> str: return self.data["name"]

    @property
    def height(self) -> str: return self.data["height"]

    @property
    def mass(self) -> str: return self.data["mass"]

    @property
    def hair_color(self) -> str: return self.data["hair_color"]

    @property
    def skin_color(self) -> str: return self.data["skin_color"]

    @property
    def eye_color(self) -> str: return self.data["eye_color"]

    @property
    def birth_year(self) -> str: return self.data["birth_year"]

    @property
    def gender(self) -> str: return self.data["gender"]

    @property
    def homeworld(self) -> int: return APIObject.getObjectID(self.data["homeworld"])

    @property
    def films(self) -> list[int]: return [APIObject.getObjectID(film) for film in self.data["films"]]

    @property
    def species(self) -> list[int]: return [APIObject.getObjectID(species) for species in self.data["species"]]

    @property
    def vehicles(self) -> list[int]: return [APIObject.getObjectID(vehicle) for vehicle in self.data["vehicles"]]

    @property
    def starships(self) -> list[int]: return [APIObject.getObjectID(starship) for starship in self.data["starships"]]
