import utils
from collections import namedtuple


def main():

    Rectangles = utils.Ingest("path to file")  # Initilize the ingestions
    Rectangles.loadFile()
    Rectangles.readFile()

    ob = utils.Solution()
    all_rectangles = Rectangles._rects

    intersections = []
    for i in range(len(all_rectangles)):  # Loop over all rectangles
        for j in range(i + 1, len(all_rectangles)):  # Loop over again
            ra = ob.process(all_rectangles[i])
            rb = ob.process(all_rectangles[j])
            coordinates = ob.area(ra, rb)
            if coordinates:
                intersections.append({
                    "index": [i, j],
                    "coordinates": {
                        "x": coordinates[0],
                        "y": coordinates[1],
                        "delta_x": coordinates[2],
                        "delta_y": coordinates[3],
                    }
                })

    for i in range(len(intersections)):
        for j in range(len(all_rectangles)):
            if not j in intersections[i]["index"]:  # No need to compare with the rectangle that is part of the index.
                #print(i, j, intersections[i])
                ra = ob.process(intersections[i]["coordinates"])
                rb = ob.process(all_rectangles[j])
                coordinates = ob.area(ra, rb)
                if coordinates:
                    index = sorted((intersections[i]["index"] + [j]))
                    intersections.append({
                        "index": index,
                        "coordinates": {
                            "x": coordinates[0],
                            "y": coordinates[1],
                            "delta_x": coordinates[2],
                            "delta_y": coordinates[3],
                        }
                    })
               #print(coordinates, intersections[i]["index"], j)

    for i in range(len(intersections)):
        print(intersections[i])


main()
