import re


# SOLUTION 1


# def unpack_reqs(i):
#     if i[0] != 0:
#         return i[1]
#     v = i[1].split()
#     return (v[0].split("-"), v[1])

# with open("i.txt") as f:
#     valid = [
#         v[1]
#         for v
#         in [
#             # ((min, max), letter, pass)
#             list(map(unpack_reqs, enumerate(y)))
#             for y
#             in [
#                 list(map(str.strip, x.split(":")))
#                 for x
#                 in f.readlines()
#             ]
#         ]
#         if int(v[0][0][1]) >= v[1].count(v[0][1]) >= int(v[0][0][0]) 
#     ]


# Thank you Lucas An'gov for recommending the regex!
# SOLUTION 2

with open("i.txt") as f:
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    valid = [
        pw
        for mn, mx, l, pw
        in [
                pattern.match(x).groups() 
               for x in f.readlines()
        ]
        if int(mx) >= pw.count(l) >= int(mn)
    ]

print(valid)
