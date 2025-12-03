from pathlib import Path

K = 12

def max_k_subsequence(digits: str, k: int) -> str:
    """Return the lexicographically largest subsequence of length k from digits (preserve order)."""
    n = len(digits)
    if n < k:
        raise ValueError(f"Line too short ({n} < {k}) to pick {k} digits.")
    drop = n - k
    stack = []
    for c in digits:
        while drop and stack and stack[-1] < c:
            stack.pop()
            drop -= 1
        stack.append(c)
    return ''.join(stack[:k])

def line_to_int_max(line: str, k: int) -> int:
    s = ''.join(ch for ch in line.strip() if ch.isdigit())
    if not s:
        return 0
    chosen = max_k_subsequence(s, k)
    return int(chosen)

def main(input_path="input.txt"):
    p = Path(input_path)
    if not p.exists():
        print(f"File not found: {input_path}")
        return

    total = 0
    per_line_results = []
    with p.open() as f:
        for i, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            try:
                val = line_to_int_max(line, K)
            except ValueError as e:
                print(f"Error on line {i}: {e}")
                return
            per_line_results.append((i, line, val))
            total += val

    for i, line, val in per_line_results:
        print(f"Line {i}: {line} -> {val}")
    print("\nTotal output joltage:", total)

if __name__ == "__main__":
    main()
