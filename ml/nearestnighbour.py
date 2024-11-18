#Implementation of k-Nearest Neighbour algorithm. 
from google.colab import files

# Upload the CSV file
uploaded = files.upload()
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# Load the dataset
data = pd.read_csv('student-por (1).csv', sep=',')  # Ensure the correct file name

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Check for null values
print("\nNull values in each column:")
print(data.isnull().sum())

# Encode categorical variables
categorical_cols = ['school', 'sex', 'address', 'famsize', 'Pstatus',
                    'Mjob', 'Fjob', 'reason', 'guardian',
                    'nursery', 'higher', 'internet', 'romantic']
encoder = OneHotEncoder(drop='first')  # Drop first to avoid dummy variable trap
encoded_features = encoder.fit_transform(data[categorical_cols]).toarray()

# Create a DataFrame for encoded features
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))

# Combine encoded features with numeric features, ensuring G3 is included
numeric_features = data[['age', 'Medu', 'Fedu', 'traveltime', 'studytime',
                         'failures', 'famrel', 'freetime', 'goout',
                         'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']]

# Create the final DataFrame that includes the dependent variable G3
final_data = pd.concat([encoded_df.reset_index(drop=True), numeric_features.reset_index(drop=True)], axis=1)

# Display the columns of final_data to confirm G3 is included
print("\nColumns in final_data:")
print(final_data.columns)

# Define independent variables (X) and dependent variable (y)
X = final_data.drop('G3', axis=1)  # Independent variables
y = final_data['G3']                 # Dependent variable (final grade)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Value (Accuracy): {r2:.2f}")

# Visualize the results
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel('Actual G3 Grades')
plt.ylabel('Predicted G3 Grades')
plt.title('Actual vs Predicted G3 Grades')
plt.plot([0, 20], [0, 20], color='red', linestyle='--')  # Diagonal line
plt.show()