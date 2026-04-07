#print("Cual es la cantidad de atun que ingresa a la tienda")
#latasAtun=int(input("Ingrese la cantidad de atun 47 "))
#estantes=int(latasAtun/10)
#almacenadas=int(latasAtun%10)

#print("Atun en exibicion")
#print("%20s:%10d" %("estantes llenos", estantes))
#print("%20s:%10d" %("latas en bodega", almacenadas))

edad=int(input("Indique su edad "))
membresia=input("indique que tipo de menbrecia posee ")
entradaSala=(edad >= 18) and (membresia=="premiun")

print("hola tu entrada a la sala VIP ")
print(f"el acceso a la sala es {entradaSala}")