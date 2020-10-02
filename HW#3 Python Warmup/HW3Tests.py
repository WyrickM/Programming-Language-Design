import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        pass
    def test_sumSales(self):
        salesLog= {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
        summedLog = {'Fri': 30, 'Mon': 80, 'Sat': 220, 'Thu': 80, 'Tue': 180, 'Wed': 225}
        self.assertDictEqual(sumSales(salesLog),summedLog)

        #Test 2
        salesLogTest2 = {'Amazon': {}, 'Etsy': {}, 'Ebay': {}, 'Shopify': {}}
        summedLogTest2 = {}
        self.assertDictEqual(sumSales(salesLogTest2), summedLogTest2)

        #Test 3
        salesLogTest3 = {'Amazon': {'Mon': -10}, 'Etsy': {'Tue': -30},
                         'Ebay': {'Tue': 10}, 'Shopify': {}}
        summedLogTest3 = {'Mon': -10, 'Tue': -20}
        self.assertDictEqual(sumSales(salesLogTest3), summedLogTest3)

    def test_sumSalesN(self):
        salesLogN = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':245,'Sat':285,'Sun': 88,'Thu': 120,'Tue':180,'Wed':225}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)

        #Test 2
        salesLogNTest2 = [
            {'Amazon': {}, 'Etsy': {}, 'Ebay': {}, 'Shopify': {}},
            {'Shopify': {}, 'Etsy': {}, 'Ebay': {}},
            {'Amazon': {}, 'Etsy': {}, 'Ebay': {}, 'Shopify': {}}]
        summedLogNTest2 = {}
        self.assertDictEqual(sumSalesN(salesLogNTest2), summedLogNTest2)

        #Test 3
        salesLogNTest3 = [{'Amazon':{'Mon': 30}},{}]
        summedLogNTest3 = {'Mon': 30}
        self.assertDictEqual(sumSalesN(salesLogNTest3), summedLogNTest3)

        # Test 4
        salesLogNTest4 = []
        summedLogNTest4 = {}
        self.assertDictEqual(sumSalesN(salesLogNTest4), summedLogNTest4)

    def test_searchDicts(self):
        #searchDicts inputs
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        self.assertEqual(searchDicts(dictList,"y"),False)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),None)

        #Test 2
        dictListTest2 = [{}]
        self.assertEqual(searchDicts(dictListTest2, 1), None)
        self.assertEqual(searchDicts(dictListTest2, None), None)
        self.assertEqual(searchDicts(dictListTest2, 'a'), None)

        #Test 3
        dictList3 = [{1: 'a', 2:'b'}, {1: 'c', 2:'d'}, {'a': 1, 'b': 2}]
        self.assertEqual(searchDicts(dictList3, 1), 'c')
        self.assertEqual(searchDicts(dictList3, 2), 'd')
        self.assertEqual(searchDicts(dictList3, 'a'), 1)
        self.assertEqual(searchDicts(dictList3, 'c'), None)

    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"t"),None)

        #Test 2
        dictList2Test2 = [(0, {}), (0, {}), (1, {}),
                     (2, {}), (3, {})]
        self.assertEqual(searchDicts2(dictList2Test2, "x"), None)
        self.assertEqual(searchDicts2(dictList2Test2, 2), None)
        self.assertEqual(searchDicts2(dictList2Test2, 3), None)
        #Test 3
        dictList2Test3 = [(0, {1: 'a', 'a': 1, 2: 'b'}), (3, {4: 2, 5: '1'}), (0, {(1,2): 3}),
                          (2, {2: 'a'}), (1, {'3': 'x', 9: 11, 100: 101})]
        self.assertEqual(searchDicts2(dictList2Test3, 100), 101)
        self.assertEqual(searchDicts2(dictList2Test3, (1,2)), 3)
        self.assertEqual(searchDicts2(dictList2Test3, 2), 'a')
        self.assertEqual(searchDicts2(dictList2Test3, 'x'), None)

    def test_busStops(self):
        routes = {
            "Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
            "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
            "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
            "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
            "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
        }
        self.assertEqual(busStops(routes,"Stadium"),['Lentil', 'Silver', 'Gray'])
        self.assertEqual(busStops(routes,"Bishop"),['Lentil', 'Wheat', 'Silver'])
        self.assertEqual(busStops(routes,"EECS"),[])

        #Test #2
        test2Dict = {1: [2,3,4,5,6,7,8,9,10,11], 2: [4,6,8,10], 3: [3,6,9,12,15], 4: [8,12,16,18]}
        self.assertEqual(busStops(test2Dict, 8), [1,2,4])
        self.assertEqual(busStops(test2Dict, 3), [1,3])
        self.assertEqual(busStops(test2Dict, 1), [])

        #Test #3
        test3Dict = {}
        self.assertEqual(busStops(test3Dict, 1), [])
        self.assertEqual(busStops(test3Dict, 'a'), [])
        self.assertEqual(busStops(test3Dict, None), [])

    def test_palindromes(self):
        self.assertEqual(palindromes ('cabbbaccab'),['abbba', 'acca', 'baccab', 'bb', 'bbb', 'cabbbac', 'cc'] )
        self.assertEqual(palindromes ('bacdcabdbacdc') ,['abdba', 'acdca', 'bacdcab', 'bdb', 'cabdbac', 'cdc', 'cdcabdbacdc', 'dcabdbacd'])
        self.assertEqual(palindromes (' myracecars')  ,['aceca', 'cec', 'racecar'])

        #Test #2 and #3
        self.assertEqual(palindromes(''),[])
        self.assertEqual(palindromes('a'),[])
        self.assertEqual(palindromes('aaa'), ['aa', 'aaa'])
        self.assertEqual(palindromes('MOM'), ['MOM'])
        self.assertEqual(palindromes('MOMmom'), ['MOM', 'mom'])



    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    #This function assumes that the first value in L is less than or equal to N.
    def getUntilN(self,L,N):
        tempL = []
        for item in L:
            tempL.append(item)
            if item>=N: break
        return tempL

    def test_interlaceIter(self):
    	#test 1
        iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(iSequence.__next__(),1)
        self.assertEqual(iSequence.__next__(),'a')
        self.assertEqual(iSequence.__next__(),2)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['b',3,'c',4,'d',5,'e',6,'f',7,'g'])

        #test2
        naturals = interlaceIter(self.OddsEvens(1),self.OddsEvens(2))
        self.assertEqual(naturals.__next__(),1)
        first20 = self.getUntilN(naturals,20)
        self.assertEqual(first20,[x for x in range(2,21)])
        self.assertEqual(naturals.__next__(),21)

        # Test 3
        iSequenceTest3 = interlaceIter(iter([(1,2),(3,4),(5,6)]),iter('123456'))
        self.assertEqual(iSequenceTest3.__next__(), (1,2))
        self.assertEqual(iSequenceTest3.__next__(), '1')
        test3List = []
        for element in iSequenceTest3:
            test3List.append(element)
        self.assertEqual(test3List, [(3,4), '2', (5,6)])

        # Test 4
        iSequenceTest4 = interlaceIter(iter([1,2,3]), iter([0,1,2,3,4,5]))
        self.assertEqual(iSequenceTest4.__next__(), 1)
        self.assertEqual(iSequenceTest4.__next__(), 0)
        test4List = []
        for element in iSequenceTest4:
            test4List.append(element)
        self.assertEqual(test4List, [2,1,3])

    def test_typeHistogram(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('str', 3), ('int', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 2), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [])
        #test 2
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequence2 = interlaceIter(iSequence1, iter([(1,'a'),(2,'b'),(3,'c'),(4,'d')]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)),sorted([('int', 2), ('str', 2),('tuple',4)]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)), [])

        # Test 3
        iSequenceTest3 = interlaceIter(iter([(1,2),(3,4),(5,6)]),iter('123456'))
        self.assertEqual(sorted(typeHistogram(iSequenceTest3,1)), sorted([('tuple',1)]))
        self.assertEqual(sorted(typeHistogram(iSequenceTest3,1)), sorted([('str',1)]))
        self.assertEqual(sorted(typeHistogram(iSequenceTest3,2)), sorted([('tuple',1), ('str', 1)]))
        self.assertEqual(sorted(typeHistogram(iSequenceTest3,5)), sorted([('tuple',1)]))

        # Test 4
        iSequenceTest4 = interlaceIter(iter([1, 2, 3, 4, 5, 6]), iter([0, 1, 2, 3, 4, 5]))
        self.assertEqual(sorted(typeHistogram(iSequenceTest4, 2)), sorted([('int', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequenceTest4, 4)), sorted([('int', 4)]))
        self.assertEqual(sorted(typeHistogram(iSequenceTest4, 10)), sorted([('int', 5)]))

if __name__ == '__main__':
    unittest.main()

