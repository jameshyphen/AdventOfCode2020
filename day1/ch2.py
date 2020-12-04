import time
import os

with open(f"{os.path.dirname(__file__)}/i.txt") as f:
    nums = [int(x) for x in f.readlines()]

# FASTEST OPTION
answer: int = 0

next(
    (answer := nums[i1]*nums[i2]*nums[i3])
    for i1 in range(len(nums))
    for i2 in range(i1+1, len(nums))
    for i3 in range(i2+1, len(nums))
    if nums[i1] + nums[i2] + nums[i3] == 2020
)

print(f"The product is: {answer}")


# Old

# VER 1

# next(
#     (answer := x*y*z)
#     for x in nums
#     for y in nums
#     for z in nums
#     if x + y + z== 2020
# )
