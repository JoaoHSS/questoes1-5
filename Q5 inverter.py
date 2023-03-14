
string = "123456789"

def f(s):
    #return s[::-1]
    new_s = ""

    for n in range(1, len(s)+1):
        new_s += s[-n]

    return new_s

print(f(string))