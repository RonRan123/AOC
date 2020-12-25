def main():
    text = open("input3.txt", "r")
    lines = text.readlines()
    graph = [list(l) for l in lines]
    print(graph[0])
    print(len(graph), len(graph[0]))
    z = len(graph[0])
    nums = list()

    pairs = [(1, 1),(3, 1),(5, 1),(7, 1), (1, 2)]
    for p in pairs:
        a, b = p
        x, y = 0, 0
        total = 0
        while y < len(graph):
            x = x % (z-1)
            # print(x, y)
            if graph[y][x] == '#':
                total += 1
            x += a
            y += b
        print(total)
        nums.append(total)
    print (nums)
    product =1
    for n in nums:
        product = product *n

    print(product)

if __name__ == '__main__':
    main()