-- CptS 355 - Spring 2020 Assignment 2
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

{-
     Mantz Wyrick
     2/25/2020
     Homework #2
     Went to Shakira Office hours
-}

module HW2
     where

{-
    countInList is a function that counts the amount of times 
    a "value" appears in a list. If the list is empty or if 
    the element is not in the list then return 0. 

    Arguements: value and a list
    Returns: (int) the amount of times value is in the list
-}
countInList :: (Num p, Eq t) => t -> [t] -> p
countInList value [] = 0
countInList value (x : xs) | value == x = 1 + (countInList value xs)
                           | value /= x = 0 + (countInList value xs)


{- intersect & intersectTail & intersectAll - 22%-}
{-
    intersect
        A function that takes 2 lists and returns a list including the
        elements that exists in both lists. The returned list should have
        no duplicate elements. Elements in list can be in any order


    Arguements: (a) list, (t) list
    Returns: (a) list
-}
--intersect
intersect :: Eq a => [a] -> [a] -> [a]
intersect [] secondList = []
intersect firstList [] = []
intersect (x:xs) secondList | (((elem x secondList) == True) && ((countInList x xs) == 0))  = x : (intersect xs secondList)
                            | otherwise = (intersect xs secondList)


{-
    intersectTail
        A function that takes 2 lists and returns a list including the
        elements that exists in both lists. The returned list should have
        no duplicate elements. Elements in list can be in any order. 

        USES TAIL RECURSION

    Arguements: (a) list, (a) list
    Returns: (a) list
-}
--intersectTail
intersectTail :: Eq a => [a] -> [a] -> [a]
intersectTail list1 list2 = intersectTailAccum list1 list2 []
                                     where
                                        intersectTailAccum :: Eq a => [a] -> [a] -> [a] -> [a]
                                        intersectTailAccum [] list2 accum = reverse (accum)
                                        intersectTailAccum list1 [] accum = reverse (accum)
                                        intersectTailAccum (x:xs) list2 accum | (((elem x list2) == True) && ((countInList x xs) == 0)) = (intersectTailAccum xs list2 (x:accum))
                                                                              | otherwise = (intersectTailAccum xs list2 accum)



{-
    intersectAll
        A function that takes a list of lists. Searches through the sublists
        and returns a list that contains the intersection of all the sublists
        of the input list

        No explicit recursion, sues foldr

    Arguements: (a) list
    Returns: (a) list
-}
--intersectAll
intersectAll :: Ord a => [[a]] -> [a]
intersectAll [] = []
intersectAll (x:list) = (foldr (intersect) x list)



{-2 - partition - 10%-}
{-
    partition is a function that takes a function(op) and a list as inputs
    and returns a 2-tuple (left,right). The left output is the list of elements
    in which (op) evaluates to be true. The right is the list of those elements 
    in which (op) evaluates to be false. The elements retain the same order 
    as in the input list.

    Not recursion. Uses filter

    Arguements: op and list
    Returns: (listT,listF)
-}
partition :: (a -> Bool) -> [a] -> ([a],[a])
partition op list = ((filter op list), (filter (not . op) list))



{- 3 - sumL, sumMaybe, and sumEither - 27% -}
{-
    sumL is a function that takes a list of lists and returns a value.
    It returns the sum of all of the numbers in all sublists of the
    input list.

    Not recursive. Uses map,foldr and a helper function

    addup is the helper function that takes a list and addes up the elements

    map -- adds up the sublists into list and then addup adds up the new list
           from map to the return value

    Arguements: list of lists
    Returns: (int) the sum of all of the elements
-}
--sumL
sumL :: (Num b, Foldable t) => [t b] -> b
sumL list =  addUp (map addUp list)
               where
                    addUp :: (Num b, Foldable t) => t b -> b 
                    addUp list = foldr (+) 0 list



{-
    sumMaybe is a function that takes a Maybe (list of lists) and returns a 
    Maybe(value). It returns the sum of all of the numbers in all sublists
    of the input list.

    Not recursive. Uses map,foldr and a helper function

    addMay is the helper function that takes a list and addes up the elements
    addMap is a function that adds that different types of (Maybe a) elements

    map -- adds up the sublists into list and then addup adds up the new list
           from map to the return value

    Arguements: Maybe(list of lists)
    Returns: (Maybe) the sum of all of the elements
-}
-- sumMaybe 
sumMaybe :: (Num a, Foldable t) => [t (Maybe a)] -> Maybe a
sumMaybe list = addMay (map addMay list)  
               where
                    addMay list = foldr (addMap) Nothing list

                    addMap Nothing Nothing = Nothing
                    addMap Nothing (Just v) = (Just v)
                    addMap (Just v) Nothing = (Just v)
                    addMap (Just x) (Just y) = (Just (x+y)) 



{-
    sumEither is a function that takes a list of lists that is of type IEither
    and returns a value. IEither is a declared data type that allows for either
    a string with a number or an int.
    It returns the sum of all of the numbers in all sublists of the
    input list.

    Not recursive. Uses map,foldr and a helper function

    addEither -- is the helper function that takes a list and addes up the elements
    getInt -- is a helper function that converts the string to a int
    addAll -- is a helper function that adds the multiple types/possibilities 
              of the IEither type so we can add the elements together
    map -- adds up the sublists into list and then addup adds up the new list
           from map to the return value

    Arguements: list of lists of type (IEither)
    Returns: (IEither) the sum of all of the elements
-}
-- sumEither
data IEither  = IString String | IInt Int
                deriving (Show, Read, Eq)

sumEither :: Foldable t => [t IEither] -> IEither
sumEither list = addEither(map addEither list)
                    where 
                         addEither list = foldr (addAll) (IInt 0) list

                         getInt x = read x::Int
                         
                         addAll (IString x) (IString y) = IInt ((getInt x) + (getInt y))
                         addAll (IString x) (IInt y) = IInt ((getInt x) + y)
                         addAll (IInt x) (IString y) = IInt (x + (getInt y))
                         addAll (IInt x) (IInt y) = IInt (x + y)




{-4 - depthScan, depthSearch, addTrees - 37%-}
-- t2 = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))
-- t1 = NODE "Science" (NODE "and" (LEAF "School")(NODE "Engineering" (LEAF "of") (LEAF "Electrical")))(LEAF "Computer")
-- t3 = NODE 1 (NODE 2 (NODE 3 (LEAF 2) (LEAF 5)) (LEAF 1)) (NODE 1 (LEAF 8) (LEAF 5))
-- left = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))
-- right = NODE 1 (NODE 2 (LEAF 3) (LEAF 6)) (NODE 7 (NODE 8 (LEAF 10) (LEAF 11)) (LEAF 9))


data Tree a = LEAF a | NODE a (Tree a) (Tree a)
              deriving (Show, Read, Eq)
 
{-
    depthScan is a function that takes a a tree of type (Tree a) declared
    above and returns a list of the (a) values stored in the leaves and the
    nodes. The order of the elements in the output is based on the depth-first
    order traversal of the tree.


    Arguements: Tree a
    Returns: list
-}
--depthScan
depthScan :: Tree a -> [a]
depthScan (LEAF x) = [x]
depthScan (NODE x t1 t2) = (depthScan t1) ++ (depthScan t2)  ++ [x]



{-
    depthSearch is a function that takes a a tree of type (Tree a) declared
    above, a value of the same type as the tree and returns the level of the
    tree where the value is found. If the value does not exist in the tree
    -1 should be returned. The tree nodes should be visited with depth-first
    order traversal and the level of the first matching node should be returned.

    depthSearchHelper -- is a helper function that compares the value in the leaf
                         and node to the inputed value to see if they match all 
                         while increasing the level counter. If there is a match
                         return the level, if no match travers through the tree
                         until reach a leaf. If leaf doesn't match return -1 and 
                         keep traversing until you searched the whole tree. If value 
                         not found return -1.


    Arguements: Tree a, value a
    Returns: (p) value (level)
-}
--depthSearch
depthSearch :: (Ord p, Num p, Eq a) => Tree a -> a -> p
depthSearch tree value = (depthSearchHelper tree value 1)
                       where 
                            depthSearchHelper :: (Ord p, Num p, Eq a) => Tree a -> a -> p -> p
                            depthSearchHelper (LEAF x) value level | (x /= value) = -1
                                                                   | otherwise = level
                            depthSearchHelper (NODE v t1 t2) value level | (depthSearchHelper t1 value (level + 1)) > 0 = (depthSearchHelper t1 value (level + 1))
                                                                         | (depthSearchHelper t2 value (level + 1)) > 0 = (depthSearchHelper t2 value (level + 1))
                                                                         | (v == value) = level
                                                                         | otherwise = -1



{-
    addTrees is a function that takes two trees (Tree int) values and returns 
    a tree (Tree int) where the corresponding nodes from the two trees are added.
    The trees could have a different depth so you should copy branches/nodes
    of the trees if the other tree doesn't have that branch/node.

     The function takes into account all of the pattern matching and uses a helper 
     function.

     copyTree -- is a helper function that just copies a tree if we are 
                 trying to add a LEAF and NODE together (in both orders).


    Arguements: Tree a, Tree a
    Returns: Tree a
-}
--addTrees
copyTree :: Tree a -> Tree a
copyTree (LEAF x) = LEAF x
copyTree (NODE v t1 t2) = NODE v (copyTree t1) (copyTree t2)


addTrees :: Num a => Tree a -> Tree a -> Tree a 
addTrees (LEAF x) (LEAF y) = LEAF (x + y)
addTrees (NODE v1 t1 t2) (NODE v2 t3 t4) = NODE (v1 + v2) (addTrees t1 t3) (addTrees t2 t4)
addTrees (LEAF x) (NODE v t1 t2) = NODE (x + v) (copyTree t1) (copyTree t2)
addTrees (NODE v t1 t2) (LEAF x) =  NODE (x + v) (copyTree t1) (copyTree t2)



{- 5- Create two trees of type Tree. The height of both trees should be at least 4. Test your functions depthScan, depthSearch, addTrees with those trees. 
The trees you define should be different than those that are given.   -}

tree1 = NODE 20 (NODE 18 (NODE 16 (LEAF 14) (LEAF 15))(LEAF 19))(LEAF 21)
fullTree = NODE 100 (NODE 99 (NODE 98 (LEAF 97)(LEAF 96)) (NODE 95 (LEAF 94)(LEAF 93))) (NODE 92 (NODE 91 (LEAF 90)(LEAF 89)) (NODE 88 (LEAF 87)(NODE 86 (LEAF 85)(LEAF 84))))

fold1 op b [] = b
fold1 op b (x:xs) = fold1 op (op b x) xs

a = [1, 2, 3]
f b = let 
        foo x y = x * y * b
      in 
        fold:1 foo 1 a   
x = f 5

mystery any = let
                foo z [] = []
                foo z (x:xs) = (x:z):(foo (x:z) xs)

                helper [] = [0]
                helper (y:ys) = y ++ (helper ys)
    in
        map helper (foo [] any)

foo z [] = []
foo z (x:xs) = (x:z):(foo (x:z) xs)
y = foo [1,2,3]