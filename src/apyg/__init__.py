"""apyg

Initialization file for the apyg application.
"""
__version__ = "0.9.1"
import sys
from pathlib import Path
from apyglib import crypt_print, phoenetic, random_password_stack
sys.path.append(str(Path(__file__).parent))
