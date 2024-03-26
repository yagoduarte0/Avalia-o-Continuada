quantia = input()
quantia = quantia.split(" ")

a = int(quantia[0])
b = int(quantia[1])
c = int(quantia[2])

relacao_ab = ((a + b + abs (a - b)) / 2)
relacao_bc = ((b + c + abs (b - c)) / 2)
relacao_ac = ((a + c + abs (a - c)) / 2)

if relacao_ab == relacao_ac:
    print(a, "eh o maior")
elif relacao_ab == relacao_bc:
    print(b, "eh o maior")
elif relacao_ac == relacao_bc:
    print(c, "eh o maior")