import tensorflow as tf
import numpy as np
from tensorflow import keras

# Generate training data points for y = 5x + 5
xs = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
ys = 5 * xs + 5  # y = 5x + 5

# Create and compile a simple model for linear relationship
model = tf.keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
print("\nTraining the model...")
model.fit(xs, ys, epochs=1000, verbose=0)

# Test predictions
print("\n" + "="*50)
print("MODEL PREDICTION RESULTS")
print("="*50)

# Test with more values
test_values = np.array([10.0, 15.0, 20.0])
predictions = model.predict(test_values, verbose=0)
expected = 5 * test_values + 5

#print("\n. Tests:")
print("-"*40)
print(f"{'Input x':>10} {'Expected y':>12} {'Predicted y':>12}")
print("-"*40)
for x, exp, pred in zip(test_values, expected, predictions.flatten()):
    print(f"{x:>10.1f} {exp:>12.1f} {pred:>12.1f}")
print("="*50)