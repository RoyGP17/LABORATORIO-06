from builtins import print

print("UNION")
color = {"rojo", "azul"}
colores = {"violeta", "amarillo", "rojo"}

union = color.union(colores)

print(union)
print()

print("INTERSECCION")
interseccion = color.intersection(colores)
print(interseccion)
print()

print("DIFERENCIA")
diferencia = color.difference(colores)
diferencia1 = color - colores
print(diferencia)
print(diferencia1)
print()

print("DIFERENCIA SIMETRICA")
diferencia_simetrica = color.symmetric_difference(colores)
print(diferencia_simetrica)