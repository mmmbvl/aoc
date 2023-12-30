inp = open("input").readlines()
test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

class Lens():
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

    def has_same_label(self, other_lens):
        return self.label == other_lens.label
    
    def show(self):
        return "[" + self.label + " " + self.focal_length + "]"

class Box():
    def __init__(self):
        self.numLenses = 0
        self.lenses = []

    def addLens(self, lens):
        for i in range(len(self.lenses)):
            if self.lenses[i].has_same_label(lens):
                self.lenses[i] = lens
                return "replaced existing lens"
        self.numLenses += 1
        self.lenses.append(lens)
        return "added lens to end of box"

    def removeLens(self, label):
        p = -1
        for i in range(len(self.lenses)):
            if self.lenses[i].label == label:
                p = i
        if p != -1:
            self.numLenses -= 1
            return self.lenses.pop(p)
        return "none to remove"
    
    def show(self, box_num):
        show_string = "Box " + box_num + ":"
        for le in self.lenses:
            show_string += " " + le.show()
        show_string += " ----- numLenses: " + str(self.numLenses)
        print(show_string)

    def focusing_power(self, box_num):
        box_power = int(box_num) + 1
        fp = 0
        for i in range(len(self.lenses)):
            focal_len = int(self.lenses[i].focal_length)
            fp += box_power * focal_len * (i + 1)
        return fp
        


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
    
    if part == "P2":
        total = 0
        boxes = {}
        for str in all_strings:
            g = decompose(str)
            if g["operation"] == "-":
                if g["box_number"] in boxes:
                    boxes[g["box_number"]].removeLens(g["label"])
            else: #operation = "="
                new_lens = Lens(g["label"], g["focal_length"])
                if g["box_number"] in boxes:
                    boxes[g["box_number"]].addLens(new_lens)
                else: #new box
                    boxes[g["box_number"]] = Box()
                    boxes[g["box_number"]].addLens(new_lens)
            
            print("After ", str, ":")
            for bx in boxes.keys():
                boxes[bx].show(bx)


        for bx in boxes.keys():
            print("box focusing power", bx, "==> ", boxes[bx].focusing_power(bx))
            # print("num of lenses", boxes[bx].numLenses)
            total += boxes[bx].focusing_power(bx)
        print("P2: ", total)   

def decompose(term):
    lt = list(term)
    if "\n" in lt:
        lt.remove("\n")
    term = "".join(lt)
    print(lt, "-" in lt, "=" in lt, term.split("-")[0])
    if "-" in lt:
        lab = term.split("-")[0]
        return {
            "label": lab,
            "box_number": str(hashstr(lab)),
            "operation": "-"
        }
    else:
        lab = term.split("=")[0]
        return {
            "label": lab,
            "box_number": str(hashstr(lab)),
            "operation": "=",
            "focal_length": term[-1]
        }

solve(inp,"P2")
# print(hashstr("qp"))

# 519083 too high