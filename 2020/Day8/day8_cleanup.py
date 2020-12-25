def run(instructions):
    ind = 0
    acc = 0
    past = set()

    while ind not in past:
        past.add(ind)
        cmd, num = instructions[ind]
        if cmd == "nop":
            ind += 1
        elif cmd == "acc":
            acc += num
            ind += 1
        elif cmd == "jmp":
            ind += num
    return acc


text = open("input8.txt", "r").readlines()
data = []

for line in text:
    words = line.split()
    data.append((words[0], int(words[1])))


# Part 1
ans1 = run(data)
print("Part 1:", ans1)
print()

# Part 2
for d in data:
    if d[0] == "j"
tmp = list(data)
print(id(tmp), id(data))
print(tmp)
print(data)


