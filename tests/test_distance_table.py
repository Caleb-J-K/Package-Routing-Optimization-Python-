import unittest
from pathlib import Path

from src.distance_table import DistanceTable


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DISTANCE_FILE = DATA_DIR / "distance_file.csv"


class TestDistanceTable(unittest.TestCase):

    def setUp(self):

        self.distance_table = DistanceTable()

        self.distance_table.load_distances(
            DISTANCE_FILE
        )

    def test_address_count(self):

        self.assertEqual(
            len(self.distance_table.addresses),
            27
        )

    def test_first_address_loaded(self):

        self.assertIn(
            "Western Governors University",
            self.distance_table.addresses[0]
        )

    def test_distance_between_two_locations(self):

        address1 = self.distance_table.addresses[0]
        address2 = self.distance_table.addresses[1]

        distance = self.distance_table.get_distance(
            address1,
            address2
        )

        self.assertEqual(
            distance,
            7.2
        )

    def test_distance_reverse_direction(self):

        address1 = self.distance_table.addresses[0]
        address2 = self.distance_table.addresses[1]

        forward = self.distance_table.get_distance(
            address1,
            address2
        )

        reverse = self.distance_table.get_distance(
            address2,
            address1
        )

        self.assertEqual(
            forward,
            reverse
        )

    def test_same_location_distance(self):

        address = self.distance_table.addresses[0]

        distance = self.distance_table.get_distance(
            address,
            address
        )

        self.assertEqual(
            distance,
            0.0
        )

    def test_find_full_address(self):

        full_address = self.distance_table.find_full_address(
            "1060 Dalton Ave S"
        )

        self.assertIn(
            "1060 Dalton Ave S",
            full_address
        )

    def test_invalid_address(self):

        with self.assertRaises(ValueError):

            self.distance_table.get_distance(
                "Fake Address",
                self.distance_table.addresses[0]
            )


if __name__ == "__main__":
    unittest.main()