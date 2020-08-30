from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:
    male = males[-1]
    women = females[0]
    if male <= 0:
        males.pop()
    elif women <= 0:
        females.popleft()
    elif women%25 == 0:
        females.popleft()
        females.popleft()
    elif male%25 == 0:
        males.pop()
        males.pop()
    elif women == male:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")