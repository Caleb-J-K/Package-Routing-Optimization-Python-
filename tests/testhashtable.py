import unittest
from hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table = HashTable()

    def test_insert_and_search(self):
        package = "Package Data"

        self.table.insert(1, package)

        result = self.table.search(1)

        self.assertEqual(result, package)


    def test_search_missing_package(self):
        result = self.table.search(99)

        self.assertIsNone(result)


    def test_update_existing_package(self):
        self.table.insert(1, "Old Package")

        self.table.insert(1, "Updated Package")

        result = self.table.search(1)

        self.assertEqual(result, "Updated Package")


    def test_collision_handling(self):
        # Default table size is 40
        # 1 and 41 will hash to the same bucket

        self.table.insert(1, "Package One")
        self.table.insert(41, "Package Forty One")

        self.assertEqual(
            self.table.search(1),
            "Package One"
        )

        self.assertEqual(
            self.table.search(41),
            "Package Forty One"
        )


if __name__ == "__main__":
    unittest.main()