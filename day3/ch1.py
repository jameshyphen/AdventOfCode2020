import os
from re import X

cur_dir = os.path.dirname(__file__)

r_map = []

with open(f"{cur_dir}/i.txt") as f:
    r_map = [x.replace("\n","") for x in f.readlines()]

vel_x = 3
vel_y = 1

x_t = 0
x_rep = 0
crds = []

[
    (crds.append(((x_rep * len(r_map[v])) + x_t, v)), x_t := x_t + vel_x)
    if x_t % len(r_map[v]) <= len(r_map[v])
    else (x_rep := x_rep + 1, crds.append(((x_rep * len(r_map[v])) + x_t, v)), x_t := x_t + vel_x)
    for v in range(0, len(r_map), vel_y)
]
fnd = [(x, y) for x, y in crds if r_map[y][int(x) % len(r_map[y])] == "#"]

print(f"{len(fnd)} out of total {len(r_map)} were trees")
