#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
"""

from fabric.api import env, local, cd, put, run, lcd
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.74.83.73', '54.172.228.152']


def do_clean(number=0):
    """Keep it clean."""
    number = int(number)
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
