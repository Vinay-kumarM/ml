# Simple Linear regression: Predict the sepal length (cm) of the iris flowers
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = datasets.load_iris()

# Convert the dataset into a pandas DataFrame
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Select all features except 'sepal length (cm)' as independent variables (X)
# Independent variables
X = iris_data[['sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
y = iris_data['sepal length (cm)']   # Dependent variable (target)

# Split the data into training (80%) and testing sets (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the sepal length for the test data
y_pred = model.predict(X_test)

# Print actual vs predicted values
for i in range(len(X_test)):
    print(f"Sepal Width: {X_test.iloc[i, 0]:.2f}, Petal Length: {X_test.iloc[i, 1]:.2f}, Petal Width: {
          X_test.iloc[i, 2]:.2f}, Actual Sepal Length: {y_test.iloc[i]:.2f}, Predicted Sepal Length: {y_pred[i]:.2f}")

# Calculate the mean squared error (MSE) and R-squared score (accuracy)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Value (Accuracy): {r2:.2f}")

# Plotting actual vs predicted values (only on one feature, for visualization)
plt.scatter(X_test['petal length (cm)'], y_test,
            color='blue', label='Actual Sepal Length')
plt.scatter(X_test['petal length (cm)'], y_pred,
            color='red', label='Predicted Sepal Length')
plt.title('Petal Length vs Sepal Length (Test Data)')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()
