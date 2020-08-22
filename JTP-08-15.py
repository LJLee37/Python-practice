def check(st):
    li = st.split()
    retli = []
    for i in li:
        chlst = []
        for j in i:
            if j in chlst:
                retli.append(False)
                break
            chlst.append(j)
        chlst = list(set(map(int,chlst)))
        cur = True
        for j in range(10):
            if chlst[j] != j:
                cur = False
                break
        retli.append(cur)
    return retli

st = input()
print(check(st))

