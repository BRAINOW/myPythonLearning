def funcion_kwargs(**kwargs): #El doble asterisco indica que el parametro va a ser un kwargs
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"Llave: {llave}, Valor: {valor}")

funcion_kwargs(nombre="Paco",apellido="Botero")