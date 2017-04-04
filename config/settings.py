from os import urandom
from binascii import hexlify


__author__ = ["mmarconm", "Marcelo Marcon"]
__version__ = "1.0.0"


DEBUG = True
SECRET_KEY = hexlify(urandom(32))
