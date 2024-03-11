"""
Programacao Estruturada
2024.1
11/04/2024
Yago Duarte de Andrade

AC2 - desenvolva uma funcao que calcule o salario liquido de um funcionario com a reducao do imposto de renda
"""

def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario = (valor_hora * num_horas) - valor_hora * num_horas * irpf
    return salario

def main():
    print('O salario liquido do funcionario e de R$', calcula_salario(100, 100, 0.275))

main()
