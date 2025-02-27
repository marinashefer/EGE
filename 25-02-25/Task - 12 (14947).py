ans = []

for n in range(4, 10000):
    st = '1' + '9'*n
    while '19' in st or '49' in st or '999' in st:
        st = st.replace('19', '9', 1)
        st = st.replace('49', '91', 1)
        st = st.replace('999', '4', 1)
    ans.append(st.count('1') + st.count('9')*9 + st.count('4')*4)

print(max(ans))
