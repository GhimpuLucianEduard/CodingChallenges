from collections import defaultdict, deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, root):

        if root is None:
            return None

        visited = defaultdict(bool)
        visited[root.val] = True
        copy = defaultdict(Node)
        queue = deque()

        queue.append(root)

        while queue:
            node = queue.popleft()
            new_node = self.get_copy(node.val, copy)

            for child in node.neighbors:
                if not visited[child.val]:
                    visited[child.val] = True
                    new_node.neighbors.append(self.get_copy(child.val, copy))
                    queue.append(child)

        return copy[root.val]

    def get_copy(self, val, copies):
        if val in copies:
            return copies[val]
        else:
            return Node(val, [])

def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)
    print(Solution().cloneGraph(node1))


if __name__ == '__main__':
    main()
