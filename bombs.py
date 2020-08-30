bomb_effect = list(map(int, input().split(", ")))
bomb_casing = list(map(int, input().split(", ")))

bombs = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
crafter_bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
Done = False
while bomb_effect and bomb_casing:
    bomb_e = bomb_effect[0]
    bomb_c = bomb_casing[-1]
    result = bomb_e + bomb_c
    if all(value >= 3 for key, value in crafter_bombs.items()):
        Done = True
        print("Bene! You have successfully filled the bomb pouch!")
        break
    if result in bombs.keys():
        crafter_bombs[bombs[result]] += 1
        bomb_effect.pop(0)
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

if Done == False:
    print("You don't have enough materials to fill the bomb pouch.")
if len(bomb_effect) == 0:
    print(F"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")
if len(bomb_casing) == 0:
    print(F"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}")

for key, value in sorted(crafter_bombs.items()):
    print(f"{key}: {value}")