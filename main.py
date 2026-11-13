from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    # Plain Dijkstra, but the heap key is the pair (weight, edges).
    # Python compares tuples left to right, so ties on weight are
    # broken by the number of edges for free.
    result = {}
    frontier = [(0, 0, source)]
    while frontier:
        weight, edges, v = heappop(frontier)
        if v in result:
            # already settled with a better (or equal) pair
            continue
        result[v] = (weight, edges)
        for neighbor, w in graph[v]:
            if neighbor not in result:
                heappush(frontier, (weight + w, edges + 1, neighbor))
    return result

    
