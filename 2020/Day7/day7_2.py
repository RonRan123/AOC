

def search(e):
    total = set()
    queue = list()
    queue.append(e)
    print(len(queue))
    print(queue)
    while(queue):
        item = queue.pop()
        total.union(*trace[item])
        for e in trace[item]:
            print(e)
            if e in trace:
                queue.append(e)
    print(total)
    print(len(total))



text = open("input7.txt", "r").readlines()
trace = {}

for l in text:
    words = l.split()
    tmp = list()
    for w in range(len(words)):
        if words[w].isdigit():
            tmp.append((w + 1, w + 3))
        # print(tmp)
        # trace[tuple(words[:2])] = [tuple(words[x:y]) for x, y in tmp]
    vals = [tuple(words[x:y]) for x, y in tmp]
    for t in vals:
        if t in trace:
            trace[t].append(tuple(words[:2]))
        else:
            trace[t] = [tuple(words[:2])]
    if tuple(words[:2]) not in trace:
        trace[tuple(words[:2])] = []


print(len(trace))
print(trace)
# ans = 0
# for entry in trace:
#     ans += search(entry)
#
# print(ans)
search(('shiny', 'gold'))
