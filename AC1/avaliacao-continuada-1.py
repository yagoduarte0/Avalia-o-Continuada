"""
Programacao Estruturada
2024.1
04/03/2024
Yago Duarte

AC (Exerc: 1) Resolver uma equacao do segundo grau
AC (Exerc: 2)Identificar se um ano e bissexto ou nao

"""

def avaliacao_continuada_1():
    a = int(input("Informe o coeficiente a: "))
    b = int(input("Informe o coeficiente b: "))
    c = int(input("Informe o coeficiente c: "))

    # x = (-b +- raiz de delta / 2a)
    x1 = (-b + (b**2 - 4*a*c)**(0.5)) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**(0.5)) / (2*a)
    print("O valor da primeira raiz e igual a: ", x1)
    print("O valor da segunda raiz e igual a: ", x2)


def avaliacao_continuada_2():
    ano = int(input("Informe o ano: "))
    print(ano %4 == 0 and not ano %100 == 0 or ano %400 == 0)

def main():
    avaliacao_continuada_1()
    avaliacao_continuada_2()

main()