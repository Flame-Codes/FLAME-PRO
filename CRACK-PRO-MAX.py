import os, sys
try:
    __import__("naim").bnsteam()
except Exception as e:
    exit(str(e))