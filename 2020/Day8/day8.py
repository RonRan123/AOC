text = open("input8.txt", "r").readlines()
instructions = []
for line in text:
    one, two = line.split()
    instructions.append((one, int(two)))

past = []
index = 0
acc = 0
options = []
while(True):
    if index in past or index >= len(instructions):
        break
    past.append(index)
    cmd, num = instructions[index]
    print(str(index)+"\t", cmd, num)
    if cmd == "nop":
        options.append((index, cmd, num))
        index += 1
    elif cmd == "acc":
        acc += num
        index += 1
    elif cmd == "jmp":
        options.append((index, cmd, num))
        index += num
    else:
        print("error")
        break
print()
print(acc)
print()

print(options)
index = 0
acc = 0
i, c, n = options.pop(0)
past = []
while (True):
    if index in past:
        index = 0
        acc = 0
        past = []
        i, c, n = options.pop()
        print()
    if index >= len(instructions):
        print('end')
        break
    past.append(index)
    cmd, num = instructions[index]
    print(str(index) + "\t", cmd, num)
    if cmd == "nop":
        if index == i:
            index += num
        else:
            index += 1
    elif cmd == "acc":
        acc += num
        index += 1
    elif cmd == "jmp":
        if index == i:
            index += 1
        else:
            index += num
    else:
        print("error")
        break

print(acc)