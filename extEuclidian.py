#numbersString = input('Digite os dois números a ser encontrado o inverso modular: ').split()
#num1, num2 = int(numbersString[0]), int(numbersString[1])


def extEuclidian(x, y):

    s = ti = 1
    si = t = quo = 0

    while y != 0:
        quo = x // y
        x, y = y, x % y

        s, si = si, s - quo * si
        t, ti = ti, t - quo * ti
        #x = mod
    return s

def decodificar(message, p, q, e):
    n = (p-1) * (q-1)
    d = extEuclidian(e, n)
    while d < 0:
        d += n
    
    return pow(message, d) % (p*q)

messageString = int(input('Digite sua mensagem: '))
constantsString = input('Agora digite p, q, e: ').split()
p, q, e = int(constantsString[0]), int(constantsString[1]), int(constantsString[2])

print(decodificar(messageString, p, q, e))