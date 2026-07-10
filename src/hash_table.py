"""
Custom hash table implementation used to store and retrieve package data 
by package ID
"""

class HashTable:
    """
    Stores Package objects using their package ID as the key.
    Uses separate chaining to handle collisions.
    """

    #initialize the hash table with a given size.
    def __init__(self, size: int = 40):
        self.size = size
        #create a list of empty lists of (size)
        self.table = [[] for _ in range(size)]

    #converts package ID into a valid table index.
    def _hash(self, key) -> int:
        return int(key) % self.size
    
    #Computes the bucket index using the package ID.
    def insert(self, package_id: int, package_data):
        index = self._hash(package_id)

        #check if the package already exists.
        for i, (key, _) in enumerate(self.table[index]):
            
            #if the package already exists, update its data.
            if key == package_id:
                self.table[index][i] = (package_id, package_data)
                return
            
        #if the package does not exist, add it to the bucket
        self.table[index].append((package_id, package_data))

    #find the correct bucket.
    def search(self, package_id):
        index = self._hash(package_id)

        #search every key-value pair in the bucket for the package ID.
        for key, value in self.table[index]:
            if key == package_id:
                return value
        
        #package ID not found.
        return None
