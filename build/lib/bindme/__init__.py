import sys

from bindme.lib import (
    container,
    inject
)

if sys.version_info < (3, 8):
    __all__ = [
        'container',
        'inject'
    ]

__version__ = '0.1.0'
__author__ = '@daniyarsus'
__doc__ = "In process..."
