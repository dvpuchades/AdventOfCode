# day 7 in advent of code :*

import os
import re


class FileSystem:
   def __init__(self):
      self.files = {} # path : storage
      self.pwd = ''

   def cd(self, dir):
      if dir == '/':
         self.pwd = ''
      elif dir == '..':
         self.pwd = os.path.dirname(self.pwd)
         if self.pwd ==  '/':
            self.pwd = ''
      else:
         self.pwd += '/' + dir

   def ls(self, element):
      # get only files
      fileFilter = re.compile(r"\d+ .+")
      if fileFilter.match(element):
         data = element.split()
         self.files[self.pwd + '/' + data[1]] = int(data[0])

   def du(self):
      directories = {}
      for file in self.files:
         dir = 'root' + os.path.dirname(file)
         folders = dir.split('/')
         folders = [element for element in folders if element != '']
         dir = ''
         for folder in folders:
            dir += '/' + folder
            if directories.get(dir) is not None:
               directories[dir] += self.files[file]
            else:
               directories[dir] = self.files[file]
      return directories


def readLog(log):
   system = FileSystem()
   for line in log:
      line = line[:-1] # remove the breakline
      if '$ cd' in line:
         system.cd(line[5:])
      if not '$' in line:
         system.ls(line)
   return system

def sumUnder(fileSystem, under=100000):
   directories = fileSystem.du()
   sum = 0
   for dir in directories:
      if directories[dir] < under:
         sum += directories[dir]
   return sum

def getSmallestToUpdate(fileSystem):
   directories = fileSystem.du()
   spaceNeeded = 30000000 - (70000000 - directories["/root"])
   minDir = ''
   min = directories["/root"]
   for dir in directories:
      if (directories[dir] < min) and (directories[dir] > spaceNeeded):
         min = directories[dir]
         minDir = dir
   return min

if __name__ == "__main__":
   with open('day7/input.txt', 'r') as file:
      log = file.readlines()
   
   fileSystem = readLog(log)
   print("Directories under 10000 sum", sumUnder(fileSystem))
   print("Directory to erase will free ", getSmallestToUpdate(fileSystem))