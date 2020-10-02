#--------------------------------------------HW #4 Part 2--------------------------------------------------------------#
# Mantz Wyrick
# No collaborators except for office hours help from Sakire
# 4/13/2020

import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    


# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parentheses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            if isInt(c) == True:
                c = int(c)
            elif c[0] == '[' and c[len(c) - 1] == ']':
                c = convertStrList(c)
            elif c == 'true' or c == 'false':
                c = convertToBool(c)
            res.append(c)
    return False

# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            if isInt(c) == True:
                c = int(c)
            elif c[0] == '[' and c[len(c)-1] == ']':
                  c = convertStrList(c)
            elif c == 'true' or c == 'false':
                c = convertToBool(c)
            res.append(c)
    return {'codearray':res}

# convertToBool
#       Is a helper function that converts a string that is a boolean value to an actual boolean value.
#       It takes one argument that is a string and returns a bool value.
#       This function will be called in parse() and groupMatch().
#
#       Since parse() and groupMatch() check the string to see if it is "true" or false. All I need to
#       is check the first character in the string to see if it is a "t" or "f". And then reassign c
#       to the appropriate bool value.
def convertToBool(c):
    if c[0] == 't':
        c = True
    elif c[0] == 'f':
        c = False
    return c

# convertStrList(c)
#       Is a helper function that allows me to convert a list that is a string
#       into a list. It takes one argument that is a str. Returns a list that
#       can contain ints, bool, and strings. #Not implementing for NESTED LISTS#
#       This function will be called in parse() and groupMatch().
#
#       I first "strip" the [] characters from the str and then split the string into
#       a list with the ' '(space) delimiter. Then go to every index and check to see
#       if it is a int, bool, or str. I have index be incrementing because I need to put the
#       updated "value" back it's same spot in the list. Which is why if the value is not an int
#       or bool I still increment so I do not replace a element in the list with something else.
def convertStrList(c):
    myArray = []
    index = 0
    c = c.strip('[]')
    myArray = list(c.split(' '))
    for value in myArray:
        if isInt(value) == True:
            myArray[index] = int(value)
            index +=1
        elif value == 'true' or value == 'false':
            myArray[index] = convertToBool(value)
            index +=1
        else:
            index += 1
    return myArray

# isInt(c)
#       Is a helper function that allows me to check to see if the parameter (c) is an integer.
#       It takes one argument that is a str and returns a bool value.
#       This function will be called in parse() and groupMatch().
#       If I can convert c into an int return true. Otherwise return false.
def isInt(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

# evaluateArray(array)
#   takes one argument: list(array)
#
#   this is a helper function for interpretSPS to evaluate an array
def evaluateArray(array, codearr):
    elements = 0
    returnArray = []
    for index in array:
        #this loop iterates through the whole array that is passed to the function
        if isinstance(index, int) or isinstance(index, bool):
            opPush(index)
            elements +=1                                        #keeping track of array elements that get pushed to the opstack
        elif isinstance(index, dict):
            opPush(index)
        elif index[0] == '/':
            opPush(index)
        elif isinstance(index, list):
            interpretSPS({'codearray': [index]})
        elif isinstance(index, str):
            if builtInOperators.get(index, 0) != 0:
                lengthOriginal = len(opstack)                   #gets the length of the opstack before operator is called
                interpretSPS({'codearray': [index]})
                lengthAfter = len(opstack)                      #gets the length of the opstack after the operator is called
                endLength = lengthOriginal - lengthAfter        #gets the difference of lengths before and after operator is called
                elements -= endLength                           #adjusts the number of elements to grab the correct amount of elements from opstack to put back in the array
            else:
                value = lookup(index)                           #checking to see if the index is in the dictstack
                if isinstance(value, dict):
                    tokenCodeArray = value.get('codearray')
                    newArray = evaluateArray(tokenCodeArray, 1)
                elif value != None:
                    interpretSPS({'codearray': [value]})
                    elements += 1                               #keeping track of array elements that get pushed to the opstack
                else:                                           # value == None
                    print("Error: undefined token")
    if codearr == 0:
        while elements > 0:
            returnArray.insert(0, opPop())                      #grabbing the elements from array that went to opstack and putting them back in the array
            elements-=1                                         #decrement elements to put correct amount of elements back in the array
    else:
        returnArray = []
    return returnArray


# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
def interpretSPS(code): # code is a code array
    index = code.get('codearray', 0)
    for token in index:
        if isinstance(token, int) or isinstance(token, bool):
            opPush(token)                                               #if token is bool/int value push onto opstack
        elif isinstance(token, dict):
            opPush(token)                                               #push token ('codearray':{})
        elif isinstance(token, list):
            newArray = evaluateArray(token, 0)                          #evaluate the array then push the evaluated array on opstack
            if len(newArray) != 0:
                opPush(newArray)
        elif isinstance(token, str):
            if token[0] == '/':
                opPush(token)                                           #push new variable/character on opstack
            elif builtInOperators.get(token, 0) != 0:
                callToken = builtInOperators.get(token)
                callToken()                                             #call the operator function
            else:
                value = lookup(token)
                if isinstance(value, dict):
                    tokenCodeArray = value.get('codearray')
                    newArray = evaluateArray(tokenCodeArray, 1)         #1 signals that it is a codearray so we do not put back in an array and just leave it on the opstack
                elif isinstance(value, list):
                    interpretSPS({'codearray': [value]})
                elif value != None:
                    opPush(value)                                       #push value onto opstack if the value is found in the dictstack
                else:                                                   #value == None
                    print("Error: undefined token")


def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))



#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []

# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

# opPop()
#   pops the top most element off of the operand stack(opstack)
#   and returns the popped element
def opPop():
    if len(opstack) > 0:
        result = opstack.pop()
    else:
        print('Error: there are no elements in the opStack, cannot pop a stack with no elements')
    return result
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

# opPush(value)
#   pushes value to the top of the operand stack (opstack)
def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

# dictPop()
#   dictPop pops the top dictionary from the dictionary stack.
def dictPop():
    if len(dictstack) > 0:
        result = dictstack.pop()
    else:
        print('Error: there are no elements in the dictStack, cannot pop a stack with no elements')

# dictPush(d)
#   takes one argument d: a dictionary
#
#   pushes the dictionary to the top most(last) dictionary in the
#   dictionary stack (dictstack)
def dictPush(d):
    dictstack.append(d)

    #dictPush pushes the dictionary ‘d’ to the dictstack.
    #Note that, your interpreter will call dictPush only when Postscript
    #“begin” operator is called. “begin” should pop the empty dictionary from
    #the opstack and push it onto the dictstack by calling dictPush.

# define()
#   takes 2 arguments: name and value. Name is a str with starting character '/'
#   and value being list/int/bool/codearray
#
#   takes the name and makes it a dictionary key and makes value the element of that
#   key and pushes it to the top of the dictionary stack (dictstack)
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

# lookup()
#   starts in the topmost dictionary(last) and looks in at each dictionary key
#   until it finds the variable name/key
def lookup(name):
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.
    index = 0
    dictName = '/' + name
    for index in reversed(dictstack):
        for key in index:
            if key == dictName:
                return index.get(key)
    print('Error: name: %s not found in dictstack!' %name)

#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.

# add()
#   add pops two operands from the operand stack (opstack): int(E2), int(E1)
#
#   E1 + E2 and push the result on the opstack,
#   does not push the values E1 and E2 back on the opstack
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

# sub()
#   sub pops two operands from the operand stack (opstack): int(E2),
#   int(E1) in that order
#
#   E1 - E2 and push the result on the opstack,
#   does not push the values E1 and E2 back on the opstack
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

# mul()
#   mul pops two operands from the operand stack (opstack): int(E2), int(E1)
#
#   multiply E1 with E2 and push the result on the opstack,
#   does not push the values E1 and E2 back on the opstack
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

# eq()
#   eq pops two operands from the operand stack (opstack): int(E2),
#   int(E1) in that order
#
#   if E1 == E2 push True on the opstack, else push False on the opstack,
#   does not push values for E1 and E2 back on opstack
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

# lt()
#   lt pops two operands from the operand stack (opstack): int(E2),
#   int(E1) in that order
#
#   if E1 < E2 push True on the opstack, else push False on the opstack,
#   does not push values for E1 and E2 back on opstack
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

# gt()
#   gt pops two operands from the operand stack (opstack): int(E2),
#   int(E1) in that order
#
#   if E1 > E2 push True on the opstack, else push False on the opstack,
#   does not push values for E1 and E2 back on opstack
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

# psAnd()
#   and pops two operands from the operand stack (opstack): bool, bool
#
#   if both operands are True then push True on the opstack,
#   else push False on the opstack. Normal "AND" statement
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

# psOr()
#   or pops two operands from the operand stack (opstack): bool, bool
#
#   if at least one of the operands is True then push True on
#   the opstack, else push False on the opstack. Normal "OR" statement
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

# psNot()
#   not pops one operand from the operand stack (opstack): bool
#
#   negates the bool value that is popped and then pushes the
#   negation on the opstack
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

# length()
#   !!! top most element in operand stack (opstack) must be a list(array) !!!
#
#   pops the list(array) from the opstack and pushes the length of the array
#   on the opstack, the array does not get pushed back on the opstack
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

# get()
#   get pops two operands from the operand stack (opstack): int(N),
#   list(array) in that order
#
#   gets the element at location N in the array and pushes that element on top
#   of the opstack, does not push array back on the opstack
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

# getinterval()
#   getinterval pops three operands from the operand stack (opstack): int(C), int(N),
#   list(array) in that order
#
#   gets the slice of the array from location N to N+C location and pushes that
#   subarray on the top of the opstack, does not push array back on the opstack
def getinterval():
    newArray = []
    if len(opstack) > 2:
        opCount = opPop()
        opIndex = opPop()
        opArray = opPop()
        if (opIndex < len(opArray)) and (opCount <= len(opArray) - opIndex):
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

# put()
#   put pops three operands form the operand stack (opstack): int/bool(V), int(N),
#   list(array) in that order
#
#   replaces the element at location N with the value V in the array, does not
#   push the back on the opstack
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

# putinterval()
#    putinterval pops three operands from the operand stack (opstack): list(array2),
#    int(N), list(array1) in that order
#
#   replaces the section of array1 with array2 starting at location N, does not
#   push array back on the opstack
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

# Inorder to save the array reference, need to either duplicate the reference
# with dup, or save the array as a variable that you can reference before calling
# any of these functions


#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark

# dup()
#   dup duplicates the top value of the operand stack (opstack) and pushes
#   it to the top of the opstack
def dup():
    if len(opstack) > 0:
        op1 = opstack[-1]
        opPush(op1)
    else:
        print("Error: dup expects 1 operand")

# copy()
#   copy pops one operand from the opstack: int(N)
#
#   copies the amount of elements (N) from the top of the operand stack
#   (opstack) and pushes them on the opstack
def copy():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, int):
            if op1 > len(opstack):
                print("Error: the list is not long enough to copy the amount of wanted operands")
            else:
                index = len(opstack) - op1
                while index < op1:
                    opPush(opstack[index])
                    index += 1
    else:
        print("Error: copy expects 1 operand")

# count()
#   count pushes that amount of elements/values that are on the
#   operand stack (opstack)
def count():
    opPush(len(opstack))

# pop()
#   pops the top value from the operand stack (opstack)
def pop():
    if len(opstack) > 0:
        dump = opPop()
    else:
        print("Error: pop expects 1 operand")

# clear()
#   clears the entire operand stack (opstack)
def clear():
    opstack.clear()

# exch()
#   exch pops two operands from the opstack: list/int/bool/codearray, list/int/bool/codearray
#
#   it then pushes them back on the operand stack (opstack) in reverse order
#   to "exchange" the top two stack values
def exch():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        opPush(op2)
        opPush(op1)
    else:
        print("Error: exch expects 2 operands")

# mark()
#   pushes '-mark-' on the operand stack (opstack)
def mark():
    opPush("-mark-")

# cleartomark()
#   !!! '-mark-' needs to be in the operand stack (opstack) !!!
#
#   pops all of the elements to '-mark-' and also '-mark-' itself
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

# counttomark()
#   !!! '-mark-' needs to be in the operand stack (opstack) !!!
#
#   counts the elements down to the top most mark (not including '-mark-')
#   then pushes that count on the opstack
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

# stack()
#   stack prints the contents of the operand stack (opstack)
def stack():
    print("[", end='')
    count = 0
    for index in opstack:
        if count == len(opstack) - 1:
            if isinstance(index, dict):
                print(index.get('codearray'), end='')
            else:
                print(index, end='')
        else:
            if isinstance(index, dict):
                print(index.get('codearray'), end=', ')
                count += 1
            else:
                print(index, end=', ')
                count += 1
    print(']')

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

# psDict()
#   dict pops one operand from the opstack: int
#
#   takes the int from the opstack and puts a new empty dictionary
#   on the operand stack (opstack)
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

# begin()
#   begin pops one operand from the opstack: dict
#
#   takes a dictionary from the top of the operand stack (opstack)
#   and pushes it on the dictionary stack (dictstack)
def begin():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1, dict):
            dictPush(op1)
        else:
            opPush(op1)
            print("Error: begin - the operand is not a dictionary")
    else:
        print("Error: begin expects 1 operand")

# end()
#   end pops the top dictionary from the dictionary stack (dictstack)
#   and throws it away, it cannot be used again
def end():
    dictPop()

# psDef()
#   def pops two operands from the opstack: list/int/bool/codearray, and
#   a str with '/' as the first character.
#
#   creates/modifies a dictionary entry in the top most dictionary on the
#   dictionary stack (dictstack)
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

#-------------------------------------Interpreter Part 2---------------------------------------------------------------#
# The operators that need to be defined for HW4 Part 2:
# if(psIf), ifelse(psIfelse), repeat(psRepeat), and forall
# use interpretSPS in the body of the if/ifelse, repeat, and forall operators recursively

# psIf()
#   if pops two operands, bool object and a code-array in that order
#
#   takes the bool object and evaluates the codearray if the boolean value is true.
#   Does not execute the codearray if the boolean value is false
def psIf():
    if len(opstack) > 1:
        opCodeArr = opPop() #pop the code array from opstack
        opCodeArr = opCodeArr.get('codearray')
        opBool = opPop() #pop the bool value form opstack
        if isinstance(opBool, Bool) and isinstance(opCodeArr,list): #check to see if opCodeArr is a code-array and if opBool is a Bool value
            if opBool == True:
                interpretSPS({'codearray': opCodeArr}) #pass code-array to interpretSPS to to run the codearray
            else:
                pass
        else:
            opPush(opBool)
            opPush(opCodeArr)
            print("Error: psIf - the boolean operand was not a boolean value and/or the code-array is not a code-array")
    else:
        print("Error: psIf expects 2 operands")

# psIfelse()
#   ifelse pops three operands, bool, code-array1, code-array2 in that order
#
#   if the boolean op is TRUE then evaluate with code-array1
#   if the boolean op is FALSE then evaluate with code-array2
def psIfelse():
    if len(opstack) > 2:
        opCodeArr2 = opPop() #pop the second (else statement) codearray
        opCodeArr2 = opCodeArr2.get('codearray')
        opCodeArr1 = opPop() #pop the first (if statement) codearray
        opCodeArr1 = opCodeArr1.get('codearray')
        opBool = opPop()    #pop the bool value that determines which codearray to evaluate
        if isinstance(opBool, bool) and isinstance(opCodeArr1,list) and isinstance(opCodeArr2,list):
            #check to see if opCodeArr1/2 are code-arrays and if opBool is Bool value
            if opBool == True:
                interpretSPS({'codearray': opCodeArr1})
                #evaluate code-array1
            else:
                interpretSPS({'codearray': opCodeArr2})
                #evaluate code-array2
        else:
            opPush(opBool)
            opPush(opCodeArr1)
            opPush(opCodeArr2)
            print("Error: psIfelse - the boolean operand is not a bool value and/or one/both code-array is not a code-array")
    else:
        print("Error: psIfelse expects 3 operands")

# psRepeat()
#   repeat pops 2 operands, an int(N) and a code-array
#
#   repeat executes the code in the code-array N times
def psRepeat():
    if len(opstack) > 1:
        opCodeArr = opPop()
        opCodeArr = opCodeArr.get('codearray')
        opInt = opPop()
        if isinstance(opInt, int) and isinstance(opCodeArr, list):
            #check to see if opCodeArr is a code-array and if opArr is an array
            while opInt > 0:
                interpretSPS({'codearray': opCodeArr}) #pass the codearray to interpretSPS to execute code-array
                opInt -= 1
        else:
            opPush(opInt)
            opPush(opCodeArr)
            print("Error: psRepeat - the int operand is not an int value and/or the code-array is not a code-array")
    else:
        print("Error: psRepeat expects 2 operands")

# forall()
#   forall pops 2 operands, an array(List) and a code-array
#
#   takes an array and a code-array and evaluates the
#   code-array on each member of the array
def forall():
    if len(opstack) > 1:
        opCodeArr = opPop()
        opCodeArr = opCodeArr.get('codearray')
        opArr = opPop()
        if isinstance(opArr, list) and isinstance(opCodeArr, list):
            #check to see if opCodeArr is a code-array and if opArr is an array
            for elemArr in opArr:
                opPush(elemArr)
                #push the element of the array on to the opstack so forall can execute the codearray
                interpretSPS({'codearray':opCodeArr})
                #pass the codearray into interpretSPS to be executed each time of the loop
        else:
            opPush(opArr)
            opPush(opCodeArr)
            print("Error: forall - the array operand is not an array and/or the code-array is not a code-array")
    else:
        print("Error: forall expects 2 operands")


builtInOperators = {'add': add, 'sub': sub, 'mul': mul, 'eq': eq, 'lt': lt, 'gt': gt,
                    'and': psAnd, 'or': psOr,'not': psNot, 'length': length, 'get': get,
                    'getinterval': getinterval, 'put': put, 'putinterval': putinterval,
                    'dup': dup, 'copy': copy, 'count': count, 'pop': pop, 'clear': clear,
                    'exch': exch, 'mark': mark, 'cleartomark': cleartomark,
                    'counttomark': counttomark, 'stack': stack, 'dict': psDict,
                    'begin': begin, 'end': end, 'def': psDef, 'if': psIf,
                    'ifelse': psIfelse, 'forall': forall, 'repeat': psRepeat}


# print(tokenize(input1))
# print(parse(tokenize(input1)))
# print(parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}']))



if __name__ == "__main__":
    testinput1 = """
        /x 4 def
        /g { x stack } def
        /f { /x 7 def g } def
        f
        """
    testinput2 = """
        /x 4 def
        [1 1 1] dup 1 [2 3] putinterval /arr exch def
        /g { x stack } def
        /f { 0 arr {7 mul add} forall /x exch def g } def
        f
        """
    testinput3 = """
        /m 50 def
        /n 100 def
        /egg1 {/m 25 def n} def
        /chic
        	{ /n 1 def /egg2 { n stack} def
    	      m  n egg1 egg2 } def
        n
        chic
            """
    testinput4 = """
        /x 10 def
        /A { x } def
        /C { /x 40 def A stack } def
        /B { /x 30 def /A { x } def C } def
        B
        """
    testinput5 = """
        /x 10 def
        /n 5  def
        /A { 0  n {x add} repeat} def
        /C { /n 3 def /x 40 def A stack } def
        /B { /x 30 def /A { x } def C } def
        B
        """
    testinput6 = """
        /out true def 
        /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
        /myput { out dup /x exch def xand } def 
        /f { /out false def myput } def 
        false f
        """
    testinput7 = """
        /x [1 2 3 4] def
        /A { x length } def
        /C { /x [10 20 30 40 50 60] def A stack } def
        /B { /x [6 7 8 9] def /A { x 0 get} def C } def
        B
        """
    testinput8 = """
        [0 1 2 3 4 5 6 7 8 9 10] 3 4 getinterval /x exch def
        /a 10 def  
        /A { x length } def
        /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
        /B { /x [6 7 8 9] def /A { x 0 get} def /a 5 def C } def
        B
        """
    testinput9 = """
    {1 2 3 add} stack pop
    /x {1 2 3 add} def
    x stack
    """
    testinput12 = """
            /add2 {/add1 { 1 add} def add1 add1} def
                /add3 {add2 add1} def
                /add4 {add2 add2} def
                0 add4 add3 add2 add1
            """
    testinput13 = """
     /myload { { } forall } def
            mark 
            /x 1 def /y 2 def /z 3 def
            [x y z 4 5 6 7] myload 
            counttomark 1 sub {add} repeat  
            exch pop
    """
    interpreter(testinput13)
    stack()

