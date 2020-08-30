string = input().split()
colors = ["red", "yellow", "blue", "orange", "purple", "green"]
my_colors = []
secondary_colors = {"orange": ["red", "yellow"], "purple": ["red", "blue"], "green": ["yellow", "blue"]}
while string:
    left = string.pop(0)
    right = ''
    if string:
        right = string.pop()
    if left + right in colors:
        my_colors.append(left + right)
    elif right + left in colors:
        my_colors.append(right + left)
    else:
        if len(left) > 1:
            string.insert(len(string)//2, left[:-1])
        if len(right) > 1:
            string.insert(len(string)//2, right[:-1])

for i in range(len(my_colors) - 1, -1, -1):
    current = my_colors[i]
    if current in secondary_colors and any(x not in my_colors for x in secondary_colors[current]):
        del my_colors[i]

print(my_colors)