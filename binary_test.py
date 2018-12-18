import timeit

class BinaryStringList:

    def __init__(self):
        self.list = []
      
    def add(self, str):
        self.list.append(str)

    def find(self, str):
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


list = []    
string = BinaryStringList()
string.add('this')
string.add('program')
string.add('is')
string.add('looking')
string.add('to')
string.add('see')
string.add('if')
string.add('it')
string.add('can')
string.add('find')
string.add('the')
string.add('added')
string.add('word')
string.add('and')
string.add('see')
string.add('if')
string.add('its')
string.add('in')
string.add('the')
string.add('list')

t = timeit.timeit(BinaryStringList)
print(t)
print(" ")

print(" ")
time1 = timeit.timeit("string.find('added')", setup = "from __main__ import string", number = 1000)
print('String found: added')
print("Run time for found string:", time1)

print(" ")
time2 = timeit.timeit("string.find('python')", setup = "from __main__ import string", number = 1000)
print('String not found: python')
print("Run time for unfound string:", time2)


