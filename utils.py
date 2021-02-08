import json
from collections import namedtuple


class Ingest(object):
    """Inititate the Rectangle class with path to .json file as argument"""

    def __init__(self, path) -> (None):
        self._path = path

    def loadFile(self) -> (str):
        """Load the .json file """
        try:
            with open('./input.json') as f:
                self._rects = json.load(f)
            return("File opened succesfully")
        except:
            return("Could not find the file")

    def readFile(self) -> (None):
        """Returns a list of rectangles """
        try:
            self._rects = self._rects['rects']
            return("List of rectangles read succesfully")
        except:
            return("Could not find key value rects")


class Solution:

    def process(self, rect):
        Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')
        one_rectangle_processed = Rectangle(rect['x'], rect['y'], rect['x']+rect['delta_x'], rect['y']+rect['delta_y'])
        return(one_rectangle_processed)

    def area(self, a, b):  # returns None if rectangles don't intersect
        xmin = max(a.xmin, b.xmin)  # x cord for first intersection
        xmax = min(a.xmax, b.xmax)  # x cord for last intersection
        ymin = max(a.ymin, b.ymin)  # y cord for first intersection
        ymax = min(a.ymax, b.ymax)  # y cord for last intersection
        dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
        dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
        if (dx >= 0) and (dy >= 0):
            return [xmin, ymin, dx, dy]


class Intersect:
    def __init__(self, index, x, y, dx, dy):
        self.index = index
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        return
