class Rectangle:
    def __init__(self, index, x, y, delta_x, delta_y):
        self.index = index
        self.x = x
        self.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.x2 = x + delta_x
        self.y2 = y + delta_y

    @classmethod
    def get_first_union(self, all_rectangles):
        intersections = []
        for i in range(len(all_rectangles)):  # Loop over all rectangles
            for j in range(i + 1, len(all_rectangles)):  # Loop over again
                coordinates = Rectangle.area(all_rectangles[i], all_rectangles[j])
                if coordinates:
                    rectObj = Rectangle(
                        [all_rectangles[i].index, all_rectangles[j].index],
                        coordinates[0],
                        coordinates[1],
                        coordinates[2],
                        coordinates[3]
                    )
                    intersections.append(rectObj)
        return intersections

    @classmethod
    def get_union(self, all_rectangles, intersections):
        intersections2 = []
        tempIndex = []
        for i in range(len(intersections)):
            for j in range(len(all_rectangles)):
                if not j in intersections[i].index:  # No need to compare with the rectangle that is part of the index.
                    coordinates = Rectangle.area(intersections[i], all_rectangles[j])
                    if coordinates:
                        index = sorted((intersections[i].index + [all_rectangles[j].index]))
                        if not index in tempIndex:  # Check that the combination have not been added
                            rectObj = Rectangle(
                                index,
                                coordinates[0],
                                coordinates[1],
                                coordinates[2],
                                coordinates[3]
                            )
                            intersections2.append(rectObj)
                        tempIndex.append(index)
        return intersections2

    @classmethod
    def area(self, a, b):  # returns None if rectangles don't intersect
        xmin = max(a.x, b.x)  # x cord for first intersection
        xmax = min(a.x2, b.x2)  # x cord for last intersection
        ymin = max(a.y, b.y)  # y cord for first intersection
        ymax = min(a.y2, b.y2)  # y cord for last intersection
        dx = min(a.x2, b.x2) - max(a.x, b.x)
        dy = min(a.y2, b.y2) - max(a.y, b.y)
        if (dx >= 0) and (dy >= 0):
            return [xmin, ymin, dx, dy]
