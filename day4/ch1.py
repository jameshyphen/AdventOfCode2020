import os
from collections import defaultdict

cur_dir = os.path.dirname(__file__)
raw_passports = []
# cid optional
# Every other field mandatory
req_flds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def contains_reqs(l1):
    for raw_index in req_flds:
        if raw_index not in l1:
            return False
    return True

with open(f"{cur_dir}/i.txt") as f:
    raw_passports = f.readlines()



passports = defaultdict(list)
passnr = 0
nr_of_valid_p = 0
nr_of_invalid_p = 0

def validate(passport):
    return contains_reqs([field[0] for field in passport])


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


print(f"Total number of passports is {passnr}")
print(f"The invalid amount of passports is: {nr_of_invalid_p}")
print(f"The answer to the puzzle: The valid amount of passports is: {nr_of_valid_p}")
