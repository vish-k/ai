import tensorflow as tf
import numpy as np
import os

def load_model(model_path):
    """Load the saved model from the specified path."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No model found at {model_path}. Please train the model first.")
    return tf.keras.models.load_model(model_path)

def predict(model, x):
    """Make predictions using the loaded model."""
    if isinstance(x, (int, float)):
        x = np.array([x])
    elif isinstance(x, list):
        x = np.array(x)
    return model.predict(x, verbose=0)

def main():
    model_path = 'linear_model.keras'  # Changed to use current directory
    
    try:
        # Load the model
        model = load_model(model_path)
        print("Model loaded successfully!")

        # Example predictions
        test_values = [25.0, 30.0, 40.0]  # Different values from training script
        predictions = predict(model, test_values)
        expected = 5 * np.array(test_values) + 5  # y = 5x + 5

        print("\nPrediction Results:")
        print("-" * 40)
        print(f"{'Input x':>10} {'Expected y':>12} {'Predicted y':>12}")
        print("-" * 40)
        for x, exp, pred in zip(test_values, expected, predictions.flatten()):
            print(f"{x:>10.1f} {exp:>12.1f} {pred:>12.1f}")

        # Interactive prediction
        while True:
            user_input = input("\nEnter a number to predict (or 'q' to quit): ").strip().lower()
            if user_input == 'q':
                print("\nExiting...")
                break
                
            try:
                x = float(user_input)
                prediction = predict(model, x)
                expected = 5 * x + 5
                print(f"\nInput x     = {x:>10.1f}")
                print(f"Expected y  = {expected:>10.1f}")
                print(f"Predicted y = {prediction[0][0]:>10.1f}")
            except ValueError:
                print("\nInvalid input. Please enter a number or 'q' to quit.")
                continue

    except FileNotFoundError as e:
        print(e)
        print("Please run hello-model.py first to train and save the model.")

if __name__ == "__main__":
    main()