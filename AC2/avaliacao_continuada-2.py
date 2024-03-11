"""
Programacao Estruturada
2024.1
11/04/2024
Yago Duarte de Andrade

AC2 - desenvolva uma funcao que calcule o salario liquido de um funcionario com a reducao do imposto de renda
"""
def eq_seg_grau(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**(0.5)) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**(0.5)) / (2*a)
    print("O valor da primeira raiz e igual a: ", x1)
    print("O valor da segunda raiz e igual a: ", x2)

def bissexto(ano):
    print(ano %4 == 0 and not ano %100 == 0 or ano %400 == 0)
    
def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario = (valor_hora * num_horas) - valor_hora * num_horas * irpf
    return salario

def main():
    print('O salario liquido do funcionario e de R$', calcula_salario(100, 100, 0.275))
    eq_seg_grau(1, -6, 8)
    bissexto(2012)

main()
