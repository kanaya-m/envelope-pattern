
"""
Created on Thu Feb 25 9:01:49 2021

@author: Kanaya Malakar
"""

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
        
    def join_margins(self, margin1, margin2, reverse=False, color='green'):
        """margin1 and margin2 are two sides of the polygon.
        eg: a square can have margins 1, 2, 3 or 4.
        Sides are numbered sequentially, starting from a arbitrary edge."""
        self.margin1 = margin1
        self.margin2 = margin2
        self.reverse = reverse
        self.color = color
        self.upright_polygon()
        self.M1 = self.create_margin(self.poly[self.margin1%self.numSides], 
                                     self.poly[(self.margin1-1)%self.numSides])
        self.M2 = self.create_margin(self.poly[self.margin2%self.numSides], 
                                     self.poly[(self.margin2-1)%self.numSides])
        if self.reverse:
            self.M1 = np.flipud(self.M1)
        for item in range(len(self.M1)):
            self.draw_line(self.M1[item], self.M2[item])

    def draw_line(self, point1, point2):
        """Draws a line between two given points."""
        self.point1 = point1
        self.point2 = point2
        plt.axis('scaled')
        plt.plot((self.point1[0], self.point2[0]),\
                (self.point1[1], self.point2[1]), color=self.color)

    def create_margin(self, end1, end2):
        """Segment a given line specified by end points."""
        self.end1 = end1
        self.end2 = end2
        self.xmargin = np.linspace(self.end1[0], self.end2[0], 
                  self.segments+1)
        self.ymargin = np.linspace(self.end1[1], self.end2[1], 
                  self.segments+1)
        return np.column_stack([self.xmargin, self.ymargin])

    def create_polygon(self):
        """Creates a polygon with given number of sides."""
        self.intAngle = 2*np.pi/self.numSides
        self.angles = np.linspace(0, self.numSides, self.numSides+1\
                )*self.intAngle
        self.xpoly = self.outRadius*np.cos(self.angles)
        self.ypoly = self.outRadius*np.sin(self.angles)
        self.poly = np.column_stack([self.xpoly, self.ypoly])
        return self.poly

    def upright_polygon(self):
        """Put the created polygon upright, i.e. with it's base horizontal."""
        self.create_polygon()
        if self.numSides%2 == 1:
            self.rot_ang = np.pi/2.0
        elif self.numSides%2 == 0 and self.numSides%4 == 0:
            self.rot_ang = np.pi/self.numSides
        else:
            self.rot_ang = 0
        self.xrot = self.xpoly * np.cos(self.rot_ang) \
                             - self.ypoly * np.sin(self.rot_ang)
        self.yrot = self.xpoly * np.sin(self.rot_ang) \
                             + self.ypoly * np.cos(self.rot_ang)
        self.poly = np.column_stack([self.xrot, self.yrot])
        return self.poly
