def is_repeated_pattern(num: int) -> bool:
    s = str(num)
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            block = s[:size]
            if block * (n // size) == s:
                return True
    return False


def sum_invalid_ids(line: str) -> int:
    total = 0
    ranges = line.strip().split(",")

    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split("-"))

        for num in range(start, end + 1):
            if is_repeated_pattern(num):
                total += num

    return total

if __name__ == "__main__":
    line = input("Enter the ID ranges:").strip()

    result = sum_invalid_ids(line)
    print("Sum of all invalid IDs:", result)