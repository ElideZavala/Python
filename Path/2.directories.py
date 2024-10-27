# -------------------------------------------------------
# ---------------**## Directories ##** ------------------

from pathlib import Path

my_directory = Path("real_estate")
new_directory = Path("new_directory")

# ------------------- Usefull Directory Methods ------------------
# 1- exists() ->> Checking whether or not the directory exists.
print(new_directory.exists())  # False

# 2- mkdir() ->> Creating a new directory.
# my_directory.mkdir()  # creating a new directory

# 3- rmdir() ->> Removing an existing directory.
# my_directory.rmdir()  # removing the directory

# 4- rename() ->> renaming the directory.
# my_directory.rename("banana-spit")  # renaming the
# my_directory.rmdir()  # removing the directory

# 5- iterdir() ->> Iterating over the content of a directory.
# print(new_directory.iterdir())

# LC

# social_data = [data for data in new_directory.iterdir()]
# print(social_data)

# Generator Object
# for data in new_directory.iterdir():
#     print(data)

# 6- is_dir() ->> Checking if a path is a directory.
# paths = [data for data in new_directory.iterdir() if data.is_file()]
# print(paths)

# case 1: Searching using a pattern using the asterisk symbol (*)
# paths = [data for data in new_directory.iterdir() if data.is_dir()]
# print(paths)  # []

# case 2: Searching using a pattern using the asterisk symbol (*)
# python_files = [data for data in new_directory.rglob("*.py")]
# print(python_files)  # [PosixPath('new_directory/vsvs.py')]

# 7- glob() ->> Searching for files using a pattern.

python_files_two = [data for data in new_directory.rglob("*.*")]
print(python_files_two)  # [PosixPath('new_directory/vsvs.py')]

# con ["*.*"] ->> Searching for files using a pattern. buscamo todos los archivos que tengan un punto en su nombre
