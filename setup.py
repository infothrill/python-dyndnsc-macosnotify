#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup for dyndnsc."""

import os
import re
from setuptools import setup

BASEDIR = os.path.dirname(__file__)

with open(os.path.join(BASEDIR, "dyndnsc_macosnotify.py"), "r") as f:
    PACKAGE_INIT = f.read()

VERSION = re.compile(
    r".*__version__ = \"(.*?)\"", re.S).match(PACKAGE_INIT).group(1)

with open(os.path.join(BASEDIR, "README.rst"), "r") as f:
    README = f.read()

with open(os.path.join(BASEDIR, "CHANGELOG.rst"), "r") as f:
    CHANGELOG = f.read()


CLASSIFIERS = (
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved",
    "License :: OSI Approved :: MIT License",
    "Topic :: Internet",
    "Topic :: Internet :: Name Service (DNS)",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Systems Administration",
    "Environment :: Console",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: POSIX :: BSD",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6"
)


setup(
    name="dyndnsc_macosnotify",
    py_modules=["dyndnsc_macosnotify"],
    version=VERSION,
    author="Paul Kremer",
    author_email="@".join(("paul", "spurious.biz")),  # avoid spam,
    license="MIT License",
    description="plugin for dyndnsc providing macos desktop notifications",
    long_description=README + "\n\n" + CHANGELOG,
    keywords="dyndnsc plugin",
    url="https://github.com/infothrill/python-dyndnsc-macosnotify",
    # https://packaging.python.org/tutorials/distributing-packages/#python-requires
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    setup_requires=["pytest-runner"],
    install_requires=[
        "pync",
        "setuptools",
    ],
    tests_require=[
        "pytest>=3.2.5"
    ],
    entry_points={
        "dyndnsc.notifier_beta": [
            "macosnotify = dyndnsc_macosnotify:MacOsNotify"
        ]
    },
    classifiers=CLASSIFIERS,
    include_package_data=False,
    zip_safe=True
)
