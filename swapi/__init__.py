"""
Star Wars API Wrapper
~~~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Star Wars API.

:copyright: (c) 2023-Present StarbuckBarista
:license: MIT, see LICENSE for more details.
"""

__title__ = "sqapi"
__author__ = "StarbuckBarista"
__license__ = "MIT"
__copyright__ = "Copyright 2023-Present StarbuckBarista"
__version__ = "1.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .main import *
from .types import *
from .exceptions import *
