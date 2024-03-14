"""
Programacao Estruturada
2024.1
11/03/2024
Yago Duarte de Andrade

AC2 (Exerc: 1) - receber tres valores inteiros e dizer se pode e o tipo de triangulo formado
AC2 (Exerc: 2) - receber um numero e dizer o dia da semana referente a ele
AC3 (Exerc: 3) - criar uma calculadora simples
"""

def determina_tipo_triangulo(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        return "Não é um triângulo!"
    elif (a == b == c):
        return "Equilátero"
    elif (a != b != c != a):
        return "Escaleno"
    else:
        return "Isóceles"

def dia_semana(num):
    if num == 1:
        return "Domingo"
    elif num == 2:
        return "Segunda-Feira"
    elif num == 3:
        return "Terça-Feira"
    elif num == 4:
        return "Quarta-Feira"
    elif num == 5:
        return "Quinta-Feira"
    elif num == 6:
        return "Sexta-Feira"
    elif num == 7:
        return "Sábado"
    else:
        return "String vazia!"
    
def calculadora_simples():
    n1 = float(input("Informe um número: "))
    n2 = float(input("Informe outro número: "))
    operacao = str(input("Informe a operação: "))
    if operacao == "soma":
        print(n1 + n2)
    elif operacao == "subtracao":
        print(n1 - n2)
    elif operacao == "multiplicação":
        print(n1 * n2)
    elif operacao == "divisão":
        print(n1 / n2)
    else:
        print("Operação inválida!")

def main():
    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5))
    print(determina_tipo_triangulo(1, 1, 4))
    
    print(dia_semana(2))
    print(dia_semana(6))
    print(dia_semana(7))
    print(dia_semana(9))

    calculadora_simples()

main()
