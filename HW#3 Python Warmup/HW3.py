#
# Mantz Wyrick
# 3/13/2020
# Homework #3
# Python Warm-up
#
# Need to go back to assignment outline and include what all of the functions do
#

from functools import reduce

debugging = True
def debug(*s):
    if debugging:
        print(*s)
#debug("This is my debugging output", x, y)

# #1 (Dictionaries)
# a) sumSales
salesList = {'Amazon':{'Mon':30, 'Wed': 100, 'Sat': 200},
 'Etsy':{'Mon':50, 'Tue':20, 'Wed':25, 'Fri':30},
 'Ebay':{'Tue':60, 'Wed':100,'Thu':30},
 'Shopify':{'Tue':100,'Thu':50, 'Sat':20}}

def sumSales(d):
    storeDays = {}
    answer = {}
    for store in d:
        storeDays = d.get(store, 0)
        for days in storeDays:
            answer[days] = storeDays.get(days, 0) + answer.get(days, 0)
    return answer

weeklySales = [
    {'Amazon':{'Mon':30,'Wed':100,'Sat':200},
     'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},
     'Ebay':{'Tue':60,'Wed':100,'Thu':30},
     'Shopify':{'Tue':100,'Thu':50,'Sat':20}},
    {'Shopify':{'Mon':25},
     'Etsy':{'Thu':40, 'Fri':50},
     'Ebay':{'Mon':100,'Sat':30}},
    {'Amazon':{'Sun':88},
     'Etsy':{'Fri':55},
     'Ebay':{'Mon':40},
     'Shopify':{'Sat':35}}
]
# b) sumSalesN
# function should use python map,reduce,sumSales,
# and an additional helper function to combine dictionaries
def sumSalesN (L):
    answer = {}
    listTemp = []
    listTemp = list(map(sumSales, L))
    for n in listTemp:
        for days in n:
            answer[days] = (reduce(lambda x, y: answer.get(days, 0) + n.get(days, 0), listTemp))
    return answer

# 2. (Dictionaries and Lists)
L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
# a) searchDicts
def searchDicts(L, k):
    answer = {}
    L = reversed(L)
    for index in L:
        for item in index:
            answer[item] = index.get(item,0)
            if item == k:
                return answer[item]


L2 = [(0,{"x":0,"y":True,"z":"zero"}),
 (0,{"x":1}),
 (1,{"y":False}),
 (1,{"x":3, "z":"three"}),
 (2,{})]
# b) searchDicts2(tL, k)
def search2Helper(tL,k,index):
    if index == 0:
        elem = tL[index]
        dict = elem[1]
        for key in dict:
            if key == k:
                value = dict.get(key, 0)
                return value
        value = None
        return value
    else:
        elem = tL[index]
        dict = elem[1]
        for key in dict:
            if key == k:
                value = dict.get(key,0)
                return value
        next = elem[0]
        return search2Helper(tL,k,next)

def searchDicts2(tL, k):
    answer = search2Helper(tL, k, -1)
    return answer

routes = {
"Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main",
"Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop",
"Derby", "Dilke"],
"Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay",
"Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
"Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco",
"RockeyWay"],
"Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell",
"Chinook", "Library"],
"Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall",
"Stadium", "Colorado"]
}
# 3. (List Comprehension)
# busStops(buses, stop)
def busStops(buses, stop):
    answer = [bus for bus in buses for elem in buses[bus] if elem == stop]
    return answer
# for elem in b if elem == stop
# def busStopsEx(buses, stop):
#     answer = []
#     for b in buses:
#         bus = buses.get(b, 0)
#         for stops in bus:
#             if stop == stops:
#                 answer.append(b)
#     return answer
# print(busStops(routes,"Stadium"))

# 4. (Lists)
# palindromes(s)

def palindromes(S):
    answer = []
    word = []
    test = list(S)
    wordReverse = []
    final = ''
    num = 0
    for letter in S:
        word.clear()
        word.append(test.pop(test.index(letter)))
        for second in test:
            word.append(second)
            wordReverse = word.copy()
            wordReverse.reverse()
            if word == wordReverse:
                for elem in word:
                    final += elem
                for index in answer:
                    if index == final:
                        num += 1
                if num == 0:
                    answer.append(final)
                num = 0
                final = ''
    answer.sort()
    return answer

# 5. Iterators
# a) interlaceIter()
class interlaceIter(object):
    def __init__(self, firstIt, secondIt):
        self.interchange = 0
        self.firstIt = firstIt
        try:
            self.current1 = self.firstIt.__next__()
        except:
            self.current1 = None
        self.secondIt = secondIt
        try:
            self.current2 = self.secondIt.__next__()
        except:
            self.current2 = None
    def __next__(self):
        if (self.interchange % 2) == 0:
            if (self.current1 is None) or (self.current2 is None):
                raise StopIteration
            result = self.current1
            self.interchange += 1
            try:
                self.current1 = self.firstIt.__next__()
            except:
                self.current1 = None
            return result
        elif (self.interchange % 2) == 1:
            if (self.current1 is None) or (self.current2 is None):
                raise StopIteration
            result = self.current2
            self.interchange += 1
            try:
                self.current2 = self.secondIt.__next__()
            except:
                self.current2 = None
            return result
    def __iter__(self):
        return self


# b) typeHistogram(it, n)
def typeHistogram(it, n):
    dict1 = {}
    list1 = []
    index = 0
    while index < n:
        try:
            list1.append(it.__next__())
        except:
            break
        index += 1
    for elem in list1:
        dict1[type(elem).__name__] = dict1.get(type(elem).__name__, 0) + 1
    answer = list(dict1.items())
    return answer

# print(typeHistogram(iSequence,5)) # returns [('int', 3), ('str', 2)])
# print(typeHistogram(iSequence,5)) # returns [('str', 3), ('int', 2)])
# print(typeHistogram(iSequence,5)) # returns [('int', 2), ('str', 2)])
# print(typeHistogram(iSequence,5)) # returns [])
# iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
#
# iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
# iSequence2 = interlaceIter(iSequence, iter([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]))

# print(iSequence.__next__())
# print(iSequence.__next__())
# print(iSequence.__next__())
# print(iSequence.__next__())
# print(iSequence.__next__())
# for item in iSequence:
#     print(item)

if __name__ == "__main__":
    L2 = [(0, {"x": 0, "y": True, "z": "zero"}),
          (0, {"x": 1}),
          (1, {"y": False}),
          (0, {"x": 3, "z": "three"}),
          (1, {})]
    print(searchDicts2(L2, "z"))