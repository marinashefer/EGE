def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

ans = []
for n in range(3, 1001):
    st = '>' + '0' * 25 + '1' * n + '2' *  25
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '1>', 1)
    ii = []
    for i in st:
        if i != '>':
            ii.append(int(i))

    if is_prime(sum(ii)):
        print(n)
        break