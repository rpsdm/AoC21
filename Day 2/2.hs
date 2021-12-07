import System.IO
import Data.List
import Data.Maybe

parse :: String -> (Char, Int)
parse xs = (xs !! 0, read (drop (ind+1) xs) :: Int)
    where ind = fromJust $ elemIndex ' ' xs

getInput :: IO [(Char, Int)]
getInput = do f <- readFile "2.txt"
              return $ map parse (lines f)

solve1 :: [(Char, Int)] -> Int
solve1 xs = h * v
    where h = sum [n | (d, n) <- xs, d == 'f']
          v = sum [if d == 'd' then n else -n | (d, n) <- xs, d /= 'f']

solve2 :: [(Char, Int)] -> Int
solve2 xs = part2 xs 0 0 0

part2 :: [(Char, Int)] -> Int -> Int -> Int -> Int
part2 [] _ h v = h * v
part2 ((d, x):rst) a h v = part2 (rst) (new_a) (new_h) (new_v)
    where new_a = case d of 'd' -> a + x
                            'u' -> a - x
                            otherwise -> a
          new_h = if d == 'f' then h + x else h
          new_v = if d == 'f' then v + a * x else v

main :: IO()
main = do
    i <- getInput
    -- Part 1
    print $ solve1 i
    -- Part 2
    print $ solve2 i
