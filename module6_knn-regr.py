import numpy as np

class KNNcalculator:
    def __init__(self):
        self.Xlist = []
        self.Ylist = []

    def insert(self, x, y):
        self.Xlist.append(x)
        self.Ylist.append(y)

    def predict(self, x_query, k):
        distances = np.abs(np.array(self.Xlist) - x_query)
        print(distances)
        nn_indices = np.argsort(distances)[:k]
        print(nn_indices)
        pred = np.mean(np.array(self.Ylist)[nn_indices])
        return pred

def main():
    N = int(input("Enter N (number of data points): "))
    k = int(input("Enter k nearest neighbor want to find: "))
    knnmethod = KNNcalculator()
    for i in range(N):
        x = float(input(f"Enter input point x {i+1}: "))
        y = float(input(f"Enter input point y {i+1}: "))
        knnmethod.insert(x, y)
    X_query = float(input("Enter X to predict: "))
    if k > N:
        print("enter k <= N")
    else:
        y_pred = knnmethod.predict(X_query, k)
        print(y_pred)

if __name__ == "__main__":
    main()
