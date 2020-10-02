import unittest
from HW4_part1 import *

class HW4Sampletests_part1(unittest.TestCase):
    #If the setUp doesn't clear the stacks succesfully, copy the following function to HW4_part1.py and call it in setup. 

    def setUp(self):
        #clear the opstack and the dictstack
        opstack [:] = []
        dictstack [:] = []  
    # Tests for helper functions : define, lookup   
    def test_lookup1(self):
        dictPush({'/v':3, '/x': 20})
        dictPush({'/v':4, '/x': 10})
        dictPush({'/v':5})
        self.assertEqual(lookup('x'),10)
        self.assertEqual(lookup('v'),5)

    def testLookup2(self):
        dictPush({'/a':355})
        dictPush({'/a':[3,5,5]})
        self.assertEqual(lookup("a"),[3,5,5])

    def test_define1(self):
        dictPush({})
        define("/n1", 4)
        self.assertEqual(lookup("n1"),4)

    def test_define2(self):
        dictPush({})
        define("/n1", 4)
        define("/n1", 5)
        define("/n2", 6)
        self.assertEqual(lookup("n1"),5)
        self.assertEqual(lookup("n2"),6)        

    def test_define3(self):
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
        opPush(9)
        opPush(3)
        add()
        self.assertEqual(opPop(),12)

    def test_sub(self):
        #10 2 sub
        opPush(10)
        opPush(2)
        sub()
        self.assertEqual(opPop(),8)

    def test_mul(self):
        #2 40 mul
        opPush(2)
        opPush(40)
        mul()
        self.assertEqual(opPop(),80)
    #-----------------------------------------------------
    #Comparison operators tests
    def test_eq1(self):
        #6 6 eq
        opPush(6)
        opPush(6)
        eq()
        self.assertEqual(opPop(),True)

    def test_eq2(self):
        #[1 2 3 4] [4 3 2 1] eq
        opPush([1,2,3,4])
        opPush([4,3,2,1])
        eq()
        self.assertEqual(opPop(),False)

    def test_lt(self):
        #3 6 lt
        opPush(3)
        opPush(6)
        lt()
        self.assertEqual(opPop(),True)

    def test_gt(self):
        #4 5 gt
        opPush(4)
        opPush(5)
        gt()
        self.assertEqual(opPop(),False)

    #-----------------------------------------------------
    #boolean operator tests
    def test_psAnd(self):
        opPush(True)
        opPush(False)
        psAnd()
        self.assertEqual(opPop(),False)
        opPush(True)
        opPush(True)
        psAnd()
        self.assertEqual(opPop(),True)

    def test_psOr(self):
        opPush(True)
        opPush(False)
        psOr()
        self.assertEqual(opPop(),True)
        opPush(False)
        opPush(False)
        psOr()
        self.assertEqual(opPop(),False)

    def test_psNot(self):
        opPush(True)
        psNot()
        self.assertEqual(opPop(),False)
        opPush(False)
        psNot()
        self.assertEqual(opPop(),True)
    #-----------------------------------------------------
    #stack manipulation operator tests
    def test_dup(self):
        #[3 5 5 True 4]  dup
        opPush([3,5,5,True,4])
        dup()
        isSame = opPop() is opPop()
        self.assertTrue(isSame)

    def test_exch(self):
        # /x 10 exch
        opPush('/x')
        opPush(10)
        exch()
        self.assertEqual(opPop(),'/x')
        self.assertEqual(opPop(),10)

    def test_pop(self):
        l1 = len(opstack)
        opPush(10)
        pop()
        l2 = len(opstack)
        self.assertEqual(l1,l2)

    def test_copy(self):
        #true 1 3 4 3 copy
        opPush(True)
        opPush(1)
        opPush(3)
        opPush(4)
        opPush(3)
        copy()
        self.assertTrue(opPop()==4 and opPop()==3 and opPop()==1 and opPop()==4 and opPop()==3 and opPop()==1 and opPop()==True)
        
    def test_clear(self):
        #10 /x clear
        opPush(10)
        opPush("/x")
        clear()
        self.assertEqual(len(opstack),0)

    def test_mark(self):
        # 1 2 3 mark 10
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

    #counttomark test that I implemented
    def test_counttomarkTest1(self):
        mark()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        counttomark() #should return 4
        self.assertEqual(opPop(), 4) #checking to see if counttomark() returns the correct count


    def test_cleartomark(self):
        # 1 2 3 mark 10 20 30 40 mark 50 cleartomark
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

    #cleartomark test that I implemented
    def test_cleartomarkTest1(self):
        mark()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        cleartomark()  # should result in an empty list
        self.assertTrue(len(opstack) == 0)  # checking to see if list is empty

    #-----------------------------------------------------
    #Array operator tests
    def test_length(self):
        #[3 5 5 True 4] length
        opPush([3,5,5,True,4])
        length()
        self.assertEqual(opPop(),5)      
        self.assertTrue(len(opstack)==0)        

    def test_get(self):
        #[3 5 5 True 4] 3 get
        opPush([3,5,5,True,4])
        opPush(3)
        get()
        self.assertEqual(opPop(),True)
        self.assertTrue(len(opstack)==0)

    #get test that I implemented
    def test_getTest1(self):
    #['This', 'is', 'a', 'test'] 0 get
        opPush(['This', 'is', 'a', 'test'])
        opPush(0)
        get()
        self.assertEqual(opPop(), 'This')
        self.assertTrue(len(opstack) == 0)

    def test_getinterval(self):
        #[3 5 5 True 4] 3 get
        opPush([4,5,3,5,5,True,4])
        opPush(2)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),[3,5,5])         
        self.assertTrue(len(opstack)==0)

    #getinterval test that I implemented
    def test_getintervalTest1(self):
        # ['This', 'is', 'a', 'test'] 0  get
        opPush(['This', 'is', 'a', 'test'])
        opPush(0)
        get()
        self.assertEqual(opPop(), 'This')
        self.assertTrue(len(opstack) == 0)

    def test_put1(self):
        #[3 5 5 True 4] dup 3 0 put
        opPush([3,5,5,True,4])
        dup()  #duplicating the array reference
        opPush(3)
        opPush(0)
        put()  #put will not push back the changed array
        self.assertEqual(opPop(),[3,5,5,0,4])  #we pop the array reference we copied with "dup"
        self.assertTrue(len(opstack)==0)

    def test_put2(self):
        #/x [3 5 5 True 4] def  x 2 0 put x
        x = [3,5,5,True,4]
        define('/x',x)
        opPush(x) #pushing the array reference onto the stack
        opPush(2)
        opPush(0)
        put()  #put will not push back the changed array
        self.assertEqual(lookup('x'),[3,5,0,True,4]) #we pop the array reference we bound to name /x     
        self.assertTrue(len(opstack)==0)

    def test_put3(self):
        #[3 5 5 True 4] dup /x exch def 2 0 put x
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

    #put test that I implemented
    def test_putTest1(self):
        # ['This', 'is', 'a', 'test'] 0  get
        x = ['This', 'is', 'a', 'test']
        define('/x', x)
        opPush(x)
        opPush(1)
        opPush("isn't")
        put()
        self.assertEqual(lookup('x'), ['This', "isn't", 'a', 'test'])
        self.assertTrue(len(opstack) == 0)

    def test_putinterval(self):
        opPush([0,1,3,5,5,True,4])
        dup() # we duplicate the array reference
        opPush(2)
        opPush([4,5,1,0])
        putinterval()
        self.assertEqual(opPop(),[0,1,4,5,1,0,4])
        self.assertTrue(len(opstack)==0)

    #putinterval test that I implemented
    def test_putintervalTest1(self):
        opPush(['This', 'is', 'a', 'test'])
        dup() # duplicate the array reference
        opPush(2)
        opPush(['for', 'putinterval'])
        putinterval()
        self.assertEqual(opPop(), ['This', 'is', 'for', 'putinterval'])
        self.assertTrue(len(opstack)==0)

    #dictionary stack operators
    def test_dict(self):
        #1 dict
        opPush(1)
        psDict()
        self.assertEqual(opPop(),{})

    def test_psDef(self):
        #/x 10 def /x 20 def x
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
        dictPush({})
        opPush("/x")
        opPush(10)
        psDef()
        dictPush({})
        opPush("/y")
        opPush(20)
        psDef()
        self.assertEqual(lookup('x'),10)

    #def test that I implemented
    def test_psDefTest1(self):
        dictPush({})
        opPush('/test')
        opPush(1)
        psDef()
        opPush('/sameDict')
        opPush('yes')
        psDef() # adding a second "variable" to the top most dict in dictstack, should not create another dict on top of current dict in dictstack
        self.assertEqual(lookup('test'), 1)
        self.assertEqual(lookup('sameDict'),'yes')
        end() # this pops the top most dict in dictstack, should contain 'test' and 'sameDict'
        self.assertTrue(len(dictstack) == 0)

    def test_beginEnd(self):
        #/x 3 def 1 dict begin /x 4 def end x
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
        self.assertEqual(lookup('x'),3)

    #begin test that I implemented
    def test_beginTest1(self):
        opPush(1)
        psDict()
        begin()
        opPush("/x")
        opPush(3)
        psDef()
        opPush(1)
        psDict()
        begin()
        opPush("/x")
        opPush(1)
        psDef()
        self.assertTrue(len(dictstack) == 2)
        self.assertEqual(lookup('x'), 1)
        end()
        self.assertTrue(len(dictstack) == 1)
        self.assertEqual(lookup('x'), 3)
        end()
        self.assertTrue(len(dictstack) == 0)

    #end test that I implemented
    def test_endTest1(self):
        opPush(1)
        psDict()
        begin()
        opPush("/x")
        opPush(3)
        psDef()
        opPush(1)
        psDict()
        begin()
        opPush("/x")
        opPush(1)
        psDef()
        self.assertTrue(len(dictstack) == 2)
        self.assertEqual(lookup('x'), 1)
        end()
        self.assertTrue(len(dictstack) == 1)
        self.assertEqual(lookup('x'), 3)
        end()
        self.assertTrue(len(dictstack) == 0)

    def test_psDef3(self):
        #/x 3 def 1 dict begin /x 30 def 1 dict begin /x 300 def end x
        # define x in the bottom dictionary
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

    #Tests to check "error checking"

    # # (4 pts) Make sure that the following test prints/raises an error message about the type of the second argument
    # #  Also make sure that the opstack content is : ['/x', 10]
    # def test_divInputs(self):
    #     opPush(10)
    #     opPush("/x")
    #     div()
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

