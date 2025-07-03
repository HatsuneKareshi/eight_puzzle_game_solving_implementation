from puzzle_module import *
from collections import deque
from itertools import count # new. remove if it messes thigns up
import heapq



def dfs_8puzzle_solve(puzzle, tracing=False):
    expansion_cnt = 0
    max_frtr = 0
    # stats. return these in a tuple

    visited_set = set()
    frontier = []
    frontier.append((puzzle, []))

    if tracing:
        print("WARNING: DEPTH FIRST SEARCH MAY LEAD TO SPECTACULARLY LONG PATHS. \nCONTINUE AT YOUR OWN PERIL")
        choice = input("press [y] and enter to continue. anything else to return and skip search.")
        if(choice != "y" and choice != "Y" ):
            return None, None, (expansion_cnt, max_frtr)
        
    
    while len(frontier) > 0:
        cur_puz_state, path = frontier.pop()

        if tracing:
            print("currently expanding:")
            print(cur_puz_state)

        if cur_puz_state in visited_set:
            continue
                
        visited_set.add(cur_puz_state)
        if(cur_puz_state.heuristics() == 0):
            return cur_puz_state, path + [cur_puz_state], (expansion_cnt, max_frtr)

        next_moves = cur_puz_state.get_possible_move()
        if tracing:
            print("neighbors:")

        for mv in next_moves:
            nb = cur_puz_state.move_ret_anew(mv)
    
            if nb in visited_set:
                continue

            if tracing:
                print(nb)
                print("___")

            frontier.append((nb, path + [cur_puz_state]))

        max_frtr = max(len(frontier), max_frtr)
        expansion_cnt += 1
        
        if tracing:
            _ = input("enter to continue next iteration")
        # finds neighbors and shoves them in. no path tracking yet
    return None, None, (expansion_cnt, max_frtr)

def bfs_8puzzle_solve(puzzle, tracing=False):
    expansion_cnt = 0
    max_frtr = 0
    # stats. return these in a tuple

    visited_set = set()
    frontier = deque()
    frontier.append((puzzle, []))
    
    while len(frontier) > 0:
        cur_puz_state, path = frontier.popleft()
        
        if tracing:
            print("currently expanding:")
            print(cur_puz_state) 

        if cur_puz_state in visited_set:
            continue
                
        visited_set.add(cur_puz_state)
        if(cur_puz_state.heuristics() == 0):
            return cur_puz_state, path + [cur_puz_state], (expansion_cnt, max_frtr)

        next_moves = cur_puz_state.get_possible_move()
        if tracing:
            print("neighbors:")

        for mv in next_moves:
            nb = cur_puz_state.move_ret_anew(mv)
    
            if nb in visited_set:
                continue
            
            if tracing:
                print(nb)
                print("___")

            frontier.append((nb, path + [cur_puz_state]))
        
        max_frtr = max(len(frontier), max_frtr)
        expansion_cnt += 1

        if tracing:
            _ = input("enter to continue next iteration")
        # finds neighbors and shoves them in. no path tracking yet
    return None, None, (expansion_cnt, max_frtr)

def a_star_8puzzle_solve(puzzle, tracing=False):
    expansion_cnt = 0
    max_frtr = 0
    # stats. return these in a tuple

    counter = count() # tie breaker thing for the minheap
    visited_set = set()
    frontier = []
    heapq.heappush(frontier, (puzzle.heuristics(), next(counter), puzzle, []))

    while(len(frontier) > 0):
        cur_f, _, cur_puz_state, path = heapq.heappop(frontier)
        
        if tracing:
            print("currently expanding:")
            print(cur_puz_state) 

        if cur_puz_state in visited_set:
            continue
        visited_set.add(cur_puz_state)

        if(cur_puz_state.heuristics() == 0):
            return cur_puz_state, path + [cur_puz_state], (expansion_cnt, max_frtr)
        
        next_moves = cur_puz_state.get_possible_move()
        if tracing:
            print("neighbors:")

        for mv in next_moves:
            nb = cur_puz_state.move_ret_anew(mv)
            if(nb in visited_set):
                continue

            if tracing:
                print(nb)
                print("___")

            new_path = path + [cur_puz_state]
            heapq.heappush(frontier, (nb.heuristics() + len(new_path), next(counter), nb, new_path))

        max_frtr = max(len(frontier), max_frtr)
        expansion_cnt += 1
        
        if tracing:
            _ = input("enter to continue next iteration")

    return None, None, (expansion_cnt, max_frtr)