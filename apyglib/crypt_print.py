""" Modules provide system print functions and hashing libraries. """
import sys
from hashlib import blake2b


class CryptPrint():
    """CryptPrint Class

    Attributes
    ----------
    pword, s, len_d
    """

    # Init
    def __init__(self):
        self.cryptprint = True

    # Crypt printing.
    def print_new_password_crypt(self, pword, s, len_d):
        """print_new_password_crypt

        Generates a crypt hash using the generated password,
        the optional seed, and the optional length.
        """
        digest_size = 4
        sys.stdout.write(" hash:")
        if len_d:
            digest_size = int(len_d)
        if s:
            seed = s.encode()
        else:
            seed = None
        pw = pword.encode()
        if seed:
            h = blake2b(key=seed, digest_size=digest_size)
        else:
            h = blake2b(digest_size=digest_size)
        h.update(pw)
        sys.stdout.write(h.hexdigest())

    # Some other crypt function TBD.
    def crypt_function(self):
        """crypt_function

        TBD in future.
        """
        return
