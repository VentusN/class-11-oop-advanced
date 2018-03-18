class OrderedDict(object):
    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        result = []
        for key, value in zip(self._keys,self._values):
            result.append((key,value))
        return result

    def __setitem__(self, key, value):
        if key in self._keys:
            for i, word in enumerate(self._keys):
                if key == word:
                    self._values[i] = value
        else:
            self._keys.append(key)
            self._values.append(value)
    
    def __getitem__(self, search_key):
        for key, value in zip(self._keys,self._values):
            if search_key == key:
                return value
        raise KeyError(repr(search_key))
    
    def __contains__(self, item):
        return bool(item in self._keys)
        
    def __len__(self):
        return len(self.items())
        
    def __eq__(self,other):
        return self.items() == other.items()
    
    def __ne__(self,other):
        return not self == other
        
    def __str__(self):
        s= '{'
        for key, value in zip(self._keys, self._values):
            s += '{key}: {value}, '.format(key=repr(key),value=repr(value))
        
        s=s.rstrip(', ')
        s+='}'
        return s
        
    __repr__ =__str__
    
    def __add__(self,other):
        result = {}
        new_keys= self._keys + other._keys
        new_values = self._values + other._values
        for key, value in zip(new_keys,new_values):
            result[key]=value
        return result
        
    @classmethod
    def from_keys(cls,sequence):
        result = {}
        for elem in sequence:
            result[elem]=None
        return result
            
            
