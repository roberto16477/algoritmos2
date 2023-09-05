notas = [0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input(f"Informe a nota {x} : "))
    soma = soma + notas[x]
    x = x+1

x = 0

while x < 5:
    print(f"nota {x} : {notas[x]:6.2f}")
    x+=1
print(f"media: {soma/ x:5.2f}")

print(type(notas))
