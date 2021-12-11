import Data.List
import Data.Char(digitToInt)

getInput :: IO String
getInput = do f <- readFile "9.txt"
              return . intercalate "" $ lines f

getVal :: String -> Int -> Int -> Int
getVal st x y = digitToInt $ st !! (100 * x + y)

isValid :: Int -> Int -> Bool
isValid x y = (x >= 0) && (y >= 0) && (x <= 99) && (y <= 99)

adj :: String -> Int -> Int -> Int -> Bool
adj st x y val = if isValid x y then (getVal st x y) > val else True

risk :: String -> Int -> Int -> Int
risk st x y = (*) (fromEnum n) $ val + 1
    where
        val = getVal st x y
        n = adj st (x-1) y val && adj st (x+1) y val && adj st x (y-1) val && adj st x (y+1) val

part1 :: String -> Int -> Int -> Int
part1 _ 100 _ = 0
part1 st x 100 = part1 st (x+1) 0
part1 st x y = (+) (risk st x y) . part1 st x $ y+1

solve1 :: String -> Int
solve1 st = part1 st 0 0

main :: IO()
main = do
    i <- getInput
    -- Part 1
    print $ solve1 i
    -- Part 2
    -- no thanks ^^