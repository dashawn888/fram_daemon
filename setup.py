# -*- coding: utf-8 -*-
from distutils.core import setup

__author__ = "Shawn Lee"
__email__ = "shawn@143t.com"


setup(
    name="python-fram_daemon",
    version="0.1.0",
    author="Shawn Lee",
    author_email="shawnl@143t.com",
    description="Fram standard py daemonization",
    keywords="fram daemon",
    packages=["fram_daemon"],
    package_dir={"fram_daemon": "."},
    # Utility function to read the README file.
    # Used for the long_description.  It's nice, because now 1) we have a top
    # level README file and 2) it's easier to type in the README file than to
    # put a raw string in below.
    long_description=open("README").read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"])
