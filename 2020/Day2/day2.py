def findCount(arr):
    tmp = list()
    for a in arr:
        char = a[1][0]
        word = a[2]
        c = word.count(char)
        tmp.append(c)
    return tmp

def countValids(num, arr):
    total = 0
    size = len(num)
    for i in range(size):
        lower, upper = arr[i][0].split("-")
        lower = int(lower)
        upper = int(upper)
        if lower <= num[i]:
            if num[i] <= upper:
                total += 1
    print(total)

def checkValids(arr):
    total = 0
    size = len(arr)
    for a in arr:
        char = a[1][0]
        word = a[2]
        lower, upper = a[0].split("-")
        lower = int(lower)
        upper = int(upper)
        # print(char, word, lower, upper)
        val1 =  (char == word[lower-1])
        val2 = (char == word[upper-1])
        if val1 ^ val2:
            print(char, word, lower, upper)
            total +=1
    print(total)

def main():
    text = open("input2.txt", "r")
    lines = text.readlines()
    lines = list(map (str.split, lines))
    print(lines)
    print(lines[0])
    nums = findCount(lines)
    countValids( nums, lines)
    checkValids(lines)

if __name__ == '__main__':
    main()
