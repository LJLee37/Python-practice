LINES = [1, 1, 2, 3, 8, 12, 24, 42, 77, 145, 267, 496]
possibleSets = []
for i in range(len(LINES)):
    for j in range(i+1, len(LINES[i:])):
        for k in range(j+1, len(LINES[j:])):
            for l in range(k+1, len(LINES[k:])):
                if(LINES[i] + LINES[j] + LINES[k] + LINES[l]) == 155 :
                    possibleSets.append([i,j,k,l])

print (possibleSets)
print (LINES[3:])
'''
망함.

'''