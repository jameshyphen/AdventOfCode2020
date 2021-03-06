import os
from re import X

cur_dir = os.path.dirname(__file__)

r_map = []

with open(f"{cur_dir}/i.txt") as f:
    r_map = [x.replace("\n","") for x in f.readlines()]
def travel_tiles(vel_x, vel_y):

    x_t = 0
    crds = []

    [
        (crds.append((x_t, v)), x_t := x_t + vel_x)
        for v in range(0, len(r_map), vel_y)
    ]
    fnd = [(x, y) for x, y in crds if r_map[y][int(x) % len(r_map[y])] == "#"]

    return(len(fnd))

ls_pths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ls_fnd = [travel_tiles(x, y) for x,y in ls_pths]

res_t = sum(ls_fnd)

res_f = 1
[res_f := res_f * r for r in ls_fnd]
[print(f"Found {ls_fnd[x]} trees with x velocy {ls_pths[x][0]} and y velocity {ls_pths[x][1]}.") for x in range(len(ls_pths))]
print(f"The total sum of the found trees: {res_t}")
print(f"The answer to the puzzle: The total product of the found trees: {res_f}")
