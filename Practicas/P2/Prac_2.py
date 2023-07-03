import re
from collections import Counter
cadena = input("Ingrese su cadena: ")
patron = "0123456789"
fuera = 'aeiouAEIOU'
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
# Programa 1


def longitud():
    print("La longitud de tu cadena es: ", len(cadena))


longitud()


# Programa 2
def numcar():
    print(Counter(cadena))


numcar()


# Programa 3
def newcad():
    nueva = cadena[:2]+cadena[-2:]
    if len(cadena) < 2:
        print("{}")
    else:
        print(nueva)


newcad()


# Programa 4
def cambcar():
    cambio = cadena[0]+cadena[1:].replace(cadena[0], '$')
    print(cambio)


cambcar()


# Programa 5
def camcad():
    ocadena = input("Ingresa otra cadena: ")
    cambio1 = cadena.replace(cadena[:2], ocadena[:2])
    cambio2 = ocadena.replace(ocadena[:2], cadena[:2])
    print(cambio1, " ", cambio2)


camcad()


# Programa 6
def mostlarge(lis):
    print(lis)
    mas_larga = max([len(c) for c in lis])
    return mas_larga


print("La longitud mas larga de la lista es: ", mostlarge(lista))


# Programa 7
def quitarcar():
    quitar = int(input("Ingrese la posicion que desee quitar: "))
    elim = cadena.replace(cadena[quitar], ' ')
    print(elim)


quitarcar()


# Programa 8
def cambio_car(text):
    return text[-1] + text[1:-1] + text[0]


print(cambio_car(cadena))


# Programa 9
def impar(cad):
    txt = ''
    for i in range(len(cad)):
        if i % 2 == 0:
            txt += cad[i]
    return txt


print(impar(cadena))


# Programa 10
def word():
    palabra = cadena.split(' ')
    frecuencia = [palabra.count(p) for p in palabra]
    print(str(list(zip(palabra, frecuencia))))


word()


# Programa 11
def maymin():
    mayus = cadena.upper()
    minus = cadena.lower()
    print("Tu cadena en mayusculas es: ", mayus)
    print("Tu cadena en minusculas es: ", minus)


maymin()


# Programa 12
def alfnum():
    entrada = input("Ingresa palabras separadas por ,:")
    paso1 = entrada.split(',')
    print(paso1)


alfnum()


# Programa 13
def fourcopies():
    tam = len(cadena)
    last = cadena[tam-2:]
    for c in range(4):
        print(last, end='')


fourcopies()


# Programa 14
def firsttres():
    tam = len(cadena)
    if tam <= 3:
        print("\n", cadena)
    else:
        print("\n", cadena[:3])


firsttres()


# Programa 15
def mitad():
    tam = len(cadena)
    if tam % 2 == 0:
        print(cadena[:tam//2])
    else:
        print("La cadena es impar")
        print(cadena)


mitad()


# Programa 16
def inversa():
    print("Mi numero de boleta es : 2020630460")
    tama = len(cadena)
    sumita = 4 + 6 + 0
    if tama == tama * sumita:
        print(cadena[::-1])
    else:
        print("No es multiplo de la suma de los ultimos tres digitos de la boleta ")
        print(cadena)


inversa()


# Programa 17
def mayusc():
    if len(cadena) > 4:
        conta = 0
        for i in range(4):
            if cadena[i] == cadena[i].upper():
                conta += 1
        if conta >= 2:
            print(cadena.upper())
        else:
            print(cadena)
    else:
        return cadena


mayusc()


# Programa 18
def lexico():
    print(''.join(sorted(cadena, key=str.upper)))


lexico()


# Programa 19
def especifico():
    status = 0
    print("La cadena es: ", cadena)
    while status != 1:
        print("¿Con que caracter comienza la cadena?")
        caracter = input()
        if caracter == cadena[0]:
            print("Afirmativo, la cadena comienza con \'", caracter, "\'")
            status = 1
            print("Programa finalizado. . .")
        else:
            print("La cadena no empieza con \'", caracter, "\'\nVuelva a intentar.")
            status = 0
            print("volviendo al principio. . .\n\n")


especifico()


# Programa 21
def multil():
    cadena_multilinea = '''uno
    dos
    tres
    cuatro
    '''
    print('La cadena multilinea original es:\n', cadena_multilinea)
    prefijo = 'HOLA'
    print('El prefijo es: ', prefijo)
    renglones = cadena_multilinea.split()
    print()
    for n in range(len(renglones)):
        renglones[n] = prefijo + renglones[n]
    print('La cadena multilinea con el prefijo al principio de cada linea es: ')
    cadena_multilinea_con_prefijo = ('\n'.join(renglones))
    print(cadena_multilinea_con_prefijo)


multil()


# Programa 22
def flotantes():
    decimal = 87.329765
    print("El flotante es: ", decimal, "\nEl flotante limitado es: %.2f" % decimal)


flotantes()


# Programa 23
def sign():
    decimal = 2.718281
    decimal2 = - 5581.199513
    print("Tu flotante es: ", decimal)
    print('Tu flotante con signo es: {:+.2f}'.format(decimal))
    print("Tu flotante es: ", decimal2)
    print('Tu flotante con signo es: {:+.2f}'.format(decimal2))


sign()


# Programa 24
def nodec():
    decimal = 7.382985
    print("Tu flotante es: ", decimal)
    print("Tu flotante limitado es %.0f" % decimal)


nodec()


# Programa 25
def cerosnum():
    ceros = ' '
    nums = '302939'
    ancho = int(input("Ingresa el ancho de ceros a agregar: "))
    for i in range(ancho):
        ceros += '0'
    final = ceros + nums
    print(final)


cerosnum()


# Programa 26
def estrellas():
    var = ' '
    num = input("Ingresa algunos numeros: ")
    ancho = int(input("Ingresa un ancho especificado: "))
    for c in range(ancho):
        var += '*'
    print(num + var)


estrellas()


# Programa 27
def comas():
    num = int(input("Ingrese un numero: "))
    print('{:,}'.format(num))


comas()


# Programa 28
def porcentaje():
    num = float(input("Ingrese un numero: "))
    if num < 1:
        numper = 'El porcentaje de {} es: {:.2%}'.format(num, num)
        print(numper)
    else:
        print(num, "%")


porcentaje()


# Programa 29
def align():
    num = input("Ingresa un numero: ")
    print("Original: ", num)
    print("Izq:", format(num, '<10'))
    print("Der:", format(num, '>10'))
    print("Cen:", format(num, '^10'))


align()


# Programa 30
def rgb():
    rojo = int(input("Ingrese el color rojo (0,256): "))
    verde = int(input("Ingrese el color verde (0,256): "))
    azul = int(input("Ingrese el color azul (0,256): "))
    if (0 <= rojo < 256) and (0 <= verde < 256) and (0 <= azul < 256):
        rgb1 = [rojo, verde, azul]
        rgb_cad = f'#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}'
        print("Tu valor hexadecimal es: ", rgb_cad)
    else:
        print("No se encuentra en el rango pedido")


rgb()


# Programa 31
def ocurr():
    subcadena = "ata"
    ocurrencias = cadena.count(subcadena)
    print("Cadena original: \'", cadena, "\'")
    print("Subcadena a buscar: \'", subcadena, "\'")
    print("El número de ocurrencias de la subcadena en la cadena es: ", ocurrencias)


ocurr()


# Programa 32
def invcad():
    print(cadena[::-1])


invcad()


# Programa 33
def supr():
    nueva = ''.join([c for c in cadena if c not in fuera])
    print(nueva)


supr()


# Programa 34
def repetidos():
    contar = Counter(cadena)
    duplicados = [t[1] for t in list(contar.items()) if t[1] > 1]

    print(duplicados)


repetidos()


# Programa 35
def caractual():
    n = 0
    while n != len(cadena):
        print("Carácter actual: ", cadena[n], " posición ", n)
        n = n + 1


caractual()


# Programa 36
def coinalfab():
    valor = 0
    for p in alfabeto:
        if re.search(p, cadena):
            valor = 1
        else:
            valor = 0
    if valor == 1:
        print("Contiene todas las letras del alfabeto")
    else:
        print("No contiene todas las letras del alfabeto")


coinalfab()


# Programa 37
def cadtolis():
    print("Cadena original: ", cadena)
    renglones = cadena.split()
    print("\nImpresión de la lista:", renglones)


cadtolis()


# Programa 38
def minusculas():
    n = int(input("Ingresa a n: "))
    res = cadena[:n].lower() + cadena[n:]
    print("Cadena original: ", cadena)
    print("Cadena con n minúsculas: ", res)


minusculas()


# Programa 39
def campyc():
    punto = ".,"
    coma = ",."
    cambio = cadena.maketrans(punto, coma)
    print(cadena.translate(cambio))


campyc()


# Programa 40
def convocales():
    res = set([c for c in cadena if c in fuera])
    print(res)
    print(len(res))


convocales()


# Programa 41
def ultimate():
    regreso = cadena.rsplit('n', maxsplit=1)
    print(regreso)


ultimate()


# Programa 42
def antescar():
    print(cadena.rsplit("e", 1))


antescar()


# Programa 43
def fijos():
    for n in range(len(cadena) + 1):
        print("\nSubcadena ", n + 1, "=", cadena[:n], end=" ")
        if cadena[:n] != cadena:
            print("Prefijo propio")
        else:
            print("Prefijo")
    for i in range(len(cadena), -1, -1):
        print("\nSubcadena ", -i + (len(cadena) + 1), "=", cadena[i:], end=" ")
        if cadena[i:] != cadena:
            print("Sufijo propio")
        else:
            print("Sufijo")


fijos()
