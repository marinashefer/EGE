def f(num):
    if num >= 2010:
        return num
    if num < 2010:
        return f(num+3) + f(num+2) + f(num+1)

print((f(2000) - 2*(f(2002) + f(2003))) // f(2004))