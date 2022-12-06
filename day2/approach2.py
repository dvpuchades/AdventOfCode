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

def getScore(matches):
   score = 0
   for match in matches:
      score += getResult(match)

   return score

if __name__ == "__main__":
   with open('day2/input.txt', 'r') as file:
      matches = file.readlines()
   
   print('Score: ', getScore(matches))