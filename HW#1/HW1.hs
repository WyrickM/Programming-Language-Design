-- CptS 355 - Spring 2020 Assignment 1
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

{-
      Mantz Wyrick
      1/31/2020
      Homework #1


      Note to self:
        To run code: In terminal in the appropriate folder locations, command: ghci .\HW1.hs      OR
                                                                               ghci HW1 + tab
                    Then run any functions with inputs from terminal
                    To run test cases:
                                        ghci .\HW1Tests.hs
                                        :r relod if you ever edit and save
                                        :t checks the type of a function
                                        run = run the tests

-}


module HW1
     where

{-buses = [("Lentil",["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"]), 
         ("Wheat",["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"]), 
         ("Silver",["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"]),
         ("Blue",["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"]),
         ("Gray",["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"])
        ]          
-}

-- 1a. exists
{-
    exists is a function that takes a "value" and a "list" as 
    arguments, and if the value is in the list then True should
    be returned. If the "value" is not in the list then False
    should be returned.

    Use recursion to iterate through the list while comparing
    the head of the list each time with the "value". 

    Arguements: (t) value, (t) list
    Returns: Bool (True or False)
-}
exists :: Eq t => t -> [t] -> Bool
exists value [] = False
exists value (x : xs) | value == x = True
                      | otherwise = (exists value xs)



-- 1b. type for exists
{- 
    The type is exists :: Eq t => t -> [t] -> Bool
    and not exists :: t -> [t] -> Bool because we need 
    the Typeclass Eq since we need to compare our first
    argument (our element we want to check if it exists)
    to 

    Arguements: 
    Returns: 
-}


{-
    countInList is a function that counts the amount of times 
    a "value" appears in a list. If the list is empty or if 
    the element is not in the list then return 0. 

    Arguements: value and a list
    Returns: (int) the amount of times value is in the list
-}
-- 1.c countInList
countInList :: (Num p, Eq t) => t -> [t] -> p
countInList value [] = 0
countInList value (x : xs) | value == x = 1 + (countInList value xs)
                           | value /= x = 0 + (countInList value xs)



{-
    listDiff
        takes two lists and returns the difference of the first list
        with respect to the second. List can have duplicate elements.
        If an element appears in both lists and if the number of
        duplicate copies of the element is bigger in the first list,
        then this element should appear in the result as many times
        as the difference of the number of occurrences in the input
        list.

    Arguements: (a) list, (a) list2         (list and list2 can be equal)
    Returns: (a) list   
-}
-- 2. listDiff
listDiff :: Eq a => [a] -> [a] -> [a]
listDiff [] secondList = []
listDiff firstList [] = firstList
listDiff (x : xs) secondList | (countInList x xs) >= (countInList x secondList) = x : (listDiff xs secondList)
                             | (countInList x xs) < (countInList x secondList) = (listDiff xs secondList)



{-
    firstN
        A function that takes a list and a number (n) and returns the 
        first n elements in the list. If list is empty or if the length
        of the list is less than n, then the function will return the
        complete list. (assume n >= 0)


    Arguements: (a) list, (t) value
    Returns: (a) list
-}
-- 3. firstN
firstN :: (Ord t, Num t) => [a] -> t -> [a]
firstN [] value = []
firstN (x : xs) value | value > 0 = x : (firstN xs (value - 1))
                      | otherwise = []




{-
    busFinder
        Takes two arguments. First is a value/name (stop)
        and a list that contains a tuple. The tuple is a
        name/value (bus) and a list with all the stops of
        the bus.
        The function takes the list of bus routes and a stop
        name, and returns a list of all of the buses that have
        a route that contains the desired stop.

        Uses the function exists.


    Arguements: (t) value/string, list that contains a tuple with a value/name and a list ([(a,[t])])
    Returns: (a) list   
-}
-- 4. busFinder
busFinder :: Eq t => t -> [(a,[t])] -> [a]
busFinder stop [] = []
busFinder stop ((bus, list): xs) | (exists stop list) == True = bus : (busFinder stop xs)
                                 | (exists stop list) == False = (busFinder stop xs)



{-
    cumulativeSums
        Takes a list of numbers and returns a list containing
        the partial sums of these numbers.

        Uses a helper function called: helperCumulativeSums
            Which takes a list and value. The value holds the
            accumulated sums and then gets added to the list.
            The list is then returned.

        cumulativeSums then returns the list that was returned 
        by the helper function.

    Arguements: (a) list
    Returns: (a) list   
-}
-- 5. cumulativeSums
helperCumulativeSums [] arg = []
helperCumulativeSums (x:xs) arg = (arg + x) : (helperCumulativeSums xs (arg + x))

cumulativeSums :: Num a => [a] -> [a]
cumulativeSums [] = []
cumulativeSums list = (helperCumulativeSums list 0)




{-
    groupNleft
        Takes two arguments a number (n) and a list. It returns a list
        in which the elements of the original list have been colleceted
        into ordered sub-lists each containing n elements. The leftover
        elements (if any) are included as a sublist with less than n
        elements. If empty retruns []

        Uses a helper function: helperGroupNleft
            Takes 3 arguments. Value and a list from groupNleft. Also 
            another list called buffer. Compare length of buffer. IF 
            length buffer < value add to buffer. If length buffer > 
            value add reversed buffer to a new list. 

    Arguements: (a) list
    Returns: (a(a)) (list(list))   
-}
-- 6. groupNleft
helperGroupNleft :: Int -> [a] -> [a] -> [[a]]
helperGroupNleft value [] buffer = ((reverse buffer) : [])
helperGroupNleft value (x:xs) buffer | (length buffer) < value = (helperGroupNleft value xs (x:buffer))
                                     | (length buffer) >= value = (reverse buffer) : (helperGroupNleft value xs (x:[]))

groupNleft :: Int -> [a] ->[[a]]
groupNleft value [] = []
groupNleft value list = (helperGroupNleft value list [])


