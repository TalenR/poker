import os
import math

os.chdir(r'C:\Users\pr5628de\Documents')

nums = []
with open('poker.txt','r') as hands:
    hands = list(hands.read())

for x in hands:
    if x == 'T':
        hands[hands.index(x)] = '10'
    elif x == 'J':
        hands[hands.index(x)] = '11'
    elif x == 'Q':
        hands[hands.index(x)] = '12'
    elif x == 'K':
        hands[hands.index(x)] = '13'
    elif x == 'A':
        hands[hands.index(x)] = '14'

handses = []
for i in range(0, len(hands), 15):
    handses.append(hands[i:i + 14])

def straight(x):
    score = 0
    num = list(map(int,x[0:13:3]))
    for i in range(1,5):
        if (max(num)-i) in num:
            score += 1
    if score == 4:
        return 5
    else:
        return 0

def flush(x):
    if x.count(x[1]) == 5:
        return 6
    else:
        return 0

def ofakind(x):
    kinds = []
    score = 0
    num = list(map(int,x[0:13:3]))
    for i in set(num):
        if num.count(i) == 2:
            score += 2
            kinds.insert(0,i)
        elif num.count(i) == 3:
            score +=4.5
            kinds.append(i)
        elif num.count(i) == 4:
            score = 8
            kinds.append(i)
    return score, kinds
def scores(x):
     return flush(x) + ofakind(x)[0] + straight(x)

def high(x):
    num = list(map(int,x[0:13:3]))
    return max(num)

tally = 0
for i in range(0,len(handses),2):
    if scores(handses[i]) > scores(handses[i+1]):
        tally += 1
    elif scores(handses[i]) < scores(handses[i+1]):
        continue
    elif scores(handses[i]) == scores(handses[i+1]) and flush(handses[i]) == 6:
        if high(handses[i]) > high(handses[i+1]):
            tally += 1
    elif scores(handses[i]) == scores(handses[i+1]) and straight(handses[i]) == 5:
        if high(handses[i]) > high(handses[i+1]):
            tally += 1
    elif scores(handses[i]) == scores(handses[i+1]) == 8 or 4.5 or 2:
        if ofakind(handses[i])[1] < ofakind(handses[i+1])[1]:
            continue
        elif ofakind(handses[i])[1] > ofakind(handses[i+1])[1]:
            tally +=1
        elif ofakind(handses[i])[1] == ofakind(handses[i+1])[1]:
            if high(handses[i]) > high(handses[i+1]):
                tally += 1
    elif scores(handses[i]) == scores(handses[i+1]) == 4:
        if max(ofakind(handses[i])[1]) < max(ofakind(handses[i+1])[1]):
            continue
        elif max(ofakind(handses[i])[1]) > max(ofakind(handses[i+1])[1]):
            tally += 1
        elif max(ofakind(handses[i])[1]) == max(ofakind(handses[i+1])[1]):
            if min(ofakind(handses[i])[1]) < min(ofakind(handses[i+1])[1]):
                continue
            elif min(ofakind(handses[i])[1]) > min(ofakind(handses[i+1])[1]):
                tally += 1
            elif min(ofakind(handses[i])[1]) == min(ofakind(handses[i+1])[1]):
                if high(handses[i]) > high (handses[i+1]):
                    tally += 1
    elif scores(handses[i]) == scores(handses[i+1]) == 6.5:
        if ofakind(handses[i])[1][1] > ofakind(handses[i+1])[1][1]:
            tally += 1

print(tally)


