class Hash_Table():
    def __init__(self,size):
        self.size = size
        self.data = [None]*self.size #Initislize an array with size 'size'
    
    # Print the hash table in dictionary format
    def __str__(self):
        return str(self.__dict__)
    
        
    # Custom hash function to return the hash value for a key
    def _hash(self,key):
        custom_hash = 0
        for i in range(len(key)):
            custom_hash = (custom_hash + ord(key[i])*i) % self.size
        return custom_hash
    
    
    def set_key(self,key,value):
        custom_hash = self._hash(key)
        if not self.data[custom_hash]:
            self.data[custom_hash] = [[key,value]]
        else:
            self.data[custom_hash].append([[key,value]])
        #print(self.data)

        
    def get(self,key):
        custom_hash = self._hash(key)
        current = self.data[custom_hash]
        if current:
            for i in range (len(current)):
                if current[i][0] == key:
                    return current[i][1]
        return None
    
   
    def keys(self):
        key_array = []
        for i in range((self.size)):
            if self.data[i]:
                if len(self.data[i])>1:
                    for j in range(len(self.data[i])):
                        key_array.append(self.data[i][j][0])
                else:
                    key_array.append(self.data[i][0][0])
        return key_array