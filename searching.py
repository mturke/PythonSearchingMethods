class SequentialStringList:
    def __init__(self):
        self.list = []

    def add(self, str):
        self.list.append(str)

    def find(self, str):
        for i in self.list:
            if i == str:
                return i

        return None
      
      
class BinaryStringList:
    def __init__(self):
        self.list = []
      
    def add(self,str):
        self.list.append(str)

    def find(self,str):
        self.list.sort()
        first = 0
        last = len(self.list)-1
        found = False

        while first <= last and not found:
            midpoint = (first + last )//2

            if self.list[midpoint] == str:              
                return self.list[midpoint]           
            else:
                if str < self.list[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        return found
