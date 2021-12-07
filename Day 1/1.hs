import System.IO

getInput :: IO [Int]
getInput = do f <- readFile "1.txt"
              return $ map (read :: String -> Int) (lines f)

eval :: Int -> Int -> Int -> Int
eval acc a b = acc + (fromEnum $ b > a)

solve :: [Int] -> Int -> Int -> Int
solve ls n acc
    | length ls < (n+1) = acc
    | otherwise = solve (tail ls) (n) $ eval (acc) (head ls) (ls !! n)

main :: IO()
main = do
    i <- getInput
    -- Part 1
    print $ solve i 1 0
    -- Part 2
    print $ solve i 3 0
