import timeit

class SequentialStringList:

    def __init__(self):
        self.list=[]

    def add(self,str):
        self.list.append(str)

    def find(self,str):
        for i in self.list:
            if i == str:
                return i
        return None


list = []    
string = SequentialStringList()
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

t = timeit.timeit(SequentialStringList)
print(t)
print(" ")

print(" ")
time1 = timeit.timeit("string.find('looking')", setup = "from __main__ import string", number = 1000)
print('String found: looking')
print("Run time for found string:", time1)

print(" ")
time2 = timeit.timeit("string.find('array')", setup = "from __main__ import string", number = 1000)
print('String not found: array')
print("Run time for unfound string:", time2)



