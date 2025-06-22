# Model Training and Inference Example

This example demonstrates the complete workflow of:
1. Training a neural network model
2. Saving the trained model
3. Loading and using the saved model for inference

## Project Structure

- `training.py`: Trains a simple linear regression model and saves it
- `inference.py`: Loads the saved model and makes predictions
- `linear_model.keras`: The saved model file (created after training)

## Workflow Steps

### 1. Training (training.py)
```bash
python training.py
```
- Trains a model to learn y = 5x + 5 relationship
- Saves the trained model as 'linear_model.keras'
- Shows initial test predictions to verify training

### 2. Inference (inference.py)
```bash
python inference.py
```
- Loads the previously saved model
- Provides an interactive interface to make predictions
- Enter any number to get a prediction
- Type 'q' to quit

## Requirements
```
tensorflow
numpy
```

## Example Usage

1. First train and save the model:
   ```bash
   python training.py
   ```
   This will create 'linear_model.keras' in the current directory.

2. Then use the model for predictions:
   ```bash
   python inference.py
   ```
   You can input any number to get predictions or 'q' to quit.

## Tips
- You only need to run training.py once to create the model
- After training, you can use inference.py as many times as needed
- The saved model can be shared and used on other machines