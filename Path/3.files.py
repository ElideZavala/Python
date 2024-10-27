from pathlib import Path
import shutil
from time import ctime

source = Path("../property_dealer/property.py")
new_source = Path("../property_dealer/appdos.py")
my_directory = Path("../property_dealer/__init__.py")

# ------------------- Usefull File Methods ------------------

# 1- exists() ->> Checking whether or not the directory exists.
# print(new_source.exists())  # True

# 2- rename() ->> renaming the file.
# source.rename("../property_dealer/app2.py")  #

# 3- unlink() ->> Removing an existing file.
# new_source.unlink() # removing the file

# 4- stat() ->> Getting the status of a file.
# print(my_directory.stat())
# print(ctime(my_directory.stat().st_atime)) # last access time
# print(ctime(my_directory.stat().st_mtime)) # last modification time
# print(ctime(my_directory.stat().st_ctime)) # creation time

# ? The following 4 methods take care of opening and closing files.

# 5- read_bytes() ->> Reading the content of a file as bytes.
# print(my_directory.read_bytes())

# 6- read_text() ->> Reading the content of a file as text.
# print(my_directory.read_text())

# 7- write_bytes() ->> Writing the content of a file as bytes.
# print(my_directory.write_bytes(b'print("Hola desde kepler-b")'))  # 28
# print(my_directory.read_text())  # print("Hola desde kepler-b")

# 8- write_text() ->> Writing the content of a file as text.
# print(my_directory.write_text(
#     "print('somos Taygeta, Maya, Electra y Alcione')"))  # 48
# print('somos Taygeta, Maya, Electra y Alcione')
# print(my_directory.read_text())

# 9- Copyng a file to another location.
target_directory = Path("../astronomy")
# print(target_directory.exists())  # False
shutil.copy(my_directory, target_directory)
