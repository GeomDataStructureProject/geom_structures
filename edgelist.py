
#pylint: disable = line-too-long, too-many-lines, no-name-in-module, import-error, multiple-imports, pointless-string-statement, wrong-import-order, invalid-name, missing-function-docstring, missing-class-docstring, consider-using-enumerate
import matplotlib.pyplot as plt
import numpy as np
import random
import time

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
    def print(self):
        print("Point:", self.x, ',', self.y, 'has', len(self.half_edges), "half edges")

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
    def print(self):
        print("Half edge with origin:", self.origin.x, ',', self.origin.y,
              "Points to: ", self.dual.origin.x, ',', self.dual.origin.y, 
              "Has face:", self.face!=0,
              "Has next:", self.next!=0,
              "Has prev:", self.prev!=0)

class Face:
    '''Face class, stores list of all adjacent halfedges'''
    def __init__(self):
        self.halfEdgeList = []
    def addHalfEdge(self, hedge):
        self.halfEdgeList.append(hedge)
    def print(self):
        print("List of half edges:")
        for i in range(len(self.halfEdgeList)):
           self.halfEdgeList[i].print()


class DCEL:
    '''Stores three arrays holding all of the vertices, halfedges, and faces'''
    def __init__(self):
        self.vertices = []
        self.half_edges = []
        self.faces = []
    def show(self):
        print("VERTICES:")
        for v in self.vertices:
            v.print()

        print("HALFEDGES")
        for h in self.half_edges:
            h.print()

        print("FACES")
        for f in self.faces:
            f.print()

    def getVertex(self, v):
        '''Returns the vertex already stored in the DCEL vertices list, or 0 if it doesn't exit yet'''
        for vertex in self.vertices:
            if v == vertex:
                return v
        return 0
    def getHalfEdge(self, origin, front):
        ''''Returns the half edge that has origin ORIGIN, and is pointing towards FRONT'''
        for half_edge in self.half_edges:
            if half_edge.origin == origin and half_edge.dual.origin == front:
                return half_edge
        return 0 #If not in list return 0
    
def leftOf(a, b, c):
    signedArea = (b.getX() - a.getX())*(c.getY() - a.getY()) - (b.getY() - a.getY())*(c.getX() - a.getX())
    return signedArea > 0

def makeTriangle(points, Dcel): #Points is list of points, 3 points lon 
    for point in points: #Appends points to DCEL vertice list if not already in the list
        if(Dcel.getVertex(point) == 0):
            Dcel.vertices.append(point)
    #Creates list of potential edges to be added to DCEL
    edge_list = [[points[0], points[1]], [points[1], points[2]], [points[2], points[0]]]
    for edge in edge_list:
        v1 = edge[0] #Points
        v2 = edge[1]
        if Dcel.getHalfEdge(v1, v2) == 0: #NEW HALF_EDGES DONT EXIST YET
            h1 = HalfEdge(v1)
            h2 = HalfEdge(v2)
            h1.setDual(h2)
            h2.setDual(h1)
            Dcel.half_edges.append(h1) #APPEND TO LIST OF HALF EDGES
            Dcel.half_edges.append(h2)
            v1.addHalfEdge(h1)
            v2.addHalfEdge(h2)
    new_face = Face()
    for i in range (0, 3): #Loops through all the edgess, and sets next and prevs
        hedge = Dcel.getHalfEdge(edge_list[i%3][0], edge_list[(i+1)%3][1]) #Computes next, prev, halfedge
        nxt = Dcel.getHalfEdge(edge_list[(i+1)%3][0], edge_list[(i+2)%3][1])
        prev = Dcel.getHalfEdge(edge_list[(i-1)%3][0], edge_list[i%3][1])

        hedge.setNext(nxt) #Sets next, prev, and face values
        hedge.setPrev(prev)
        hedge.setFace(new_face)

        new_face.addHalfEdge(hedge) #Sets half edge to the corresponding face
        
    Dcel.faces.append(new_face)

        
    
  
        
        
    

# random point generation
def randPoints(numPoints, low, high):
    points = []

    for i in range(numPoints):
        points.append(Vertex(random.uniform(low, high), random.uniform(low, high)))

    return points
    
# plotting points
def addToPlot(Dcel):
    points = Dcel.vertices
    x = []
    y = []
    for pt in points:
        x.append(pt.getX())
        y.append(pt.getY())
        plt.scatter(pt.getX(), pt.getY(), s = 100)

    x = np.array(x)
    y = np.array(y)
    print(x)
    print(y)

    for i in Dcel.half_edges:
        dX = i.dual.origin.x - i.origin.x
        dY = i.dual.origin.y - i.origin.y
        shift_x = 0.01
        shift_y = 0.01
        # Changes which way is "left"
        if dX <= 0:
            shift_x = -0.01
        elif dY <= 0:
            shift_y = -0.01
        plt.arrow(i.origin.x + shift_x, i.origin.y + shift_y, dX, dY, head_width=0.05, length_includes_head=True)

    # Add on last coordinate to the end
    #x = np.append(x, x[0]) # add X coordinate
    #y = np.append(y, y[0]) # add Y coordinate
    #plt.plot(x, y)
    plt.show()

def sortByX(points):
    #x = []
    #for pt in points:
    #    x.append(pt.getX())

    swapped = False # used for deterining whether to exit loop permaturely

    for i in range(len(points) - 1):
        for j in range(len(points) - i - 1):
            if points[j+1].x < points[j].x:
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

    for i in range(len(vertexList)):
        # find last left
        if leftOf(vertexList[i], vertexList[i+1], newPoint):
            firstPoint = i+1
            print(firstPoint)
        # find last right
        if not leftOf(vertexList[i], vertexList[i+1], newPoint):
            secondPoint = i+1
            if i + 1 == len(vertexList):
                if leftOf(vertexList[i+1],vertexList[1],newPoint):
                    break
            elif leftOf(vertexList[i+1],vertexList[i+2],newPoint):
                break
    # append actual points and return list
    print("returned from findVisible: ", firstPoint, secondPoint)
    return firstPoint, secondPoint
    

def incrementalTriangulate(points, DCEL):
    '''Calls makeTriangle with the correct triangles in the incremental triangulation'''
    points = sortByX(points)
    hull = [points[0], points[1], points[2]]
    if points[1].y > points[2].y:
        hull[1], hull[2] = hull[2], hull[1]
    makeTriangle(hull, DCEL)
    #vertex_list = [points[0], points[1], points[2]]
    #double_edge_list = [HalfEdge(points[0]), HalfEdge(points[1]), HalfEdge(points[2])]
    #hull = [points[0], points[1], points[2]] 

    hull.append(points[0])
        
    for i in range(3, len(points)):
        #points = sortByX(points)
        leftmost, rightmost = findVisible(points[i], hull)
        for j in range(leftmost, rightmost):
            newTriangle = [hull[j],points[i],hull[j+1]]
            makeTriangle(newTriangle, DCEL)
        addToPlot(DCEL)
    



        # removes all points in between (not in hull)
        print("i:", i, "leftmost:", leftmost, "rightmost:", rightmost)
        hull = hull[:leftmost] + [points[i]] + hull[rightmost:]
        print("hull:", hull)
            
            
#pts = randPoints(6, -10, 10)




#pts = randPoints(10, -10, 10)
#pts = sortByX(pts)                

A = Vertex(1,1)
B = Vertex(3,1)
C = Vertex(2,3)
D = Vertex(3,3)
E = Vertex(4,4)
pts = [A, B, C, D, E]

DCEL_data = DCEL() #Creates Dcel object
#makeTriangle(pts, DCEL_data)
incrementalTriangulate(pts, DCEL_data)
#DCEL_data.show()

addToPlot(DCEL_data)
