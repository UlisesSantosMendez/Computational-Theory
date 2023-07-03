from io import open
import re
print("EXPRESIONES REGULARES")
archivo_texto = open("rfcip.txt", "r")
texto = archivo_texto.readlines()
archivo_texto.close()
print(texto)

regulares1 = re.search(r".*[0-9].*", texto[0])
print(regulares1)
regulares2 = re.search(r".*\D.*", texto[1])
print(regulares2)
