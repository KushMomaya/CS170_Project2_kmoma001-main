import numpy as np
from CrossValidation import *

data = np.loadtxt('../CS170_Small_Data__60.txt')
X = data[:, 1:]
Y = data[:, 0]

def forward_search(X, Y):
    current_set = []
    best_set = []
    best_accuracy = 0

    for i in range(1, len(X[0]) + 1):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_add = []
        best_sofar_accuracy = 0

        for k in range(1, len(X[0]) + 1):
            if k in current_set:
                continue

            print("Considering adding the " + str(k) + "th feature")
            accuracy = loocv(X, Y, current_set, k)

            if accuracy > best_accuracy:
                best_sofar_accuracy = accuracy
                feature_to_add = k

        current_set.append(feature_to_add)
        print("Added feature " + str(feature_to_add) + " to current set")
        
        if best_sofar_accuracy > best_accuracy:
            best_accuracy = best_sofar_accuracy
            best_set = current_set


forward_search(X, Y)