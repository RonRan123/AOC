import re
def search(e):
    # print()
    # print(e)
    if len(trace2[e]) == 0:
        # print(e, 1)
        return 1
    else:
        tmp = 1
        for i in trace2[e]:
            n, k = i
            tmp += n*search(k)
        print(e, tmp)
        return tmp

# text = open("input7.txt", "r").readlines()
text = open("input7.txt", "r").readlines()
trace = {}

for l in text:
    words = l.split()
    entry = tuple(words[:2])
    # print(entry)
    tmp = list()
    for w in range(len(words)):
        if words[w].isdigit():
            tmp.append((w+1, w+3))
    # print(tmp)
    for t in tmp:
        x, y = t
        key = tuple(words[x:y])
        if key in trace:
            trace[key].append(entry)
        else:
            trace[key] = list()
            trace[key].append(entry)
    if entry not in trace:
        trace[entry] = list()


    # print(tmp)
    # trace[tuple(words[:2])] = [tuple(words[x:y] )for x, y in tmp]

print(len(trace))
print(trace)
print(('wavy', 'teal') in trace)

total =0

queue = list()
queue.append(('shiny', 'gold'))

ans = set()
while queue:
    curr = queue.pop(0)
    # print(curr, trace[curr])
    for i in trace[curr]:
        ans.add(i)
    if curr in trace:
        queue +=trace[curr]
print(ans)
print(len(ans))


# -------------
trace2 = {}
for l in text:
    words = l.split()
    entry = tuple(words[:2])
    # print(entry)
    tmp = list()
    for w in range(len(words)):
        if words[w].isdigit():
            tmp.append((int(words[w]),tuple(words[w+1 :w+3])))
    trace2[entry] = tmp

    # for i in tmp:
    #     if i not in trace:
    #         trace2[i] = []
print(trace2[('shiny', 'gold')])

queue2 = list()
ans = 0
queue2.append(('shiny', 'gold'))

ans = search(('shiny', 'gold'))-1


print(ans)