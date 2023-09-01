l1 = []
l2 = []
l3 = []
n = 5 

for i in range(n):
    l1.append(int(input("Insira um numero na primeira lista: ")))
    l2.append(int(input("Insira um numero na segunda lista: ")))
print(l1, l2)

for i in range(n):
    l3.append(l1[i])
    l3.append(l2[i])

print(l3)
