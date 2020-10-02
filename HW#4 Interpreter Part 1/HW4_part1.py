# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Mantz Wyrick
# 3/30/2020
# No collaborators
#
# In the correct directory run this code in terminal to run tests without changing configuration
    #   python -m unittest -v HW4Sampletests_part1

# Go back and add all the comments that say what the functions do.

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if len(opstack) > 0:
        result = opstack.pop()
    else:
        print('Error: there are no elements in the opStack, cannot pop a stack with no elements')
    return result
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    if len(dictstack) > 0:
        result = dictstack.pop()
    else:
        print('Error: there are no elements in the dictStack, cannot pop a stack with no elements')
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)

    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    dict = {name: value}
    if len(dictstack) > 0:
        dictstack[-1].update(dict)
    else:
        dictstack.insert(0,dict)
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.


def lookup(name):
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.
    index = 0
    dictName = '/' + name
    for index in reversed(dictstack):
        for key in index:
            if key == dictName:
                return index.get(key)
    print('Error: name:%s not found in dictstack!' %name)


#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2, int)):
            opPush(op1 + op2)
        else:
            print("Error: add - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: add expects 2 operands")

def sub():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2, int)):
            opPush(op1 - op2)
        else:
            print("Error: sub - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: sub expects 2 operands")

def mul():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2, int)):
            opPush(op1 * op2)
        else:
            print("Error: mul - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: mul expects 2 operands")

def eq():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(op1 == op2):
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: eq expects 2 operands")

def lt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2, int)):
            if(op1 < op2):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: lt - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: lt expects 2 operands")

def gt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1, int) and isinstance(op2, int)):
            if (op1 > op2):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: gt - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: gt expects 2 operands")

def psAnd():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1, bool) and isinstance(op2, bool)):
            if op1 == False and op2 == False:
                opPush(False)
            elif op1 == op2:
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: psAnd - one of the operands is not a Boolean value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: psAnd expects 2 operands")

def psOr():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1, bool) and isinstance(op2, bool)):
            if op1 == True or op2 == True:
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: psOr - one of the operands is not a Boolean value")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: psOr expects 2 operands")


def psNot():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, bool):
            if op1 == True:
                opPush(False)
            else:
                opPush(True)
        else:
            opPush(op1)
            print("Error: psNot - the operand is not a Boolean value")
    else:
        print("Error: psNot expects 1 operand")

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, list):
            arrayLength = len(op1)
            opPush(arrayLength)
        else:
            print("Error: length - the operand is not an array")
            opPush(op1)
    else:
        print("Error: length expects 1 operand")


def get():
    if len(opstack) > 1:
        opIndex = opPop()
        opArray = opPop()
        if opIndex < len(opArray):
            if isinstance(opIndex, int) and isinstance(opArray, list):
                value = opArray[opIndex]
                opPush(value)
            else:
                print("Error: get - the operands need to be an array and int in that order")
                opPush(opArray)
                opPush(opIndex)
        else:
            print("Error: get - the index operand is out of scope of the array")
            opPush(opArray)
            opPush(opIndex)
    else:
        print("Error: get expects 2 operands")


def getinterval():
    newArray = []
    if len(opstack) > 2:
        opCount = opPop()
        opIndex = opPop()
        opArray = opPop()
        if (opIndex < len(opArray)) and (opCount < len(opArray) - opIndex):
            if isinstance(opCount, int) and isinstance(opIndex, int) and isinstance(opArray, list):
                while opCount != 0:
                    newArray.append(opArray[opIndex])
                    opCount -= 1
                    opIndex += 1
                opPush(newArray)
            else:
                print("Error: getinterval - the operands need to be an array, int, and int in that order")
                opPush(opArray)
                opPush(opIndex)
                opPush(opCount)
        else:
            print("Error: getinterval - either the index operand is out of scope of the array or the count goes out of scope of the array")
            opPush(opArray)
            opPush(opIndex)
            opPush(opCount)
    else:
        print("Error: getinterval expects 3 operands")


def put():
    if len(opstack) > 2:
        opValue = opPop()
        opIndex = opPop()
        opArray = opPop()
        if opIndex < len(opArray):
            if isinstance(opIndex, int) and isinstance(opArray, list):
                opArray[opIndex] = opValue
            else:
                print("Error: put - the operands need to be an array, int, and anything in that order")
                opPush(opArray)
                opPush(opIndex)
                opPush(opValue)
        else:
            print("Error: put - the index operand is out of scope of the array")
            opPush(opArray)
            opPush(opIndex)
            opPush(opValue)
    else:
        print("Error: put expects 3 operands")


def putinterval():
    if len(opstack) > 2:
        opArray2 = opPop()
        opIndex = opPop()
        opArray1 = opPop()
        if (opIndex < len(opArray1)) and (opIndex + len(opArray2) <= len(opArray1)):
            if isinstance(opArray1, list) and isinstance(opIndex, int) and isinstance(opArray2, list):
                lenghtArray2 = len(opArray2)
                index = 0
                while index <= lenghtArray2 - 1:
                    opArray1[opIndex] = opArray2[index]
                    index += 1
                    opIndex += 1
            else:
                print("Error: putinterval - the operands need to be an array, int, and int in that order")
                opPush(opArray1)
                opPush(opIndex)
                opPush(opArray2)
        else:
            print("Error: putinterval - the index operand is out of scope of the array or the second array is too long and goes out of scope")
            opPush(opArray1)
            opPush(opIndex)
            opPush(opArray2)
    else:
        print("Error: putinterval expects 3 operands")

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    if len(opstack) > 0:
        op1 = opstack[-1]
        opPush(op1)
    else:
        print("Error: dup expects 1 operand")

def copy():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, int):
            if op1 > len(opstack):
                print("Error: the list is not long enough to copy the amount of wanted operands")
            else:
                index = len(opstack) - op1
                while index <= op1:
                    opPush(opstack[index])
                    index += 1
    else:
        print("Error: copy expects 1 operand")


def count():
    opPush(len(opstack))

def pop():
    if len(opstack) > 0:
        dump = opPop()
    else:
        print("Error: pop expects 1 operand")


def clear():
    opstack.clear()


def exch():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        opPush(op2)
        opPush(op1)
    else:
        print("Error: exch expects 2 operands")


def mark():
    opPush("-mark-")

def cleartomark():
    if len(opstack) > 0:
        indexMark = len(opstack) - 1
        while indexMark >= 0 and opstack[indexMark] != "-mark-":
            indexMark -= 1
        if indexMark < 0:
            print("Error: -mark- was not found in opStack")
        else:
            clearIndex = len(opstack) - 1
            while clearIndex >= indexMark:
                clearIndex -= 1
                pop()
    else:
        print("opstack is empty, -mark- is not in the stack")


def counttomark():
    if len(opstack) > 0:
        indexMark = len(opstack) - 1
        while indexMark >= 0 and opstack[indexMark] != "-mark-":
            indexMark -= 1
        if indexMark < 0:
            print("Error: -mark- was not found in opStack")
        else:
            endIndex = len(opstack) - 1
            result = endIndex - indexMark
            opPush(result)
    else:
        print("opstack is empty, -mark- is not in the stack")


def stack():
    print(opstack)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, int):
            tempDict = {}
            opPush(tempDict)
        else:
            opPush(op1)
            print("Error: psDict - the operand is not an int value")
    else:
        print("Error: psDict expects 1 operand")

def begin():
    op1 = opPop()
    dictPush(op1)

def end():
    dictPop()

def psDef():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, str) and op1[0] == "/":
            define(op1, op2)
        else:
            opPush(op1)
            opPush(op2)
            print("Error: psDef - the op1 operand is not an str value or does not have a forward slash")
    else:
        print("Error: psDef expects 2 operands")

#-------------------------------Interpreter Part 2---------------------------------------------------------------#
# The operators that need to be defined for HW4 Part 2
# if(psIf), ifelse(psIfelse), repeat(psRepeat), and forall
# interpret the body of the if/ifelse, repeat, and forall operators recursively

# if(psIf) operator
# if pops two operands, bool object and a code-array in that order
# def psIf():
#     if len(opstack) > 1:
#         opCodeArr = opPop()
#         opBool = opPop()
#         if isinstance(opBool, Bool): #might need to check to see if opCodeArr is a code-array
#             if opBool == True:
#                 # evaluate the code-array
#             else:
#                 pass
#         else:
#             opPush(opBool)
#             opPush(opCodeArr)
#             print("Error: psIf - the boolean operand was not a boolean value and/or the code-array is not a code-array")
#     else:
#         print("Error: psIf expects 2 operands")
#
#
# # ifelse(psIfelse) operator
# # ifelse pops three operands, bool, code-array1, code-array2 in that order
# # if the boolean op is TRUE then evaluate with code-array1
# # if the boolean op is FALSE then evaluate with code-array2
# def psIfelse():
#     if len(opstack) > 2:
#         opCodeArr2 = opPop()
#         opCodeArr1 = opPop()
#         opBool = opPop()
#         if isinstance(opBool, bool): #might need to check to see if the code-arrays are actually code-arrrays
#             if opBool == True:
#                 #evaluate code-array1
#             else:
#                 #evaluate code-array2
#         else:
#             opPush(opBool)
#             opPush(opCodeArr1)
#             opPush(opCodeArr2)
#             print("Error: psIfelse - the boolean operand is not a bool value and/or one/both code-array is not a code-array")
#     else:
#         print("Error: psIfelse expects 3 operands")
#
# # repeat(psRepeat) operator
# # repeat pops 2 operands, an int(N) and a code-array
# # repeat executes the code in the code-array N times
# def psRepeat():
#     if len(opstack) > 1:
#         opCodeArr = opPop()
#         opInt = opPop()
#         if isinstance(opInt, int): # might need to check to see if the code-array is a code-array
#             while opInt > 0:
#                 #execute code-array
#                 opInt -= 1
#         else:
#             opPush(opInt)
#             opPush(opCodeArr)
#             print("Error: psRepeat - the int operand is not an int value and/or the code-array is not a code-array")
#     else:
#         print("Error: psRepeat expects 2 operands")
#
# # forall operator
# # forall pops 2 operands, an array(List) and a code-array
# # forall takes an array and a code-array and evaluates the code-array on each member of the array
# def forall():
#     if len(opstack) > 1:
#         opCodeArr = opPop()
#         opArr = opPop()
#         if isinstance(opArr, list): #need to check that opcodeArr is actually a code-array
#             #evaluate the code-array on each element of the array
#             #for index in opArr:
#             #   evaluate the codearray with index
#         else:
#             opPush(opArr)
#             opPush(opCodeArr)
#             print("Error: forall - the array operand is not an array and/or the code-array is not a code-array")
#     else:
#         print("Error: forall expects 2 operands")
#
#
#
#
#
