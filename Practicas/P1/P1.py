cadena = input("Ingrese una cadena: ")

for n in range(len(cadena)+1):
    print("\nSubcadena ", n+1, "=", cadena[:n], end=" ")
    if cadena[:n] != cadena:
        print("Prefijo propio")
    else:
        print("Prefijo")
for i in range(len(cadena), -1, -1):
    print("\nSubcadena ", -i+(len(cadena)+1), "=", cadena[i:], end=" ")
    if cadena[i:] != cadena:
        print("Sufijo propio")
    else:
        print("Sufijo")