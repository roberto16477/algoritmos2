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
print(v[x+y])    # item na posição 6
print(v[8-v[2]]) # ele encontra o v2 e subtrai do valor 8
# print(v[v[4]]) # da erro pois o indice de posição 4 tem o valor 10, e não existe indice 10 para buscar depois
print(v[ v[ v[0]]]) # o exercicio pediu indice 7 pra dar erro como no anterior
# print(v[v[1]*v[4]]) #erro de estouro também
print(v[x+4])
