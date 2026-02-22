# Import libraries
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data (Hours Studied -> Exam Score)
X = np.array([2, 4, 6, 8]).reshape(-1, 1)  # Input (feature)
y = np.array([50, 65, 80, 90])            # Output (label)

# Create the model
model = LinearRegression()

# Train the model (supervised learning)
model.fit(X, y)

# Make predictions
new_hours = np.array([5]).reshape(-1, 1)
predicted_score = model.predict(new_hours)

print(f"Predicted exam score for 5 hours studied: {predicted_score[0]:.2f}")
