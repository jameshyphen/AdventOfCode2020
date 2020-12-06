import os
import re
from collections import defaultdict

cur_dir = os.path.dirname(__file__)

with open(f"{cur_dir}/i.txt") as f:
    codes = f.readlines()


# 0 to 127 rows
# we work with bits
# First 7 letters are F or B
# F - Lower
# B - Higher

# First letter indicates if it's in the front 0-63 or back 64 - 127
# That means we can use the following bits:
# 64 32 16 8 4 2 1
# First letter B means
# 1 0 0 0 0 0 0
# Second letter B means the back(bigger number) of that half so 64-127 means we get 96-127 and not 64-97
# 1 1 0 0 0 0 0
# and so on until you're left with exactly one row

# Last 3 letters are L or R
# L - Lower
# R - Higher
# That means we can use the following bits:
# 4 2 1
# First letter R means 
# 1 0 0
# etc

# Answer is Rows * 8 + Columns


pattern = re.compile("^([F|B]{7})([L|R]{3})$")

hi_id: int = 0
hi_row: int = 0
hi_col: int = 0
# cords = []

cur_row: int = 0
cur_col: int = 0
cur_id: int = 0

def cal_id(r, c):
    return r*8+c


[((
            cur_row := int("".join([
            "1"
                if b_int == "B"
                else "0"
                for b_int
                in row
            ]), 2),
            cur_col := int("".join([
                "1"
                if b_int == "R"
                else "0"
                for b_int
                in col
            ]), 2),
    ),
        (cur_id := cal_id(cur_row, cur_col)),
        (hi_id := cur_id, hi_row := cur_row, hi_col := cur_col)
        if cur_id > hi_id
        else ()
    )
    for row, col
    in [pattern.match(code).groups()
        for code
        in codes
    ]
]

print(f"Highest Seat Id row is {hi_row} and col {hi_col}")
print(f"The answer to the puzzle: Highest Seat ID in this plane is {(hi_row*8)+hi_col}")
