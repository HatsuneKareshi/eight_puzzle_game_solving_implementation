from puzzle_module import *
from collections import deque
from itertools import count # new. remove if it messes thigns up
import heapq



def dfs_8puzzle_solve(puzzle):
    visited_set = set()
    frontier = []
    frontier.append((puzzle, []))
    
    while len(frontier) > 0:
        cur_puz_state, path = frontier.pop()

        if cur_puz_state in visited_set:
            continue
                
        visited_set.add(cur_puz_state)
        if(cur_puz_state.heuristics() == 0):
            return cur_puz_state, path + [cur_puz_state]

        next_moves = cur_puz_state.get_possible_move()
        for mv in next_moves:
            nb = cur_puz_state.move_ret_anew(mv)
    
            if nb in visited_set:
                continue

            frontier.append((nb, path + [cur_puz_state]))
        # finds neighbors and shoves them in. no path tracking yet
    return None, None

def bfs_8puzzle_solve(puzzle):
    visited_set = set()
    frontier = deque()
    frontier.append((puzzle, []))
    
    while len(frontier) > 0:
        cur_puz_state, path = frontier.popleft()

        if cur_puz_state in visited_set:
            continue
                
        visited_set.add(cur_puz_state)
        if(cur_puz_state.heuristics() == 0):
            return cur_puz_state, path + [cur_puz_state]

        next_moves = cur_puz_state.get_possible_move()
        for mv in next_moves:
            nb = cur_puz_state.move_ret_anew(mv)
    
            if nb in visited_set:
                continue

            frontier.append((nb, path + [cur_puz_state]))
        # finds neighbors and shoves them in. no path tracking yet
    return None, None

def a_star_8puzzle_solve(puzzle):
    counter = count() # tie breaker thing for the minheap
    visited_set = set()
    frontier = []
    heapq.heappush(frontier, (puzzle.heuristics(), next(counter), puzzle, []))

    while(len(frontier) > 0):
        cur_f, _, cur_puz_state, path = heapq.heappop(frontier)

        if cur_puz_state in visited_set:
            continue
        visited_set.add(cur_puz_state)

        if(cur_puz_state.heuristics() == 0):
            return cur_puz_state, path + [cur_puz_state]
        
        next_moves = cur_puz_state.get_possible_move()
        for mv in next_moves:
            nb = cur_puz_state.move_ret_anew(mv)
            if(nb in visited_set):
                continue

            new_path = path + [cur_puz_state]
            heapq.heappush(frontier, (nb.heuristics() + len(new_path), next(counter), nb, new_path))

    return None, None