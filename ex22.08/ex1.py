v = [2, 6, 8, 3, 10, 9, 1, 21, 33, 14]
x = 2
y = 4

print("Somados: ")
print(v[x+1])
print(v[x+2])
print(v[x+3])

print("Multiplicados: ")

print(v[x*4])
print(v[x*1])
print(v[x*2])
print(v[x*3])

print("Mais elaborados:")
print(v[v[x+y]]) # está pegando a posição 1 do vetor pois o valor na posição 6 é 1