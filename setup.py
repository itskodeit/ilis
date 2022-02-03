# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ilis/__init__.py
from ilis import __version__ as version

setup(
	name="ilis",
	version=version,
	description="Ikode-It logistics information system",
	author="Ikode-IT",
	author_email="info@kodeit.co.tz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
