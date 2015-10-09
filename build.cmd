@echo off
del /s /f /q dist
del /s /f /q edvard
python setup.py
copy *.xml dist
copy *.ini dist
copy d*.vap dist
move dist edvard
