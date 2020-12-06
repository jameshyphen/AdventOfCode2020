import os
from collections import defaultdict
import re

cur_dir = os.path.dirname(__file__)
raw_passports = []
# cid optional
# Every other field mandatory
req_flds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def validate_reqs(l1):
    for i in req_flds:
        if i not in l1:
            return False
    return True

def validate_fields(flds):
    validators = {
        "byr": "^(19[2-9][0-9]|200[0-2])$",
        "iyr": "^(201[0-9]|2020)$",
        "eyr": "^(202[0-9]|2030)$",
        "hgt": "^(((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in))$",
        "hcl": "^#[0-9a-f]{6}$",
        "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": "^([0-9]){9}$",
        "cid": ".*",
    }
    for fld in flds:
        if fld[0] == "cid":
            continue
        if bool(re.compile(validators[str(fld[0])]).match(str(fld[1]))) == False:
            return False
    return True

with open(f"{cur_dir}/i.txt") as f:
    raw_passports = f.readlines()


passports = defaultdict(list)
passnr = 0
nr_of_valid_p = 0
nr_of_invalid_p = 0

def validate(passport):
    if validate_reqs([field[0] for field in passport]) and validate_fields(passport):
        return True
    return False

[(  passports[passnr].extend([y.split(":") 
    for y in raw_passports[raw_index].split()]),
        ((  nr_of_valid_p := nr_of_valid_p + 1)
            if validate(passports[passnr])
            else (nr_of_invalid_p := nr_of_invalid_p + 1),
            passnr := passnr + 1) 
        if (raw_index+1) == len(raw_passports)
        else ())
    if raw_passports[raw_index] != "\n"
    else (( nr_of_valid_p := nr_of_valid_p + 1)
            if validate(passports[passnr])
            else (nr_of_invalid_p := nr_of_invalid_p + 1),
            passnr := passnr + 1) 
    for raw_index in range(len(raw_passports)
)]


print(f"Total passports are {passnr}")
print(f"The invalid amount of passports is: {nr_of_invalid_p}")
print(f"The answer to the puzzle: The valid amount of passports is: {nr_of_valid_p}")
