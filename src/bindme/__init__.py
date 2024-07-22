import sys

from .lib import (
    container,
    inject
)

if sys.version_info < (3, 8):
    __all__ = [
        'container',
        'inject'
    ]
else:
    sys.exception("Python version is not available!")

__version__ = '0.1.0'
__author__ = '@daniyarsus'
__doc__ = "In process..."
