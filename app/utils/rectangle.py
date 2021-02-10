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
    def object_creator(self, all_rects_list):
        """Method: Loop over the list of all_rectangles and return them in a list of objects"""
        rects = []
        for i, v in enumerate(all_rects_list):
            rects.append(Rectangle(i, v["x"], v["y"], v["delta_x"], v["delta_y"]))
        return rects

    @classmethod
    def get_first_union(self, all_rects_list_obj):
        """Method: Returns the rectangle unions where every rectangle is
        compared with the rest in the list"""
        intersections = []
        for i in range(len(all_rects_list_obj)):  # Loop over all rectangles
            for j in range(i + 1, len(all_rects_list_obj)):  # Loop over again
                coordinates = Rectangle.area(all_rects_list_obj[i], all_rects_list_obj[j])
                if coordinates:
                    rectObj = Rectangle(
                        [all_rects_list_obj[i].index, all_rects_list_obj[j].index],
                        coordinates[0],
                        coordinates[1],
                        coordinates[2],
                        coordinates[3]
                    )
                    intersections.append(rectObj)
        return intersections

    @classmethod
    def get_union(self, all_rects_list_obj, intersections):
        """Method: Returns the rectangle unions comparing the original list of rectangles
        with the previous unions """
        intersections2 = []
        tempIndex = []
        for i in range(len(intersections)):
            for j in range(len(all_rects_list_obj)):
                if not j in intersections[i].index:  # No need to compare with the rectangle that is part of the index.
                    coordinates = Rectangle.area(intersections[i], all_rects_list_obj[j])
                    if coordinates:
                        index = sorted((intersections[i].index + [all_rects_list_obj[j].index]))
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
        """Method: Returns the union area between two rectangles if it is above 0"""
        xmin = max(a.x, b.x)  # x cord for first intersection
        xmax = min(a.x2, b.x2)  # x cord for last intersection
        ymin = max(a.y, b.y)  # y cord for first intersection
        ymax = min(a.y2, b.y2)  # y cord for last intersection
        dx = min(a.x2, b.x2) - max(a.x, b.x)
        dy = min(a.y2, b.y2) - max(a.y, b.y)
        if (dx > 0) and (dy > 0):
            return [xmin, ymin, dx, dy]
