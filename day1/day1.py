# Day 1 in Advent of Code

def sumCalories(caloriesList) -> int:
   total = 0
   for calories in caloriesList:
      total += calories

   return total

def rankCalories(pathToInput):
   with open(pathToInput, 'r') as file:
      lines = file.readlines()
   
   scores = [] # to sort
   caloriesList = []
   for line in lines:
      if line == "\n":  # empty line
         scores.append(sumCalories(caloriesList))
         caloriesList = []
      else:
         caloriesList.append(int(line))

   ranking = sorted(scores, reverse=True)
   return ranking

if __name__ == "__main__":
   ranking = rankCalories('input.txt')
   print('Top 1: ', ranking[0])
   print('Sum Top 3: ', sum(ranking[:3]))