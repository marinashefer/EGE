from string import ascii_lowercase, digits
alph = digits + ascii_lowercase

for x in alph[1:35]:
    num1 = int('6' + x + 'QR'+ x, 35)
    num2 = int(x + '59SH', 35)
    num3 = int('PH' + x + '69YW', 35)
    num = num1 + num2 + num3
    count = [0] * 10
    for i in str(num):
        count[int(i)] += 1
    digit = 9 - count[::-1].index(max(count))
    if num % digit**2 == 0:
        print(num // digit**2)

    #digit = int(sorted(Counter(str(num)).most_common(), key=lambda x:(-x[1], -int(x[0])))[0][0])
    #if num % digit**2 == 0:
    #   print(num // digit**2)
