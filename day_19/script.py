inp = open("input").readlines()

sections = inp.split("\n\n")
workflows = []
parts = []


class Part():
    def __init__(self, x, m, a, s):
        self.props = {
            "x": x,
            "m": m,
            "a": a,
            "s": s
        }

class Flow():
    def __init__(self, target, minimum, maximum, success_target) -> None:
        self.target = target
        self.minimum = minimum
        self.maximum = maximum
        self.success_target = success_target

    def test_part(self, part):
        test_prop = part.props[self.target]
        if self.minimum != -1:
            if test_prop > self.minimum:
                return ["pass", self.success_target]
            else:
                return ["fail"]
        elif self.maximum != -1:
            if test_prop < self.maximum:
                return ["pass", self.success_target]
            else:
                return ["fail"]
        else:
            return ["invalid"]


class Workflow():
    def __init__(self, name):
        self.name = name
        self.flows = []

    def add_flow(self, flow):
        self.flows.append(flow)
        
    def route_part(self, part):
        self
    


for line in inp:
    section = "workflows"
    if line == "\n":
        section = "parts"

    if section == "workflows":
        x = line.split("{")
        name = x[0]
        dirs = x[1][:-2]

print(workflows, parts)