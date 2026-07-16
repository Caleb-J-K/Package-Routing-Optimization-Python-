import unittest

from src.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):

        self.table = HashTable()

    def test_insert_and_search(self):

        package = "Package Data"

        self.table.insert(
            1,
            package
        )

        result = self.table.search(
            1
        )

        self.assertEqual(
            result,
            package
        )

    def test_search_missing_package(self):

        result = self.table.search(
            99
        )

        self.assertIsNone(
            result
        )

    def test_update_existing_package(self):

        self.table.insert(
            1,
            "Old Package"
        )

        self.table.insert(
            1,
            "Updated Package"
        )

        result = self.table.search(
            1
        )

        self.assertEqual(
            result,
            "Updated Package"
        )

    def test_collision_handling(self):

        # Package IDs 1 and 41 both hash to bucket 1 when the
        # default table size is 40.

        self.table.insert(
            1,
            "Package One"
        )

        self.table.insert(
            41,
            "Package Forty One"
        )

        self.assertEqual(
            self.table.search(1),
            "Package One"
        )

        self.assertEqual(
            self.table.search(41),
            "Package Forty One"
        )

    def test_multiple_packages(self):

        for package_id in range(1, 21):

            self.table.insert(
                package_id,
                f"Package {package_id}"
            )

        for package_id in range(1, 21):

            self.assertEqual(
                self.table.search(package_id),
                f"Package {package_id}"
            )


if __name__ == "__main__":
    unittest.main()