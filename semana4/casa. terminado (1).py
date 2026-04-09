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
    cantidad_unidades = [0, 0, 0]
   

    while True:
        codigo_ingresado = input("Ingrese el código de producción (o 'fin'): ")

        if codigo_ingresado.lower() == "fin":
            break

        if len(codigo_ingresado) != 5:
            print(f"Dato invalido: {codigo_ingresado}")
            continue

        num_lote = int(codigo_ingresado[0])

        if num_lote not in [1, 2, 3]:
            print("Lote inválido")
            continue

        ultimo_digito = int(codigo_ingresado[-1])

        if ultimo_digito not in [0, 1]:
            print("Ultimo dígito inválido")
            continue


        cantidad_producto = int(codigo_ingresado[1:4])

        indice_lote = num_lote - 1

        cantidad_unidades[indice_lote] += cantidad_producto

        total_lotes += 1
        total_unidades += cantidad_producto

        lotes[indice_lote] += 1
    print()
    print(f"{'Producto':<15} {'Lotes':<15} {'Total unidades':<15} {'Prom. por lote':<15} {'Categoria':<15}")

    # ========= TABLA =========
    promedio_por_producto = []
    for i in range(3):

        if lotes[i] == 0:
            promedio_lote = 0
        else:
            promedio_lote = cantidad_unidades[i] / lotes[i]

        if promedio_lote <= 99:
            categoria = "Insuficiente"
        elif promedio_lote <= 299:
            categoria = "Regular"
        elif promedio_lote <= 599:
            categoria = "Idoneo"
        else:
            categoria = "Sobreproduccion"
        producto = productos_agroindustriales(i+1)
        print(f"{producto:<15} {lotes[i]:15d} {cantidad_unidades[i]:15d} {promedio_lote:15.2f} {categoria:<15}")
        promedio_por_producto.append(promedio_lote)

    # ========= RESUMEN =========

    producto_mayor_cantidades = 0
    producto_menor_cantidades = 0

    for i in range(3):
        if cantidad_unidades[i] > producto_mayor_cantidades:
            producto_mayor_cantidades = cantidad_unidades[i]
            producto_menor_cantidades = i

    mayor_lotes = 0
    menor_lotes = 0

    for i in range(3):
        if lotes[i] > mayor_lotes:
            mayor_lotes = lotes[i]
            menor_lotes = i

    if total_lotes == 0:
        promedio_general = 0
    else:
        promedio_general = promedio_lote / cantidad_unidades[i]

    print("Producto mayor cantidades:", productos_agroindustriales(producto_menor_cantidades + 1))
    print("Producto con mas lotes:", productos_agroindustriales(menor_lotes + 1))
    print("Promedio de productos producidos:", round(promedio_general, 2))


# ejecutar
linea_produccion()