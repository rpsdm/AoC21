import System.IO
import Data.List
import Data.Maybe

parse :: String -> [Int]
parse [] = []
parse xs = (read (take ind xs) :: Int):(parse $ drop (ind+1) xs)
    where ind = fromMaybe (length xs) (elemIndex ',' xs)

getInput :: IO [[Int]]
getInput = do f <- readFile "7.txt"
              return $ map (parse) (lines f)

solve1 :: [Int] -> Int
solve1 xs = sum [abs (x-m) | x <- xs]
    where m = (sort xs) !! (div (length xs) 2)

solve2 :: [Int] -> Int
solve2 xs = sum [div (n*(n+1)) (2) | n <- [abs (x-m) | x <- xs]]
    where m = div (sum xs) (length xs)

main :: IO()
main = do
    i <- getInput
    -- Part 1
    print $ solve1 $ i !! 0
    -- Part 2
    print $ solve2 $ i !! 0
