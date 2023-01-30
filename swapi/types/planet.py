from swapi.types.api import APIObject

class Planet(APIObject):
    """Wrapper for the planet object in the Star Wars API."
    
    Represents a planet in the Star Wars universe, denoted <Planet - ID>.
    """

    def __repr__(self) -> str:
        return f"<Planet - {APIObject.getObjectID(self.data['url'])}>"

    @property
    def name(self) -> str: return self.data["name"]

    @property
    def rotation_period(self) -> int: return int(self.data["rotation_period"])

    @property
    def orbital_period(self) -> str: return int(self.data["orbital_period"])

    @property
    def diameter(self) -> str: return self.data["diameter"]

    @property
    def climate(self) -> str: return self.data["climate"]

    @property
    def gravity(self) -> str: return self.data["gravity"]

    @property
    def terrain(self) -> str: return self.data["terrain"]

    @property
    def surface_water(self) -> str: return self.data["surface_water"]

    @property
    def population(self) -> str: return self.data["population"]

    @property
    def residents(self) -> list[int]: return [APIObject.getObjectID(resident) for resident in self.data["residents"]]

    @property
    def films(self) -> list[int]: return [APIObject.getObjectID(film) for film in self.data["films"]]
