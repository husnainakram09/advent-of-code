def count_fresh_ids_from_file(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    # Find blank line separating ranges and IDs
    if "" in lines:
        blank_index = lines.index("")
    else:
        raise ValueError("Input file must contain a blank line between ranges and IDs.")

    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    # Parse fresh ranges
    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    # Parse ingredient IDs
    ids = list(map(int, id_lines))

    fresh_count = 0

    # Count how many IDs fall inside any range
    for x in ids:
        if any(s <= x <= e for s, e in ranges):
            fresh_count += 1

    print(f"Number of fresh ingredient IDs: {fresh_count}")


# Change 'input.txt' to your file name
count_fresh_ids_from_file("input.txt")