
funcionamiento = True
ingresarProductos = True
totalSinDesc = 0

while funcionamiento == True:
    
    cedula = input("Ingrese su número de cédula: ")
    rol = input("¿Es profesor/a o estudiante? ")

    if rol == "Profesora" or rol == "profesora" or rol == "PROFESORA":
        ans = "La profesora con cédula "
        ansParcial = "La profesora con cédula "
        desc = 0.2

    elif rol == "Profesor" or rol == "profesor" or rol == "PROFESOR":
        ans = "El profesor con cédula "
        ansParcial = "El profesor con cédula "
        desc = 0.2

    elif rol == "Estudiante" or rol == "estudiante" or rol == "ESTUDIANTE":
        ans = "El estudiante con cédula "
        ansParcial = "El estudiante con cédula "
        desc = 0.5
            
    while ingresarProductos == True:
        
        codProducto = input("Ingrese el código del producto: ")
        unidades = int(input("¿Cuántas unidades va a adquirir?(números): "))
        precio = int(input("Ingrese el precio de una unidad del producto(sin puntos ni comas): "))

        totalProducto = int(unidades * precio)
        totalParcial = int(totalProducto - (totalProducto * desc))
        
        totalSinDesc += totalProducto

        ansParcial = ansParcial + cedula + " debe pagar $" + str(totalParcial) + " por el producto " + codProducto + "."

        print("")
        print(ansParcial)
        print("")
        
        checkRegistro = input("¿Desea registrar más productos? (Si o No): ")

        if checkRegistro == "Si" or checkRegistro == "Sí" or checkRegistro == "SI" or checkRegistro == "si" or checkRegistro == "sí":   
            ingresarProductos = True

        elif checkRegistro == "No" or checkRegistro == "NO" or checkRegistro == "no":
            ingresarProductos = False

        if rol == "Profesora" or rol == "profesora":
            ansParcial = "La profesora con cédula "

        elif rol == "Profesor" or rol == "profesor":
            ansParcial = "El profesor con cédula "

        elif rol == "Estudiante" or rol == "estudiante":
            ansParcial = "El estudiante con cédula "        

    total = int(totalSinDesc - (totalSinDesc * desc))
    ans = ans + cedula + " debe pagar $" + str(total) + " en total."
    print("")
    print(ans)
    print("")
    
    checkFunc = input("¿Seguir registrando usuarios? (Si o No): ")

    if checkFunc == "Si" or checkFunc == "Sí" or checkFunc == "SI" or checkFunc == "si" or checkFunc == "sí":
        funcionamiento = True
        ingresarProductos = True
        ans = ""
        ansParcial = ""
        totalSinDesc = 0
        print("--------------")
    elif checkFunc == "No" or checkFunc == "NO" or checkFunc == "no":
        funcionamiento = False
