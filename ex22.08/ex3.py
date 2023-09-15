r = []
s = []
x = []
nr = 5
ns = 10
nx = 0

for i in range(nr):
    r.append(int(input("Informe um valor para o primeiro vetor: ")))

for i in range(ns):
    s.append(int(input("Informe um valor para o SEGUNDO VETOR: ")))

for i in range(nr):
    nx = r[i]
    for j in range(ns):
        if s[j] == nx:
            x.append(nx)

print("Vetor R: ", r)
print("Vetor S: ", s)
print("Valores comuns de R e S: ", x)
