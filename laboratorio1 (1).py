
### Creacion de la funcion del codigo ###
def lista_productos():
    lotes = [0, 0, 0]
    unidades = [0, 0, 0]
    total_lotes = 0
    total_unidades = 0

    while True:
        codigo_ingresado = input("Ingrese su codigo o Fin para salir: ")                          

        if codigo_ingresado.lower() == "fin":
            break

        if len(codigo_ingresado) != 5:
            print("Dato invalido debe tener unicamente 5 dígitos numericos:", codigo_ingresado)
            continue

        codigo_ingresado = True
        numeros = "0123456789"
        for caracter in codigo_ingresado:
            if caracter not in numeros: 
                print("dato invalido (solo números):", codigo_ingresado)
                break 

        num_lote = int(codigo_ingresado[0])
        cantidad_lote = int(codigo_ingresado[1:3])
        lote_entregado = int(codigo_ingresado[4])
               

        if lote_entregado < 0 or lote_entregado > 1:
            print(f"Seleccione una opcion valida si fue entregado si: 1 , No: 0 {lote_entregado}")

        indice = codigo - 1
        lotes[indice] = lotes[indice] + 1
        unidades[indice] = unidades[indice] + cantidad_lote
        total_lotes = total_lotes + 1
        total_unidades = total_unidades + cantidad

    if total_lotes > 0:
        promedio_total_produccion = total_unidades / total_lotes

    # Buscamos los mayores
    maximo_unidades = unidades[0]
    posicion_unidades = 0
    maximo_lotes = lotes[0]
    posicion_lotes = 0

    for i in range(1, 3):
        if unidades[i] > maximo_unidades:
            maximo_unidades = unidades[i]
            posicion_unidades = i 
        
     

lista_productos()
