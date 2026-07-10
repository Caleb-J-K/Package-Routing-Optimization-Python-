"""
Unit tests for the DistanceTable class.
"""

import unittest

from src.distance_table import DistanceTable
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DISTANCE_FILE = DATA_DIR / "distance_file.csv"


class TestDistanceTable(unittest.TestCase):

    def setUp(self):
        """
        Creates a DistanceTable instance loaded with test data.
        """
        
        self.distance_table = DistanceTable()

        self.distance_table.load_distances(DISTANCE_FILE)

    def test_address_count(self):
        """
        Verify every delivery locations was loaded from the csv file.
        """

        self.assertEqual(
            len(self.distance_table.addresses),
            27
        )

    def test_first_address_loaded(self):
        """
        Verify the first address is WGU.
        """

        self.assertIn(
            "Western Governors University",
            self.distance_table.addresses[0]
        )

    def test_distance_between_two_locations(self):
        """
        Verify a known distance is returned correctly.
        """

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
        """
        Verify the table works in both directions.

        The CSV only stores half of the distance matrix,
        so this confirms our lookup logic handles reversal.
        """

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
        """
        Distance from a location to itself should be zero.
        """

        address = self.distance_table.addresses[0]

        distance = self.distance_table.get_distance(
            address,
            address
        )

        self.assertEqual(
            distance,
            0.0
        )

    def test_invalid_address(self):
        """
        Verify that an unknown address raises an error.
        """

        with self.assertRaises(ValueError) as context:
            self.distance_table.get_distance(
                "Fake Address",
                self.distance_table.addresses[0]
            )

if __name__ == "__main__":
    unittest.main()