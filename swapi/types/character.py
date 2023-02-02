from swapi.types.api import APIObject, TypePointer

class Character(APIObject):
    """Wrapper for the character object in the Star Wars API."
    
    Represents a character in the Star Wars universe, denoted <Characted - Name - ID>.
    """

    def __repr__(self) -> str:
        return f"<Character - {self.name} - {APIObject.getObjectID(self.data['url'])}>"

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
    def homeworld(self) -> TypePointer: return APIObject.getTypePointer("Planet", self.data["homeworld"])

    @property
    def films(self) -> list[TypePointer]: return [APIObject.getTypePointer("Film", film) for film in self.data["films"]]

    @property
    def species(self) -> list[TypePointer]: return [APIObject.getTypePointer("Species", species) for species in self.data["species"]]

    @property
    def vehicles(self) -> list[TypePointer]: return [APIObject.getTypePointer("Vehicle", vehicle) for vehicle in self.data["vehicles"]]

    @property
    def starships(self) -> list[TypePointer]: return [APIObject.getTypePointer("Starship", starship) for starship in self.data["starships"]]
