import System.IO

getInput :: IO [Int]
getInput = do f <- readFile "1.txt"
              return (map (read :: String -> Int) (lines f))

eval :: Int -> Int -> Int -> Int
eval acc a b = acc + (fromEnum $ b > a)

task :: [Int] -> Int -> Int -> Int
task ls n acc
    | length ls < (n+1) = acc
    | otherwise = task (tail ls) (n) $ eval (acc) (head ls) (ls !! n)

main :: IO()
main = do
    i <- getInput
    -- Task 1
    print $ task i 1 0
    -- Task 2
    print $ task i 3 0
