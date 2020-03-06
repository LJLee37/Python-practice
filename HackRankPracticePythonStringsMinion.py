def minion_game(string):
    # your code goes here
    score = [0,0]#0: Stuart, 1: Kevin
    string = list(string)
    #VOWEL = ['A', 'E', 'I', 'O', 'U']
    for i in string:
        temp2 = [i]
        isVowel = False
        for j in ['A', 'E', 'I', 'O', 'U']:
            if temp2[0] == j:
                isVowel = True
                #break
        """if isVowel:
            score[1] += 1
        else:
            score[0] += 1"""
        for j in string:
            """
            temp2.append(j)
            isVowel = False
            for k in ['A', 'E', 'I', 'O', 'U']:
                if temp2[0] == k:
                    isVowel = True
                    """
            if isVowel:
                score[1] += 1
            else:
                score[0] += 1
        string = list(''.join(string)[1:])
    if score[0] > score[1]:
        print("Stuart", end = ' ')
        print(score[0])
    elif score[0] < score[1]:
        print("Kevin", end = ' ')
        print(score[1])
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)