import re
def checkRange(val, lower, upper):
    return lower <= int(val) <= upper


text = open("input4.txt", "r")
data = [l.strip() for l in text.readlines()]


ans = 0
passport = {}
for line in data:
    if not line:
        valid = all([f in passport for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
        print(valid)
        if valid:
            if not checkRange(passport['byr'], 1920, 2002):
                valid = False
            if not checkRange(passport['iyr'], 2010, 2020):
                valid = False
            if not checkRange(passport['eyr'], 2020, 2030):
                valid = False
            if passport['hgt'].endswith('in'):
                if not checkRange(passport['hgt'][:-2], 59, 76):
                    valid = False
            elif passport['hgt'].endswith('cm'):
                if not checkRange(passport['hgt'][:-2], 150, 193):
                    valid = False
            else:
                valid = False
            if '#' not in passport['hcl'][0] or any([c not in 'abcdef0123456789' for c in passport['hcl'][1:]]):
                valid = False
            if passport['ecl'] not in ["amb", "blu", "brn", "gry", "grn" , "hzl", "oth"]:
                valid = False
            if len(passport['pid']) != 9:
                valid = False

            if valid:
                ans += 1
            passport = {}
    else:
        words = line.split()
        for w in words:
            key, value = w.split(":")
            passport[key] = value
print(ans)




