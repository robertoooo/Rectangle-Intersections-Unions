import json

from jsonschema import validate


class Ingest:
    """Inititate the Rectangle class with path to .json file as argument"""

    def __init__(self, path) -> (None):
        self._path = path
        self.loadStatus = self.loadFile()
        if (self.loadStatus is not False):
            self.readstatus = self.readFile()

    def loadFile(self):
        """Loads the .json file, validates the schema """

        schema = {
            "type": "object",
                    "required": [
                        "rects"
                    ],
            "properties": {
                        "rects": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": [
                                    "x",
                                    "y",
                                    "delta_x",
                                    "delta_y"
                                ],
                                "properties": {
                                    "x": {
                                        "type": "integer",
                                    },
                                    "y": {
                                        "type": "integer",
                                    },
                                    "delta_x": {
                                        "type": "integer",
                                        "minimum": 0,
                                    },
                                    "delta_y": {
                                        "type": "integer",
                                        "minimum": 0,
                                    }
                                }
                            }
                        }
                    }
        }

        try:
            with open(self._path) as f:
                self._rects = json.load(f)
        except Exception as e:
            self.error = "Failed to load file, check the path or the format of the file"
            return False

        try:
            validate(instance=self._rects, schema=schema)
        except Exception as e:
            self.error = "\n\nCheck the input file schema above"
            print(e)
            return False

    def readFile(self):
        """Returns a list of rectangles """
        try:
            # Also possible to read the first key value, not restricting the read to the name "rects", but not implemented here.
            # Not really nececcary in this application but can be used for more advanced reads
            self._rects = self._rects['rects']
            return("List of rectangles read succesfully")
        except:
            self.error = "\n\nCould not find key value rects, see output above"
            return False
