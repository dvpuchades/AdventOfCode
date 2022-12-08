# Day 8 - Advent of code 

def getForest(lines):
    # lines = lines[:-1] # remove blank line at the end
    forest = [[] for i in range(len(lines[0][:-1]))]
    idNumber = 0
    for i, line in enumerate(lines):
        line = line[:-1] # remove break line
        for digit in line:
            forest[i].append({"id": idNumber, "height": int(digit)})
            idNumber += 1
    return forest

def  getVisibleTree(lane) -> list:
    max = -1
    visible = []
    for tree in lane:
        if tree["height"] == 9:
            visible.append(tree["id"])
            break
        if tree["height"] > max:
            max = tree["height"]
            visible.append(tree["id"])
    return visible

def getVisibleBySide(lanes):
    visible = []
    for lane in lanes:
        visible += getVisibleTree(lane)
    return visible

def translateIndex(oi, oj, deepth):
    deepth -= 1 # first index is 0
    return {"i": (deepth - oj), "j": oi}

def rotateForest(forest):
    rotated = [[] for i in range(len(forest))]
    for i, lane in enumerate(forest):
        for j, tree in enumerate(lane):
            newIndex = translateIndex(i, j, len(forest))
            rotated[newIndex["i"]].append(tree)
    return rotated

def getVisibleInForest(forest):
    visible = []
    for i in range(4):
        visibleInForest = getVisibleBySide(forest)
        treesToAdd = [tree for tree in visibleInForest if tree not in visible]
        visible += treesToAdd
        forest = rotateForest(forest)
    return visible

if __name__ == "__main__":
    with open("input2.txt", "r") as file:
        forest = getForest(file.readlines())
    print("Number of visible trees", len(getVisibleInForest(forest)))