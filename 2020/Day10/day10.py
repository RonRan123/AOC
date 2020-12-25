import sys, copy, re, math

data = [int(line.strip()) for line in open("sample.txt", "r").readlines()]
data.append(0)
data.append(max(data)+3)
data.sort()
print(data)
print(len(data))

oneJolt = 0
threeJolt = 0
last = 0
for d in data:
    if d - last == 1:
        oneJolt += 1
    elif d-last == 3:
        threeJolt += 1
    last = d
# threeJolt +=1
print(oneJolt, threeJolt, oneJolt*threeJolt)
data.sort()

vals = [1, 2, 3]
count = 0
path = {}

for i in range(len(data)):
    tmp = []
    for j in range(i+1, i+4):
        if j in range(len(data)) and data[j] - data[i] <= 3:
            tmp.append(data[j])
    path[data[i]] = tmp
print(path)

v = set()
t = 0
total = 0
routes = set()


def dfs(visited, graph, node, route):
    for neighbor in path[node]:
        dfs(visited, graph, neighbor, route+str(neighbor))
        global total
        total += 1
    # print(node, path[node], route)
    if len(path[node]) == 0:
        routes.add(route)


# Part 2
# Was not able to solve Part 2 on my own
# My version of the solution (using depth-first search) worked on the two sample
# But would not work for the true input because of run time
# Thank you to Jonathan Paulson for sharing and explaing DP

# dfs(v, path, 0, '')
# print(v)
# print(total)
# print(len(routes))

# Dynamic Programming
# data = [int(line.strip()) for line in open("sample.txt", "r").readlines()]
# data.append(0)
# data.append(max(data)+3)
# data.sort()

DP = {}
# dp(i) = the number of ways to complete the adapter chain given that you are currently at adapter
# that you are currently at adapter xs[i]
def dp(i):
    if i == len(data)- 1:
        return 1
    if i in DP:
        return DP[i]
    print(i)
    tmp = 0
    for j in range(i+1, len(data)):
        if data[j]-data[i] <= 3:
            # One way to get from i to the end is to first step to j
            # the number of paths for i that start by stepping to j is just DP[j]
            # So dp(i) = \sum_{valid j} dp(j)
            tmp += dp(j)
    DP[i] = tmp
    return tmp

print(dp(0), DP)