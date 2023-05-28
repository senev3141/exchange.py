"""
Stack Exchange API Wrapper
~~~~~~~~~~~~~~~~~~

A basic wrapper for the Stack Exchange API.

:copyright: Copyright (c) 2023-present Senev
:license: MIT, see LICENSE for more details.
"""

__title__ = "exchange"
__author__ = "Senev"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2023-present Senev"
__version__ = "0.1.0a"
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=1, micro=0, releaselevel="alpha", serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, NamedTuple, Literal, VersionInfo
