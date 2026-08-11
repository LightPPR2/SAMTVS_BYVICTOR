"""
SAMTVS_BYVICTOR
Controle de TVs Samsung via WebSocket.

Autor: Victor Fernando
"""

__version__ = "1.0.7"

from .tv import SamsungTV

from .discovery import discover

from .exceptions import (
    SamsungTVError,
    ConnectionError,
    AuthenticationError,
)

__all__ = [
    "SamsungTV",
    "discover",
    "SamsungTVError",
    "ConnectionError",
    "AuthenticationError",
]