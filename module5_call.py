from module5_oop import NumberList

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