# ai_student_performance.py
# Beginner AI project: Student Performance Prediction

"""
This is a simple machine learning example that predicts student performance
based on study hours using Linear Regression.
This project is for learning and portfolio demonstration purposes.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

# Create sample dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6],
    "Score": [35, 45, 50, 60, 70, 85]
}

df = pd.DataFrame(data)

# Split into features and target
X = df[["StudyHours"]]
y = df["Score"]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict score for a student who studies 7 hours
predicted_score = model.predict([[7]])

print("Predicted score for 7 study hours:", predicted_score[0])
