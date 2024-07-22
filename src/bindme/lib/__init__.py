import sys

from .di_container import container
from .di_injector import inject

if sys.version_info < (3, 8):
    __all__ = [
        'container',
        'inject'
    ]
else:
    sys.exception("Python version is not available!")

__version__ = '0.1.0'
__author__ = '@daniyarsus'
