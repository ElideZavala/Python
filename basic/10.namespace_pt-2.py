def outer():
    outer_number = 100 # local variable, esta dentro del namespace local y no puede ser accedido desde el namespace global pero si desde el namespace local de la funcion outer
    print(id(outer_number))
    global global_number
    global_number = 101 # nueva variable que pertece a la funcion outer, no es la misma que la global_number

    print("Global number = ", global_number) # podemos acceder a el por que esta en el namespace global pero no podemos modificarlo

    def inner():
        inner_number = 200 # local variable, esta dentro del namespace local y no puede ser accedido desde el namespace global pero si desde el namespace local de la funcion inner
        inner_number = "Jack"
        print("inner_number", inner_number)

        outer_number = 500
        print(id(outer_number)) # hace referencia al nuevo valor de outer_number
        
        print("outer_number", outer_number)
    inner()

global_number = 300 # global variable esta dentro del namespace global
print("Global number la 1 = ", global_number)

# obtener inner_number desde la funcion outer
outer()

print("Global number la 2 = ", global_number) # cambia el valor de global_number por que se modifico en la funcion outer