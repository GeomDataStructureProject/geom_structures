

class Vertex:
    '''Vertex class'''
    def __init__(self, coordinates_tuple, adjacent_half_edge):
        self.coord = coordinates_tuple
        self.half_edge = adjacent_half_edge
    
    def print(self):
        '''Prints coordinates'''
        print(self.coord[0][0])
        print(self.coord[0][1])



a = Vertex((1,2), 'test')
a.print()
    

