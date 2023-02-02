from __future__ import annotations
from swapi.exceptions import InvalidURL, InvalidFormat

from requests import get
from typing import Callable

class APIObject:
    """Wrapper for objects in the Star Wars API."
    
    Attributes:
        request: The request object from the requests library.
        data: The fetched dictionary data from the Star Wars API.

    Raises:
        InvalidURL: The URL provided is not found in the Star Wars API.
        JSONDecodeError: The URL provided is not in the correct format.
    """

    def __init__(self, apiURL) -> None:
        APIObject.getObjectID(apiURL)

        self.url = apiURL
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

    @staticmethod
    def getTypePointer(type: str, url: str) -> Callable[[], APIObject]:
        """Returns a function that returns an object of the specified type and ID.

        Arguments:
            type: The type of object to return.
            url: The URL of the object to return.
        
        Returns:
            A function that returns an object of the specified type and ID.

        Raises:
            InvalidURL: The URL provided is not found in the Star Wars API.
            InvalidFormat: The URL provided is not in the correct format.
        """

        class TypePointer:
            def __init__(self, type: str, url: str) -> None:
                self.type = type
                self.url = url

            def __repr__(self) -> str:
                return f"<Type Pointer - {self.type.title()} - {APIObject.getObjectID(self.url)}>"

            def __call__(self) -> APIObject:
                return APIObject(self.url)

        return TypePointer(type, url)
