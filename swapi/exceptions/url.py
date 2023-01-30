class InvalidURL(Exception):
    """Raised when the URL provided is not found in the Star Wars API."""
    
    def __init__(self, url) -> None:
        self.message = f"The URL '{url}' is not found in the Star Wars API."
        super().__init__(self.message)

class InvalidFormat(Exception):
    """Raised when the URL provided is not in the correct format."""
    
    def __init__(self, url) -> None:
        self.message = f"The URL {url} is not in the correct format."
        super().__init__(self.message)
