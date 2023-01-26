
#pylint: disable = line-too-long, too-many-lines, no-name-in-module, import-error, multiple-imports, pointless-string-statement, wrong-import-order, invalid-name, missing-function-docstring, missing-class-docstring, consider-using-enumerate

class Vertex:
    '''Vertex class, stores an x, y value, and pointer list of adjacent halfedges'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.half_edges = [] #array of every half edge whose origin is this vertex
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def addHalfEdge(self, half_edge):
        self.half_edges.append(half_edge)

class HalfEdge:
    '''halfEdge class, stores pointers to: adjacent face, its dual, next and previous half edge, and its origin point '''
    def __init__(self, origin_point):
        self.face = 0
        self.dual = 0
        self.next = 0
        self.prev = 0
        self.origin = origin_point
    
    def setFace(self, face):
        self.face = face
    def setDual(self, dual):
        self.dual = dual
    def setNext(self, next_edge):
        self.next = next_edge
    def setPrev(self, prev_edge):
        self.prev = prev_edge

class Face:
    '''Face class, stores list of all adjacent halfedges'''
    def __init__(self, half_edge_list):
        self.halfEdgeList = half_edge_list


class DCEL:
    '''Stores three arrays holding all of the vertices, halfedges, and faces'''
    def __init__(self):
        self.vertices = []
        self.half_edges = []
        self.faces = []

    def getVertex(self, v):
        '''Returns the vertex already stored in the DCEL vertices list, or 0 if it doesn't exit yet'''
        for vertex in self.vertices:
            if v == vertex:
                return v
        return 0
    def getHalfEdges(self, p1, p2):
        ''''Returns the two half edges that correspond to an edge between points p1 and p2''''
        for half_edge in self.half_edges:
            if half_edge.origin == p1 and half_edge.dual.origin == p2:
                return [half_edge, half_edge.dual]
        return 0
                
    def create_DCEL(self, points, edge_list): #EDGE LIST IS LIST OF EDGES IN THE TRIANGULATION, POINTS IS EVERY POINT
        '''Takes points, and list of edges as arguments to fill in all of the DCEL info'''
        for point in points:# This loop Appends each point to the list of points in the DCEL
            self.vertices.append(point) 
        for edge in edge_list: #This loop creates the half_edges, gives them their appropriate dual and appends them to the half_edge DCEL list, as well as gives each vertex its appropriate half_edge as well
            v1 = self.getVertex(edge[0]) #Retrieves the ACTUAL vertices in the DCEL object
            v2 = self.getVertex(edge[1])

            h1 = HalfEdge(v1) #Creates half_edges with respective origin points and sets them as eachothers dual
            h2 = HalfEdge(v2)
            h1.setDual(h2)
            h2.setDual(h1)

            v1.addHalfEdge(h1) #Appends appropriate half_edge to the DCEL list of half_edges for these vertices
            v2.addHalfEdge(h2)

            self.half_edges.append(h1)
            self.half_edges.append(h2)
    
        

def leftOf(a, b, c):
    signedArea = (b.getX() - a.getX())*(c.getY() - a.getY()) - (b.getY() - a.getY())*(c.getX() - a.getX())
    return signedArea > 0

def makeTriangle(points, DCEL): #Points is list of points, 3 points lon 
    for point in points: #Appends points to DCEL vertice list if not already in the list
        if(DCEL.get_vertex(point) == 0):
            DCEL.vertices.append(point)
    
    #Creates list of potential edges to be added to DCEL
    edge_list = [[points[0], points[1]], [points[1],points[2]], [points[2], points[0]]]
    half_edge_list = []
     
    for edge in edge_list:
        v1 = DCEL.getVertex(edge[0])
        v2 = DCEL.getVertex(edge[1])

        if half_edge_list in DCEL.half_edges:
            
        
        if DCEL.getHalfEdges(v1, v2 == 0): #NEW HALF_EDGES
            h1 = HalfEdge(v1)
            h2 = HalfEdge(v2)
            h1.setDual(h2)
            h2.setDual(v1)
            DCEL.half_edges.append(h1)
            DCEL.half_edges.append(h2)
            half_edge_list.append(h1)
        else:                       #HALF_EDGES ALREADY IN LIST
            edges = DCEL.getHalfEdges(v1, v2)
            h1 = edges[0]
            h2 = edges[1]
            half_edge_list.append(h1)
        
        v1.addHalfEdge(h1)
        v2.addHalfEdge(h2)
        #No way to check if half_edge already in half_edge list yet

        
    
    # Face
    f = Face(half_edge_list)
    DCEL.faces.append(f)
        
        
    

# random point generation
def randPoints(numPoints, low, high):
    points = []

    for i in range(numPoints):
        points.append(Vertex((random.randint(low, high), random.randint(low, high)), 0))

    return points
    
# plotting points
def addToPlot(points):
    pointsXY = [*zip(*points)] # turns points into two lists, one for x and another for y
    pointsXY = [np.array(pointsXY[0]), np.array(pointsXY[1])]
    plt.scatter(pointsXY[0], pointsXY[1])

    # Add on last coordinate to the end
    pointsXY[0] = np.append(pointsXY[0], pointsXY[0][0]) # add X coordinate
    pointsXY[1] = np.append(pointsXY[1], pointsXY[1][0]) # add Y coordinate
    plt.plot(pointsXY[0], pointsXY[1])

def sortByX(points):
    swapped = False # used for deterining whether to exit loop permaturely

    for i in range(len(points) - 1):
        for j in range(len(points) - i - 1):
            if points[j+1] < points[j]:
                swapped = True
                points[j], points[j+1] = points[j+1], points[j]
        if not swapped:
            break

    return points


def findList(firstPoint, secondPoint, vertexList):
    visibleList = []

    for i in range(firstPoint, secondPoint+1):
        visibleList.append(vertexList[i])
    
    return visibleList
    

def findVisible(newPoint, vertexList):
    '''Returns all visible points to the left from given point, idk how to do this'''
    firstPoint = 0
    secondPoint = 1

    for i in range(vertexList - 1):
        # find last left
        if leftOf(vertexList[i], vertexList[i+1], newPoint):
            firstPoint = i
        # find last right
        if not leftOf(vertexList[i], vertexList[i+1], newPoint):
            secondPoint = i + 1
            if i + 2 > len(vertexList):
                if leftOf(vertexList[i+1],vertexList[1],newPoint):
                    break
            elif leftOf(vertexList[i+1],vertexList[i+2],newPoint):
                break
    # append actual points and return list
    return firstPoint, secondPoint
    

def incrementalTriangulate(points, DCEL):
    '''Given a list of sorted points, returns Double edge list of the incremental triangulation of the points'''
    points = sortByX(points)
    DCEL.makeTriangle(points, DCEL)
    #vertex_list = [points[0], points[1], points[2]]
    #double_edge_list = [HalfEdge(points[0]), HalfEdge(points[1]), HalfEdge(points[2])]
    hull = [points[0], points[1], points[2]] 
    #note: sort the hull from lowest counterclockwise
    if points[1][1] > points[2][1]:
        hull[1], hull[2] = hull[2], hull[1]
    hull.append(points[0])
        
    for i in range(3, points):
        leftmost, rightmost = findVisible(points[i], hull)
        

        for j in range(leftmost, rightmost):
            newTriangle = [hull[j],points[i],hull[j+1]]
            makeTriangle(newTriangle, DCEL)

        # removes all points in between (not in hull)
        hull = hull[:leftmost] + points[i] + hull[rightmost:]
        
            
            
pts = randPoints(10, -10, 10)

a = Vertex((1,2), 0)
b = Vertex((3,2), 0)
b.print()

#pts = randPoints(10, -10, 10)
#pts = sortByX(pts)                

A = Vertex(1,1)
B = Vertex(3,1)
C = Vertex(2,3)


edges_in_triangulation = [ #This would be all of the edges in the triangulation, have a funciton ahead of time to find these
    [A,B],
    [B,C],
    [C,A]
]
abc = Face(edges_in_triangulation)
pts = [A, B, C]

DCEL_data = DCEL() #Creates Dcel object
DCEL_data.create_DCEL(pts, edges_in_triangulation)
