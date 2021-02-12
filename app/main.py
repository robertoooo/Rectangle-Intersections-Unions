import sys
from utils import Ingest, Rectangle, PrintRectangle


def main():
    # Use the input argument as path to file and ingest the file creating an all_rectangles object with the list of dictionaries
    try:  # Check if there is an input argument, otherwise inform.
        path_to_file = sys.argv[1]
        print(path_to_file)
        try:  # Depending on the error (if any), it will be infromed.

            # Initilize the ingestions
            all_rectangles = Ingest(path_to_file)

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
            serve_object = PrintRectangle(rects_list_obj, unions)
            serve_object.print_input()
            serve_object.print_output()
        except:
            print(all_rectangles.error)

    except:
        print("Please specify the path to the input json file")


main()
