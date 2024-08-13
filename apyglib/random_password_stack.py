"""Import modules for string manipulation and processing
random values."""
import string
import random


###############
# RandomPasswordStack class:
# This class is used to build the Random Password Stack. pwords
# is the list of passwords.
class RandomPasswordStack():
    """RandomPasswordStack

    Generates a pool of characters and selects them via
    a random algorithm.
    """
    # Set up the object container for the password stack.

    def __init__(self):
        self.pwords = []
    # Create a pool of random characters (twice the length of the
    # requested password). jlen is the length of the password.

    def genpool(self, jlen, jseed, jspc):
        """genpool

        Create a pool of random characters for processing.
        """
        tmps = []    # List of characters
        random.seed(jseed or
                    random.uniform(100.00, 999.9) / random.uniform(4.0, 9.9))
        d = [random.choice(string.digits) for x in range(jlen)]
        c = [random.choice(string.ascii_letters) for x in range(jlen)]
        tmps += d
        tmps += c
        if jspc:
            sp = [random.choice(string.punctuation) for x in range(jlen)]
            tmps += sp
        s = self.cleanpool(tmps)
        random.shuffle(s)
        return (s)

    # Clean ambiguous and unwated characters from the genpool.
    def cleanpool(self, pool):
        """cleanpool

        Check for ambiguous and unwanted characters.
        """
        # Unwanted special or ambiguous characters.
        deletechars = '<>\\`|~O0Il1'
        rem_sp = [item for item in pool if item not in deletechars]
        return rem_sp

    # Perform strict checks to ensure lower, upper,
    # digit, and special characters.
    def strictpool(self, pool, strict):
        """strictpool

        Runs checks for lower, upper, digits, and punctuation
        in the final password.
        """
        check1 = check2 = check3 = check4 = False
        for chk in pool:
            if chk.lower():
                check1 = True
                break
        for chk in pool:
            if chk.upper():
                check2 = True
                break
        for chk in pool:
            if chk in string.digits:
                check3 = True
                break
        for chk in pool:
            if chk in string.punctuation:
                check4 = True
                break
        if any(checks is False for checks in (check1, check2, check3, check4)):
            check = False
        else:
            check = True
        return check

    # Create 1 password, between m and l characters long.
    def genpword(self, l, m, s, sp):
        """genpword

        Generates a random password from a pool.
        """
        c = ''
        apass = ''
        pool = self.genpool(l, m, s, sp, str)
        for k in range(random.randint(m, l)):
            random.shuffle(pool)
            while pool[k] == c:
                del pool[k]
            apass += pool[k]
            c = pool[k]
        return (apass)

    # Push a new password onto the stack.
    def push(self, length, minlength, seed, spc):
        """push method for processing the pool."""
        self.pwords.append(self.genpword(length, minlength, seed, spc))

    # Pop a new password from the stack.
    def pop(self):
        """pop method for processing the pool."""
        if len(self.pwords) != 0:
            newpword = self.pwords.pop()
            return newpword
# End of class RandomPasswordStack
###############
