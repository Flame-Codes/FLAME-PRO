import os, sys
try:
    __import__("srv").st()
except Exception as e:
    exit(str(e))
