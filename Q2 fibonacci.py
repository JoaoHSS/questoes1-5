
def fibonacci(alvo):
    if alvo == 1: 
        return True
    a, b = 1, 0
    while b < alvo:
        c = b
        b = a
        a = a + c
        if b == alvo: return True
    return False


while True:
    a = input(" Digite um númeoro para eu conferir se está no fibonacci:")
    try: 
        a = int(a)
        break
    except: print(" Digite um número válido")


resultado = fibonacci(a)

if resultado:
    print(f"o número {a} pertence a sequência fibonacci")
else:
    print(f"o número {a} NÃO pertence a sequência fibonacci")