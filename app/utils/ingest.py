import json

from jsonschema import validate


class Ingest:
    """Inititate the Rectangle class with path to .json file as argument"""

    def __init__(self, path) -> (None):
        self._path = path
        self.loadStatus = self.loadFile()
        self.readstatus = self.readFile()

    def loadFile(self) -> (str):
        """Load the .json file """

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
            print("Failed to load file")
            print(e)
            return False

        try:
            validate(instance=self._rects, schema=schema)
            return True
        except Exception as e:
            print("Check the input file schema")
            print(e)
            return False

    def readFile(self) -> (str):
        """Returns a list of rectangles """
        try:
            self._rects = self._rects['rects']
            return("List of rectangles read succesfully")
        except:
            return("Could not find key value rects")
