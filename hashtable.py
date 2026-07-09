

class HashTable:

    #initialize the hash table with a given size
    def __init__(self, size=40):
        self.size = size
        #create a list of empty lists of (size)
        self.table = [[] for _ in range(size)]

    #converts package ID into a valid table index
    def _hash(self, key):
        return int(key) % self.size
    
    def insert(self, package_id, package_data):
        #find the bucket this package belongs in
        index = self._hash(package_id)

        #check if the package already exists
        for i, (key, value) in enumerate(self.table[index]):
            #if the package already exists, update its data
            if key == package_id:
                self.table[index][i] = (package_id, package_data)
                return
            
        #if the package does not exist, add it to the bucket
        self.table[index].append((package_id, package_data))

    def search(self, package_id):
        #find the correct bucket
        index = self._hash(package_id)

        #search every item the bucket
        for key, value in self.table[index]:
            if key == package_id:
                return value
        
        #package ID not found
        return None
