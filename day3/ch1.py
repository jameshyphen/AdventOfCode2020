import os
from re import X

cur_dir = os.path.dirname(__file__)

r_map = []

with open(f"{cur_dir}/i.txt") as f:
    r_map = [x.replace("\n","") for x in f.readlines()]

vel_x = 3
vel_y = 1

x_t = 0
crds_trvl = []

tls_trvl = 0
trs_enc = 0

[
    (
        (
            (trs_enc := trs_enc + 1) 
            if r_map[v][x_t % len(r_map[v])] == "#" 
            else (trs_enc := trs_enc)
        ),
        crds_trvl.append((x_t, v)), x_t := x_t + vel_x, tls_trvl := tls_trvl + 1)
    for v in range(0, len(r_map), vel_y)
]

print(f"The answer to the puzzle: {trs_enc} out of total {tls_trvl} were trees")
