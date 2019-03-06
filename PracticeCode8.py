class PowTwo:
    def __init__(self, max = 0):
        self.max = 0
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < self.max:
            result = 2**self.n
            self.n +=1
            return result
        else:
            raise StopIteration
class ReplaceRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        self.instance = self.start
        return self
    def __next__(self):
        result = 0
        if self.instance < self.stop:
            val = self.instance
            self.instance += self.step
            return val
        else:
            raise StopIteration
def main():
    x = ReplaceRange(0,5,1)
    print(x)
    for i in x:
        print(i)
main()
