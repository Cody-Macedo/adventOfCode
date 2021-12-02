horizontal = 0;
depth = 0;

instructions = open("day2.txt").readlines()
# print(instructions)
for i in range(len(instructions)):
    splited = instructions[i].split(" ")
    print(splited[0] + splited[1])
    if splited[0] == "forward":
        horizontal += int(splited[1])
    elif splited[0] == "down":
        depth += int(splited[1])
    else:
        depth -= int(splited[1])

print(horizontal);
print(depth);
res = horizontal*depth
print(res);