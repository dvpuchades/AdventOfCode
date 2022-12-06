# day 6 at advent of code :0

def getPacketMarker(datastream):
   for i in range(len(datastream)):
      if (i > 3) and areAllDifferent(datastream[i - 4:i]):
         return i

def getMessageMarker(datastream):
   for i in range(len(datastream)):
      if (i > 13) and areAllDifferent(datastream[i - 14:i]):
         return i

def areAllDifferent(substring):
   if substring == '':
      return False
   checked = []
   for char in substring:
      if char in checked:
         return False
      checked.append(char)
   return True

if __name__ == "__main__":
   with open("day6/input.txt", 'r') as file:
      datastream = file.readline()

   print("Packet Marker at ", getPacketMarker(datastream))
   print("Packet Marker at ", getMessageMarker(datastream))