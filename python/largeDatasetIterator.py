# LargeDatasetIterator.py

class LargeDatasetIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
        

#small number
numbers = [1, 2, 3, 4, 5]
 
iterator = LargeDatasetIterator(numbers)

 
for number in iterator:
    print(number)



#large number
largeNumbers = list(range(1, 1001))


largeIterator = LargeDatasetIterator(largeNumbers)

for number in largeIterator:
    print(number)