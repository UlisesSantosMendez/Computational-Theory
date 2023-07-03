print("Programa que reconoce a^(n+3)b^n")
tokens = ('a', 'b');
t_a = r'a';
t_b = r'b';

# Definimos la funcion de error por si hay algun caracter no valido dentro del lenguaje
def t_error(t):
    print("Caracter ilegal ", t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

# funcion encargada de las producciones de la forma de Backus Naur
def p_S(p):
    ''' S : a a a
          | a a a a b
          | a a a a X b b T'''
    pass

# funcion que permita la produccion de epsilon
def p_empty(p):
    'empty :'
    pass

# definimos la produccion de X
def p_X(p):
    ''' X : a X
          | empty'''
    pass

# definimos la produccion de T
def p_T(p):
    ''' T : b T
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