ans = []
for n in range(3, 2001):
    st = '3' * n + '5'
    while '23' in st or '5333' in st or '33333' in st:
        st = st.replace('23', '3', 1)
        st = st.replace('5333', '32', 1)
        st = st.replace('33333', '55', 1)

    ans.append(st.count('5')* 5 + st.count('3')*3 + st.count('2')*2)

print(min(ans))