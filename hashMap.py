'''
This class holds the structure of a hashMap
Where the insult is the key
and the fittness score as deremined by the nlp.py class
is the value

'''
class HashMap:
        def __init__(self):
                self.size = 1000
                self.map = [None] * self.size
        #Hash function
        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size

        #adds the insult and the fittness_score to hashMap
        def add(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
                #checks to see if it's already in the map
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                    #adds the new insults to the map
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True
        #checks map to see if insult is already in HashMap
        #if it is then it returns the value if not returns false
        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None

        #sets list of keys
        def keys(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr

        #print for debugging
        def print(self):
                print('Insult Terms Already Found')
                for item in self.map:
                        if item is not None:
                                print(str(item))
