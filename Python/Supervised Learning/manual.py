# Sample data
X = [2, 4, 6, 8]   # hours studied
y = [50, 65, 80, 90]  # exam scores

# Calculate means
x_mean = sum(X) / len(X)
y_mean = sum(y) / len(y)

# Calculate slope (m)
numerator = sum((X[i] - x_mean) * (y[i] - y_mean) for i in range(len(X)))
denominator = sum((X[i] - x_mean)**2 for i in range(len(X)))
m = numerator / denominator

# Calculate intercept (b)
b = y_mean - m * x_mean

print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")

# Prediction function
def predict(x):
    return m * x + b

# Predict exam score for 5 hours studied
predicted_score = predict(5)
print(f"Predicted exam score for 5 hours studied: {predicted_score:.2f}")
