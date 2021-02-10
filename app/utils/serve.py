class Serve:
    def __init__(self, all_rectangles, unions):
        self.unions = unions
        self.all_rectangles = all_rectangles

    def print_input(self):
        print("Input: ")
        for i, v in enumerate(self.all_rectangles):
            print("\t{}: Rectangle at ({},{}), delta_x={}, delta_y={}.".format(
                i+1, v.x, v.y, v.delta_x, v.delta_y))

    def print_output(self):
        print("Intersections: ")
        for i, v in enumerate(self.unions):

            index_string = ""
            for j in range(len(v.index)):
                if(j+1 < len(v.index)):
                    index_string = index_string + "{} ".format(v.index[j]+1)
                else:
                    index_string = index_string + "and {}".format(v.index[j]+1)

            lenght = len(v.index)
            print("\t{0}: Between rectangle {1} at ({2},{3}), delta_x={4}, delta_y={5}.".format(
                i+1, index_string, v.x, v.y, v.delta_x, v.delta_y

            ))
