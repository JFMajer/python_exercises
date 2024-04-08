class Circle:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.num:
            raise StopIteration
        value = self.seq[self.counter % len(self.seq)]
        self.counter += 1
        return value


c = Circle('abc', 5)
print(list(c))
