
'''
def auto1():
# ADPND
# an y bn Q=[ 'q0',' q1',' q2',' q3']
    sigma= [ 'a',' b',' e']
    Ap= [ 'A',' B',' ']
    s= ' q0'
    z= ' A'
    F= [ 'q3']
    pila= [ ]


    def insertar(gamma,p ila):
        for s in gamma[::-1]:
        pila.insert(0,s )
        return pila


    Ejemplos_L= [ '',' ab',' aabb',' aaabbb',' aaaabbbb',' a',' b',' bbaa',' baba',' aab']
    estado = s

    for w in Ejemplos_L:
        pila= [ z]
        estado = s
        pos= w .find("b")
        bs= w [pos: ]
        ca= w [:pos]

    p= 'w' + ' e'
        for x in p:
            if estado= =s :
                if x= =s igma[0]:
                    pila.pop(0)
                    insertar('BA',p ila)
                    estado= Q [1]
                if x= =s igma[2] and pila[0]= =z :
                    pila.pop(0)
                    estado= Q [3]
                if x= =s igma[1]:
                break;

            elif estado= =Q [1]:
                if x= =s igma[0] and pila[0]= =A p[1]:
                    pila.pop(0)
                    insertar('BB',p ila)

                if x= =s igma[1] and pila[0]= =A p[1]:
                    pila.pop(0)
                    estado= Q [2]

            elif estado= =Q [2]:
                if x= =s igma[0]:
                break;
                if x= =s igma[1] and pila[0]= =A p[1]:
                    pila.pop(0)

                if  x = =sigma[2] and pila[0 ]= =Ap[0]:
                    pila.pop(0)
                    pila.insert(0 ,'A')
                    estad o =Q[3]
        if estado in F:
            if len(bs )! =len(ca):
                print(w, "No aceptada")
            else:
                print(w, " es aceptada")
        else:
            print(w ,"No aceptada")

'''


# Programa de ejemplo para insertar y quitar letras del alfabeto de pila y de gamma
def ejemplo():
    pila = []
    pila.insert(0, 'Z')
    gamma = 'ABCD'
    for s in gamma[::-1]:
        pila.insert(0, s)
    print(pila)
    pila.pop(0)
    pila.pop(0)
    print(pila)


ejemplo()


def autom2():
    Q = ['q1', 'q2']
    Sigma = ['a', 'b']
    s = 'q1'
    F = ['q2']
    z = 'Z'
    gamma = ['A', 'B', 'Z']

    delta = {('q1', 'a', 'Z'): ['q1', 'AZ'],
             ('q1', 'b', 'Z'): ['q1', 'BZ'],
             ('q1', 'a', 'A'): ['q1', 'AA'],
             ('q1', 'b', 'B'): ['q1', 'BB'],
             ('q1', 'a', 'B'): ['q1', ''],
             ('q1', 'b', 'A'): ['q1', ''],
             ('q1', '', 'Z'): ['q2', 'Z'],
             ('q2', '', 'Z'): ['q2', 'Z']}

    L = ['', 'ab', 'ba', 'abba', 'bbaa', 'baba', 'abab']

    print("\n---------------ADPND MISMO NUMERO DE A'S QUE DE B'S-----------------------\n")

    # funcion
    def transicion(estado, sigma, gamus):
        print("estado = ", estado, "sigma = ", sigma, "gamma = ", gamus)
        estado_siguiente = delta[(estado, sigma, gamus)]
        print("estado_siguiente = ", estado_siguiente, "sigma = ", sigma, "gamma =", gamus)
        return estado_siguiente

    for w in L:
        estado = s
        for sigma in w:
            estado = transicion(estado, sigma, gamus)

        if estado in F:
            print(w, "es aceptada")
        else:
            print(w, "no es aceptada")


autom2()

