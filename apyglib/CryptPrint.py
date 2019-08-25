
import sys
import crypt


class CryptPrint(object):

    # Init
    def __init__(self):
        self.cryptprint = True

    # Crypt printing.
    def printNewPasswordsCrypt(self, pword, l, m):
        pw = ""
        if pw:
            sys.stdout.write(" ")
        sys.stdout.write(crypt.crypt(pw, pw[(len(pw) - m) - (l % m):]))
