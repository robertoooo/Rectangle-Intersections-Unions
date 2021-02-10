import json
import subprocess
import unittest
from utils.ingest import Ingest
from utils.rectangle import Rectangle
import pytest


class TestClass(unittest.TestCase):

    def test_ingest_read_1(self):
        """Test the Ingest class methods loadFile and readFile"""
        subprocess.call(["touch", "testfile.json"], shell=True)
        testinput1 = {
            "rects": [
                {"x": 100, "y": 100, "delta_x": 250, "delta_y": 80},
                {"x": 120, "y": 200, "delta_x": 250, "delta_y": 150},
                {"x": 140, "y": 160, "delta_x": 250, "delta_y": 100},
                {"x": 160, "y": 140, "delta_x": 350, "delta_y": 190}
            ]}

        with open("testfile.json", "w") as outfile:
            json.dump(testinput1, outfile)

        data = Ingest("./testfile.json")
        subprocess.call(["rm", "testfile.json"], shell=True)

        self.assertEqual(data._rects, testinput1['rects'])
        self.__class__._rects = data

    def test_ingest_read_2(self):
        """Test the Ingest class methods loadFile and readFile"""
        subprocess.call(["touch", "testfile.json"], shell=True)
        testinput2 = {
            "rects": [
                {"x": 100, "y": 100, "delta_x": -250, "delta_y": 80},
                {"x": 120, "y": 200, "delta_x": 250, "delta_y": 150},
                {"x": "140", "y": 160, "delta_x": 250, "delta_y": 100},
                {"x": 160, "y": 140, "delta_x": 350, "delta_y": 190}
            ]}

        with open("testfile.json", "w") as outfile:
            json.dump(testinput2, outfile)

        data = Ingest("./testfile.json")
        subprocess.call(["rm", "testfile.json"], shell=True)
        self.assertEqual(data.loadStatus, False)

    def test_rectangle_object_creator(self):
        rects_list_obj = Rectangle.object_creator([{'x': -100, 'y': 100, 'delta_x': 250, 'delta_y': 80}])
        self.assertEqual(rects_list_obj[0].x, -100)
        self.assertEqual(rects_list_obj[0].delta_y, 80)

    def test_rectangle_get_first_union(self):
        rects_list_obj = [Rectangle(0, 100, 100, 50, 50), Rectangle(1, 50, 50, 60, 60)]
        unions = Rectangle.get_first_union(rects_list_obj)
        self.assertEqual(unions[0].x, 100)
        self.assertEqual(unions[0].delta_y, 10)
        self.assertEqual(unions[0].index, [0, 1])
