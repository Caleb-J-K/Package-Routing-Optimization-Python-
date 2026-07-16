from src.package import Package

DEFAULT_TABLE_SIZE = 40


class HashTable:

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
        return key % self.size
    
    # Inserts a package into the hash table, replaces existing package data if the package ID already exists.
    def insert(self, package_id: int, package_data: Package) -> None:
        index = self._hash(package_id)

        # Replace existing package with updated data.
        for i, (key, _) in enumerate(self.table[index]):
            if key == package_id:
                self.table[index][i] = (package_id, package_data)
                return
            
        # If the package does not exist, add a new key-value pair.
        self.table[index].append((package_id, package_data))

    # Returns a package using its package ID.
    def search(self, package_id: int) -> Package | None:
        index = self._hash(package_id)

        for key, value in self.table[index]:
            if key == package_id:
                return value
        
        # Package ID not found.
        return None