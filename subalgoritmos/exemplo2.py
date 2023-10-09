def e_impar(x):
    return x % 2 == 1

def par_ou_impar(x):
    if e_impar(x):
        return "Impar"
    else:
        return "Par"

print(par_ou_impar(4))
print(par_ou_impar(5))