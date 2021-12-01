depths = []
lines = []
sums = []

with open("depths.txt") as fp:
    lines = fp.readlines()

print("Count: ",len(lines))

for line in lines:
    depths.append(int(line))

print("Count: ",len(depths))


for i in range(3,len(depths)):
    j = i - 1
    k = j - 1
    print(i,j,k)
    sums.append(depths[i] + depths[j] + depths[k])

last = 0
increases = 0
for i in range(len(sums)):
    if i != 0 and sums[i] > last:
        increases += 1
    last = sums[i]

print("Increases: ",increases)
