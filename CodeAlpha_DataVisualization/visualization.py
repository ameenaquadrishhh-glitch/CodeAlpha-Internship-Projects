from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(
    df["sepal length (cm)"],
    df["petal length (cm)"]
)
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length")
plt.show()

# Histogram
plt.figure(figsize=(6,4))
df["sepal width (cm)"].hist()
plt.title("Sepal Width Distribution")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()