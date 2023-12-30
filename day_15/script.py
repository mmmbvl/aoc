inp = open("input").readlines()
test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def hashstr(s):
    current_value = 0
    a = list(s)
    for c in a:
        if (c == "\n"):
            continue
        current_value += ord(c)
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value

def solve(inp, part):
    # all_strings = test.split(",")
    all_strings = inp[0].split(",")
    if part == "P1":
        total = 0
        for str in all_strings:
            total += hashstr(str)
        print("P1: ", total)

solve(inp,"P1")

# 519083 too high