from _collections import deque

material_values = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while material_values and magic_values:
    material = material_values.pop()
    magic = magic_values.popleft()
    result = material*magic
    if result in presents:
        crafted[presents[result]] += 1
    elif result not in presents:
        if result < 0:
            material_values.append(magic + material)
        elif result > 0:
            material_values.append(material + 15)
        else:
            if material:
                material_values.append(material)
            if magic:
                magic_values.appendleft(magic)

success=(crafted["Doll"] and crafted["Wooden train"] or (crafted["Teddy bear"] and crafted["Bicycle"]))
if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if material_values:
    print(f"Materials left: {', '.join(str(x)for x in reversed(material_values))}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for key, value in sorted(crafted.items()):
    if value>0:
        print(f"{key}: {value}")