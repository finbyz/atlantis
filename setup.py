from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in atlantis/__init__.py
from atlantis import __version__ as version

setup(
	name="atlantis",
	version=version,
	description="CRM Project",
	author="Finbyz tech pvt plt",
	author_email="info@finbyz.tech",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
