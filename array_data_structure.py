class MyArray():
    def __init__(self):
        self.length = 0;
        self.data = {};
        
    def __str__(self):
        """"Print the array in Dictionary format with index as the key and elements as the values"""
        return str(self.__dict__);
    
    def get(self,index):
        """Get the element of the an array for a given index"""
        return self.data[index];
    
    def push(self,item):
        """Add a new item at the end of the array"""
        self.length += 1
        self.data[self.length-1] = item
        
    def pop(self):
        """Removes the last item from the array"""
        self.length -= 1
        last_item = self.data[self.length]
        del self.data[self.length]
        return last_item
    
    def delete(self,index):
        """Removing an element for a given index"""
        for i in range(index, self.length-1):
            self.data[i]=self.data[i+1];
        del self.data[self.length -1];
        self.length-=1;
        
    def insert(self,index,item):
        """Insert an item at certain index"""
        self.length +=1
        for i in range(index, self.length-1):
            self.data[i+1]=self.data[i]
        self.data[index]=item