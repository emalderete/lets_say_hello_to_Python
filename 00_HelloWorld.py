# Colocando un # se puede comentar el código
# Hola mundo (mensaje mostrado por consola)
# El punto de interrupción del VS Code permite interrumpir la ejecución del código, es muy útil para hacer debug.

print('Hello World!')

"""
Este sería un comentario
en varias líneas
muy útil para poder comentar el código
sin hacer textos muy largos
"""

'''
Este también es un comentario
en varias líneas
Se puede usar tanto comillas simples
como las comillas dobles
'''

# Vamos a probar una función propia de python, el método "type"
# El método type sirve para identificar que tipo de valor se ingresó (string, boolean, int)

# En consola debe mostrar que este dato es un tipo string
'''
type('Hello Python') será igual a <class 'str'>
type(5) será igual a <class 'int'>
type(1.5) será igual a <class 'float'>
type(False) será igual a <class 'bool'>
'''
print(type('Hello Python!'))
print(type(5))
print(type(1.5))
print(type(False))

# Los números complejos serían números imaginarios
# El resultado sería <class 'complex'>

print(type(3 + 1j))