class Listas:
    def __init__(self, n):
        elementos=[]
        size=n

    # Add at end of list
    def append(self, element):
        elementos[self.size:] = [element]
        size+=1
    
    #def 

class Node:
    def __init__(self, id):
        self.id=id

class Edge:
    def __init__(self, nodeFrom, nodeTo):
        self.nodeFrom=nodeFrom
        self.nodeTo=nodeTo

class Graph:
    def __init__(self):
        self.nodes=[]
        self.edges=[]

    def addNode(self, id):
        self.nodes.append(Node(id))

    def addEdge(self, nodeFrom, nodeTo):
        self.nodes.append(Edge(nodeFrom, nodeTo))

if __name__ == "__main__":
    print("hello")