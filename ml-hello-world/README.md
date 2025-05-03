# Simple Neural Network Training Example

This example demonstrates how to train a basic neural network using TensorFlow to learn a linear relationship. The model learns the pattern `y = 5x + 5` through training data and iterative improvement.

## Overview

The model learns to predict values based on the linear equation `y = 5x + 5`. For example:
- When x = 1, y should be 10 (5×1 + 5)
- When x = 2, y should be 15 (5×2 + 5)
- And so on...

## How the Model Works

1. **Model Architecture**
   ```python
   model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
   ```
   - Uses a single dense layer with one neuron
   - Perfect for learning linear relationships
   - Takes a single input value and produces a single output

2. **Training Data**
   - Input values (xs): [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
   - Output values (ys): [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
   - Each pair follows the pattern y = 5x + 5

## Impact of Training Data and Epochs

### Training Data
- **More data points** help the model:
  - Learn the pattern more accurately
  - Generalize better to new inputs
  - Understand the relationship across a wider range
- Our example uses 14 points spanning from -5 to 8
- This wide range helps the model learn the pattern reliably

### Epochs
An epoch is one complete pass through all training data. The model improves with more epochs:

- **10 epochs**: Initial learning, rough approximation
- **50 epochs**: Better understanding of the pattern
- **100 epochs**: Further refinement
- **500 epochs**: Very precise predictions
- **1000 epochs**: Extremely accurate results

You can observe this improvement in the training output:
1. Loss decreases with more epochs
2. Predictions become more accurate
3. Model confidence increases

## Running the Example

1. Requirements:
   ```
   tensorflow
   numpy
   ```

2. Run the script:
   ```bash
   python hello-model.py
   ```

## Experiment Yourself!

Try modifying:
1. **Number of epochs**: Increase/decrease to see impact on accuracy
2. **Training data**: Add more points or change the range
3. **Test values**: Try predicting different values

## Understanding the Output

The script tests the model's predictions with multiple test values (10, 15, 20) and shows both the expected and predicted values. You can observe how well the model has learned the linear relationship y = 5x + 5.

The loss value shown during training indicates how far the model's predictions are from the true values. A decreasing loss means the model is improving, and in this implementation, the loss becomes extremely small (on the order of 1e-10), indicating that the model has learned the relationship very accurately.

## Tips for Better Results

1. **Data Quality**:
   - Use evenly spaced data points
   - Cover the range you're interested in
   - Include both positive and negative values

2. **Training Duration**:
   - More epochs generally give better results
   - Stop when improvement plateaus
   - Watch for diminishing returns

3. **Validation**:
   - Test with values outside your training range
   - Verify predictions match the expected pattern
   - Monitor the loss value during training