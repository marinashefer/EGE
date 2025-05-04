def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

num1 = 43**56
num2 = 113**841
for x in range(1, 2006)[::-1]:
    num = num1 + num2 - x
    num_4 = convert(num, 4)
    if (num_4.count('0') + num_4.count('2')) % 2 == 0:
        if (num_4.count('1') + num_4.count('3')) % 2 == 0:
            if num_4.count('2') <= 712:
                print(x)
                break






















