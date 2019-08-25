
from distutils.core import setup
from time import strftime as date

setup(name = "apyg",
	version = "0.8b-" + date('%g%m%d-%H%M%S'),
	description = "Random Password Generator.",
	author = "Chuck Stearns",
	author_email = "apyg@ozymo.com",
	url="http://apyg.ozymo.com",
	packages = ['apyglib'],
	scripts = ['apyg'],
	)
