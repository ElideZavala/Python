# ---------------------------------------------------------------------------------------
# ? Chaining Decorators in Python

#! Ejemplo 10 >>>> Chaining Decorators
def info_name(func):

    def full_name(*args):
        func(*args)

    return full_name


def last_name(func):

    def full_name(*args):
        func(*args)

    return full_name


@info_name
@last_name
def name(name, last_name):
    print(f"mi nombre es {name} {last_name}")


name("Elide", "Zavala Vinagre")
