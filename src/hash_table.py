"""
Custom hash table implementation used to store and retrieve package data.

This implementation uses separate chaining to handle collisions and provides
efficient package lookup by package ID.
"""

from src.package import Package

DEFAULT_TABLE_SIZE = 40


class HashTable:
    """
    Hash table for storing Package objects using package ID as the key.

    The table uses separate chaining, where each index contains a list of
    key-value pairs. This allows multiple packages with different IDs to
    exist in the same bucket if a collision occurs.
    """

    # Initialize the hash table with a given size.
    def __init__(self, size: int = DEFAULT_TABLE_SIZE) -> None:
        self.size = size

        # Each bucket stores a list of (package_id, Package) pairs.
        self.table: list[list[tuple[int, Package]]] = [
            []
            for _ in range(size)
        ]

    # Converts package ID into a valid table index.
    def _hash(self, key: int) -> int:
        return key % self.size # Returns bucket index for the given package.
    
    # Inserts a package into the hash table, replaces existing package data if the package ID already exists.
    def insert(self, package_id: int, package_data: Package) -> None:
        index = self._hash(package_id)

        # Check if the package already exists.
        for i, (key, _) in enumerate(self.table[index]):
            
            # If the package already exists, update its data.
            if key == package_id:
                self.table[index][i] = (package_id, package_data)
                return
            
        # If the package does not exist, add a new key-value pair.
        self.table[index].append((package_id, package_data))

    # Returns a package using its package ID.
    def search(self, package_id: int) -> Package | None:
        index = self._hash(package_id)

        # Search every key-value pair in the bucket for the package ID.
        for key, value in self.table[index]:
            if key == package_id:
                return value
        
        # Package ID not found.
        return None
