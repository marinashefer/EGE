
num = 3*15**1140 + 2*15**1025 + 15**923 - 3*15**85 + 2*15**74 + 3

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[-1::]

num_2 = convert(num, 15)
