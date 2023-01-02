Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import shutil
>>> path = "D:/Downloaded_Files"
>>> print(os.path.exists(path))
True
>>> True
True
>>> path2 = "D:/Other_Stuff"
>>> print(os.path.exists(path2))
True
>>> cucumber = shutil.move(path,path2)
