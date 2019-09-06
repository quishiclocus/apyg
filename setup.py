
from distutils.core import setup
from time import strftime as date

setup(name = "apyg",
	version = "0.8b-" + date('%g%m%d-%H%M%S'),
	description = "Random Password Generator.",
	author = "Chuck Stearns",
	author_email = "chuck.stearns@gmail.com",
	url="",
	packages = ['apyglib'],
	scripts = ['apyg.py'],
	)
