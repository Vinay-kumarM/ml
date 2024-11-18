# Implementation of K Means
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
# Using the Iris dataset (this dataset is often used for clustering tasks)
iris = datasets.load_iris()
X = iris.data  # Feature matrix (4 features for each data point)
y = iris.target  # Target labels (not used for clustering)

# Step 2: Preprocess the data (Standardizing)
# We use only the first two features for 2D visualization
X = X[:, :2]  # First two features: sepal length and sepal width

# Standardizing the data to have mean=0 and variance=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply K-Means clustering
# Let's choose k=3 since we know that the Iris dataset has 3 classes
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Step 4: Get the results of clustering
labels = kmeans.labels_  # Cluster labels for each data point
centroids = kmeans.cluster_centers_  # Coordinates of the centroids
inertia = kmeans.inertia_  # Sum of squared distances to the closest centroid

# Print the cluster centers and inertia
print("Cluster Centers (Centroids):")
print(centroids)
print(f"Inertia: {inertia}")

# Step 5: Visualize the clusters (using 2D data)
plt.figure(figsize=(8, 6))

# Plot the data points with different colors based on their cluster labels
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels,
            cmap='viridis', marker='o', label='Data Points')

# Plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], c='red',
            marker='X', s=200, label='Centroids')

# Customize the plot
plt.title('K-Means Clustering on Iris Dataset (First 2 Features)')
plt.xlabel('Standardized Sepal Length')
plt.ylabel('Standardized Sepal Width')
plt.legend()
plt.grid(True)
plt.show()
