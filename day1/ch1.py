import time
from uvicorn.logging import logging
import os

cur_dir = os.path.dirname(__file__)

with open(f"{cur_dir}/i.txt") as f:
    nums = [int(x) for x in f.readlines()]

answer: int

# FASTEST OPTION

next(
    (answer := nums[i1]*nums[i2])
    for i1 in range(len(nums))
    for i2 in range(i1+1, len(nums))
    if nums[i1] + nums[i2] == 2020
)

print(answer)


# Old

# VER 1
# SLOW

# with open("i.txt") as f:
#     nums = [int(x) for x in f.readlines()]

# result = [
#     e * e
#     for e
#     in [(x, y)
#         for x in nums
#         for y in nums
#         if x + y == 2020
#         ][0]
# ][0]

# print(result)

# VER 2
# COMPREHENSION WONT STOP EVEN THOUGH FOUND

# found = False
# def setTrue():
#     found = True

# [
#     (print(x*y), print(found), setTrue())
#     for x in nums
#     for y in nums
#     if (
#         not found
#         and x + y == 2020 
#     )
# ]


# VER 3
# FOUND BUG WHERE IF 1010 WAS IN INPUTS IT WOULD MULTIPLY ITSELF

# next(
#     (answer := x*y)
#     for x in nums
#     for y in nums
#     if x + y == 2020
# )

