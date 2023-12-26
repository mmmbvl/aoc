inp = open("input").readlines()

sum = 0

def nextVal(arr):
    allZeroes = True
    for i in arr:
        if i != 0:
            allZeroes = False
    
    if allZeroes:
        print(arr, " ===== ", 0)
        return 0
    else:
        subtArr = []
        for (i,x) in enumerate(arr):
            if i > 0:
                subtArr.append(arr[i] - arr[i - 1])
        g = nextVal(subtArr)
        print(arr, " ===== ", arr[-1] + g)
        return arr[-1] + g

for line in inp:
    parsedLine = list(map(lambda x : int(x), line.split(" ")))
    sum += nextVal(parsedLine)

print("P1: ", sum)