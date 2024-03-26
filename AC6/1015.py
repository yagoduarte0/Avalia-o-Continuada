x = input()
y = input()

x = x.split(" ")
y = y.split(" ")

x1 = float(x[0])
x2 = float(x[1])

y1 = float(y[0])
y2 = float(y[2])

distancia = ((x2 - x1)**2 + (y2 - y1)**2)
distancia = distancia**0.5

print("%.4f" %distancia)