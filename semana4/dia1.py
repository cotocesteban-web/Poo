
        es_valido = True
        numeros = "0123456789"
        for caracter in dato:
            if caracter not in numeros: 
                es_valido = False
                break 

        if not es_valido:
            print("dato invalido (solo números):", dato)
            continue

        codigo = int(dato[0])
        # Tomamos los dígitos de la cantidad (del índice 1 al 4 sin incluir el 4)
        cantidad = int(dato[1:4])

        if codigo < 1 or codigo > 3:
            print("dato invalido (codigo debe ser 1, 2 o 3):", dato)
            continue

        indice = codigo - 1
        lotes[indice] = lotes[indice] + 1
        unidades[indice] = unidades[indice] + cantidad
        total_lotes = total_lotes + 1
        total_unidades = total_unidades + cantidad

    # --- CÁLCULOS FINALES ---
    # Cambiamos promedio_gral por un nombre más claro
    promedio_total_produccion = 0
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
        if lotes[i] > maximo_lotes:
            maximo_lotes = lotes[i]
            posicion_lotes = i 

    # Muestra de resultados
    print("\n--- RESUMEN FINAL ---")
    print("Producto con mayores cantidades:", nombre_producto(posicion_unidades + 1))
    print("Producto con mas lotes:", maximo_lotes(posicion_lotes + 1))
    print(f"Promedio total de producción: {promedio_total_produccion:.2f}")

mi_lista_principal()