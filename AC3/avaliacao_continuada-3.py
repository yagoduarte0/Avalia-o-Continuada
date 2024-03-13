"""
Programacao Estruturada
2024.1
18/03/2024
Yago Duarte de Andrade

AC2 (Exerc: 1) - 
AC2 (Exerc: 2) - 
"""

def determina_tipo_triangulo():
    a = float(input("Informe o primeiro lado: "))
    b = float(input("Informe o segundo lado: "))
    c = float(input("Informe o terceiro lado: "))
    if (a + b < c) or (a + c < b) or (b + c < a):
        print("Não é um triangulo!")
    elif (a == b == c):
        print("Equilátero")
    elif (a != b != c != a):
        print("Escaleno")
    else:
        print("Isóceles")

determina_tipo_triangulo()
