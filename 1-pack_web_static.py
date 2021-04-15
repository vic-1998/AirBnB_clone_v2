#!/usr/bin/python3
"""
script that generates a .tgz
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """create this folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None
