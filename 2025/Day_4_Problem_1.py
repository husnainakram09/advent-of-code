def count(input_text: str) -> int:
    grid = [list(line.rstrip()) for line in input_text.strip().splitlines() if line.strip() != '']
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            adj = 0
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == '@':
                    adj += 1

            if adj < 4:
                count += 1

    return count

def main():
    try:
        with open("input.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found. Create input.txt with your diagram and re-run.")
        return

    result = count(data)
    print("Accessible rolls of paper:", result)

if __name__ == "__main__":
    main()