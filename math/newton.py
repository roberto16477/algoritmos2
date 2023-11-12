#import time

def calcular_raiz_quadrada(numero, precisao=1e-6):
    if numero < 0:
        return None  # Lidando com números negativos (raiz quadrada não real)

    aproximacao = numero  # Comece com uma estimativa inicial
    while abs(aproximacao * aproximacao - numero) > precisao:   # o abs impede a duplicação dos números positivos e negativos
        aproximacao = 0.5 * (aproximacao + numero / aproximacao)

    return aproximacao


num = float(input("Insira um número para calcular a raiz quadrada: "))
elevado = num**12
raiz_quadrada = calcular_raiz_quadrada(elevado)
print(f"A raiz quadrada de {elevado} é aproximadamente {raiz_quadrada:.6f}")

