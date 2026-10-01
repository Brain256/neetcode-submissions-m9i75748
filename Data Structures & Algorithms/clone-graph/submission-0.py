"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        newNodes = {}
        newNodes[node] = Node(node.val)

        q = deque([node])

        while q: 

            cur = q.popleft()

            for nei in cur.neighbors: 
        
                if nei not in newNodes: 
                    q.append(nei)
                    newNodes[nei] = Node(nei.val)

                newNodes[cur].neighbors.append(newNodes[nei])
            
        return newNodes[node]

