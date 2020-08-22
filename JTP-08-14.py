def compress(st):
    li = []
    c = 0
    i = 0
    while i < len(st):
        c = 0
        for j in range(i, len(st)):
            if st[i] != st[j]:
                li.append(st[i])
                li.append(str(c))
                break
            else:
                c+=1
                if j == len(st) - 1:
                    li.append(st[i])
                    li.append(str(c))
                    break

        i += c
    return ''.join(li)


st = input()
print(compress(st))
