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

def main():
    N = int(input("Enter n values to save in list: "))
    num_list = NumberList()
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        num_list.insert(num)
    X = int(input("Enter the value to search: "))
    result = num_list.search(X)
    print(result)

if __name__ == "__main__":
    main()
