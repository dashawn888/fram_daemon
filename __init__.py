# -*- coding: utf-8 -*-
"""The standard fram config library."""
import os
import sys

__author__ = "Shawn Lee"
__email__ = "shawn@143t.com"


def main_decorator(func):
    """Make sure that the forking is handled properly."""
    def wrapped(fram):
        if fram["argparse"].daemon:
            if os.fork() != 0:
                sys.exit(0)
            pid_fh = open(fram["argparse"].pid_file, "w")
            pid_fh.write(str(os.getpid()))
            pid_fh.close()
        return func(fram)
    return wrapped


FRAM_PLUGIN = {
    "argparse": {
        "--daemon": {
            "help": "Causes the process to fork in the background.",
            "action": "store_true"},
        "--pid_file": {
            "help": "Location of pid file (after fork)"}
    },
    "main_decorator": main_decorator}
