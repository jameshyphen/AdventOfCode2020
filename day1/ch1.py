import time

t1 = time.time()

with open("input.txt") as f:
    nums = [int(x) for x in f.readlines()]

# FASTEST OPTION
answer: int

next(
    (answer := x*y)
    for x in nums
    for y in nums
    if x + y == 2020
)

t2 = time.time()

print(answer)
print(f"Time spent = {(t2-t1)*1000}ms")


# Old

# VER 1
# SLOW

# with open("input.txt") as f:
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

