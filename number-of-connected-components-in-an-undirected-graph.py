def countComponentsA(n, edges):
    parents = list(range(n))

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    for e in edges:
        root1 = find(e[0])
        root2 = find(e[1])

        if root1 != root2:
            parents[root1] = root2
            n -= 1

    return n


def countComponentsB(n, edges):
    # Create a list to store the parent of each node
    parents = [-1] * n

    def find(parents, x):
        root = x
        # Traverse the parents list until we find a node with a parent of -1
        while parents[root] != -1:
            root = parents[root]
        # Return the root parent of the node
        return root

    # Iterate over each edge in the 'edges' list
    for e in edges:
        # Find the root parent of the first node in the edge
        root1 = find(parents, e[0])
        # Find the root parent of the second node in the edge
        root2 = find(parents, e[1])

        # If the root parents are different, they belong to different components
        if root1 != root2:
            # Update the parent of root1 to root2
            parents[root1] = root2
            # Decrement the count of components
            n -= 1

    # Return the final count of components
    return n
