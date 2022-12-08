def getScore(i, j, forest):
    return getScoreToRight(forest[i][j], i, j, forest) * getScoreToLeft(forest[i][j], i, j, forest) * getScoreToUp(forest[i][j], i, j, forest) * getScoreToDown(forest[i][j], i, j, forest)

def getScoreToRight(originalValue, i, j, forest):
    if j == (len(forest[i]) - 1):
        return 0
    if originalValue > forest[i][j + 1]:
        return 1 + getScoreToRight(originalValue, i, j + 1, forest)
    else:
        return 1

def getScoreToLeft(originalValue, i, j, forest):
    if j == 0:
        return 0
    if originalValue > forest[i][j - 1]:
        return 1 + getScoreToLeft(originalValue, i, j - 1, forest)
    else:
        return 1

def getScoreToUp(originalValue, i, j, forest):
    if i == 0:
        return 0
    if originalValue > forest[i - 1][j]:
        return 1 + getScoreToUp(originalValue, i - 1, j, forest)
    else:
        return 1

def getScoreToDown(originalValue, i, j, forest):
    if i == (len(forest) - 1):
        return 0
    if originalValue > forest[i + 1][j]:
        return 1 + getScoreToDown(originalValue, i + 1, j, forest)
    else:
        return 1

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.readlines()

    forest = [[int(char) for char in line[:-1]] for line in input]

    bestScore = 0
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            score = getScore(i, j, forest)
            if score > bestScore:
                bestScore = score
    
    print("Best score is", bestScore)