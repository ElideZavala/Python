# -----------------------------------------------------------------------------------------
#! ------------------- Paths ------------------ !#

# https://docs.python.org/3/library/

from pathlib import Path

# *_*_*_*_*_*_*_*_*_*_* Crating an absolute path on Windows *_*_*_*_*_*_*_*_*_*_*
# path = Path("C:\\Program Files\\Python 3")
# print(path)

# *_*_*_*_*_*_*_*_*_*_* Using raw string to simplify the path creation *_*_*_*_*_*_*_*_*_*_*

# *_*_*_*_*_*_*_*_*_*_* relative paths *_*_*_*_*_*_*_*_*_*_*
# path = Path("users/__init__.py")
# print(path)
# *_*_*_*_*_*_*_*_*_*_* combining Path() objects together *_*_*_*_*_*_*_*_*_*_*
# path_2 = Path("Some_Path") / Path("users")
# print(path_2) # Some_Path\users

# *_*_*_*_*_*_*_*_*_*_* combining Path() object with a string *_*_*_*_*_*_*_*_*_*_*
# path_3 = Path("some_file") / "ecommerce" / "__init__.py"
# print(path_3) # some_file\ecommerce\__init__.py

# *_*_*_*_*_*_*_*_*_*_* Getting the home directory of the current user *_*_*_*_*_*_*_*_*_*_*
# print(Path.home()) # C:\Users\hp

# *_*_*_*_*_*_*_*_*_*_* ----------------- *_*_*_*_*_*_*_*_*_*_*
# path = Path("social/audio")
# path2 = Path("social/images/__init__.py")
# path3 = Path("users")

# *_*_*_*_*_*_*_*_*_*_* to check to see if this path is a file *_*_*_*_*_*_*_*_*_*_*

# path = Path("social/audio")
# path2 = Path("social/images/__init__.py")
# path3 = Path("users")

# print(path.suffix) #
# print(path2.suffix) #.py
# print(path3.suffix) #

# *_*_*_*_*_*_*_*_*_*_* extracting individual components in the this path *_*_*_*_*_*_*_*_*_*_*
# returns the parent of the file.

# path = Path("social/audio")
# path2 = Path("social/images/__init__.py")
# path3 = Path("users")

# path3 = path2.with_name("__init__.txt")

# print(path)
# print(path2)
# print(path3)  # social\images\__init__.txt
# con .with_name() cambiamos el nombre del archivo, pero no cambiamos la extensión del archivo, el .txt es el nombre del archivo y no la extensión del archivo.

# *_*_*_*_*_*_*_*_*_*_* getting the absolute path for the newly created file *_*_*_*_*_*_*_*_*_*_*

# path = Path("social/audio")
# path2 = Path("social/images/__init__.py")
# path3 = Path("users")

# path3 = path2.with_name("__init__.txt")
# print(path3.absolute())  # C:\Users\hp\PycharmProjects\Python\social\images\__init__.txt

# *_*_*_*_*_*_*_*_*_*_* changing the extension of a file *_*_*_*_*_*_*_*_*_*_*

path = Path("social/audio")
path2 = Path("social/images/__init__.py")
path3 = Path("users")

path3 = path2.with_name("__init__.txt")

print(path3.with_suffix(".js"))  # social\images\__init__.js
# C:\Users\hp\PycharmProjects\Python\social\images\__init__.txt
print(path3.absolute())
