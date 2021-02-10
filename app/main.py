from utils.ingest import Ingest
from utils.rectangle import Rectangle
from utils.serve import Serve
import sys


def main():
    # Use the input argument as path to file and ingest the file creating an all_rectangles object with the list of dictionaries
    path_to_file = sys.argv[1]
    all_rectangles = Ingest(path_to_file)  # Initilize the ingestions

    # Loop over the list of all_rectangles and return them in a list of objects
    rects_list_obj = Rectangle.object_creator(all_rectangles._rects)

    # Produce the first set of unions
    unions = Rectangle.get_first_union(rects_list_obj)
    temp_union = unions

    # Loop that can handle as many unions there is
    while temp_union:
        union = Rectangle.get_union(rects_list_obj, temp_union)
        temp_union = union
        unions = unions + union

    # Serve object handles the prints
    serve_object = Serve(rects_list_obj, unions)
    serve_object.print_input()
    serve_object.print_output()


main()
