import string
import random


###############
# RandomPasswordStack class:
# This class is used to build the Random Password Stack. pwords
# is the list of passwords.
class RandomPasswordStack(object):
    # Set up the object container for the password stack.
    def __init__(self):
        self.pwords = []
    # Create a pool of random characters (twice the length of the
    # requested password). jlen is the length of the password.

    def genpool(self, jlen, jmin, jseed, jspc, jstr):
        tmps = []    # List of characters
        random.seed(jseed or
                    random.uniform(100.00, 999.9) / random.uniform(4.0, 9.9))
        d = [random.choice(string.digits) for x in xrange(jlen)]
        c = [random.choice(string.letters) for x in xrange(jlen)]
        tmps += d
        tmps += c
        if jspc:
            sp = [random.choice(string.punctuation) for x in xrange(jlen)]
            tmps += sp
        s = self.cleanpool(tmps)
        random.shuffle(s)
        return(s)

    # Clean ambiguous and unwated characters from the genpool.
    def cleanpool(self, pool):
        # Unwanted special or ambiguous characters.
        deletechars = '<>\\`|~O0Il1'
        rem_sp = [item for item in pool if item not in deletechars]
        return rem_sp

    # Perform strict checks to ensure lower, upper,
    # digit, and special characters.
    def strictpool(self, pool, strict):
        check1 = check2 = check3 = check4 = False
        for chk in pool:
            if chk in string.lowercase:
                check1 = True
                break
        for chk in pool:
            if chk in string.uppercase:
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
    def genpword(self, l, m, s, sp, st):
        c = ''
        apass = ''
        pool = self.genpool(l, m, s, sp, str)
        for k in xrange(random.randint(m, l)):
            random.shuffle(pool)
            while pool[k] == c:
                del pool[k]
            apass += pool[k]
            c = pool[k]
        return(apass)

    # Push a new password onto the stack.
    def push(self, length, minlength, seed, spc, strict):
        self.pwords.append(self.genpword(length, minlength, seed, spc, strict))

    # Pop a new password from the stack.
    def pop(self):
        if len(self.pwords) != 0:
            newpword = self.pwords.pop()
            return newpword
        else:
            print("No more passwords.")
# End of class RandomPasswordStack
###############
