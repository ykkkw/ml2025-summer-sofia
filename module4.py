N = int(input("Input N numbers: "))
nbr_lst = []
for i in range(N):
    num = int(input(f"Input the {i+1} number: "))
    nbr_lst.append(num)
X = int(input("Enter the number to search: "))
if X in nbr_lst:
    print(f"The index of value {X} is:", nbr_lst.index(X) + 1)
else:
    print(-1)
