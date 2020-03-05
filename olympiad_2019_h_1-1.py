#-100 <= x <= 100
#-100 <= y <= 100
a = int(input())
b = int(input())
Answer = []

flag = False
for x in range (-100, 101):
    for y in range (-100, 101):
        if (a * x + b * y) == 48:
            flag = True
            Answer.append(x)
            Answer.append(y)

print (flag)
if flag:
    print (Answer)

