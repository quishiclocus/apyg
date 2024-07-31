"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="apyg",  # Required
    version="0.9.0",  # Required
    description="A random password generator",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/plain",  # Optional (see note above)
    url="https://github.com/quishiclocus/apyg",  # Optional
    author="quishiclocus",  # Optional
    author_email="chuck.stearns@gmail.com",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="apyg, setuptools, development, password, generator",  # Optional
    packages=find_packages(where=""),  # Required
    python_requires=">=3.7, <4",
    install_requires=["crypt", "argparse"],  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "apyg=apyg:main",
        ],
    },
    project_urls={  # Optional
        "Bug Reports": "https://github.com/quishiclocus/apyg/issues",
        "Source": "https://github.com/quishiclocus/apyg/",
    },
)
