import re, math
def main():
    text = open("input6.txt", "r").read().strip().split('\n\n')
    # data = [l for l in text]
    # print(len(text))

    # sum = 0
    # for t in text:
    #     count = t.count('\n') + 1
    #     t = t.replace('\n', '')
    #     # print(t)
    #     # print(set(t), len(set(t)))
    #     # sum += len(set(t))
    #     # tmp = list(t)
    #     tmp = {}
    #     for char in t:
    #         if char not in tmp:
    #             tmp[char] = 1
    #         else:
    #             tmp[char] += 1
    #     print(tmp)
    #     for key in tmp:
    #         # key, value = entry
    #         if tmp[key] == count:
    #             sum +=1
    #
    #
    # print(sum)

    print(sum(len(set.union(*map(set, x.split('\n')))) for x in text))
    print(sum(len(set.intersection(*map(set, x.split('\n')))) for x in text))

if __name__ == '__main__':
    main()