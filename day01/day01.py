import timeit
import os

with open("01.txt", "r+") as f:
    puzzle_input = [int(i) for i in f.read().splitlines()]

# puzzle_input = [
#     int(depth)
#     for depth in """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263""".splitlines()
# ]

increased = 0
for idx, val in enumerate(puzzle_input[1:]):
    if val > puzzle_input[idx]:
        increased += 1

print(f"Part 1: Depth increased {increased} times.")
os.system(f'echo "{increased}" | pbcopy')


increased = 0
last_smoothed_val = sum(puzzle_input[:3])
for idx, val in enumerate(puzzle_input[1:-2]):
    smoothed_val = sum(puzzle_input[idx + 1 : idx + 4])
    if smoothed_val > last_smoothed_val:
        increased += 1
    last_smoothed_val = smoothed_val

print(f"Part 2: Depth increased {increased} times.")
os.system(f'echo "{increased}" | pbcopy')
