class Node:
    value = ""
    children = []
    
    def __init__(self, val, dictionary):
        self.setValue(val)
        self.genChildren(dictionary)
    
    def __str__(self):
        return str(self.value)
    
    def setValue(self, val):
        self.value = val
        
    def genChildren(self, dictionary):
        if(isinstance(dictionary, dict)):
            self.children = dictionary.keys()
    
    