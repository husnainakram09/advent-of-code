def count_all_clicks(lines):
    pos = 50
    total = 0
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        dirc = s[0].upper()
        d = int(s[1:])  
        p = pos  
        if dirc == 'R':
            k0 = (100 - p) % 100
        else: 
            k0 = p % 100

        if k0 == 0:
            k0 = 100  
            
        if k0 <= d:
            hits = 1 + (d - k0) // 100
            total += hits

        if dirc == 'R':
            pos = (pos + d) % 100
        else:
            pos = (pos - d) % 100

    return total

def read_input(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == "__main__":
    lines = read_input("input.txt")
    part2 = count_all_clicks(lines)
    print("Part 2: ", part2)
