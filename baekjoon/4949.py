from collections import deque

checkdata = ['(', '[', ']', ')']

def check_sentance(sentance):
    check = deque()
    
    for s in sentance:
        if s in checkdata:
            if s in list("(["): 
                check.append(s)
            elif s == ')':
                if check and check[-1] == '(':
                    check.pop()
                else: 
                    return "no"
            elif s == ']':
                if check and check[-1] == '[':
                    check.pop()
                else: 
                    return "no"

    if check: return "no"
    return "yes"


inputdata = []

while True:
    inputdata.append(input())
    if inputdata[-1] == ".":
        break

for sentance in inputdata[:-1]:
    print(check_sentance(sentance))