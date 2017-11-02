import Test.QuickCheck

fact2 0 = 1
fact2 n = n * fact2(n-1)
 
getstuff = do
             putStrLn "Enter stuff"
             x <- getLine
             putStrLn x
-- is this a comment? yes

newhead = head [1,2,3,4]

newtake = take 3 [5,4,3,2,1]

newtail = tail [10,9,8,7,6]

