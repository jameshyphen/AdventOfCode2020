import os
import re
from collections import defaultdict

cur_dir = os.path.dirname(__file__)

with open(f"{cur_dir}/i.txt") as f:
    codes = f.readlines()


# My seat should be the only missing one in the list
# Catch is that some of the seats are missing in the very front and very back
# so they'll be missing from my list aswell
# My seat isnt on the very front or very back (that means no FF or BB)
# And my SeatID +1 and -1 exist in the list

# 1) Filter out all the seats that start as FF or BB
# 2) Find which Seat IDs x-1 < x < x+1 exist


pattern = re.compile("^([F|B]{7})([L|R]{3})$")

cords = []

cur_row: int = 0
cur_col: int = 0
cur_id: int = 0

def cal_id(r, c):
    return r*8+c


[(
            ((cur_row := int("".join([
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
            ]), 2)),
            cords.append((cur_row, cur_col, cal_id(cur_row, cur_col)))
            )
            if row[0] != row[1]
            else (),
    )
    for row, col
    in [pattern.match(code).groups()
        for code
        in codes
    ]
]

sor_cords = sorted(cords, key=lambda x: x[2])

prev_id = sor_cords[0][2]
up_id: int = 0
dwn_id: int = 0

[
    (up_id := cur_cord[2], dwn_id := prev_id)
    if cur_cord[2] == prev_id + 2
    else (
        prev_id := cur_cord[2]
    )
    for cur_cord
    in sor_cords    
]

print(f"The seat left of you is is {dwn_id} and the seat right of you is {up_id}")
print(f"The answer to the puzzle: The Seat Id belonging to you is {up_id - 1}")