a = [1, 2, 3, 4]
b = set(a)      # um conjunto pode ser criado a partir de qualquer estrutura que tenha índice
c = set([1, 2, 6, 28]) # c = {1, 2, 6, 28}
d = set([2, 3, 6, 12]) # d = {2, 3, 6, 12}

#print(type(a))
#print(type(b))
#print(b)

print(c - d) #exibe os valores de c que não existem em d (diferença)
print(c | d) #exibe todos os valores contidos em c e d   (união)
print(c & d) #exibe os valores comuns entre c e d        (intersecção)
