# Manual Básico de Markdown y Fundamentos Iniciales de Programación

Este material reúne dos partes:

1. **Conceptos básicos de Markdown**, para escribir documentos con formato.
2. **Bases iniciales de programación en Python**, para comprender entrada, salida, variables y formato de impresión.

La idea es que este documento funcione como una **guía explicativa**, no solo como una lista de ejemplos.  
Piense en Markdown como el **cuaderno ordenado** donde se documenta el contenido, y en Python como la **herramienta** que ejecuta instrucciones.

---

# Parte 1. Manual básico de Markdown

## ¿Qué es Markdown?

Markdown es un lenguaje de marcado ligero que permite dar formato a un texto usando símbolos simples.  
Se utiliza mucho para:

- documentar proyectos
- escribir manuales
- crear archivos `README.md`
- tomar apuntes estructurados
- preparar contenido para plataformas como GitHub

### Analogía
Markdown es como escribir en un cuaderno usando reglas simples:

- `#` sirve para títulos
- `*` o `-` sirven para listas
- `` ` `` sirve para resaltar código

No se necesita un editor complicado. Basta con escribir texto plano siguiendo ciertas convenciones.

---

# Títulos y encabezados

Los encabezados se crean usando el símbolo `#`.  
Mientras más `#` se coloquen, menor será el nivel del encabezado.

## Ejemplos

# Título principal (nivel 1)
## Subtítulo (nivel 2)
### Sección (nivel 3)
#### Subsección (nivel 4)

## Sintaxis

```md
# Título principal
## Subtítulo
### Sección
#### Subsección
````

## Definición

Los encabezados permiten **organizar jerárquicamente** un documento.

## Caso de uso

Sirven para dividir un manual, una guía o un informe por temas.
Por ejemplo:

* un título principal para el nombre del documento
* subtítulos para las unidades
* secciones para los contenidos específicos

---

# Texto en cursiva y negrita

## Cursiva

La cursiva se utiliza para resaltar una palabra o frase de manera suave.

Ejemplo:

Esto es un ejemplo de *cursiva*. Continuar con el texto.

Sintaxis:

```md
Esto es un ejemplo de *cursiva*.
```

## Negrita

La negrita se utiliza para dar mayor énfasis a una palabra o idea importante.

Ejemplo:

Esto es un ejemplo de **negrita**.

Sintaxis:

```md
Esto es un ejemplo de **negrita**.
```

## Caso de uso

En un manual técnico:

* la **negrita** puede resaltar definiciones importantes
* la *cursiva* puede destacar términos o palabras clave
---

# Viñetas y listas

Las listas ayudan a presentar información de forma ordenada y fácil de leer.

---

## Listas desordenadas

Se usan cuando el orden no importa.

### Ejemplo

Ingredientes:

* Huevos
* Harina
* Azúcar
* Azúcar moreno

### Sintaxis

```md
Ingredientes:
- Huevos
- Harina
- Azúcar
- Azúcar moreno
```

---

## Listas ordenadas

Se usan cuando sí importa el orden.

### Ejemplo

Pasos a seguir:

1. Precalentar
2. Mezclar
3. Hornear

### Sintaxis

```md
Pasos a seguir:
1. Precalentar
2. Mezclar
3. Hornear
```

---

# Enlaces

Los enlaces permiten dirigir al lector hacia otra página o recurso.

## Ejemplo

[Enlace de interés](https://www.google.com)


## Definición

Un enlace está formado por dos partes:

* el texto visible entre corchetes `[]`
* la dirección entre paréntesis `()`

## Caso de uso

Sirve para enlazar:

* páginas web
* repositorios de GitHub
* videos
* documentos de apoyo

## Recomendación importante

Conviene escribir la dirección completa, por ejemplo:

```md
https://www.google.com
```

y no solo:

```md
google.com
```

porque algunos visores de Markdown requieren el protocolo completo.

---

# Imágenes

Las imágenes se insertan con una sintaxis parecida a la de los enlaces, pero agregando `!` al inicio.

## Sintaxis

```md
![Texto alternativo](nombre.png)
```

## Definición

Una imagen en Markdown tiene:

* un texto alternativo, que describe la imagen
* una ruta o nombre del archivo

## Nota

El archivo debe existir en la ruta indicada.
Si `nombre.png` no está donde corresponde, la imagen no se verá.

---

# Citas o bloques de cita

Las citas se crean con el símbolo `>`.

## Sintaxis

```md
> holaMundo.py
```

## Definición

Una cita resalta un texto como si fuera una observación, una nota o una referencia textual.

## Caso de uso

Sirve para:

* destacar una frase importante
* mostrar una observación del profesor
* presentar una nota técnica

---

# Bloques de código

Markdown permite mostrar código de forma clara.

---

## Código en una línea

Se encierra entre acentos graves simples:

Ejemplo:

`print("Hola mundo")`

## Caso de uso

Sirve para mencionar funciones, variables o fragmentos cortos de código dentro de un párrafo.

Por ejemplo:

La función `input()` permite leer datos desde el teclado.

---

## Código en varias líneas

Se encierra entre tres acentos graves.

### Ejemplo

```python
print("Hola mundo")
print("Hola mundo")
input()
```

````

## Definición
El bloque de código conserva:

- saltos de línea
- indentación
- estructura del código

## Caso de uso
Sirve para:

- mostrar programas completos
- explicar ejemplos
- documentar soluciones

## Nota importante
En el ejemplo original faltaban comillas de cierre.  
La forma correcta es:

```python
print("Hola mundo")
````

y no:

```python
print("hola mundo)
```

---

# Tablas

Las tablas permiten organizar datos en filas y columnas.

## Ejemplo

| Nombre | Apellido |
| ------ | -------- |
| Diego  | Orozco   |


## Definición

Una tabla está formada por:

* una fila de encabezados
* una línea separadora
* una o más filas de datos

## Caso de uso

Sirve para:

* comparar datos
* mostrar registros
* resumir información

---

# Parte 2. Las bases del código

# ¿Qué es programar?

Programar es **dar instrucciones claras, ordenadas y finitas** para que una computadora realice una tarea.

## Ideas clave

* crear una solución
* dar instrucciones
* seguir una secuencia de pasos
* resolver un problema de manera finita
* lograr que la computadora ejecute una tarea concreta

## Definición formal

Programar consiste en diseñar y escribir instrucciones en un lenguaje que la computadora pueda interpretar o ejecutar.

## Explicación

La computadora no adivina.
Necesita que cada paso esté indicado con claridad.
Si una instrucción es ambigua, incompleta o incorrecta, el programa puede fallar.

---

## Algoritmo y pseudocódigo

### ¿Qué es un algoritmo?

Un algoritmo es una **secuencia de pasos ordenados y finitos** para resolver un problema.

### ¿Qué es el pseudocódigo?

El pseudocódigo es una forma de describir un algoritmo usando lenguaje estructurado y entendible por personas, sin necesidad de usar la sintaxis real de un lenguaje de programación.

## Idea importante

Un algoritmo **no es lo mismo que un código**.

* el algoritmo describe la lógica
* el código traduce esa lógica a un lenguaje como Python

## Características de un algoritmo

1. **Finito**
   Debe terminar en algún momento.

2. **Preciso**
   Cada paso debe estar claramente definido.

3. **Definido**
   Si se ejecuta varias veces bajo las mismas condiciones, debe dar el mismo resultado.

---

# Actividad

## Enunciado

Describir el algoritmo exacto para que un empleado le venda una bolsa de arroz a un cliente que acaba de entrar a la tienda.

## Ejemplo de algoritmo

1. INICIO
2. Saludar al cliente.
3. Preguntar qué producto desea.
4. Escuchar la respuesta del cliente.
5. Si el cliente pide arroz, caminar al pasillo 3, estante 2.
6. Tomar 1 bolsa de arroz.
7. Caminar a la caja registradora.
8. Decir el precio: "Son 2000 colones".
9. Recibir el dinero.
10. Entregar el arroz y el cambio.
11. Despedirse.
12. FIN

## Explicación

Este ejemplo muestra que incluso una tarea cotidiana puede descomponerse en pasos lógicos.

---

# Entrada y salida

En programación, muchos programas funcionan con este esquema:

* **entrada**: datos que recibe el programa
* **salida**: resultados que muestra

En Python, las funciones más básicas para esto son:

* `print()` para salida
* `input()` para entrada

---

## Salida

## La función `print()`

La función `print()` se usa para mostrar información en pantalla.

### Reglas básicas de sintaxis

* se escribe en minúscula: `print`
* lo que se quiere mostrar va entre paréntesis `()`
* el texto debe ir entre comillas simples `' '` o dobles `" "`

## Ejemplos

```python
print("Hola Mundo")
```

```python
print('Bienvenido a la tienda digital')
```

## Definición

`print()` envía información a la consola para que el usuario pueda verla.

## Caso de uso

Sirve para:

* mostrar mensajes
* dar instrucciones al usuario
* imprimir resultados
* depurar programas

---

## Entrada

## La función `input()`

La función `input()` se usa para pedir información al usuario.

### Reglas básicas de sintaxis

* se escribe en minúscula: `input`
* el mensaje va entre paréntesis
* espera una respuesta del usuario
* el dato devuelto por `input()` es de tipo `string`
* normalmente se guarda en una variable

## Ejemplo

```python
print('Bienvenido a la tienda digital')

producto_cliente = input('¿Qué deseas comprar? ')

print('El producto que escogió es:')
print(producto_cliente)
```

## Explicación

Aquí ocurre lo siguiente:

1. Se muestra un mensaje de bienvenida.
2. Se le pide al usuario que escriba un producto.
3. La respuesta se guarda en `producto_cliente`.
4. Luego se imprime lo que escribió.

## Nota importante

Aunque el usuario escriba números, `input()` los recibe como texto.

Por ejemplo, si el usuario escribe:

```text
25
```

Python lo recibirá como `"25"` y no como número entero `25`.

---

# Convenciones para nombrar variables

Nombrar bien las variables es importante porque el código debe ser entendible.

## Camel case

Ejemplo:

```python
miNombreApellido
```

## Snake case

Ejemplo:

```python
mi_nombre_apellido
```

## Pascal case

Ejemplo:

```python
MiNombreApellido
```

## Recomendación en Python

En Python normalmente se prefiere **snake_case** para variables.

## Caso de uso

Si un estudiante escribe:

```python
x = "Diego"
```

el programa puede funcionar, pero el nombre no explica nada.
En cambio:

```python
nombre_estudiante = "Diego"
```

es mucho más claro.

---

## Código explicado de entrada y salida

```python
# saludo inicial de la tienda digital
print("================================")
print("Bienvenido a la tienda digital")
print("================================")

producto_cliente = input("¿Qué deseas comprar? ")
edad_cliente = input("¿Cuál es tu edad? ")

# opción 1: dos print separados
print("1. El producto que escogió es: ", end="")
print(producto_cliente)

# opción 2: un solo print con formato
print(f"2. El producto que escogió es: {producto_cliente}. Y la edad del cliente es: {edad_cliente}")

# opción 3: un solo print con concatenación
print("3. El producto que escogió es: " + producto_cliente)
```

## Explicación por partes

### Encabezado visual

```python
print("================================")
print("Bienvenido a la tienda digital")
print("================================")
```

Sirve para que la salida se vea más ordenada.

### Lectura de datos

```python
producto_cliente = input("¿Qué deseas comprar? ")
edad_cliente = input("¿Cuál es tu edad? ")
```

Aquí se piden dos datos al usuario y se guardan en variables.

### Opción 1: dos `print`

```python
print("1. El producto que escogió es: ", end="")
print(producto_cliente)
```

El parámetro `end=""` evita que el primer `print` haga salto de línea.
Así, el segundo `print` continúa en la misma línea.

#### Sin `end=""`

La salida sería:

```text
1. El producto que escogió es:
Arroz
```

#### Con `end=""`

La salida queda:

```text
1. El producto que escogió es: Arroz
```

### Opción 2: f-string

```python
print(f"2. El producto que escogió es: {producto_cliente}. Y la edad del cliente es: {edad_cliente}")
```

Esta es una forma moderna y clara de insertar variables dentro de un texto.

### Opción 3: concatenación

```python
print("3. El producto que escogió es: " + producto_cliente)
```

Une cadenas de texto con el operador `+`.

## Recomendación

En Python suele preferirse usar **f-strings** porque son más legibles y cómodas.

---

# Ejercicio práctico de entrada y salida

## Ejercicio 1

Al salir de la tienda, se desea que el sistema haga dos preguntas al usuario:

* su producto favorito
* qué calificación le da a la tienda del 1 al 10

Luego, ambas respuestas deben guardarse e imprimirse en un mensaje final.

## Solución

```python
print("--- Encuesta de salida ---")
producto_fav = input("¿Cuál fue su producto favorito hoy? ")
calificacion = input("Del 1 al 10, ¿cómo califica nuestro servicio? ")

print("¡Gracias por sus respuestas!")
print("Tomaremos en cuenta su gusto por:")
print(producto_fav)
print("La calificación brindada fue:")
print(calificacion)
```

## Explicación

Este ejercicio refuerza tres ideas:

1. pedir datos al usuario
2. almacenarlos en variables
3. mostrarlos después en la salida

---

# Caracteres de escape (`\n` y `\t`)

Los caracteres de escape permiten controlar el formato del texto.

## `\n` salto de línea

Hace lo mismo que presionar Enter.

## `\t` tabulación

Inserta un espacio amplio o tabulación entre elementos.

## Ejemplo

```python
# salto de línea
print("1. leche")
print("2. café")
print("3. arroz")

print("1. leche\n2. café\n3. arroz")

# tabulación
print("Productos\tPrecio")
print("1. leche\t$2.50")
print("2. café\t\t$3.00")
print("3. arroz\t$1.50")

print("Productos\tPrecio\n1. leche\t$2.50\n2. café\t\t$3.00\n3. arroz\t$1.50")
```

## Explicación

Con `\n` se pueden escribir varias líneas dentro de un solo `print`.
Con `\t` se pueden separar columnas de manera básica.

## Caso de uso

Sirve para:

* menús
* reportes sencillos
* facturas en consola
* salidas más limpias

---

# Variables

Una variable es un **espacio en memoria** con un **nombre** donde se guarda un valor.

## Definición sencilla

Una variable funciona como una caja etiquetada.

* la etiqueta es el nombre
* el contenido es el valor guardado

## Crear variables

Sintaxis general:

```python
nombre_variable = valor
```

## Ejemplo

```python
nombre = "Diego"
```

Aquí:

* `nombre` es la variable
* `"Diego"` es el valor almacenado

---

## Reglas básicas para nombrar variables

* no usar espacios
* no iniciar con números
* usar nombres descriptivos
* seguir una convención consistente

## Ejemplos incorrectos

```python
4x = 522
x = "hola"
mi nombre = "Diego"
```

## Explicación

### `4x = 522`

Es incorrecto porque una variable no puede comenzar con número.

### `x = "hola"`

Puede funcionar, pero no es descriptiva.

### `mi nombre = "Diego"`

Es incorrecto porque contiene espacio.

## Ejemplos correctos

```python
edad_cliente = 25
nombre_estudiante = "Diego"
producto_principal = "Arroz"
```

---

# Ejercicio de inventario

## Enunciado

Declarar 3 productos.
El usuario debe indicar:

* el nombre de cada producto
* el precio de cada producto
* la cantidad disponible de cada producto

Luego, se debe generar una factura o reporte con este formato general:

* encabezado
* producto
* precio
* cantidad

---

## Pseudocódigo

```text
solicitar productos, precio y cantidad

leer nombre del producto 1
leer precio del producto 1
leer cantidad del producto 1

leer nombre del producto 2
leer precio del producto 2
leer cantidad del producto 2

leer nombre del producto 3
leer precio del producto 3
leer cantidad del producto 3

imprimir la factura
imprimir encabezado
imprimir producto 1 con su información
imprimir producto 2 con su información
imprimir producto 3 con su información
```

## Explicación

Este pseudocódigo organiza primero la **entrada de datos** y luego la **salida final**.

---

## Solución corregida y explicada

```python
producto1 = input("Ingrese el nombre del producto 1: ")
precio1 = input("Ingrese el precio del producto 1: ")
cantidad1 = input("Ingrese la cantidad del producto 1: ")

producto2 = input("Ingrese el nombre del producto 2: ")
precio2 = input("Ingrese el precio del producto 2: ")
cantidad2 = input("Ingrese la cantidad del producto 2: ")

producto3 = input("Ingrese el nombre del producto 3: ")
precio3 = input("Ingrese el precio del producto 3: ")
cantidad3 = input("Ingrese la cantidad del producto 3: ")

print("==============================")
print("FACTURA DE LA TIENDA")
print("==============================")

print(f'{"Producto":15}{"Precio":10}{"Cantidad":10}')
print(f'{producto1:15}{precio1:10}{cantidad1:10}')
print(f'{producto2:15}{precio2:10}{cantidad2:10}')
print(f'{producto3:15}{precio3:10}{cantidad3:10}')
```

---

# Explicación detallada del formato en `print`

Esta parte es muy importante porque aquí se trabaja el **ancho del texto**, la **alineación** y el **orden visual** de los datos.

## Ejemplo clave

```python
print(f'{"Producto":15}{"Precio":10}{"Cantidad":10}')
```

y también:

```python
print(f'{producto1:15}{precio1:10}{cantidad1:10}')
```

## ¿Qué significa `:15` o `:10`?

Dentro de una f-string, esto indica el **ancho mínimo del campo**.

Por ejemplo:

```python
{producto1:15}
```

significa:

* mostrar el valor de `producto1`
* reservar 15 espacios para imprimirlo

Si el texto ocupa menos de 15 caracteres, Python agrega espacios sobrantes.

## Ejemplo práctico

Si:

```python
producto1 = "Arroz"
```

entonces:

```python
print(f'{producto1:15}Fin')
```

podría verse así:

```text
Arroz          Fin
```

Observe que entre `Arroz` y `Fin` hay espacios automáticos.

---

## ¿Para qué sirve esto?

Sirve para **alinear columnas** y hacer que la salida se vea como una tabla.

### Sin formato

```python
print(producto1, precio1, cantidad1)
```

podría verse desordenado:

```text
Arroz 2500 10
Leche Entera 1800 2
Café 3500 15
```

### Con formato

```python
print(f'{producto1:15}{precio1:10}{cantidad1:10}')
```

se ve más uniforme:

```text
Arroz          2500      10
Leche Entera   1800      2
Café           3500      15
```

---

## Longitud del campo

Cuando se escribe:

```python
{variable:15}
```

el número `15` representa la **longitud mínima del espacio reservado** para esa variable.

* si el contenido es más corto, se rellena con espacios
* si el contenido es más largo, se imprime completo y puede romper la alineación

## Ejemplo

```python
nombre = "Ana"
print(f'{nombre:10}Fin')
```

Salida:

```text
Ana       Fin
```

Aquí se reservaron 10 espacios para `"Ana"`.

---

## Alineación

También se puede indicar cómo alinear el contenido.

### Alineación a la izquierda

```python
print(f'{"Ana":<10}Fin')
```

Salida:

```text
Ana       Fin
```

### Alineación a la derecha

```python
print(f'{"Ana":>10}Fin')
```

Salida:

```text
       AnaFin
```

### Centrado

```python
print(f'{"Ana":^10}Fin')
```

Salida aproximada:

```text
   Ana    Fin
```

## Significados

* `<` alinea a la izquierda
* `>` alinea a la derecha
* `^` centra el contenido

## Caso de uso

Esto es útil cuando:

* nombres van a la izquierda
* números van a la derecha
* encabezados se quieren centrar

---

## Ejemplos adicionales de formato

### Ejemplo 1: tabla simple

```python
producto = "Arroz"
precio = "2500"
cantidad = "10"

print(f'{"Producto":15}{"Precio":10}{"Cantidad":10}')
print(f'{producto:15}{precio:10}{cantidad:10}')
```

### Salida esperada

```text
Producto       Precio    Cantidad
Arroz          2500      10
```

---

### Ejemplo 2: alineación explícita

```python
producto = "Leche"
precio = "1800"
cantidad = "5"

print(f'{"Producto":<15}{"Precio":>10}{"Cantidad":>10}')
print(f'{producto:<15}{precio:>10}{cantidad:>10}')
```

### Salida esperada

```text
Producto            Precio  Cantidad
Leche                 1800         5
```

Aquí:

* el nombre del producto queda a la izquierda
* los números quedan alineados a la derecha

Eso mejora mucho la lectura.

---

### Ejemplo 3: encabezado decorado

```python
print("=" * 40)
print(f'{"FACTURA DE INVENTARIO":^40}')
print("=" * 40)
```

### Salida esperada

```text
========================================
          FACTURA DE INVENTARIO
========================================
```

## Explicación

* `"=" * 40` repite el símbolo `=` cuarenta veces
* `^40` centra el texto dentro de un ancho de 40 caracteres

---

