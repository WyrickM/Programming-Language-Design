import unittest
from HW4_part1 import *

# Grading rubric:
# lookup + define :  10 points
# add , sub, mul, eq, lt, gt, psAnd, psOr, psNot, dup, clear, exch, copy - 2 points each : total 26 points
# mark, length – 2 points each  - total 4 points
# counttomark, cleartomark -  4 points each : total 8 points
# get , getinterval – each 4 points : total 8 points
# put1,put2,putinterval1,putinterval2 – each 3 points : total 12 points
# dict, psDef, begin, end :  total 20 points
#
# additional unit tests : 5 points
# error checking : 7 points
#
# partial credit : up to 50%


class HW4Sampletests_part1(unittest.TestCase):
    #If the setUp doesn't clear the stacks succesfully, copy the following function to HW4_part1.py and call it in setup. 

    def setUp(self):
        #clear the opstack and the dictstack
        opstack [:] = []
        dictstack [:] = []

    def printTestInput(self, funcName, pts):
        # print("-------------------------")
        print("\n{funcName} - {pts} ".format(funcName=funcName, pts=pts))

    # Tests for helper functions : define, lookup
    def test_lookup1(self):
        self.printTestInput("lookup-1", '2 pts')
        dictPush({'/v':3, '/x': 20})
        dictPush({'/v':4, '/x': 10})
        dictPush({'/v':5})
        self.assertEqual(lookup('x'),10)
        self.assertEqual(lookup('v'),5)

    def testLookup2(self):
        self.printTestInput("lookup-2", '3 pts')
        dictPush({'/b':[4,5,1]})
        dictPush({'/a':355})
        dictPush({'/a':[3,5,5]})
        self.assertEqual(lookup("a"),[3,5,5])
        self.assertEqual(lookup("b"), [4,5,1])

    def test_define1(self):
        self.printTestInput("define-1", '1 pts')
        dictPush({})
        define("/n1", 10)
        dictPush({})
        dictPush({})
        self.assertEqual(lookup("n1"),10)

    def test_define2(self):
        self.printTestInput("define-2", '2 pts')
        dictPush({})
        define("/n1", 4)
        define("/n1", 5)
        define("/n1", 6)
        define("/n2", 6)
        self.assertEqual(lookup("n1"),6)
        self.assertEqual(lookup("n2"),6)        

    def test_define3(self):
        self.printTestInput("define-3", '2 pts')
        dictPush({})
        define("/n1", 4)
        dictPush({})
        define("/n2", 6)
        define("/n2", 7)
        dictPush({})
        define("/n1", 6)
        self.assertEqual(lookup("n1"),6)
        self.assertEqual(lookup("n2"),7)    
    #-----------------------------------------------------
    #Arithmatic operator tests
    def test_add(self):
        #9 3 add
        self.printTestInput("add", '2 pts')
        opPush(9)
        opPush(3)
        add()
        self.assertEqual(opPop(),12)

    def test_sub(self):
        #10 2 sub
        self.printTestInput("sub", '2 pts')
        opPush(2)
        opPush(10)
        sub()
        self.assertEqual(opPop(),-8)

    def test_mul(self):
        #2 40 mul
        self.printTestInput("mul", '2 pts')
        opPush(2)
        opPush(40)
        mul()
        self.assertEqual(opPop(),80)
    #-----------------------------------------------------
    #Comparison operators tests
    def test_eq(self):
        #[1 2 3 4] [4 3 2 1] eq
        self.printTestInput("eq", '2 pts')
        opPush([1,2,3,4])
        opPush([4,3,2,1])
        eq()
        self.assertEqual(opPop(),False)

    def test_lt(self):
        #3 6 lt
        self.printTestInput("lt", '2 pts')
        opPush(3)
        opPush(6)
        lt()
        self.assertEqual(opPop(),True)

    def test_gt(self):
        #4 5 gt
        self.printTestInput("gt", '2 pts')
        opPush(4)
        opPush(5)
        gt()
        self.assertEqual(opPop(),False)

    #-----------------------------------------------------
    #boolean operator tests
    def test_psAnd(self):
        self.printTestInput("psAnd", '2 pts')
        opPush(True)
        opPush(False)
        psAnd()
        self.assertEqual(opPop(),False)
        opPush(True)
        opPush(True)
        psAnd()
        self.assertEqual(opPop(),True)

    def test_psOr(self):
        self.printTestInput("psOr", '2 pts')
        opPush(True)
        opPush(False)
        psOr()
        self.assertEqual(opPop(),True)
        opPush(False)
        opPush(False)
        psOr()
        self.assertEqual(opPop(),False)

    def test_psNot(self):
        self.printTestInput("psNot", '2 pts')
        opPush(True)
        psNot()
        self.assertEqual(opPop(),False)
        opPush(False)
        psNot()
        self.assertEqual(opPop(),True)
    #-----------------------------------------------------
    #stack manipulation operator tests
    def test_dup(self):
        self.printTestInput("dup", '2 pts')
        #[3 5 5 True 4]  dup
        opPush([3,5,5,True,4])
        dup()
        isSame = opPop() is opPop()
        self.assertTrue(isSame)

    def test_exch(self):
        # /x 10 exch
        self.printTestInput("exch", '2 pts')
        opPush('/x')
        opPush(10)
        exch()
        self.assertEqual(opPop(),'/x')
        self.assertEqual(opPop(),10)

    def test_copy(self):
        #true 1 3 4 3 copy
        self.printTestInput("copy", '2 pts')
        opPush(True)
        opPush(1)
        opPush(3)
        opPush(4)
        opPush(3)
        copy()
        self.assertTrue(opPop()==4 and opPop()==3 and opPop()==1 and opPop()==4 and opPop()==3 and opPop()==1 and opPop()==True)
        
    def test_clear(self):
        #10 /x clear
        self.printTestInput("clear", '2 pts')
        opPush(10)
        opPush("/x")
        clear()
        self.assertEqual(len(opstack),0)

    def test_mark(self):
        # 1 2 3 mark 10
        self.printTestInput("mark", '2 pts')
        opPush(1)
        opPush(2)
        opPush(3)
        mark()
        opPush(10)
        print(opstack)
        pop()
        self.assertEqual(opPop(),'-mark-')

    def test_counttomark(self):
        # 1 2 3 mark 10 20 30 40 mark 50 counttomark
        self.printTestInput("copy", '4 pts')
        opPush(1)
        opPush(2)
        opPush(3)
        mark()
        opPush(10)
        opPush(20)
        opPush(30)
        opPush(40)
        mark()
        opPush(50)
        counttomark()
        self.assertEqual(opPop(),1)
        pop() # pop 50 
        pop() # pop -mark-
        counttomark() 
        self.assertEqual(opPop(),4)
        self.assertTrue(opPop()==40 and opPop()==30 and opPop()==20 and opPop()==10 and opPop()=='-mark-' and opPop()==3 and opPop()==2 and opPop()==1)    

    def test_cleartomark(self):
        # 1 2 3 mark 10 20 30 40 mark 50 cleartomark
        self.printTestInput("copy", '4 pts')
        opPush(1)
        opPush(2)
        opPush(3)
        mark()
        opPush(10)
        opPush(20)
        opPush(30)
        opPush(40)
        mark()
        opPush(50)
        cleartomark()
        self.assertEqual(opPop(),40)
        cleartomark() 
        self.assertTrue(opPop()==3 and opPop()==2 and opPop()==1)   

    #-----------------------------------------------------
    #Array operator tests
    def test_length(self):
        #[3 5 5 True 4] length
        self.printTestInput("length", '2 pts')
        opPush([3,5,5,True,4])
        length()
        self.assertEqual(opPop(),5)      
        self.assertTrue(len(opstack)==0)        

    def test_get(self):
        #[3 5 5 True 4] 3 get
        self.printTestInput("get", '4 pts')
        opPush([3,5,5,True,4])
        opPush(3)
        get()
        self.assertEqual(opPop(),True)
        self.assertTrue(len(opstack)==0)
    
    def test_getinterval(self):
        #[3 5 5 True 4] 3 get
        self.printTestInput("getinterval", '4 pts')
        opPush([4,5,3,5,5,True,4])
        opPush(2)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),[3,5,5])         
        self.assertTrue(len(opstack)==0)        

    def test_put1(self):
        #/x [3 5 5 True 4] def  x 2 0 put x
        self.printTestInput("put1", '3 pts')
        x = [3,5,5,True,4]
        define('/x',x)
        opPush(x) #pushing the array reference onto the stack
        dup()
        opPush(2)
        opPush(0)
        put()  #put will not push back the changed array
        self.assertEqual(lookup('x'),[3,5,0,True,4]) #we pop the array reference we bound to name /x     
        self.assertEqual(opPop(), [3, 5, 0, True, 4])
        self.assertTrue(len(opstack)==0)

    def test_put2(self):
        #[3 5 5 True 4] dup /x exch def 2 0 put x
        self.printTestInput("put2", '3 pts')
        opPush([3,5,5,True,4])
        dup()
        opPush('/x')
        exch()
        psDef()
        opPush(2)
        opPush(0)
        put()
        self.assertEqual(lookup('x'),[3,5,0,True,4])      
        self.assertTrue(len(opstack)==0)

    def test_putinterval1(self):
        self.printTestInput("putInterval-1", '3 pts')
        opPush([0,1,3,5,5,True,4])
        dup() # we duplicate the array reference
        opPush(2)
        opPush([4,5,1,0])
        putinterval()
        self.assertEqual(opPop(),[0,1,4,5,1,0,4])
        self.assertTrue(len(opstack)==0)

    def test_putinterval2(self):
        self.printTestInput("putInterval-2", '3 pts')
        define('/a',[0,1,3,5,5,True,4])
        opPush(lookup('a'))
        opPush(lookup('a'))
        dup()
        opPush(5)
        opPush([False])
        putinterval()
        self.assertEqual(opPop(),[0,1,3,5,5,False,4])
        self.assertEqual(opPop(), [0, 1, 3, 5, 5, False, 4])
        self.assertTrue(len(opstack)==0)

    #dictionary stack operators
    def test_dict(self):
        #1 dict
        self.printTestInput("dict", '1 pts')
        opPush(1)
        psDict()
        self.assertEqual(opPop(),{})

    def test_psDef1(self):
        #/x 10 def /x 20 def x
        self.printTestInput("psDef-1", '2 pts')
        dictPush({})
        opPush("/x")
        opPush(10)
        psDef()
        opPush("/x")
        opPush(20)
        psDef()
        self.assertEqual(lookup('x'),20)

    def test_psDef2(self):
        #/x 10 def 1 dict begin /y 20 def x
        self.printTestInput("psDef-2", '4 pts')
        dictPush({})
        opPush("/x")
        opPush(10)
        psDef()
        dictPush({})
        opPush("/y")
        opPush(20)
        psDef()
        self.assertEqual(lookup('x'),10)

    def test_psDef3(self):
        #/x 3 def 1 dict begin /x 30 def 1 dict begin /x 300 def end x
        # define x in the bottom dictionary
        self.printTestInput("psDef-3", '4 pts')
        dictPush({})
        opPush("/x")
        opPush(3)
        psDef()
        # define x in the second dictionary
        dictPush({})
        opPush("/x")
        opPush(30)
        psDef()
        # define x in the third dictionary
        dictPush({})
        opPush("/x")
        opPush(300)
        psDef()
        dictPop()
        self.assertEqual(lookup('x'),30)

    def test_beginEnd1(self):
        # /x 3 def 1 dict begin /x 4 def end x
        self.printTestInput("begin-1", '4 pts')
        opPush(1)
        psDict()
        opPush("/x")
        opPush(3)
        psDef()
        opPush(1)
        psDict()
        begin()
        opPush("/x")
        opPush(4)
        psDef()
        end()
        self.assertEqual(lookup('x'), 3)

    def test_beginEnd2(self):
        # /x 3 def 1 dict begin /x 4 def end x
        self.printTestInput("begin-2", '5 pts')
        opPush("/y")
        opPush(3)
        psDef()
        opPush("/z")
        opPush(lookup('y'))
        psDef()
        opPush(1)
        psDict()
        begin()
        opPush("/z")
        opPush(4)
        psDef()
        opPush("/y")
        opPush(5)
        psDef()
        opPush(lookup('z'))
        opPush(lookup('y'))
        mul()
        end()
        opPush(lookup('y'))
        mul()
        self.assertEqual(opPop(), 60)
        self.assertEqual(lookup('y'), 3)
        self.assertEqual(lookup('z'), 3)


            #Tests to check "error checking"

    # # (4 pts) Make sure that the following test prints/raises an error message about the type of the second argument
    # #  Also make sure that the opstack content is : ['/x', 10]
    # def test_divInputs(self):
    #     opPush(10)
    #     opPush("/x")
    #     sub()
    #     print(opstack)

    # # Make sure that the following test prints/raises an error message about the type of the first argument (the variable name needs be a string)
    # # 4 pts
    # def test_psDefInputs(self):
    #     opPush(1)
    #     opPush(10)
    #     psDef()
    #     print(opstack)


if __name__ == '__main__':
    unittest.main()

