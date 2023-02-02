from swapi.types.api import APIObject

class Starship(APIObject):
    """Wrapper for the starship object in the Star Wars API."
    
    Represents a starship in the Star Wars universe, denoted <Starship - Name - ID>.
    """

    def __repr__(self) -> str:
        return f"<Starship - {self.name} - {APIObject.getObjectID(self.data['url'])}>"

    @property
    def name(self) -> str: return self.data["name"]

    @property
    def model(self) -> str: return self.data["model"]

    @property
    def starship_class(self) -> str: return self.data["starship_class"]

    @property
    def manufacturer(self) -> str: return self.data["manufacturer"]

    @property
    def length(self) -> str: return self.data["length"]

    @property
    def cost_in_credits(self) -> str: return self.data["cost_in_credits"]

    @property
    def crew(self) -> str: return self.data["crew"]

    @property
    def passengers(self) -> str: return self.data["passengers"]

    @property
    def max_atmosphering_speed(self) -> str: return self.data["max_atmosphering_speed"]

    @property
    def hyperdrive_rating(self) -> str: return self.data["hyperdrive_rating"]

    @property
    def MGLT(self) -> str: return self.data["MGLT"]

    @property
    def cargo_capacity(self) -> str: return self.data["cargo_capacity"]

    @property
    def consumables(self) -> str: return self.data["consumables"]

    @property
    def pilots(self) -> list[int]: return [APIObject.getTypePointer("Characrer", pilot) for pilot in self.data["pilots"]]

    @property
    def films(self) -> list[int]: return [APIObject.getTypePointer("Film", film) for film in self.data["films"]]
