# Advent of code, day 5

import re

class Stack:
   def __init__(self) -> None:
      self.crates = []

   def base(self, crate) -> None:
      self.crates.insert(0, crate)
   
   def put(self, crate) -> None:
      self.crates.append(crate)

   def putSome(self, some) -> None:
      self.crates += some

   def take(self) -> str:
      return self.crates.pop()

   def takeSome(self, number) -> list:
      token = []
      for i in range(number):
         token.insert(0, self.take())
      return token


class Rack:
   def __init__(self, lines):
      numberOfStacks = int(lines[-1][-3]) # char of the last number
      lines = lines[:-1] # remove base line
      self.stacks = [Stack() for i in range(numberOfStacks)]
      for line in lines:
         for i in range(numberOfStacks):
            charIndex = i * 4 + 1
            if line[charIndex] != " ":
               self.stacks[i].base(line[charIndex])

   def move(self, origin, destiny): # moves one crate
      origin = origin - 1
      destiny = destiny - 1
      self.stacks[destiny].put(self.stacks[origin].take())

   def moveSome(self, number, origin, destiny): # moves one crate
      origin = origin - 1
      destiny = destiny - 1
      self.stacks[destiny].putSome(self.stacks[origin].takeSome(number))

   def getTops(self) -> str:
      top = ""
      for stack in self.stacks:
         top += stack.crates[-1]
      return top



if __name__ == "__main__":
   with open("day5/input.txt") as file:
      lines = file.readlines()

   stackBase = re.compile(r"^[0-9|\s]+$")
   for i, line in enumerate(lines):
      if stackBase.search(line):
         breakLine = i + 1
         break
   
   initLines = lines[:breakLine]
   moveLines = lines[breakLine + 1:]

   rack = Rack(initLines)
   rack9001 = Rack(initLines)

   catchMovement = re.compile(r"move (\d+) from (\d+) to (\d+)")
   for line in moveLines:
      match = catchMovement.match(line)
      numberOfCrates = int(match.group(1))
      origin = int(match.group(2))
      destiny = int(match.group(3))

      for i in range(numberOfCrates):
         rack.move(origin, destiny)

      rack9001.moveSome(numberOfCrates, origin, destiny)

   print("Top crates are ", rack.getTops())
   print("Top crates for CrateMover 9001 are ", rack9001.getTops())