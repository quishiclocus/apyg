#!/usr/bin/env python3

"""
quishiclocus, 2024
v 0.9.1

Generate random alphanumeric strings.
See README for usage and installation.
"""

# Standard Library Imports
import argparse
import sys

# Custom Library Imports
from apyglib.phoenetic import Phoenetic
from apyglib.crypt_print import CryptPrint
from apyglib.random_password_stack import RandomPasswordStack
from __init__ import __version__

# Set up default values and arguments with argparse
if __name__ == '__main__':
    o = argparse.ArgumentParser(
        description="A random password generator",
        epilog="Defaults: 1 password, 8 characters long",
    )
    o.add_argument("-V", "-v", "--version",
                   action="version", version="%(prog)s " + __version__)
    o.add_argument(
        "-t",
        "--strict",
        action="store_true",
        dest="strict",
        default=False,
        help="require 1 each of upper, lower, digit, and special",
    )
    o.add_argument(
        "-p",
        "--phoenetic",
        action="store_true",
        dest="phoenetic",
        default=False,
        help="spell each password phoenetically",
    )
    o.add_argument(
        "-s",
        "--spec-chars",
        action="store_true",
        dest="special_chars",
        default=False,
        help="use special characters",
    )
    o.add_argument(
        "-y",
        "--crypt",
        action="store_true",
        dest="crypt",
        help="print cryptographic hash of password",
    )
    o.add_argument(
        "-n", "--number", type=int, dest="n",
        help="no. of passwords to generate"
    )
    o.add_argument("-l", "--maxlen", type=int, dest="l",
                   help="maximum length of passwords")
    o.add_argument(
        "-m",
        "--minlen",
        type=int,
        dest="m",
        default=False,
        help="if not defined, length is L",
    )
    o.add_argument("-c", "--seed", dest="seed",
                   default=False,
                   help="custom seed string, for repeatability")

    o.set_defaults(n=1, l=16)

    opt = o.parse_args()

    # Main Program #

    # Do some checks on m to make sure it is equal to l if unset,
    # or smaller than l if set larger.
    if opt.m == 0:
        opt.m = opt.l
    if opt.m > opt.l:
        print("Switched max(", opt.l, ") and min(", opt.m, ")...")
        c = opt.l
        opt.l = opt.m
        opt.m = c
    if opt.strict:
        # imply special characters
        opt.special_chars = True
        # print("Strict checks are still under development. \
        #      Don't rely on them... yet.")

    g = RandomPasswordStack()

    # Create i passwords of j length
    for x in range(opt.n):
        g.push(opt.l, opt.m, opt.seed, opt.special_chars)

    # Print passwords
    while len(g.pwords) > 0:
        newpword = g.pop()
        sys.stdout.write(newpword)
        # Alternate print options
        # Phoenetic printing
        if opt.phoenetic:
            p = Phoenetic()
            p.print_new_password_phoenetic(newpword)
        # Cryptographic hashing
        if opt.crypt:
            p = CryptPrint()
            p.print_new_password_crypt(newpword, opt.seed, opt.l)
        # Strict checking
        if g.strictpool(newpword) is True and opt.strict is True:
            sys.stdout.write(" --> passes strict checks")
            # sys.stdout.write("")
        sys.stdout.write("\n")
