def compute_password(lines):
    pos = 50
    count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            pos = (pos - distance) % 100
        else:
            pos = (pos + distance) % 100

        if pos == 0:
            count += 1

    return count

def read_input(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == "__main__":
    lines = read_input("input.txt")
    password = compute_password(lines)
    print("Password: ", password)
