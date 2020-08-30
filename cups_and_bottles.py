from _collections import deque

cups=deque(map(int, input().split()))
bottles=list(map(int, input().split()))
water=0

while cups and bottles:
    cup=cups.popleft()
    bottle=bottles.pop()
    if cup>bottle:
        result=cup-bottle
        cups.appendleft(result)
    elif bottle>cup:
        water+=bottle-cup


if bottles:
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")
if cups:
    print(f"Cups: {' '.join(str(x) for x in cups)}")
print(f"Wasted litters of water: {water}")