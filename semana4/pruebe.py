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

    print("=== SISTEMA DE PRODUCCIÓN AGROINDUSTRIAL ===\n")

    while True:
        codigo_ingresado = input("Ingrese el código de producción (o 'fin'): ").strip()

        if codigo_ingresado.lower() == "fin":
            break

        if len(codigo_ingresado) != 5:
            print(f"Dato inválido: {codigo_ingresado} → Debe tener 5 dígitos\n")
            continue

        try:
            num_lote = int(codigo_ingresado[0])
            cantidad_producto = int(codigo_ingresado[1:4])
            ultimo_digito = int(codigo_ingresado[-1])
        except ValueError:
            print(f"Dato inválido: {codigo_ingresado} → Solo números\n")
            continue

        if num_lote not in [1, 2, 3]:
            print("Lote inválido. Use 1, 2 o 3.\n")
            continue

        if ultimo_digito not in [0, 1]:
            print("Último dígito inválido. Solo 0 o 1.\n")
            continue

        indice = num_lote - 1
        cantidad_unidades[indice] += cantidad_producto
        lotes[indice] += 1
        total_lotes += 1
        total_unidades += cantidad_producto

    if total_lotes == 0:
        print("\nNo se registraron lotes.")
        return

    # ========= TABLA =========
    print("\n" + "=" * 85)
    print(f"{'Producto':<15} {'Lotes':<10} {'Total unidades':<18} {'Prom. por lote':<18} {'Categoria':<15}")
    print("=" * 85)

    promedio_por_producto = []   # Guardamos solo los promedios de productos con lotes
    productos_con_lotes = 0

    for i in range(3):
        if lotes[i] == 0:
            promedio_lote = 0
            categoria = "Sin producción"
        else:
            promedio_lote = cantidad_unidades[i] / lotes[i]
            productos_con_lotes += 1

            if promedio_lote <= 99:
                categoria = "Insuficiente"
            elif promedio_lote <= 299:
                categoria = "Regular"
            elif promedio_lote <= 599:
                categoria = "Idoneo"
            else:
                categoria = "Sobreproduccion"

        producto = productos_agroindustriales(i + 1)
        print(f"{producto:<15} {lotes[i]:10d} {cantidad_unidades[i]:18d} "
              f"{promedio_lote:18.2f} {categoria:<15}")

        if lotes[i] > 0:                     # Solo guardamos productos que tienen lotes
            promedio_por_producto.append(promedio_lote)

    # ========= RESUMEN GENERAL =========
    if productos_con_lotes == 0:
        promedio_general = 0
    else:
        # ← Aquí está lo que pediste: se divide solo por los productos que ingresaron lotes
        promedio_general = sum(promedio_por_producto) / productos_con_lotes

    # Producto con más unidades
    indice_mayor_unidades = 0
    for i in range(1, 3):
        if cantidad_unidades[i] > cantidad_unidades[indice_mayor_unidades]:
            indice_mayor_unidades = i

    # Producto con más lotes
    indice_mayor_lotes = 0
    for i in range(1, 3):
        if lotes[i] > lotes[indice_mayor_lotes]:
            indice_mayor_lotes = i

    print("\n" + "=" * 70)
    print("RESUMEN GENERAL")
    print("=" * 70)
    print(f"Producto con mayor cantidad de unidades : {productos_agroindustriales(indice_mayor_unidades + 1)} "
          f"({cantidad_unidades[indice_mayor_unidades]:,} unidades)")
    print(f"Producto con más lotes                 : {productos_agroindustriales(indice_mayor_lotes + 1)} "
          f"({lotes[indice_mayor_lotes]} lotes)")
    print(f"Promedio general                       : {promedio_general:.2f} "
          f"(promedio de los {productos_con_lotes} productos con producción)")
    print("=" * 70)


# ===================== EJECUCIÓN =====================
if __name__ == "__main__":
    linea_produccion()