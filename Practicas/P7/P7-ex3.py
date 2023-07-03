print("Programa que reconoce {a^i b^j c^k | i =j o j = k}")
tokens = ('a', 'b', 'c');
t_a = r'a';
t_b = r'b';
t_c = r'c';

# Definimos la funcion de error por si hay algun caracter no valido dentro del lenguaje
def t_error(t):
    print("Caracter ilegal ", t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

# funcion encargada de las producciones de la forma de Backus Naur
def p_S(p):
    ''' S : X
          | Y'''
    pass

# funcion que permita la produccion de epsilon
def p_empty(p):
    'empty :'
    pass

# definimos la produccion de X
def p_X(p):
    ''' X : Z T'''
    pass

# definimos la produccion de T
def p_Z(p):
    ''' Z : a Z b
          | empty'''
    pass

def p_T(p):
    ''' T : c T
          | empty'''
    pass

def p_Y(p):
    ''' Y : F W'''
    pass

def p_W(p):
    ''' W : b W c
          | empty'''
    pass

def p_F(p):
    ''' F : a F
          | empty'''
    pass

s = '';

# Funcion para la impresion de errores
def p_error(p):
    global s
    if p:
        print("Error de sintaxis en ", p.value)
    else:
        print("Error de sintaxis en EOF")

    print(s, "no está en el lenguaje")

import ply.yacc as yacc
yacc.yacc()
while 1:
    try:
        s = input('> ')
    except EOFError:
        break
    t = yacc.parse(s)