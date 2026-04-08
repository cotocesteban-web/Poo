# ### Creacion de la funcion del codigo ###
# def linea_produccion():
#     lotes = [0, 0, 0]
#     unidades = [0]
#     total_lotes = 0
#     total_unidades = 0

# def productos_agroindustriales():
#     if num_lote == 1:
#         return "Fertilizante"
#     if num_lote == 2:
#         return "Insecticida"
#     if num_lote == 3:
#         return "Herbicida"
    
#     while True:
#         codigo_ingresado = input("Por favor ingrese el codigo de produccion: ")                          

#         if codigo_ingresado.lower() == "fin":
#             break

#         if len(codigo_ingresado) != 5:
#             print("Dato invalido debe tener unicamente 5 dígitos numericos:", codigo_ingresado)
#             continue
    
#         numeros = "0123456789"
#         for caracter in codigo_ingresado:
#             if caracter not in numeros: 
#                 print("dato invalido (solo números):", codigo_ingresado)
#                 break

#         num_lote = int(codigo_ingresado[0])
#         cantidad_lote = int(codigo_ingresado[1:3])
#         lote_entregado = int(codigo_ingresado[4])


#         if num_lote < 1 or num_lote > 3:
#             print(f"dato invalido (codigo debe ser 1, 2 o 3): {codigo_ingresado}")
#             continue
#         elif lote_entregado < 0 or lote_entregado > 1:
#             print(f"Dato invalido: {codigo_ingresado}")

#         indice = codigo_ingresado - 1
#         lotes[indice] = lotes[indice] + 1
#         unidades[indice] = unidades[indice] + cantidad_lote
#         total_lotes = total_lotes + 1
#         total_unidades = total_unidades + cantidad

#     if total_lotes > 0:
#         promedio_total_produccion = total_unidades / total_lotes

#     # Buscamos los mayores
#     maximo_unidades = unidades[0]
#     posicion_unidades = 0
#     maximo_lotes = lotes[0]
#     posicion_lotes = 0

#     for i in range(1, 3):
#         if unidades[i] > maximo_unidades:
#             maximo_unidades = unidades[i]
#             posicion_unidades = i 
        
     

# linea_produccion()


def productos_agroindustriales(num_lote):
    if num_lote == 1:
        return "Fertilizante"
    elif num_lote == 2:
        return "Insecticida"
    elif num_lote == 3:
        return "Herbicida"
    else:
        return "Desconocido"
    
def linea_produccion():
    total_lotes = 0
    total_unidades = 0
    lotes = [0, 0, 0]
    unidades = [0, 0, 0]
    lote_entregado = 0
    lote_no_entregado = 0
   

    while True:
        codigo_ingresado = input("Ingrese el código de producción (o 'fin'): ")

        if codigo_ingresado.lower() == "fin":
            break

        if len(codigo_ingresado) != 5 or not codigo_ingresado():
            print("Dato invalido, debe tener 5 dígitos numéricos:", codigo_ingresado)
            continue

        # Ejemplo: primer dígito = tipo de lote
        num_lote = int(codigo_ingresado[0])

        if num_lote not in [1, 2, 3]:
            print("Lote inválido")
            continue
        ultimo_digito = int(codigo_ingresado[-1])

        if ultimo_digito not in [0, 1]:
            print("Ultimo dígito inválido (debe ser 0 o 1)")
            continue
        if ultimo_digito == 1:
         lote_entregado += 1
        else:
           lote_no_entregado += 1
        
        cantidad = int(codigo_ingresado[1:3])
        # Contador de unidades
        indice = num_lote - 1
        unidades[indice] += cantidad

        total_lotes += 1
        total_unidades += cantidad

    # Aquí guardas la unidad en su posición
    
        lotes[num_lote - 1] += 1
        unidades[num_lote - 1] += 1
        total_lotes += 1
        total_unidades += 1

        producto = productos_agroindustriales(num_lote)
        print(f"Registrado: {producto}")

    # Resumen final
    print("\nResumen:")
    for i in range(3):
        print(f"{productos_agroindustriales(i+1)}: {lotes[i]} lotes, {unidades[i]} unidades")

    print("Total lotes:", total_lotes)
    print("Total unidades:", total_unidades)


# Ejecutar
linea_produccion()
