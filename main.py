from algorithms import *
import time


def bench_once():
    sample = puzzle_o_eight()
    sample.self_legal_shuffle(100)
    print(sample)

    bfs = puzzle_o_eight(sample)
    astar = puzzle_o_eight(sample)
    dfs = puzzle_o_eight(sample)

    start = time.perf_counter()
    res, p = bfs_8puzzle_solve(bfs)
    end = time.perf_counter()
    if(res is None):
        print("NON-SOLVABLE TIME!!!")
        print("execution time for bfs this run: ", end - start)
    else:
        print("final state:")
        print(res)
        print("execution time for bfs this run: ", end - start)
        print("number of steps in solution: ", len(p))


    start = time.perf_counter()
    res, p = a_star_8puzzle_solve(astar)
    end = time.perf_counter()
    if(res is None):
        print("NON-SOLVABLE TIME!!!")
        print("execution time for a*  this run: ", end - start)
    else:
        print("final state:")
        print(res)
        print("execution time for a*  this run: ", end - start)
        print("number of steps in solution: ", len(p))

    start = time.perf_counter()
    res, p = dfs_8puzzle_solve(dfs)
    end = time.perf_counter()
    if(res is None):
        print("NON-SOLVABLE TIME!!!")
        print("execution time for dfs this run: ", end - start)
    else:
        print("final state:")
        print(res)
        print("execution time for dfs this run: ", end - start)
        print("number of steps in solution: ", len(p))

# def avg_bench(iter):
#     time_bfs = 0
#     time_astar = 0
#     time_dfs = 0

#     for i in range(iter):
#         sample = puzzle_o_eight()
#         sample.self_legal_shuffle(100)
#         bfs = puzzle_o_eight(sample)
#         astar = puzzle_o_eight(sample)
#         dfs = puzzle_o_eight(sample)

#         start = time.perf_counter()
#         res, p = bfs_8puzzle_solve(bfs)
#         end = time.perf_counter()
#         time_bfs += end-start


#         start = time.perf_counter()
#         res, p = a_star_8puzzle_solve(astar)
#         end = time.perf_counter()
#         time_astar += end-start
        

#         # start = time.perf_counter()
#         # res, p = dfs_8puzzle_solve(dfs)
#         # end = time.perf_counter()
#         # time_dfs += end-start

    
#     print("AVERAGE OVER", iter, "RUNS:")
#     print("BFS\t: ", time_bfs / float(iter))
#     print("A*\t: ", time_astar / float(iter))
#     # print("DFS\t: ", time_dfs / float(iter))

# a = puzzle_o_eight()
# a.self_legal_shuffle(4)
# print("SOLVING FOR: ")
# print(a)
# print("SOLUTION BELOW")
# res, steps = dfs_8puzzle_solve(a, 1)
# for sp in steps:
#     print(sp)
#     print("next")

bench_once()