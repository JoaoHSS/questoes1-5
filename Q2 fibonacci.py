#   solução usando loop
def fibonacci(alvo):
    a, b = 1, 0
    while b < alvo:
        c = b
        b = a
        a = a + c
        if b == alvo: return True
    return False

#   solução usando recursividade
def firstCheck(number):
    if number < 4: return True
    return isFib(number)

def isFib(number, a=1, b=1):
    next = a + b
    if next > number:   return False
    elif number == next: return True
    return isFib(number, b, next)

while True:
    a = input(" Digite um número para conferir se está na sequência fibonacci:\n")
    try: 
        a = int(a)
        break
    except: print(" Digite um número válido")

resultado = fibonacci(a)
#resultado = firstCheck(a)

if resultado:
    print(f"o número {a} pertence a sequência fibonacci")
else:
    print(f"o número {a} NÃO pertence a sequência fibonacci")
