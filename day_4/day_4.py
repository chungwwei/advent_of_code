with open('day_4/day_4.txt') as file:
    data = file.read()

A = [lst for lst in data.split('\n\n')]
# print(A)
B = []
'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''
import collections
import re
def part_one():
    res = 0
    for passport in A:
        passport = passport.replace('\n', ' ')
        cols = passport.split(' ')
        d = {}
        for col in cols:
            temp = col.split(':')
            d.setdefault(temp[0], temp[1])
        if 'cid' in d and len(d) == 8:
            res += 1
            B.append(passport)
        if 'cid' not in d and len(d) == 7:
            res += 1
            B.append(passport)
    
    # print(res)
    
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

'''
def part_two():
    res = 0
    for passport in B:
        cols = passport.split(' ')
        d = {}
        for col in cols:
            temp = col.split(':')
            d.setdefault(temp[0], temp[1])
        
        byr = d['byr']
        if len(byr) != 4 or not 1920 <= int(byr) <= 2002:
            continue
        iyr = d['iyr']
        if len(iyr) != 4 or not 2010 <= int(iyr) <= 2020:
            continue
        eyr = d['eyr']
        if len(eyr) != 4 or not 2020 <= int(eyr) <= 2030:
            continue
        hgt = d['hgt']
        if not 4 <= len(hgt) <= 5:
            continue
        a, b = False, False
        if ('cm' in hgt and len(hgt) == 5 and 150 <= int(hgt[:3]) <= 193):
            a = True
        if ('in' in hgt and len(hgt) == 4 and  59 <= int(hgt[:2]) <= 76):
            b = True
        if not a and not b:
            continue
        hcl = d['hcl']
        if len(hcl) != 7:
            continue
        if hcl[0] != '#':
            continue
        if not re.match('^\#[0-9a-f]{6}$', hcl):
            continue
        # if not all(c in ['0123456789abcdef'] for c in hcl[1:]):
        #     continue
        ecl = d['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        pid = d['pid']
        if len(pid) != 9 or not all(c.isdigit() for c in pid):
            continue
        print(passport)
        res += 1
    print(res)
    
part_one()
part_two()
