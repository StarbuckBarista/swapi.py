from swapi.types.api import APIObject

class Species(APIObject):
    """Wrapper for the species object in the Star Wars API."
    
    Represents a species in the Star Wars universe, denoted <Species - Name - ID>.
    """

    def __repr__(self) -> str:
        return f"<Species - {self.name} - {APIObject.getObjectID(self.data['url'])}>"

    @property
    def name(self) -> str: return self.data["name"]

    @property
    def classification(self) -> str: return self.data["classification"]

    @property
    def designation(self) -> str: return self.data["designation"]

    @property
    def average_height(self) -> str: return self.data["average_height"]

    @property
    def skin_colors(self) -> str: return self.data["skin_colors"]

    @property
    def hair_colors(self) -> str: return self.data["hair_colors"]

    @property
    def eye_colors(self) -> str: return self.data["eye_colors"]

    @property
    def average_lifespan(self) -> str: return self.data["average_lifespan"]

    @property
    def homeworld(self) -> id: return APIObject.getTypePointer("Planet", self.data["homeworld"])

    @property
    def language(self) -> str: return self.data["language"]

    @property
    def people(self) -> list[id]: return [APIObject.getTypePointer("Character", person) for person in self.data["people"]]

    @property
    def films(self) -> list[id]: return [APIObject.getTypePointer("Film", film) for film in self.data["films"]]
