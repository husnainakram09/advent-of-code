def is_repeated_pattern(n: int) -> bool:
    s = str(n)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


def sum_invalid_ids(range_input: str) -> int:
    total = 0
    ranges = range_input.split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))
        for num in range(start, end + 1):
            if is_repeated_pattern(num):
                total += num

    return total

if __name__ == "__main__":
    line = input("Enter the ID ranges:").strip()

    result = sum_invalid_ids(line)
    print("Sum of all invalid IDs:", result)