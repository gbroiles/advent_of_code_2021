depths = []
lines = []

with open("depths.txt") as fp:
    lines = fp.readlines()

print("Count: ",len(lines))

for line in lines:
    depths.append(int(line))

print("Count: ",len(depths))

last = 0
increases = 0
for depth in depths:
    if int(depth) > int(last):
        increases += 1
        print(depth)
    last = depth


increases -= 1
print("Increases: ",increases)
