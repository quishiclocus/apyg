"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

<<<<<<< HEAD
from setuptools import setup, find_packages

setup(
    packages=find_packages(where="."),  # Required
)
||||||| parent of 41937d5 (nix-flake-testing)
setup(name = "apyg",
	version = "0.8b-" + date('%g%m%d-%H%M%S'),
	description = "Random Password Generator.",
	author = "Chuck Stearns",
	author_email = "chuck.stearns@gmail.com",
	url="",
	packages = ['apyglib'],
	scripts = ['apyg.py'],
	)
=======
setup(name = "apyg",
  version = "0.8b-" + date('%g%m%d-%H%M%S'),
  description = "Random Password Generator.",
  author = "Chuck Stearns",
  author_email = "chuck.stearns@gmail.com",
  url="",
  packages = ['apyglib'],
  scripts = ['apyg.py'],
)
>>>>>>> 41937d5 (nix-flake-testing)
