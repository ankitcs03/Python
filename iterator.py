## If you want to add an iterator behaviour to your class, you have to add the __iter__ and the __next__ method to
## your class. The __iter__ method returns an iterator object. If the class contains a __next__,it is enough for 
## the __iter__ method to return self, i.e. a reference to itself:

class Reverse:
    """iterate a sequence in reverse order"""

    def __init__ (self,data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1 
        return self.data[self.index]

lst = [1,2,3,4,5,6]
for item in Reverse(lst):
    print(item)
    
## output will be:
## 6
## 5
## 4
## 3
## 2
