@echo off
py -3.4 -m py2exe.build_exe edward.py --bundle-files 0
copy *.xml dist
copy *.ini dist
copy d*.vap dist