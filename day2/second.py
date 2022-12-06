def getResult(match):
   if match[0] == 'A' and match[2] == 'X':
      return 4
   if match[0] == 'A' and match[2] == 'Y':
      return 8
   if match[0] == 'A' and match[2] == 'Z':
      return 3
   if match[0] == 'B' and match[2] == 'X':
      return 1
   if match[0] == 'B' and match[2] == 'Y':
      return 5
   if match[0] == 'B' and match[2] == 'Z':
      return 9
   if match[0] == 'C' and match[2] == 'X':
      return 7
   if match[0] == 'C' and match[2] == 'Y':
      return 2
   if match[0] == 'C' and match[2] == 'Z':
      return 6

def getHand(match) -> str:
   hands = ['X', 'Y', 'Z']
   elfHands = ['A', 'B', 'C']

   #draw
   if match[2] == 'Y':
      return hands[elfHands.index(match[0])]

   #loose
   if match[2] == 'X':
      index = elfHands.index(match[0]) - 1
      if index < 0:
         index = 2
      return hands[index]

   #win
   if match[2] == 'Z':
      index = elfHands.index(match[0]) + 1
      if index > 2:
         index = 0
      return hands[index]

def getScore(matches):
   score = 0
   for match in matches:
      newMatch = match[0] + " " + getHand(match)
      score += getResult(newMatch)

   return score

if __name__ == "__main__":
   with open('day2/input.txt', 'r') as file:
      matches = file.readlines()
   
   print('Score: ', getScore(matches))