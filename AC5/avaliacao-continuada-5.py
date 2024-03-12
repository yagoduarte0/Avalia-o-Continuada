"""
Programação Estruturada
2024.1
05/03/2024
Yago Duarte de Andrade

Avaliação Continuada 5

"""

import random

def main():
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)

    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    r = 1

    print("Aventureiro -", "Vida:" ,vida_aventureiro, "Ataque:", ataque_aventureiro, "Defesa:", defesa_aventureiro)
    print("Monstro -", "Vida:", vida_monstro, "Ataque:", ataque_monstro)

    while vida_aventureiro > 0 or vida_monstro > 0:
        print("Rodada ", r)
        vida_monstro -= random.randint(1, ataque_aventureiro)
        if vida_monstro <= 0:
            print("O monstro morreu!")
            break
        dano = random.randint(1, ataque_monstro) - defesa_aventureiro
        if dano > 0:
            vida_aventureiro -= dano

        if vida_aventureiro <= 0:
            print("O aventureiro morreu!")
            break

        print("Aventureiro -", "Vida:" ,vida_aventureiro, "Ataque:", ataque_aventureiro, "Defesa:", defesa_aventureiro)
        print("Monstro -", "Vida:", vida_monstro, "Ataque:", ataque_monstro)
        r += 1




main()
