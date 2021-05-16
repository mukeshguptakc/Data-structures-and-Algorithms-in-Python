
class AdjMatrixNonWeightedGraph:
    def __init__(self, vCount):
        self.vertCount = vCount
        self.edgeCount = 0
        self.mat = []
        for _ in range(self.vertCount):
            self.mat.append([0] * self.vertCount)

    def accept(self):
        self.edgeCount = int(input("Enter number of edges: "))
        print(f"Enter {self.edgeCount} edges -- src dest:")
        for _ in range(self.edgeCount):
            (src_str, dest_str) = input().split()
            (src, dest) = (int(src_str), int(dest_str))
            self.mat[src][dest]= 1
            self.mat[dest][src] = 1 # for undirected graph src -> dest ==> dest -> src

    def display(self):
        for i in range(self.vertCount):
            print(f"v{i}", end="")
            for j in range(self.vertCount):
                print("\t{}".format(self.mat[i][j]), end="")
            print()

if __name__=="__main__":
    graph = AdjMatrixNonWeightedGraph(6)
    graph.accept()
    graph.display()

"""
python AdjMatrixNonWeightedGraph.py
Enter number of edges: 7
Enter 7 edges -- src dest:
0 1
0 2
0 3
1 2
1 4
3 4
3 5
v0      0       1       1       1       0       0
v1      1       0       1       0       1       0
v2      1       1       0       0       0       0
v3      1       0       0       0       1       1
v4      0       1       0       1       0       0
v5      0       0       0       1       0       0
"""