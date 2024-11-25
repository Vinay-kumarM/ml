import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
# Step 1: Load the Iris dataset
iris = datasets.load_iris()
X = iris.data # Features (sepal length, sepal width, petal length, petal width)
y = iris.target # Target (species label)
# For binary classification, we'll select only two classes: 0 (setosa) and 1 (versicolor)
binary_classes = [0, 1]
X_binary = X[np.isin(y, binary_classes)]
y_binary = y[np.isin(y, binary_classes)]
# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.3, random_state=42)
# Step 3: Train the SVM model
# We will use the linear kernel for simplicity
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)
# Step 4: Predict the labels for the test set
y_pred = svm_model.predict(X_test)
# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
# Step 6: Visualize the decision boundary (using only 2 features for simplicity)
# Let's consider only two features for easy visualization (sepal length and sepal width)
X_train_2D = X_train[:, :2] # Use only sepal length and sepal width
X_test_2D = X_test[:, :2]
# Train the model on the 2D data
svm_model.fit(X_train_2D, y_train)
# Create a mesh grid to plot decision boundaries
x_min, x_max = X_train_2D[:, 0].min() - 1, X_train_2D[:, 0].max() + 1
y_min, y_max = X_train_2D[:, 1].min() - 1, X_train_2D[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
 np.arange(y_min, y_max, 0.1))
# Predict for every point in the mesh grid
Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# Plot the decision boundaries
plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm)
plt.scatter(X_train_2D[:, 0], X_train_2D[:, 1], c=y_train, marker='o', label='Training points',
cmap=plt.cm.coolwarm)
plt.scatter(X_test_2D[:, 0], X_test_2D[:, 1], c=y_test, marker='x', label='Testing points',
cmap=plt.cm.coolwarm)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('SVM Decision Boundary (Binary Class: Setosa vs Versicolor)')
plt.legend()
plt.show()
