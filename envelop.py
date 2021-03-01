import numpy as np
import matplotlib.pyplot as plt

class Envelope:
    """create pattern using the bounding envelopes.
    The sides are numbered from 1 to numSides in anticlockwise direction.
    For odd-sided polygons, side 1 is to the left of top vertex.
    For even sided polygons, side 1 is to the left of right center."""

    def __init__(self, numSides, outRadius=1, segments=10):
        self.numSides = numSides
        self.outRadius = outRadius
        self.segments = segments
        self.poly = np.array([])
        #self.color = 'red'
        self.create_polygon()
    
    def set_numsides(self, newnumsides):
        self.numSides = newnumsides
        self.create_polygon()
        
    def join_margins(self, margin1, margin2, reverse=False, color='green'):
        """Draws the line between two sides of the polygon.
        margin1 and margin2 are two sides of the polygon.
        eg: a square can have margins 1, 2, 3 or 4.
        Sides are numbered sequentially, starting from a arbitrary edge."""
        side11 = margin1 % self.numSides
        side12 = (margin1-1) % self.numSides
        side21 = margin2 % self.numSides
        side22 = (margin2-1) % self.numSides
        M1 = self.create_margin(self.poly[side11], self.poly[side12])
        M2 = self.create_margin(self.poly[side21], self.poly[side22])
        if reverse:
            M1 = np.flipud(M1)
        for item in range(len(M1)):
            draw_line(M1[item], M2[item], color)

    def draw_line(self, point1, point2, color):
        """Draws a line between two given points."""
        plt.axis('scaled')
        plt.plot((point1[0], point2[0]),\
                (point1[1], point2[1]), color=color)

    def create_margin(self, end1, end2):
        """Segment a given line specified by end points."""
        xmargin = np.linspace(end1[0], end2[0], self.segments+1)
        ymargin = np.linspace(end1[1], end2[1], self.segments+1)
        return np.column_stack([xmargin, ymargin])

    def create_polygon(self):
        """Creates a polygon with given number of sides."""
        intAngle = 2*np.pi/self.numSides
        angles = np.linspace(0, self.numSides, self.numSides+1 )* intAngle
        self.xpoly = self.outRadius*np.cos(angles)
        self.ypoly = self.outRadius*np.sin(angles)
        self.poly = np.column_stack([self.xpoly, self.ypoly])
        self.upright_polygon()

    def upright_polygon(self):
        """Put the created polygon upright, i.e. with it's base horizontal."""
        if self.numSides%2 == 1:
            rot_ang = np.pi/2.0
        elif self.numSides%2 == 0 and self.numSides%4 == 0:
            rot_ang = np.pi/self.numSides
        else:
            rot_ang = 0
        xrot = self.xpoly * np.cos(rot_ang) \
                             - self.ypoly * np.sin(rot_ang)
        yrot = self.xpoly * np.sin(rot_ang) \
                             + self.ypoly * np.cos(rot_ang)
        self.poly = np.column_stack([xrot, yrot])
        #return self.poly

def draw_line(point1, point2, color):
    """Draws a line between two given points."""
    plt.axis('scaled')
    plt.plot((point1[0], point2[0]),\
            (point1[1], point2[1]), color=color)