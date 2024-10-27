# ----------------------------------------------------------------------------
#! ---------------------------- *** 4. Zip *** --------------------------------

from pathlib import Path

from zipfile import ZipFile

# * Create a Zip file
all_z = ZipFile("./zip_dir/all.zip", "w")  # Create a Zip file object
py_z = ZipFile("./zip_dir/py.zip", "w")  # Create a Zip file object

# print(all_z)

# *-*-*-*-*-*-*-*-* Adding File to Zip Files *-*-*-*-*-*-*-*-*
# # Approach One >>> all files
for path in Path("./Error-Handling").rglob("*.*"):
    all_z.write(path)
all_z.close()

# Approach Two >>> py files
with ZipFile("zip_dir/py.zip", "w") as py_files:
    for path in Path("./Error-Handling").rglob("*.py"):
        py_files.write(path)

# Lo que hace es que recorre todos los archivos y directorios de la carpeta social y los añade al archivo zip all.zip
# * Extract a Zip file
# with ZipFile("zip_dir/all.zip") as all_files:
#     print(all_files.namelist())
# .namelist() ->> List all files in the archive

# getting the information of the file
with ZipFile("zip_dir/py.zip") as file_info:
    info = file_info.getinfo("Error-Handling/1.what_are_exceptions.py")
    print(info.file_size)  # 648
    print(info.compress_size)  # 648
    print(info.filename)  # Error-Handling/1.what_are_exceptions.py
    print(info.__module__)  # zipfile

# * Extract a Zip file
with ZipFile("zip_dir/all.zip") as all_files_2:
    all_files_2.extractall("Extracted")
