def parse_problems_part1(lines):
    width = len(lines[0])
    problems = []
    col = 0

    while col < width:
        if all((row[col] == " " for row in lines)):
            col += 1
            continue

        start = col
        while col < width and not all((row[col] == " " for row in lines)):
            col += 1

        block = [row[start:col] for row in lines]
        problems.append(block)

    return problems


def parse_problem_vertical(block):
    stripped = [row.strip() for row in block]
    operator = stripped[-1]
    operator = operator[0]
    nums = [int(x) for x in stripped[:-1]]
    return nums, operator

def solve_part1(lines):
    blocks = parse_problems_part1(lines)
    total = 0
    for block in blocks:
        nums, op = parse_problem_vertical(block)
        if op == "+":
            res = sum(nums)
        else:  # "*"
            res = 1
            for n in nums:
                res *= n
        total += res
    return total

# PART 2 LOGIC
def parse_problems_part2(lines):
    width = len(lines[0])
    problems = []
    col = width - 1

    while col >= 0:
        if all(row[col] == " " for row in lines):
            col -= 1
            continue

        end = col
        while col >= 0 and not all(row[col] == " " for row in lines):
            col -= 1
        start = col + 1

        block = [row[start:end+1] for row in lines]
        problems.append(block)

    return problems


def parse_problem_columns(block):
    h = len(block)
    w = len(block[0])

    operator_row = block[-1]
    op = ""
    for ch in operator_row:
        if ch in "+*":
            op = ch
            break

    digit_rows = block[:-1]

    numbers = []

    for c in range(w):
        col_digits = [digit_rows[r][c] for r in range(len(digit_rows))]
        col_digits = "".join(col_digits).strip()
        if col_digits:
            numbers.append(int(col_digits))

    return numbers, op


def solve_part2(lines):
    blocks = parse_problems_part2(lines)
    total = 0
    for block in blocks:
        nums, op = parse_problem_columns(block)
        if op == "+":
            res = sum(nums)
        else:
            res = 1
            for n in nums:
                res *= n
        total += res
    return total

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    part1 = solve_part1(lines)
    part2 = solve_part2(lines)

    print("Part 1 Answer:", part1)
    print("Part 2 Answer:", part2)