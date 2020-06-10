c = int(input("enter temperature"))
sel = input("c-celcius,f-farhenite,k-kelvin")

def kelvin(a):
    print(a+273)

def celcius(a):
    return print(a-273)

def fareihneite(a):
    print((a*9/5)+32)

if sel=="c":
    kelvin(c)
    fareihneite(c)
elif sel=="f":
    celcius(c)
    kelvin(c)
else:
    fareihneite(c)
    celcius(c)

