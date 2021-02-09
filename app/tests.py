import json
import subprocess
import unittest
from utils.ingest import Ingest


class TestIngest(unittest.TestCase):

    def test_loadReadFile(self):
        subprocess.call(["touch", "testfile.json"], shell=True)
        testjson = {
            "rects": [
                {"x": 100, "y": 100, "delta_x": 250, "delta_y": 80},
                {"x": 120, "y": 200, "delta_x": 250, "delta_y": 150},
                {"x": 140, "y": 160, "delta_x": 250, "delta_y": 100},
                {"x": 160, "y": 140, "delta_x": 350, "delta_y": 190}
            ]}

        with open("testfile.json", "w") as outfile:
            json.dump(testjson, outfile)

        data = Ingest("./testfile.json")
        subprocess.call(["rm", "testfile.json"], shell=True)

        self.assertEqual(data._rects, testjson['rects'])

    def test_read_input(self):
        """
        Test that we can read input.
        """

        #result = data._rects


if __name__ == '__main__':
    unittest.main()
