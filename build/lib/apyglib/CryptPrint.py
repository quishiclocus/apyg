
import sys, string, crypt, math

class CryptPrint(object):
# Init
    def __init__(self):
        self.cryptprint=True
# Crypt printing.
    def printNewPasswordsCrypt(self,pword,l,m):
        count = 0
        if pword:
            sys.stdout.write(" ")
	sys.stdout.write(crypt.crypt(pword,pword[(len(pword)-m)-(l%m):]))
