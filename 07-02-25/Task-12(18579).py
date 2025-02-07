st = '>' + '3'*10 + '5'*10 + '7'*10
while '>3' in st or '>5' in st or '>7' in st:
    st = st.replace('>3', '55>', 1)
    st = st.replace('>5', '5>3', 1)
    st = st.replace('>7', '3>5', 1)

count = (st.count('3')* 3 + st.count('5')* 5 + st.count('7')* 7)
print(count)