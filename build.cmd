@echo off
del /s /f /q dist
python setup.py
copy *.xml dist
copy *.ini dist
copy d*.vap dist
move dist edvard
