Version: apyg.py 0.9.1

Requirements: Python 3 or higher

```
usage: apyg.py [-h] [-V] [-t] [-p] [-s] [-y] [-n N] [-l L] [-m M] [-c SEED]

A random password generator

options:
  -h, --help            show this help message and exit
  -V, -v, --version     show program's version number and exit
  -t, --strict          require 1 each of upper, lower, digit, and special
  -p, --phoenetic       spell each password phoenetically
  -s, --spec-chars      use special characters
  -y, --crypt           print cryptographic hash of password
  -n N, --number N      no. of passwords to generate
  -l L, --maxlen L      maximum length of passwords
  -m M, --minlen M      if not defined, length is L
  -c SEED, --seed SEED  custom seed string, for repeatability

Defaults: 1 password, 8 characters long
```

\*\*NOTE: If you use the crypt function, it is best to have a diverse set of
minimum and maximum lengths. Also, the crypt function is currently broken.

To build and install apyg, run the following commands from the top directory.

Build a source distribution:

`poetry build`

To use the script, run `pip install .` in the repo directory.

Bugs: chuck.stearns@gmail.com

Changelog:

0.9.1 - Fixed cryptographic hash function. Changed default password length
to 16. Added version option. 240813

0.9.0 - Finally pushed the commits for updating to Python3 syntax.

0.8c - Updated the code to be Python 3 compliant. 190906

0.8b - Added an argument to specify inclusion of special characters. 120906

0.8a - Added the ability to seed the random pool. 111007

0.8 - Added min/max length functionality; added "Defaults" listing to README
and help. 111006

0.7 - Modularized the RandomPasswordStack class and the stuff that handles
phoenetic spelling. Added logic to handle zero-length passwords. 111005

0.6 - Made RandomPasswordStack class containing the logic for building
the passwords. Fixed broken phoenetic spelling for more than one password.
Included optparse to handle options. Added an argument to turn phoenetic
spelling on or off dynamically. 110930

0.5 - Added git repo to manage versioning. 110917

0.4 - Functionalized each step of the process and added
phoenetic spelling (off by default) of generated passwords. 110831

0.3 - Eliminated repeated characters from passwords. Added
date code to Changelog. 110804

0.2 - Changed password generation to use entire 16-character
pool and eliminate used entries; documented code.

0.1 - Wrote it.
