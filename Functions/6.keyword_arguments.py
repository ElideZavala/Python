# ---------------------------------------------------------------------------------------------------------
# ------------------------------------**## Keyword Arguments ##**------------------------------------------

# ! ************** Ejemplo 11 **************
def employee(**info):
    # {'name': 'Popeye', 'last_name': 'Gomez', 'age': 25, 'skill_set': 'Developer '}
    print(info)
    # retorna un diccionario con los valores ingresados


employee(name="Popeye", last_name="Gomez", age=25, skill_set="Developer")

# ! ************** Ejemplo 12 **************


def to_do(**to_do_status):
    return to_do_status


to_do_status_result = to_do(
    get_coffee="Done", exercise="Pending", watch_tv="In Progress")

# {'get_coffee': 'Done', 'exercise': 'Pending', 'watch_tv': 'In Progress'}
print(to_do_status_result)

# esto se llama keyword arguments, se puede pasar un número variable de argumentos a una función y se almacenan en un diccionario
# retornaremos un diccionario con los valores ingresados como argumentos en la función
