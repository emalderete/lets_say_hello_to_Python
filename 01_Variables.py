# Empezamos declarando una variable
# ATENCIÓN: Dato de color, no menor:
# Las variables no deben declararse en camelcase, deben escribirse en snakecase y en minúscula (my_variable, name_person, friendly_dog, etc.)

my_variable = 'Esta es mi primera variable'
print(my_variable)

first_int = 5
print(first_int)

first_float = 1.5
print(first_float)

# Probemos a modificar el valor de una variable previamente declarada.
mutable_variable = 'Una variable que cambiará su valor'
print(mutable_variable)
mutable_variable = 'Ahora vale otra cosa'
print(mutable_variable)

# Intentemos algo nuevo, vamos a declarar un objeto

person_info = {
    'firstname' : 'Nicolas',
    'lastname' : 'Alderete',
    'country' : 'Argentina',
    'city' : 'Las Talitas',
    'age' : 26,
    'tall' : 1.72,
    'married' : False
}
print(person_info) #esto imprime por consola el objeto creado

# Pero que pasaría si quisiera imprimir solo un valor de todo el objeto?

# print(person_info.firstname)

# La línea anterior quedará comentada dado que el programa no compila con esa sintaxis

print(person_info['firstname'])

# Esta es la forma correcta de llamar un dato específico dentro de un objeto.

# Ahora que tenemos las variables necesarias vamos a crear un texto completo por consola
# Recordar que con la función "print" se pueden pasar varios valores separados por comas para que haca la concatenación

print('Hello world! My name is', person_info['firstname'], person_info['lastname'], '.', 'I have', person_info['age'], 'years old and I came from the city of', person_info['city'], 'on Tucumán,', person_info['country'])

# Ahora bien, veamos como transformar un valor en otro tipo de valor, es decir, un número entero en un string, por ejemplo.

int_to_string_variable = str(first_float)
print(int_to_string_variable)
print(type(int_to_string_variable))

# Ahora solo por diversión, que tal si probamos usar la función type en todo el print

print(type(print('Hello world! My name is', person_info['firstname'], person_info['lastname'], '.', 'I have', person_info['age'], 'years old and I came from the city of', person_info['city'], 'on Tucumán,', person_info['country'])))

# Como vimos nos da como resultado <class 'NoneType>

# Esto se debe a que el type está tratando de determinar que tipo de dato es "print" efectivamente, sin embargo print es una función
# propia del sistema de Python, por lo tanto no tiene algún valor propio

# Vamos a probar una función nueva, veamos que hace "len()"

print(len(person_info['firstname']))

# La función len() nos permite contar cuantas letras tiene un string
# NOTA: Esta función solo es capaz de recibir un solo valor, no puede contar los caracteres de una cadena de múltiples valores
# para ello tendríamos que almacenar la cadena en una variable que podamos pasarle como valor a len()

# my_string_chain = str('Hello world! My name is', person_info['firstname'], person_info['lastname'], '.', 'I have', person_info['age'], 'years old and I came from the city of', person_info['city'], 'on Tucumán,', person_info['country'])
# Con esta variable notamos que la función "str()" puede recibir como múcho 3 valores, sin embargo la concatenación que hicimos tiene 10
# por lo tanto para poder hacer un string a partir de un valor tan numeroso, habría que hacer una construcción de strings mediante dicha función
# y haciendo uso de múltiples variables.

# build_string_step_one = str('Hello world! My name is', 'other string', 'another one string')
# build_string_step_two = str('I have', person_info['age'], 'years old and I came from the city of')
# build_string_step_three = str(person_info['city'], 'on Tucumán,', person_info['country'])

# my_string_chain = str(build_string_step_one, build_string_step_two, build_string_step_three)

# print(my_string_chain)

# Bueno, eso no ha funcionado como esperábamos. Sigamos adelante

# Vamos a aprender que son las variables en una sola línea

name, surname, alias, age = 'Emanuel', 'Alderete', 'Nemeck', 26
print('Hola, yo soy', alias, 'tengo', age, 'años y mi verdadero nombre es', name, surname)

# Se puede hacer de esta manera sin embargo no es muy buena práctica. Usarlo con mucho cuidado
# La idea es poder declarar múltiples variables con cada valor respectivo según la posición en la que se asignan para que optimice el espacio del código

# En esta parte veremos un método input() que lo que hace es parar la ejecución y esperar a la entrada de algún dato por consola
# La sintaxis es la siguiente
first_name = input('What is your name: ')
another_age = input('How old are you? ')

print(first_name)
print(another_age)