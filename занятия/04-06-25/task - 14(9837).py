from string import digits, ascii_lowercase

alph = digits + ascii_lowercase
for x in alph[:23]:
    num1 = int(f'7{x}38596', 23)
    num2 = int(f'14{x}36', 23)
    num3 = int(f'61{x}7', 23)
    num = num1 + num2 + num3
    if num % 22 == 0:
        print(num//22)
        break