# Lafalaise, Tedros
# Implements depth first search algorithm from book using nested functions.

# Sample adjacency matrix
sample_adjMaxtrix = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

# Sample vertices
sample_vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Depth first search algorithm
def depthFirstSearch(graph):
    # Init count
    count = 0
    # Init visited array
    visited = [0] * len(graph)

    # Nested dfs function
    def dfs(vertex):
        # Makes sure the nested function uses the count in the outer function
        nonlocal count
        # Increment count and set the order in which the vertex was visited
        count += 1
        visited[vertex] = count
        # For each adjacent vertex...
        for w in range(len(graph[vertex])):
            # If it hasn't been visited
            if graph[vertex][w] == 1 and visited[w] == 0:
                # Call nested dfs once again
                dfs(w)

    # For each vertex in the graph
    for v in range(len(graph)):
        # If we haven't visited
        if visited[v] == 0:
            # Called nested dfs
            dfs(v)

    # Return the order in which each vertex was visited
    return visited

# In order perform the depth first search, the user must input an adjacency matrix that represents the graph.
# This object is a matrix (n x n) of 0s and 1s where 0 at coordinate [i, j] means the ith vertex is not adjacent with the jth vertex. 
# If it is a 1, that means the ith vertex is adjacent with the jth vertex.

# The instructions to create the graph are given as the user uses the implementation.
# The vertices and their adjacency to other vertices are taken as space seperated lists before being inserted into an adjacency matrix.

# Main function that calls everything
def main():
    # First we get the name of the vertices
    vertices = input("What are the names of your vertices?\nPlease enter them as a list seperated by spaces, i.e. 'a b c d e f g':\n").split()

    # Creates empty adjacency matrix 
    adjMatrix = [[0 for i in range(len(vertices))] for j in range(len(vertices))]

    # For each given vertex
    for i in range(len(vertices)):
        # Get the adjacent vertices by name
        adj = input("What vertices are adjacent to vertex " + vertices[i] + "? Please enter them as a list seperated by spaces, i.e. 'a b c'.\n").split()
        # For each adjacent vertex given...
        for j in adj:
            # Get their index in the vertices array
            idx = vertices.index(j)
            # Set their adjacency in the current vertex's to 1
            adjMatrix[i][idx] = 1

    # Debugging print statements and sample code using the sample graphs
    #print(adjMatrix)
    #print(sample_adjMaxtrix)
    #print(depthFirstSearch(sample_adjMaxtrix))

    # Get the order in which each vertex was visited from DFS algorithm
    order = depthFirstSearch(adjMatrix)

    # Init final order array
    final = [0] * len(vertices)

    # For each vertex
    for i in range(len(vertices)):
        # Get the place of the vertex from the order array
        place = order[i]
        # Put it into the right index in the array
        final[place - 1] = vertices[i]

    # Print everything out in a "pretty" manner
    print("The vertices were visited in this order:")
    for i in range(len(final)):
        print(str(i + 1) + ". " + final[i])
    
# Call main function
main()