class MyIterator:
    def __init__(self,data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            result=self.data[self.index]
            self.index+=1
            return result
        else:
            raise StopIteration
list=[2,3,5,6,7,9]
it=MyIterator(list)
for iten in it:
    print(iten)