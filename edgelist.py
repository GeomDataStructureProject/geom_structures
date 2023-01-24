import matplotlib.pyplot as plt
import numpy as np
import random

#pylint: disable = line-too-long, too-many-lines, no-name-in-module, import-error, multiple-imports, pointless-string-statement, wrong-import-order, invalid-name, missing-function-docstring, missing-class-docstring, consider-using-enumerate
class Vertex:
    '''Vertex class, stores an x, y value, and pointer list of adjacent halfedges'''
    def __init__(self, point):
        self.point = point
        self.halfEdgeList = 0
    def getX(self):
        return self.point[0]
    def getY(self):
        return self.point[1]

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
    def setNext(self, next):
        self.next = next
    def setPrev(self, prev):
        self.prev = prev

class Face:
    '''Face class, stores list of all adjacent halfedges'''
    def __init__(self, half_edge_list):
        self.halfEdgeList = half_edge_list


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
    
def leftOf(a, b, c):
    signedArea = (b.getX() - a.getX())*(c.getY() - a.getY()) - (b.getY() - a.getY())*(c.getX() - a.getX())
    return signedArea > 0

def findVisible(p, edgeList):
    '''Returns all visible points to the left from given point, idk how to do this'''
    

def incrementalTriangulate(points):
    '''Given a list of sorted points, returns Double edge list of the incremental triangulation of the points'''
    vertex_list = [points[0], points[1], points[2]]
    double_edge_list = [HalfEdge(points[0]), HalfEdge(points[1]), HalfEdge(points[2])]
    
    for i in range(points):
        visible_points = findVisible(i, )
        for j in range(visible_points()):
            
pts = randPoints(10, -10, 10)
pts = sortByX(pts)




a = Vertex((1,2), 0)
b = Vertex((3,2), 0)
b.print()

half_a = HalfEdge(0, 0, 0, 0, b)
half_b = HalfEdge(0, half_a, 0, 0, a)
half_a.setDual(half_b)

half_a.dual[0].origin[0].print()