from setuptools import setup
from setuptools import find_packages

version = "0.1"

setup(name="sphinxtheme-simple",
      version=version,
      description="Simple sphinx theme",
      long_description=open("README", "r").read(),
      author="Andrey Popp",
      author_email="8mayday@gmail.com",
      url="http://pypi.python.org/pypi/sphinxtheme-simple",
      license="BSD3",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=False)
