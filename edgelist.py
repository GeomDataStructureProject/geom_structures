class vertex:
    def __init__(self, point, halfEdge):
        self.point = point
        self.halfEdge = halfEdge

class halfEdge:
    def __init__(self, point1, point2, face, direction):
        self.point1 = point1
        self.point2 = point2
        self.face = face
        self.direction = direction

class face:
    def __init__(self, halfEdge1, halfEdge2):
        self.halfEdge1 = halfEdge1
        self.halfEdge2 = halfEdge2