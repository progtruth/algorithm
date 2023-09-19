from collections import deque

bars = input()
dbar = deque()
cut_count = 0

for i, bar in enumerate(bars):
    if bar == '(':
        dbar.append(bar)
    elif bar == ')':
        if bars[i-1] == '(':
            dbar.pop()
            cut_count += len(dbar)
        else:
            cut_count += 1
            dbar.pop()

print(cut_count)