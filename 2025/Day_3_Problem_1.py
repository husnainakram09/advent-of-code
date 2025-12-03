def max_joltage_for_line(line: str) -> int:
    digits = [int(c) for c in line.strip() if c.isdigit()]
    if len(digits) < 2:
        return 0
    
    n = len(digits)
    suffix_max = [0] * n
    suffix_max[-1] = digits[-1]

    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(digits[i+1], suffix_max[i+1])

    best = 0
    for i in range(n - 1):
        val = 10 * digits[i] + suffix_max[i]
        if val > best:
            best = val

    return best


def main():
    total = 0
    with open("input.txt", "r") as f:
        for line in f:
            if line.strip():
                total += max_joltage_for_line(line)

    print("Total output joltage:", total)


if __name__ == "__main__":
    main()
