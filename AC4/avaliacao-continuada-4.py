"""
Programação Estruturada
2024.1
05/03/2024
Yago Duarte de Andrade

Avaliação Continuada 4

"""

def ler_nome_usuario():
    nome = input("Informe o seu nome: ")
    if not nome:
        print("Nome inválido!")
    return nome

def ler_notas():
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    ac = float(input("Informe a nota da AC: "))
    asub = float(input("Informe a nota da ASUB: "))
    return ap1, ap2, ac, asub

def validar_notas(ap1, ap2, ac, asub):
    if ap1 < 0 or ap1 > 10:
        return False
    elif ap2 < 0 or ap2 > 10:
        return False
    elif ac < 0 or ac > 10:
        return False
    elif asub < 0 or asub > 10:
        return False
    return ap1, ap2, ac, asub


def duas_maiores_notas(ap1, ap2, asub):
    if asub > ap1:
        return asub, ap2
    if asub > ap2:
        return ap1, asub
    return ap1, ap2

def calcular_media(n1, n2, ac):
    return (n1 + n2) * 0.4 + ac * 0.2


def informar_aprovacao(media):
    print("Sua média foi", round(media, 2))
    if media >=7:
        print("Parabéns você foi aprovado!")
    else:
        print("Você foi reprovado!")


def main():
    nome = ler_nome_usuario()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

main()