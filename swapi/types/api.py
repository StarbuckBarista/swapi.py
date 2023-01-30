from requests import get
from swapi.exceptions import InvalidURL, InvalidFormat

class APIObject:
    """Wrapper for objects in the Star Wars API."
    
    Attributes:
        request: The request object from the requests library.
        data: The fetched dictionary data from the Star Wars API.

    Raises:
        InvalidURL: The URL provided is not found in the Star Wars API.
        JSONDecodeError: The URL provided is not in the correct format.
    """

    def __init__ (self, apiURL) -> None:
        APIObject.getObjectID(apiURL)

        self.request = get(apiURL)
        self.data = self.request.json()

    @staticmethod
    def getObjectID(url: str) -> int:
        """Fetches the Object ID from an APIObject.

        Arguments:
            data: The fetched dictionary data from the Star Wars API.
        
        Returns:
            An integer representing the ID of the object.

        Raises:
            InvalidURL: The URL provided is not found in the Star Wars API.
            InvalidFormat: The URL provided is not in the correct format.
        """

        try: return int(url.split("/")[-2])
        except IndexError: raise InvalidURL(url)
        except ValueError: raise InvalidFormat(url)
