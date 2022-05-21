# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
palabra1_3letras = palabra_1 [0:3]
print('Las primeras 3 letras de la primera palabra son:', palabra1_3letras)
# De la segunda palabra tome las primeras dos letras, utilice el operador :
palabra2_2letras = palabra_2 [0:2]
print('Las primeras 2 letras de la segunda palabra son:', palabra2_2letras)
# Formar una nueva palabra con los recortes solicitados
nueva_palabra = palabra1_3letras + palabra2_2letras
# Imprima en pantalla los resultados
print('La nueva palabra es:', nueva_palabra)