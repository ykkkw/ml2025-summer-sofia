class NumberList:
    def __init__(self):
        self.numbers = []

    def insert(self, n_i):
        self.numbers.append(n_i)

    def search(self, x):
        try:
            # Return 1-based index
            return self.numbers.index(x) + 1
        except ValueError:
            return -1
