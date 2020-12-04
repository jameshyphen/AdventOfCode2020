import re

# SOLUTION 1

with open("i.txt") as f:
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    valid = [
        pw
        for mn, mx, l, pw
        in [
                pattern.match(x).groups() 
               for x in f.readlines()
        ]
        if len([x for x in range(len(pw)) if x+1 in (int(mn), int(mx)) and pw[x] == l ]) == 1
    ]

print(len(valid))
