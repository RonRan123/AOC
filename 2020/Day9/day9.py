import sys, copy
data = [int(line.strip()) for line in open("input9.txt", "r").readlines()]
original = copy.deepcopy(data)
preamble = data[:25]
data = data[25:]
c = 25
for d in data:
    c += 1
    valid = False
    for x in range(len(preamble)):
        for y in range(len(preamble)):
            if x == y:
                continue
            elif preamble[x] + preamble[y] == d:
                valid = True
                break
            else:
                continue
    if valid:
        preamble.pop(0)
        preamble.append(d)
    else:
        print(d)

print()
print()
target = 507622668
#
# curr = list()
# ind = 0
# for i in range(len(data)):
#     for j in range(len(data)):
#         total = sum(data[i:j])
#         # print(total, ind, i)
#         if total == target:
#             print(i, j)
#             sys.exit()
#         elif total > target:
#             break
#         else:
#             continue

print(min(data[490:507]))
print(max(data[490:507]))
print(min(data[490:507])+max(data[490:507]))

# for d in data:
#     sumCurr = sum(curr)
#     if sumCurr == target:
#         print(curr)
#         break
#     elif sumCurr > target:
#         while(sum(curr) > target):
#             # print(sumCurr, target)
#             curr.pop(0)
#     else:
#         curr.append(d)
# print(curr)
# print(sum(curr))
# print(target)
print()
for i in range(len(data)):
    if original[i] > 150000000000:
        print(i, original[i])
        break