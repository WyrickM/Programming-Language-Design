# In the correct directory run this code in terminal to run tests without changing configuration
    #   python -m unittest -v HW4tests_part2.py
import unittest
from HW4_part2 import *

# Please don't redefine opstack and dictstack in this test file. 
# The test methods should refer to the opstack and dictstack in your HW4_part2.py file.  
class HW4_part2_SampleTests(unittest.TestCase):
    def setUp(self):
        clearStacks()  #clear both stacks
        dictstack.append({})

    def test_input1(self):
        testinput1 = """
            /square {dup mul} def 
            0 [-5 -4 3 -2 1]     
            {square add} forall 
            55 eq false and
        """
        opstackOutput = [False]
        interpreter(testinput1)
        self.assertEqual(opstack,opstackOutput)

    def test_input2(self):
        testinput2 = """
            /x 1 def
            /y 2 def
            1 dict begin
            /x 10 def
            1 dict begin /y 3 def x y end
            /y 20 def
            x y
            end
            x y
        """
        opstackOutput = [10, 3, 10, 20, 1, 2]
        interpreter(testinput2)
        self.assertEqual(opstack,opstackOutput)


    # test with getinterval, putinterval
    def test_input3(self):
        testinput3 = """
            [3 2 1 3 2 2 3 5 5] dup  
            3
            [4 2 1 4 2 3 4 5 1] 6 3 getinterval
            putinterval
        """
        opstackOutput = [[3,2,1,4,5,1,3,5,5]]
        interpreter(testinput3)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input4(self):
        testinput4 = """
           /a [1 2 3 4 5] def 
           a {dup mul} forall
        """
        opstackOutput = [1,4,9,16,25]
        interpreter(testinput4)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input5(self):
        testinput5 = """
           /a [10 20 30 40 50] def 
           [4 2 0] {a exch get} forall
        """
        opstackOutput = [50,30,10]
        interpreter(testinput5)
        self.assertEqual(opstack,opstackOutput)

    # test with forall and repeat
    def test_input6(self):
        testinput6 = """
           /N 5 def 
            N { N N mul /N N 1 sub def} repeat
        """
        opstackOutput = [25,16,9,4,1]
        interpreter(testinput6)
        self.assertEqual(opstack,opstackOutput)

    def test_input7(self):
        testinput7 = """
            /n 5 def
            /fact {
                0 dict begin
                /n exch def
                n 2 lt
                { 1}
                {n 1 sub fact n mul }
                ifelse
                end 
            } def
            n fact
        """
        opstackOutput = [120]
        interpreter(testinput7)
        self.assertEqual(opstack,opstackOutput)

    def test_input8(self):
        testinput8 = """
            /fact{
                0 dict
                begin
                    /n exch def
                    1
                    n  {n mul /n n 1 sub def} repeat
                end
            } def
            6 fact 
        """
        opstackOutput = [720]
        interpreter(testinput8)
        self.assertEqual(opstack,opstackOutput)

    # test with getinterval, putinterval
    def test_input9(self):
        testinput9 = """
            /sumArray { 0 exch {add} forall  } def
            /x 5 def
            /y 10 def 
            [1 2 3 add 4 x] sumArray
            [x 7 8 9 y] sumArray
            [y 2 5 mul 1 add 12] sumArray 
        """
        opstackOutput = [15,39,33]
        interpreter(testinput9)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input10(self):
        testinput10 = """
            1 2 3 4 5 count copy 15 5 {exch sub} repeat 0 eq  
        """
        opstackOutput = [1,2,3,4,5,True]
        interpreter(testinput10)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input11(self):
        testinput11 = """
            /xor {true eq {true eq {false} {true} ifelse } {true eq {true} {false} ifelse } ifelse } def
		    true [true false and false true or false false] {xor} forall
        """
        opstackOutput = [False]
        interpreter(testinput11)
        self.assertEqual(opstack,opstackOutput)

    def test_input12(self):
        testinput12 = """
        /add2 {/add1 { 1 add} def add1 add1} def
            /add3 {add2 add1} def
            /add4 {add2 add2} def
            0 add4 add3 add2 add1
        """
        opstackOutput = [10]
        interpreter(testinput12)
        self.assertEqual(opstack, opstackOutput)

    def test_input13(self):
        testinput13 = """
         /myload { { } forall } def
            mark 
            /x 1 def /y 2 def /z 3 def
            [x y z 4 5 6 7] myload 
            counttomark 1 sub {add} repeat  
            exch pop
        """
        opstackOutput = [28]
        interpreter(testinput13)
        self.assertEqual(opstack, opstackOutput)


#---------------------------The 5 tests that I created are below-----------------------#
    #test with forall, mark, couttomark, and cleartomark
    def test_myInput1(self):
        myTestInput1 = """
            /myarr [1 2 3 4 5] def 
            myarr {12 mul} forall
            mark /y myarr /x
            counttomark 1 add def
            x get 12 mul def cleartomark
            y eq  
        """
        interpreter(myTestInput1)
        result = opPop()
        self.assertEqual(result, True)

    def test_myInput2(self):
        myTestInput2 = """
            /y 3 def
            /f {/z y def 1 dict begin
                /z 4 def
                /y 5 def
                z y mul
                end
                } def
            f y mul
        """
        opstackOutput = [60]
        interpreter(myTestInput2)
        self.assertEqual(opstack, opstackOutput)

    #test with count, ifelse, length, and put
    def test_myInput3(self):
        myTestInput3 = """
            1 10 2 20 3 30 count
            /x exch def x gt
                {clear x 12 mul 10 sub}
                {clear x x sub}
            ifelse
            /new exch def
            /y [1 10 2 20 3 30] def y length
            1 sub /len exch def
            y dup len new put
            /y exch def
            y
        """
        opstackOutput = [[1,10, 2, 20, 3, 62]]
        interpreter(myTestInput3)
        self.assertEqual(opstack, opstackOutput)

    #test with forall and repeat
    def test_myInput4(self):
        myTestInput4 = """
            /happy 1 def
            happy dict begin
            /func {/arr [-1 -2 -3 -4 -5] 
                    def /neg -1 def
                    arr {neg mul} forall
                    /value exch def
                    value {1 sub} repeat
                    } def
            func happy lt
            /stillhappy exch def
            clear
            stillhappy                  
        """
        opstackOutput = [True]
        interpreter(myTestInput4)
        self.assertEqual(opstack, opstackOutput)

    #test with nested ifelse statements
    def test_myInput5(self):
        myTestInput5 = """
            /x 1 def
            x 2 eq
                {count x add}
                {1 dict begin /x 2 def
                 x 1 eq
                    {x end x add /y exch def}
                    {x end x mul /y exch def}
                ifelse}
            ifelse
            y
        """
        opstackOutput = [2]
        interpreter(myTestInput5)
        self.assertEqual(opstack, opstackOutput)



if __name__ == '__main__':
    unittest.main()

