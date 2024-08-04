# in this class i get the data from the graph and create a matrix(2D array to display the whole graph),
# grapg (all the connections) and vertecies
class CreateGraph:
    # default constructor with values of graph, matrix and vertecies
    def __init__(self) -> None:
        self.__INT_MAX = 2147483647
        self.__txt_data = self.read_file_into_tuple()
        self.__verticies = self.__txt_data[0][0]
        self.__graph = self.__txt_data[1:]
        self.__matrix = self.create_matrix()

    # basic way to read data from a txt file in python
    def read_file_into_tuple(self):
        # here I open the txt file and input the data into a tuple (tupe is an imutable data type in python)
        with open('C:\\Users\\danny\\Desktop\\Python_dev\\homework5\\lol.txt', 'r') as file:
            content = file.readlines()
            content_list = [tuple(int(num) for num in line.strip().split()) for line in content]
            content_tuple = tuple(content_list)
        return content_tuple

    # here I create a matrix (a 2D array) that represents the graph
    def create_matrix(self):
        # created a 2D array and filled it with INT_MAX (INT_MAX means no connection)
        matrix_list = [[self.__INT_MAX] * self.__verticies for _ in range(self.__verticies)]
        # here i fill the array
        for i in self.__graph:
            matrix_list[int(i[0])][int(i[1])] = int(i[2])
            matrix_list[int(i[1])][int(i[0])] = int(i[2])  # Because the graph is undirected
        
        # i make the matrix a tuple
        matrix = tuple(tuple(row) for row in matrix_list)

        return matrix

    # below I created properties of classes. The reason is to make it easier to work with the class
    @property
    def verticies(self):
        return self.__verticies

    @property
    def matrix(self):
        return self.__matrix

    @property
    def graph(self):
        return self.__graph

# my own stack implemination
class Stack:
    # basic default constructor that has size, top pos and the stack itself (array wise)
    def __init__(self, size) -> None:
        self.INT_MAX = 2147483647
        self.size = size
        self.top = -1
        self.stack = [self.INT_MAX] * self.size

    # chesking if stack is empty
    def stack_empty(self) -> bool:
        # in python its a for loop that retuns if condition is true and retuens false if its not true
        return self.top == -1

    # remove element from stack
    def pop(self):
        # if stack empty then not good
        if self.stack_empty():
            raise IndexError("Underflow")
        # else remove the element
        else:
            self.stack[self.top] = self.INT_MAX
            self.top -= 1

    # add element to stack
    def push(self, val):
        # if stack is full then not good
        if self.top == self.size - 1:
            raise IndexError("Overflow")
        # else add the element to the stack
        else:
            self.top += 1
            self.stack[self.top] = val

    # like in rhe prev class I have created class properties for easy use of class
    @property
    def top_val(self):
        return self.stack[self.top]

    # this property was made for debugging and checking purposes
    @property
    def print_all(self):
        # if empty then print nothing
        if self.stack_empty():
            print("")
        else:
            # else print the stack out
            for i in range(0, self.top + 1):
                print(self.stack[i], end=' ')
            print()


class DFS:
    # basic default constructor that has verticies and matrix
    def __init__(self, verticies, matrix):
        self.INT_MAX = 2147483647
        self.verticies = verticies
        self.matrix = matrix

    # here I created a private(not accesable from main) function to find unvisited vertecies
    def __check_unvisited_verticies(self, adjacent_vertecies, visited):
        # basic for loop that checks for unvisited vert from the adj vertecies
        for i in adjacent_vertecies:
            if i != self.INT_MAX and not visited[i]:
                return True
        return False

    # private function to get unvisited vertecies
    def __get_unvisited_vertex(self, adjacent_vertecies, visited) -> int:
        # basic for loop to get the first unvisited adj vertecie
        for i in adjacent_vertecies:
            if i != self.INT_MAX and not visited[i]:
                return i

    # private function to get the vertecies 
    def __get_vrticies(self, adjacent_vertecies):
        # basic for loop that cheks if the connection is INT_MAX(means no connection) then not good 
        # else we get the vertecie (since vert corresponds to the range in the for loop then we get the verticie)
        for i in range(len(adjacent_vertecies)):
            if adjacent_vertecies[i] != self.INT_MAX:
                adjacent_vertecies[i] = i
        return adjacent_vertecies

    # private function for the dfs algo
    def __dfs(self, v):
        # visited array full of false(nothing is visited yet)
        visited = [False] * self.verticies
        # create an empty stack and push v to it and specify v as visited
        s = Stack(self.verticies)
        s.push(v)
        visited[v] = True
        # continue until stack is empty
        while not s.stack_empty():
            # here i get the adj verticies
            adjacent_vertecies = self.__get_vrticies(list(self.matrix[s.top_val]))
            # if there are no unsited verticies then I pop
            if not self.__check_unvisited_verticies(adjacent_vertecies, visited):
                s.pop()
            else:
                # else I get the adj verticies and push them to the stack and mark them as visited
                u = self.__get_unvisited_vertex(adjacent_vertecies, visited)
                s.push(u)
                visited[u] = True
        return visited

    # private func to check if graph is connected
    def __check_if_connected(self):
        # for loop to go over all the vertecies
        for i in range(self.verticies):
            # if all of the visited are true that means graphn is connected
            visited = self.__dfs(i)
            if not all(visited):
                return False
        return True

    # property to make it easier to work with the class
    @property
    def connected(self):
        return self.__check_if_connected()


class MST:
    # initialize MST class with private variabels which are number of vertices, adjacency matrix, and graph edges
    def __init__(self, verticies, matrix, graph) -> None:
        self.INT_MAX = 2147483647
        self.__verticies = verticies
        self.__matrix = matrix
        self.__graph = [list(sub_tuple) for sub_tuple in graph]

    # here i crated a prive class called __Set to represent a disjoint set data strucrure
    class __Set:
        # initialize the set class for union-find operations
        def __init__(self, size) -> None:
            # initialize rank and parent arrays for union find structure
            self.__rank = [0] * size
            self.__parent = [0] * size

        # create a set for each vertex by initializing parent pointers to themselves
        def make_set(self):
            for i in range(len(self.__parent)):
                self.__parent[i] = i

        # find the root of the set containing vertex `vertecie`
        def find_set(self, vertecie):
            if self.__parent[vertecie] != vertecie:
                # path compression (used in union find data structure)
                self.__parent[vertecie] = self.find_set(self.__parent[vertecie])
            return self.__parent[vertecie]

        # union of two sets 
        def union(self, u, v):
            # get the initial sets
            root_u = self.find_set(u)
            root_v = self.find_set(v)
            # Union by rank 
            if root_u != root_v:
                # if the rank of u is bigger then rank of v then the parent of v is u
                if self.__rank[root_u] > self.__rank[root_v]:
                    self.__parent[root_v] = root_u
                # if the rank of v is bigger then rank of u then the parent of u is v
                elif self.__rank[root_u] < self.__rank[root_v]:
                    self.__parent[root_u] = root_v
                # else parent of v is u
                else:
                    self.__parent[root_v] = root_u
                    self.__rank[root_u] += 1

    # sort edges by weight using selection sort(implemented in prev hw)
    def __selection_sort(self):
        # get length
        n = len(self.__graph)
        # iterate over the array
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                # get the minimum edge weight in the unsorted part of the array
                if self.__graph[j][2] < self.__graph[min_idx][2]:
                    min_idx = j
            # swap the found minimum element with the first element
            self.__graph[i], self.__graph[min_idx] = self.__graph[min_idx], self.__graph[i]

    # private function for implementation of Kruskal
    def __mst_kruskal(self):
        # initialize the result array(full of None)
        A = [[None, None, None] for _ in range(self.__verticies - 1)]
        # create a set for each vertex
        s = self.__Set(self.__verticies)
        s.make_set()
        # sort edges by weight
        self.__selection_sort()
        pos_to_add = 0
        for connection in self.__graph:
            u, v, weight = int(connection[0]), int(connection[1]), connection[2]
            # if including this edge doesn't cause a cycle
            if s.find_set(u) != s.find_set(v):
                # include it in the result
                A[pos_to_add] = [u, v, weight]
                pos_to_add += 1
                # union the two vertices
                s.union(u, v)
        return A

    # vertex class for prims algo
    class __Vertex:
        # default constructor with key, parent and verticie
        def __init__(self, vert=None) -> None:
            self.__INT_MAX = int(2147483647)
            self.key = self.__INT_MAX
            self.parent = None
            self.verticie = vert

    class __Queue:
        # initialize min heap priority queue wirh head, size and max_size
        def __init__(self, size) -> None:
            self.heap = [None] * size
            self.size = 0
            self.max_size = size

        # return index of left child
        def left(self, i):
            return 2 * i + 1

        # return index of right child
        def right(self, i):
            return 2 * i + 2

        # return index of parent
        def parent(self, i):
            return (i - 1) // 2

        # build a min heap from the current heap
        def build_min_heap(self):
            for i in range(self.size // 2, -1, -1):
                self.min_heapify(i)

        # maintain the min heap property
        def min_heapify(self, i):
            # get left and right
            l = self.left(i)
            r = self.right(i)
            # assume current node is the smallest
            smallest = i
            # check if left child exist and is smaller 
            if l < self.size and self.heap[l].key < self.heap[i].key:
                smallest = l
            # check if the right child exists and is smaller
            if r < self.size and self.heap[r].key < self.heap[smallest].key:
                smallest = r
            if smallest != i:
                # swap the current node with the smallest child and heapify the smallest child
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                self.min_heapify(smallest)

        # insert a new key into the priority queue
        def insert(self, key):
            # if full not good
            if self.size >= self.max_size:
                raise IndexError("insert into a full priority queue")
            # else insert
            self.heap[self.size] = key
            self.size += 1

        # Extract the minimum key from the priority queue
        def extract_min(self):
            # if empty then not good
            if self.size == 0:
                raise IndexError("extract_min from an empty priority queue")
            # else get first value and min heapify again
            root = self.heap[0]
            # replace the first value with last
            self.heap[0] = self.heap[self.size - 1]
            # equate the extracted value to None
            self.heap[self.size - 1] = None
            # decrease size
            self.size -= 1
            # heapify again
            self.min_heapify(0)
            return root

        # decrease the key value of a given vertex
        def decrease_key(self, vertex, new_key):
            # iterarte over heap to find the vertex
            for i in range(self.size):
                # if current element matches then update the key of found vertex to the new key
                if self.heap[i].verticie == vertex:
                    self.heap[i].key = new_key
                    # move the node up until the heap property is restored
                    while i > 0 and self.heap[self.parent(i)].key > self.heap[i].key:
                        self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                        i = self.parent(i)
                    break

        # check if a vertex is in the queue
        def in_queue(self, vertex):
            # basic for loop over the heap
            for verticie in self.heap:
                # if already extracted then continue (now the vertex but in general)
                if verticie is None:
                    continue
                # if found then good
                if verticie.verticie == vertex:
                    return True
            # else bad
            return False
        
        # properties of classes to make it easier to work with
        @property
        def min(self):
            return self.extract_min()

        # basic print for debug purposses
        @property
        def print_queue(self):
            # basic for loop to get all the elements. skip iteration if vertex is None
            for vertex in self.heap:
                if vertex is None:
                    continue
                print(f"{vertex.verticie} - {vertex.key}", end=" ")

    # Prims algorihm (private)
    def __mst_prim(self):
        # initialize vertices with their keys set to INT_MAX
        v = [self.__Vertex(i) for i in range(self.__verticies)]
        for u in v:
            u.key = self.INT_MAX
            u.parent = None
        # set the key of the first vertex to 0
        v[0].key = 0

        # initialize priority queue with all vertices
        Q = self.__Queue(self.__verticies)
        for vertex in v:
            Q.insert(vertex)

        # build the min-heap
        Q.build_min_heap()

        # array to store MST edges
        mst = [None] * (self.__verticies - 1)
        pos = 0
        
        while Q.size != 0:
            u = Q.min
            # if the vertex has a parent, add the edge to the MST
            if u.parent is not None:
                mst[pos] = [u.parent, u.verticie, u.key]
                pos += 1
            for i in range(self.__verticies):
                weight = self.__matrix[u.verticie][i]
                # if there is a connection and the vertex is in the queue and the weight is less than the current key
                if weight != 0 and weight != self.INT_MAX and Q.in_queue(i) and weight < v[i].key:
                    v[i].parent = u.verticie
                    v[i].key = weight
                    Q.decrease_key(i, weight)

        return mst

    # basic properties to make it easer to work with class
    @property
    def kruskal(self):
        return self.__mst_kruskal()

    @property
    def prim(self):
        return self.__mst_prim()

# implemntaion of dejikstra and bellman ford
class SSSP:
    # same defualt constructor as in previous classes
    def __init__(self, verticies, matrix, graph) -> None:
        self.INT_MAX = 2147483647
        self.__verticies = verticies
        self.__matrix = matrix
        self.__graph = [list(sub_tuple) for sub_tuple in graph]
    
    # similar queue to what implemnted previously
    class __Queue:
        def __init__(self, size) -> None:
            self.heap = [None] * size
            self.size = 0
            self.max_size = size

        def left(self, i):
            return 2 * i + 1

        def right(self, i):
            return 2 * i + 2

        def parent(self, i):
            return (i - 1) // 2

        def build_min_heap(self):
            for i in range(self.size // 2, -1, -1):
                self.min_heapify(i)

        def min_heapify(self, i):
            l = self.left(i)
            r = self.right(i)
            smallest = i
            if l < self.size and self.heap[l].d < self.heap[i].d:
                smallest = l
            if r < self.size and self.heap[r].d < self.heap[smallest].d:
                smallest = r
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                self.min_heapify(smallest)

        def insert(self, key):
            if self.size >= self.max_size:
                raise IndexError("insert into a full priority queue")
            self.heap[self.size] = key
            self.size += 1

        def extract_min(self):
            if self.size == 0:
                raise IndexError("extract_min from an empty priority queue")
            root = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap[self.size - 1] = None
            self.size -= 1
            self.min_heapify(0)
            return root

        def decrease_key(self, vertex, new_key):
            for i in range(self.size):
                if self.heap[i].vertecie == vertex:
                    self.heap[i].d = new_key
                    while i > 0 and self.heap[self.parent(i)].d > self.heap[i].d:
                        self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                        i = self.parent(i)
                    break

        def in_queue(self, vertex):
            for verticie in self.heap:
                if verticie is None:
                    continue
                if verticie.vertecie == vertex:
                    return True
            return False

        @property
        def min(self):
            return self.extract_min()

        @property
        def print_queue(self):
            for vertex in self.heap:
                if vertex is None:
                    continue
                print(f"{vertex.vertecie} - {vertex.d}", end=" ")

    # vertex class similar to previous implmentaion to help with implemnting dejikstra
    class __Vertex:
        def __init__(self, vert) -> None:
            self.INT_MAX = 2147483647
            self.d = self.INT_MAX
            self.p = None
            self.vertecie = vert

    def __sp_dejikstra(self):
        # initialize vertecies array 
        vertercies = [self.__Vertex(i) for i in range(self.__verticies)]
        # distance to source is set to 0
        vertercies[0].d = 0
        # create a priority queue
        Q = self.__Queue(self.__verticies)
        # insert vertecies into queue
        for vertex in vertercies:
            Q.insert(vertex)
        # build the (min heap) queue
        Q.build_min_heap()
        
        while Q.size != 0:
            # get minimum and get adj verts
            u = Q.min
            adj_verteices_weight = self.__matrix[u.vertecie]
            # go over all vertecies and relax edges
            for v in range(self.__verticies):
                # skip if no edge
                if adj_verteices_weight[v] == self.INT_MAX or v == u.vertecie:
                    continue
                # relax edge if a shorter path is found
                if vertercies[v].d > (u.d + adj_verteices_weight[v]):
                    # update distance to vertex v
                    vertercies[v].d = u.d + adj_verteices_weight[v]
                    # set the parent of v to u
                    vertercies[v].p = u
                    # dec the key val in priority queue
                    Q.decrease_key(vertercies[v].vertecie, vertercies[v].d)
        return [[v.vertecie, v.d, self.__get_path(v)] for v in vertercies]

    def __get_path(self, vertex):
        # get empty array to store the path
        path = []
        # get current vertex
        current = vertex
        # create a set to keep track of visited verts(for cycle detection)
        visited = set()  
        # traverse from curent vertex to the source
        while current is not None:
            # check if the current node is visited 
            if current.vertecie in visited:
                break
            # add the vertex to the visited set
            visited.add(current.vertecie)
            # insert the current vertex at the begining of path array
            path.insert(0, current.vertecie)  
            # move to the parent of the current vertex
            current = current.p
        return path

    def __sp_bellman_ford(self):
        # created empty array for verteices
        vertercies = [self.__Vertex(i) for i in range(self.__verticies)]
        # set the distance to 0 to the source
        vertercies[0].d = 0
        # relax all edges __vertecies - 1 times
        for _ in range(self.__verticies - 1):
            for u, v, w in self.__graph:
                # if the dist to vertex u is not INT_MAX and a shorter path to v is found
                if vertercies[u].d != self.INT_MAX and vertercies[v].d > vertercies[u].d + w:
                    # update the distance to vertex v
                    vertercies[v].d = vertercies[u].d + w
                    # set the parent of v to u
                    vertercies[v].p = vertercies[u]
        # check for negative weight            
        for u, v, w in self.__graph:
            # if a shorter path v is found a negative weight cycle exists
            if vertercies[u].d != self.INT_MAX and vertercies[v].d > vertercies[u].d + w:
                return False, [(v.vertecie, v.d, self.__get_path(v)) for v in vertercies]
        
        return True, [(v.vertecie, v.d, self.__get_path(v)) for v in vertercies]

    # regular properies of the class for easy access
    @property
    def dejikstra(self):
        return self.__sp_dejikstra()

    @property
    def bellman_ford(self):
        return self.__sp_bellman_ford()

def main():
    # create graph
    graph_create = CreateGraph()
    matrix = graph_create.matrix
    verticies = graph_create.verticies
    graph = graph_create.graph
    # do the DFS and check if graph is connected
    dfs_create = DFS(verticies, matrix)
    if not dfs_create.connected:
        print("The graph is not connected.")
        return
    else:
        print("The graph is connected.")
    # MST for kruskals and prims
    mst_create = MST(verticies, matrix, graph)
    kruskal_result = mst_create.kruskal
    prim_result = mst_create.prim
    print("Kruskal's MST:", kruskal_result)
    print("Prim's MST:", prim_result)
    # SSSP for dejikstra and bellman ford
    sssp_create = SSSP(verticies, matrix, graph)
    dijkstra_result = sssp_create.dejikstra
    bellman_ford_result, bellman_ford_paths = sssp_create.bellman_ford
    print("Dijkstra's shortest paths:")
    for v, d, path in dijkstra_result:
        print(f"Vertex {v}: distance {d}, path {path}")
    if bellman_ford_result:
        print("Bellman-Ford shortest paths:")
        for v, d, path in bellman_ford_paths:
            print(f"Vertex {v}: distance {d}, path {path}")
    else:
        print("Bellman-Ford detected a negative-weight cycle.")

if __name__ == "__main__":
    main()