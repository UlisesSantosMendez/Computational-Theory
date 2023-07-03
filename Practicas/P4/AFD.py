# AFD Ejemplo clase
def ejemplo():
    Q = ['q0', 'q1']
    Sigma = ['a', 'b']
    s = 'q0'
    F = ['q0']

    delta = {('q0', 'a'): 'q0',
             ('q0', 'b'): 'q1',
             ('q1', 'a'): 'q1',
             ('q1', 'b'): 'q0'}

    Ejemplos_L = ['', 'bb', 'abb', 'aaa']
    Ejemplos_Lc = ['b', 'aba', 'ba', 'bbb']

    print("\n---------------AFD de ejemplo-----------------------\n")

    # funcion
    def transicion(estado, sigma):
        print("estado = ", estado, "sigma = ", sigma)
        estado_siguiente = delta[(estado, sigma)]
        print("estado_siguiente = ", estado_siguiente, "sigma = ", sigma)
        return estado_siguiente

    # cad
    for w in Ejemplos_L:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")

    for w in Ejemplos_Lc:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")


ejemplo()


def autdos():
    # L(M)= Cadena que tengan a*b*
    # conjunto de estados con conjunto de caracteres
    Q = ['q0', 'q1', 'q2']
    sigma = ['a', 'b']
    # estado inicial
    s = 'q0'
    # Estado de aceptacion
    F = ['q0', 'q1', ]
    # delta como diccionario donde las llaves sean duplas
    delta = {('q0', 'a'): 'q0',
             ('q0', 'b'): 'q1',
             ('q1', 'b'): 'q1',
             ('q1', 'a'): 'q2',
             ('q2', 'b'): 'q2',
             ('q2', 'a'): 'q2'}

    Ejemplos_L = ['', 'a', 'b', 'aa', 'bb', 'aabb', ]
    Ejemplos_Lc = ['ba', 'aba', 'baa', 'ababa']

    print("\n-----------------AFD {a^n b^m}--------------------------\n\n")

    # funcion
    def transicion(estado, sigma):
        print("estado = ", estado, "sigma = ", sigma)
        estado_siguiente = delta[(estado, sigma)]
        print("estado_siguiente = ", estado_siguiente, "sigma = ", sigma)
        return estado_siguiente

    for w in Ejemplos_L:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")

    for w in Ejemplos_Lc:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")


autdos()


def autparimpar():
    # L(M)= Cadena que tengan un numero impar de a's y un numero par de b's
    # conjunto de estados con conjunto de caracteres
    Q = ['q0', 'q1', 'q2', 'q3']
    sigma = ['a', 'b']
    # estado inicial
    s = 'q0'
    # Estado de aceptacion
    F = ['q1']
    # delta como diccionario donde las llaves sean duplas
    delta = {('q0', 'a'): 'q1',
             ('q0', 'b'): 'q3',
             ('q1', 'a'): 'q0',
             ('q1', 'b'): 'q2',
             ('q2', 'a'): 'q3',
             ('q2', 'b'): 'q1',
             ('q3', 'a'): 'q2',
             ('q3', 'b'): 'q0'}

    Ejemplos_L = ['a', 'aaa', 'abbaa', 'aabbbba']
    Ejemplos_Lc = ['','b', 'aabbbaa', 'bbbaa', 'abbba']

    print("\n-----------------AFD {a impar y b par}--------------------------\n\n")

    # funcion
    def transicion(estado, sigma):
        print("estado = ", estado, "sigma = ", sigma)
        estado_siguiente = delta[(estado, sigma)]
        print("estado_siguiente = ", estado_siguiente, "sigma = ", sigma)
        return estado_siguiente

    for w in Ejemplos_L:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")

    for w in Ejemplos_Lc:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")


autparimpar()

def terminacon():
    # L(M)= Cadenas que terminan ya sea con la subcadena ab o con la subcadena aa
    # conjunto de estados con conjunto de caracteres
    Q = ['q0', 'q1', 'q2', 'q3', 'q4']
    sigma = ['a', 'b']
    # estado inicial
    s = 'q0'
    # Estado de aceptacion
    F = ['q0', 'q1']
    # delta como diccionario donde las llaves sean duplas
    delta = {('q0', 'a'): 'q0',
             ('q0', 'b'): 'q1',
             ('q1', 'a'): 'q2',
             ('q1', 'b'): 'q4',
             ('q2', 'a'): 'q1',
             ('q2', 'b'): 'q3',
             ('q3', 'a'): 'q3',
             ('q3', 'b'): 'q3',
             ('q4', 'a'): 'q0',
             ('q4', 'b'): 'q4'}

    Ejemplos_L = ['ab', 'aa', 'abbab', 'abaa', 'abaabbbab']
    Ejemplos_Lc = ['', 'ba', 'aaba', 'ababa', 'aababa']

    print("\n-----------------AFD {terminan con ab y aa}--------------------------\n\n")

    # funcion
    def transicion(estado, sigma):
        print("estado = ", estado, "sigma = ", sigma)
        estado_siguiente = delta[(estado, sigma)]
        print("estado_siguiente = ", estado_siguiente, "sigma = ", sigma)
        return estado_siguiente

    for w in Ejemplos_L:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")

    for w in Ejemplos_Lc:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")


terminacon()