import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Read N and k
    N = int(input("Enter N points: "))
    k = int(input("Enter k nearest-neighbors: "))

    # Read N (x, y) points
    x_list = []
    y_list = []
    for i in range(N):
        x = float(input(f"Enter x {i+1}: "))
        y = float(input(f"Enter y {i+1}: "))
        x_list.append([x])
        y_list.append(y)

    x_train = np.array(x_list)
    y_train = np.array(y_list)

    # Variance of labels
    y_var = np.var(y_train)
    print(f"Variance of labels: {y_var}")

    # Read query X
    X_new = float(input("Enter X to predict Y: "))

    # k-NN Regression
    if k > N:
        print("Error: k <= N")
    else:
        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(x_train, y_train)
        y_pred = knn.predict(np.array([[X_new]]))
        print(f"For X={X_new}, Y is predicted as {y_pred[0]} via kNN")


if __name__ == "__main__":
    main()