import timeit
import os

test = False
# test = True


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")
    print(f"Copied {answer} to clipboard.")


start_time = timeit.default_timer()

with open("02.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]

if test:
    puzzle_input = """forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2""".splitlines()

puzzle_input = [[i.split()[0], int(i.split()[1])] for i in puzzle_input]

dir_map = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}
pos = (0, 0)
for d, m in puzzle_input:
    pos = (pos[0] + dir_map[d][0] * m, pos[1] + dir_map[d][1] * m)

ans = pos[0] * pos[1]
answer_to_clipboard(ans)
print(f"Part 1: {ans}")
end_time = timeit.default_timer()
print(f"Completed in {end_time}s.")


pos = (0, 0)
aim = 0
for d, m in puzzle_input:
    if d == "forward":
        pos = (pos[0] + m, pos[1] + aim * m)
    elif d == "down":
        aim += m
    elif d == "up":
        aim -= m

ans = pos[0] * pos[1]
answer_to_clipboard(ans)
print(f"Part 2: {ans}")


print(f"Completed in {round(timeit.default_timer()-end_time, 4)}s.")
