import os, sys


try:
    print("Trying import local.py settings...", file=sys.stderr)
    from .local import *
except ImportError:
    print("Trying import development.py settings...", file=sys.stderr)
    from .development import *