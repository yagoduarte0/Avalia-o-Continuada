peca1 = input() .split()
codigo1 = int(peca1[0])
numero1 = int(peca1[1])
valor1 = float(peca1[2])
total1 = numero1 * valor1

peca2 = input() .split()
codigo2 = int(peca2[0])
numero2 = int(peca2[1])
valor2 = float(peca2[2])
total2 = numero2 * valor2

total3 = round((total1 + total2),2)

print("O VALOR A PAGAR: R$", total3)