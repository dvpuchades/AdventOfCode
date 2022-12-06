# Day 2 in advent of code

class Hand:
   def __init__(self, letter) -> None:
      self.letter = letter
      self.score = {'A': 1, 'B': 2, 'C': 3}[letter]

   def __eq__(self, other) -> bool:
      return self.letter == other.letter

   def __lt__(self, other) -> bool:
      if other.letter == 'A' and self.letter == 'C':
         return True
      return self.letter < other.letter

def getRoundScore(yourHand, elfHand) -> int:
   if elfHand == yourHand:
      return 3
   if yourHand < elfHand:
      return 0

   return 6

def getScore(matches):
   ## ELF Hands
   # A Rock
   # B Paper
   # C Scissors
   handTranslator = {
      'X':'A',
      'Y':'B',
      'Z':'C'
   }

   score = 0
   for match in matches:
      elfHand = Hand(match[0])
      yourHand = Hand(handTranslator[match[2]])
      score += getRoundScore(yourHand, elfHand) + yourHand.score
   return score

if __name__ == "__main__":
   with open('day2/input.txt', 'r') as file:
      matches = file.readlines()
   
   print('Score: ', getScore(matches))