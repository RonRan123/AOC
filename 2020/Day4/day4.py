import re
def main():
    text = open("input4.txt", "r")
    data = [l.strip() for l in text.readlines()]
    print(data)
    total = 0
    tmp = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for r in data:
        if r == '':
            if len(tmp) == 0:
                total += 1
            tmp = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        tmp2 = list()
        for t in tmp:
            if t in r:
                tmp2.append(t)
        for ti in tmp2:
            tmp.remove(ti)

    passports = open("input4.txt", "r").read().split("\n\n")
    print(passports)
    total = 0
    tmp = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    # for p in passports:
    #     criteria = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #     tmp2 = list()
    #     for c in criteria:
    #         if c in p:
    #             tmp2.append(c)
    #     for ti in tmp2:
    #         criteria.remove(ti)
    #     if len(criteria) == 0:
    #         total += 1
    haveCrit = list()
    for p in passports:
        criteria = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        tmp2 = list()
        for c in criteria:
            if c in p:
                tmp2.append(c)
        for ti in tmp2:
            criteria.remove(ti)
        if len(criteria) == 0:
            haveCrit.append(p)

    dictPass = list()
    for passport in haveCrit:
        d = dict()
        for i in passport.split():
            k, v = i.split(':')
            d[k] = v
        dictPass.append(d)


    for pp in dictPass:
        sum = 0
        sum += int(1920 <= int(pp['byr']) <= 2002)
        sum += int(2010 <= int(pp['iyr']) <= 2020)
        sum += int(2020 <= int(pp['eyr']) <= 2030)
        # height
        tmp = ""
        for h in pp['hgt']:
            # print(h)
            if h.isdigit():
                tmp += h
            elif h =='i':
                sum += int(59<=int(tmp)<=76)
                break
            else:
                sum += int(150 <= int(tmp) <= 193)
                break
        # hai
        sum += ('#' in pp['hcl'])
        # pattern = re.compile("#[a-f0-9]{6}}")
        # print(pp['hcl'],pattern.match(pp['hcl']))
        sum += int(len(pp['pid']) == 9)
        sum += int(pp['ecl'] in ["amb", "blu", "brn", "gry", "grn" , "hzl", "oth"])
        # print(sum)
        if sum == 7:
            total +=1


    print(total)
    print('pid' in data[0])
if __name__ == '__main__':
    main()