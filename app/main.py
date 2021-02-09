from utils.ingest import Ingest
from utils.rectangle import Rectangle
import sys


def main():
    path_to_file = sys.argv[1]
    allRectangles = Ingest(path_to_file)  # Initilize the ingestions

    rects = []
    for i, v in enumerate(allRectangles._rects):
        rects.append(Rectangle(i, v["x"], v["y"], v["delta_x"], v["delta_y"]))

    Union1 = Rectangle.get_first_union(rects)
    Union2 = Rectangle.get_union(rects, Union1)
    Union3 = Rectangle.get_union(rects, Union2)
    for i in range(len(Union1)):
        print(Union1[i].x, Union1[i].y, Union1[i].delta_x, Union1[i].delta_y, Union1[i].index)
    for i in range(len(Union2)):
        print(Union2[i].x, Union2[i].y, Union2[i].delta_x, Union2[i].delta_y, Union2[i].index)
    for i in range(len(Union3)):
        print(Union3[i].x, Union3[i].y, Union3[i].delta_x, Union3[i].delta_y, Union3[i].index)


main()
