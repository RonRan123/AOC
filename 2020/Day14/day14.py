import re

def posBin(res, ret = []):
    i = res.find('X')
    # print(res, i)
    if i == -1:
        # print(int(res, 2))
        return [int(res, 2)]
    else:
        tmp1 = posBin(res[:i] + '0' +res[i+1:])
        tmp2 = posBin(res[:i] + '1' +res[i+1:])
        # Unpack int from list to keep it all on the same level
        return [*tmp1, *tmp2]


text = open("input14.txt", "r").readlines()
print(len(text))
pattern = 'mem\[(\d+)\] = (\d+)'
memory = {}
currMask = ''
# Part 1
# for t in text:
#     # print("mask" in t)
#     t = t.strip()
#     if "mask" in t:
#         currMask = t.split("=")[1].strip()
#     else:
#         capture = re.search(pattern, t)
#         loc, val = int(capture.group(1)), int(capture.group(2))
#         binVal = bin(val)[2:]
#         print(val, binVal)
#         newVal = ''
#         for m in reversed(currMask):
#             if m == 'X':
#                 if binVal:
#                     newVal += binVal[-1]
#                 else:
#                     newVal += "0"
#             else:
#                 newVal += m
#             binVal = binVal[:-1]
#         newVal = newVal[::-1]
#         print(newVal)
#         print()
#         memory[loc] = int(newVal, 2)

# Part 2
for t in text:
    t = t.strip()
    if "mask" in t:
        currMask = t.split("=")[1].strip()
    else:
        capture = re.search(pattern, t)
        loc, val = int(capture.group(1)), int(capture.group(2))
        binVal = bin(loc)[2:]
        print(loc, binVal)
        newVal = ''
        for m in reversed(currMask):
            if m == '0':
                if binVal:
                    newVal += binVal[-1]
                else:
                    newVal += "0"
            elif m == 'X':
                newVal += 'X'
            else:
                newVal += m
            binVal = binVal[:-1]
        newVal = newVal[::-1]
        print(newVal)
        # print(posBin(newVal))
        for b in posBin(newVal):
            memory[b] = val
        # print(memory[loc])
        print()


total = sum(memory.values())

print(total)