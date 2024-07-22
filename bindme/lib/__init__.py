import sys

from bindme.lib.di_container import container
from bindme.lib.di_injector import inject

if sys.version_info < (3, 8):
    __all__ = [
        'container',
        'inject'
    ]

__version__ = '0.1.0'
__author__ = '@daniyarsus'
__doc__ = "In process..."
