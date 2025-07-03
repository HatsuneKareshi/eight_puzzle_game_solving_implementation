from algorithms import *
import time


def bench_once(shuffle_iter = 100):
    sample = puzzle_o_eight()
    sample.self_legal_shuffle(shuffle_iter)
    print(sample)

    bfs = puzzle_o_eight(sample)
    astar = puzzle_o_eight(sample)
    dfs = puzzle_o_eight(sample)

    start = time.perf_counter()
    res, p, stats = bfs_8puzzle_solve(bfs)
    end = time.perf_counter()
    if(res is None):
        print("NON-SOLVABLE TIME!!!")
        print("execution time for bfs this run: ", end - start)
    else:
        print("final state (BFS):")
        print(res)
        print("execution time for bfs this run: ", end - start)
        print("number of steps in solution: ", len(p))
        print("nodes expanded:", stats[0])
        print("max frontier count:", stats[1])
        print("==========================")


    start = time.perf_counter()
    res, p, stats = a_star_8puzzle_solve(astar)
    end = time.perf_counter()
    if(res is None):
        print("NON-SOLVABLE TIME!!!")
        print("execution time for a*  this run: ", end - start)
    else:
        print("final state (A*):")
        print(res)
        print("execution time for a*  this run: ", end - start)
        print("number of steps in solution: ", len(p))
        print("nodes expanded:", stats[0])
        print("max frontier count:", stats[1])
        print("==========================")

    start = time.perf_counter()
    res, p, stats = dfs_8puzzle_solve(dfs)
    end = time.perf_counter()
    if(res is None):
        print("NON-SOLVABLE TIME!!!")
        print("execution time for dfs this run: ", end - start)
    else:
        print("final state (DFS):")
        print(res)
        print("execution time for dfs this run: ", end - start)
        print("number of steps in solution: ", len(p))
        print("nodes expanded:", stats[0])
        print("max frontier count:", stats[1])

# sample = puzzle_o_eight()
# sample.self_legal_shuffle(4)

# bfs = puzzle_o_eight(sample)
# a_star = puzzle_o_eight(sample)

# print("8-puzzle PROBLEM:")
# print(sample)

# print("\nBFS:")
# bfs_8puzzle_solve(bfs, True)

# _ = input("ENTER TO CONTINUE TO A*")

# print("\nA*")
# a_star_8puzzle_solve(a_star, True)

bench_once(25)

# Should you want to run something yourself:
# puzzle_o_eight() constructor returns a new object representing the puzzle, in its completed state. to use, simply
# puzzle0 = puzzle_o_eight()
# puzzle1 = puzzle_o_eight(puzzle0) # to clone from puzzle0
# to shuffle, use puzzle0.self_legal_shuffle(cnt). cnt is number of random moves to move in. 
# usage of self_random_shuffle(cnt) is not recommended, since it can create unsolvable puzzles.
# to use the algorithms:
# bfs_8puzzle_solve(puzzle0) # this returns 3 things, the final state (completed puzzle); a list of all the states in the solution, and tuple containing expanded count and max frontier.
# bfs_8puzzle_solve(puzzle0, True) sets tracing to true. in tracing mode, the algorithm displays current node, as well as all neighbors. to step through each iteration, press enter. 