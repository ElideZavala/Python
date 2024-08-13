# --------------------------------------------------------------------------------------
# Custom Containers Part 1

#! creating a custom container
print("******************* Example 21 *********************")


# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark] = self.bookmarks.get(
#             bookmark, 0) + 1  # increment the count


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Javascipt")

# print(target_bookmark.bookmarks)
print("******************* Ejercicio 22 *********************")


# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(
#             bookmark.lower(), 0) + 1  # increment the count

#     def __getitem__(self, bookmark):
#         return self.bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         # increment the count by the given value
#         self.bookmarks[bookmark.lower()] = count

#     def __len__(self):
#         return len(self.bookmarks)

#     def __iter__(self):
#         return iter(self.bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("Golang")
# target_bookmark.add("Golang")
# target_bookmark.add("Angular")

# print(target_bookmark.bookmarks["PYTHON"])  # 5


# target_bookmark["python"] = 110  # set the count to 110

# # print(target_bookmark)
# # print(target_bookmark.bookmarks) # {'python': 110, 'javascipt': 4, 'java': 3, 'golang': 2, 'angular': 1}
# # print(len(target_bookmark))  # 5

# # print(target_bookmark["python"])  # 5

# for bookmark in target_bookmark:
#     print(bookmark) # python, javascipt, java, golang, angular
# # print(target_bookmark.bookmarks)
print("****************************************")


# class BookmarkedPage:
#     def __init__(self):
#         self.__bookmarks = {}

#     def add(self, bookmark):
#         self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(
#             bookmark.lower(), 0) + 1  # increment the count

#     def __getitem__(self, bookmark):
#         return self.__bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         # increment the count by the given value
#         self.__bookmarks[bookmark.lower()] = count

#     def __len__(self):
#         return len(self.__bookmarks)

#     def __iter__(self):
#         return iter(self.__bookmarks)

# # CUANDO SE PONE __ ANTES DE UNA VARIABLE O METODO SE CONVIERTE EN PRIVADO y no se puede acceder desde fuera de la clase

# target_bookmark = BookmarkedPage()
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Javascipt")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("Golang")
# target_bookmark.add("Golang")
# target_bookmark.add("Angular")

# target_bookmark.bookmarks # AttributeError: 'BookmarkedPage' object has no attribute 'bookmarks' No se puede acceder a la variable bookmarks porque es privada
# print(target_bookmark.bookmarks) # AttributeError: 'BookmarkedPage' object has no
# attribute 'bookmarks'

#! Accessing a blocked dict key from outside
print("****************** Example 19 **********************")


class BookmarkedPage:
    def __init__(self):
        self.__bookmarks = {}

    def add(self, bookmark):
        self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(
            bookmark.lower(), 0) + 1  # increment the count

    def __getitem__(self, bookmark):
        return self.__bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        # increment the count by the given value
        self.__bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.__bookmarks)

    def __iter__(self):
        return iter(self.__bookmarks)

# CUANDO SE PONE __ ANTES DE UNA VARIABLE O METODO SE CONVIERTE EN PRIVADO y no se puede acceder desde fuera de la clase


target_bookmark = BookmarkedPage()
target_bookmark.add("Python")
target_bookmark.add("Python")
target_bookmark.add("Python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("Javascipt")
target_bookmark.add("Javascipt")
target_bookmark.add("Javascipt")
target_bookmark.add("Javascipt")
target_bookmark.add("Java")
target_bookmark.add("Java")
target_bookmark.add("Java")
target_bookmark.add("Golang")
target_bookmark.add("Golang")
target_bookmark.add("Angular")

# {'_BookmarkedPage__bookmarks': {'python': 5, 'javascipt': 4, 'java': 3, 'golang': 2, 'angular': 1}}
print(target_bookmark.__dict__)

# {'python': 5, 'javascipt': 4, 'java': 3, 'golang': 2, 'angular': 1}
print(target_bookmark._BookmarkedPage__bookmarks)
