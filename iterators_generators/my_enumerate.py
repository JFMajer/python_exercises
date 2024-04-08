class MyEnumerate:
    def __init__(self, data, start_index=0):
        if hasattr(data, '__iter__'):
            self.data = data
        else:
            raise TypeError("provided data is not iterable")
        self.start_index = start_index
        self.counter = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.data):
            raise StopIteration
        else:
            value = (self.counter, self.data[self.counter])
            self.counter += 1
            return value


print("Test 1: Simple usage")
for index, letter in MyEnumerate('abc'):
    print(f'{index}: {letter}')

# Test 2: Starting index
print("\nTest 2: Starting index")
for index, letter in MyEnumerate('abc', start_index=1):
    print(f'{index}: {letter}')

# Test 3: Non-iterable argument
print("\nTest 3: Non-iterable argument")
try:
    for index, value in MyEnumerate(123):
        print(f'{index}: {value}')
except ValueError as e:
    print(e)
