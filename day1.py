measurements = open("day1.txt").readlines()
# print(measurements)

total = 0
for i in range(len(measurements)):
    if int(measurements[i]) > int(measurements[i - 1]):
        total += 1

print(total)
