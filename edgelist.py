#pylint: disable = line-too-long, too-many-lines, no-name-in-module, import-error, multiple-imports, pointless-string-statement, wrong-import-order, invalid-name, missing-function-docstring, missing-class-docstring, consider-using-enumerate
class vertex:
    '''Vertex class, stores an x, y value, and pointer list of adjacent halfedges'''
    def __init__(self, point, adj_halfEdge):
        self.point = point
        self.halfEdgeList = adj_halfEdge
    def print(self):
        print(self.point)

class halfEdge:
    '''halfEdge class, stores pointers to: adjacent face, its dual, next and previous half edge, and its origin point '''
    def __init__(self, adj_face, dual_half_edge, next_half_edge, prev_half_edge, origin_point):
        self.face = [adj_face]
        self.dual = [dual_half_edge]
        self.next = [next_half_edge]
        self.prev = [prev_half_edge]
        self.origin = [origin_point]

    def setDual(self, dual):
        self.dual = [dual]

class face:
    '''Face class, stores list of all adjacent halfedges'''
    def __init__(self, half_edge_list):
        self.halfEdgeList = half_edge_list




a = vertex((1,2), 0)
b = vertex((3,2), 0)
b.print()

half_a = halfEdge(0, 0, 0, 0, b)
half_b = halfEdge(0, half_a, 0, 0, a)
half_a.setDual(half_b)

half_a.dual[0].origin[0].print()

a = [1]
b = a
a[0] = 2
print(b[0])
