from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "0.1.2"
        self.company_name = "SEVENGEAR"
        self.copyright = "Copyright (c) 2015 Sven Schmid."
        self.name = "edvard"

target = Target(
    description = "Elite Dangerous Voice Attack Relation Designer",
    script = "edvard.py",
    dest_base = "edvard")

setup(
    options = {'py2exe': {'bundle_files': 1,
                          'compressed': True}},
    zipfile = None,
    console = [target]
)