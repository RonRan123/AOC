import re, math
def main():
    text = open("input5.txt", "r")
    data = [l.strip() for l in text.readlines()]
    boardingPass = list()
    for bp in data:
        lower = 0
        upper =127
        left =0
        right = 7
        for char in bp[:6]:
            if char == 'F':
                upper = int((upper+lower)/2)
            elif char == 'B':
                lower = math.ceil((upper+lower)/2)
            else:
                print("error")
        if bp[6] == 'F':
            row = lower
        else:
            row = upper

        for char in bp[7:9]:
            if char == 'L':
                right = int((left+right)/2)
            elif char == 'R':
                left = math.ceil((left+right)/2)
            else:
                print('lf error')

        if bp[9] == 'L':
            col = left
        else:
            col = right
        boardingPass.append((row, col))
    # print(boardingPass)

    totals = list()
    for r, c in boardingPass:
        # print(r,c, r*8+c)
        totals.append(r*8+c)
    print(max(totals))

    for r in range(0, 127):
        for c in range(0, 7):
            if (r,c) not in boardingPass:
                print(r,c, (r))
    tmp = list()
    for i in range(0, 832):
        if i not in totals:
            tmp.append(i)

    print(tmp)
    print(int("0101100101", 2))

    # One line code (from Leo)
    # For loop through each line of the txt
    # Replace the F/L to 0 and B/R to 1
    # int function with base two
    print(max(int(d.replace("F", "0").replace("B", '1').replace("L", "0").replace("R", '1'), 2) for d in data))

if __name__ == '__main__':
    main()