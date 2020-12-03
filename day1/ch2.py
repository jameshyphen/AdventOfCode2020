import time

t1 = time.time()

with open("i.txt") as f:
    nums = [int(x) for x in f.readlines()]

# FASTEST OPTION
answer: int


next(
    (answer := nums[i1]*nums[i2]*nums[i3])
    for i1 in range(len(nums))
    for i2 in range(i1+1, len(nums))
    for i3 in range(i2+1, len(nums))
    if nums[i1] + nums[i2] + nums[i3] == 2020
)

t2 = time.time()

print(answer)
print(f"Time spent = {(t2-t1)*1000}ms")


# Old

# VER 1

# next(
#     (answer := x*y*z)
#     for x in nums
#     for y in nums
#     for z in nums
#     if x + y + z== 2020
# )
