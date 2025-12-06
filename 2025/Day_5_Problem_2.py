def parse_input(lines):
    ranges = []
    ids = []

    section = 0
    for line in lines:
        if line == "":
            section = 1
            continue

        if section == 0:
            # Fresh ranges: "a-b"
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
        else:
            # Available ingredient IDs
            ids.append(int(line))

    return ranges, ids


def merge_ranges(ranges):
    """
    Merge overlapping or touching ranges.
    Example: (3,5) and (5,8) → (3,8)
    """
    ranges.sort()
    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


def part1(ranges, ids):
    # Merge ranges to make searching efficient
    merged = merge_ranges(ranges)

    fresh_count = 0
    for x in ids:
        for a, b in merged:
            if a <= x <= b:
                fresh_count += 1
                break
    return fresh_count


def part2(ranges):
    # Merge ranges and count how many unique IDs are covered
    merged = merge_ranges(ranges)

    total = 0
    for a, b in merged:
        total += (b - a + 1)
    return total


if __name__ == "__main__":
    # Read input file
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    ranges, ids = parse_input(lines)

    # Solve Part 1
    p1 = part1(ranges, ids)
    print("Part 1 - Fresh available ingredient IDs:", p1)

    # Solve Part 2
    p2 = part2(ranges)
    print("Part 2 - Total fresh IDs according to ranges:", p2)