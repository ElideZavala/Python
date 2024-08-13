# -------------------------------------------------------------------------------------------
# Class Property & Property Decorator

print("******************** Example 30 ********************")


# class MovieRating:
#     def __init__(self, rating):
#         self.rating = rating


# movie_rating = MovieRating(10)
# movie_rating = MovieRating(-10)

print("******************* Ejemplo 31 *********************")


# class MovieRating:
#     def __init__(self, rating):
#         self.set_rating(rating)

#     def get_rating(self):
#         return self.__rating

#     def set_rating(self, value):
#         if value < 0:
#             raise ValueError("Rating must be a positive number")
#         self.__rating = value

#     rating = property(get_rating, set_rating) # property(getter, setter) funciona como un decorador de propiedad y ayuda a definir una propiedad en una clase


# movie_rating = MovieRating(7)  # ValueError: Rating must be a positive number
# # movie_rating.set_rating(0)
# print(movie_rating.get_rating())
# movie_rating.set_rating(10)
# print(movie_rating.get_rating()) # 10

print("******************* Ejercicio 32 *********************")


# class MovieRating:
#     def __init__(self, rating):
#         self.set_rating(rating)

#     def get_rating(self):
#         return self.__rating

#     def set_rating(self, value):
#         if value < 0:
#             raise ValueError("Rating must be a positive number")
#         self.__rating = value

#     # property(getter, setter) funciona como un decorador de propiedad y ayuda a definir una propiedad en una clase
#     rating = property(get_rating, set_rating)


# movie_rating = MovieRating(5)
# print(movie_rating.rating)  # 5


print("******************* Example 33 *********************")


class MovieRating:
    def __init__(self, rating):
        self.rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Rating must be a positive number")
        self.__rating = value


movie_rating = MovieRating(5)
print(movie_rating.rating)  # 5
movie_rating.rating = 10
print(movie_rating.rating)  # 10
