texto = '       hola, mi nombre es Constanza Pérez Olivares y estoy haciendo un bootcamp que es el mejor del mundo mundial y del universo   '

texto_limpio= texto.strip()
# .strip Elimina espacios en blanco de ambos extremos.
# .strip(): Elimina espacios en blanco de ambos extremos.
# .lstrip(): Elimina espacios en blanco del lado izquierdo.

print('-----------------------------Ej1------------------------------------------')
print(texto)
print(texto_limpio)
print('--------------------------------Ej2---------------------------------------')
print(texto.lower())
print(texto.upper())
print('----------------------------------Ej3------------------------------------')
print(texto_limpio.replace('mundo','universo'))
        # replace() no modifica la cadena original, sino que devuelve una nueva cadena con los reemplazos realizados.
        # El método replace() es muy útil para realizar reemplazos de subcadenas dentro de una cadena de texto, ya sea para todas las apariciones de la subcadena o para un número específico de ellas.

print('----------------------------------Ej4------------------------------------')
print(texto_limpio.split())

print('----------------------------------Ej4------------------------------------')
print(texto_limpio.count('universo'))