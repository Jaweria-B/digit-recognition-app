# 🎨✏️ Handwritten Digit Recognition App 🤖💡

<p align="center">
  <img src="./assets/imgs/pencil.png" alt="Handwritten Digit Recognition" width="600" height="400">
</p>

### 🚀 Overview
Welcome to the Handwritten Digit Recognition App! 🎉 This exciting app allows users to unleash their creativity by drawing handwritten digits and receiving predictions using a machine learning model. Users can interact with the app through a Streamlit interface and a Pygame window.

### 📁 File Structure
- **handwriting.py**: This script 📊📈 loads the dataset, preprocesses it, trains a convolutional neural network (CNN) model, and saves the trained model as `model.h5`.
- **recognition.py**: This script loads the trained model from `model.h5` and implements a Pygame interface where users can draw digits and get predictions using the loaded model.
- **app.py**: This is the Streamlit app file where users interact with the digit recognition app. It includes a button to start the drawing process.

### 🛠️ Commands
To run each file separately:

1. **handwriting.py**:
   - To create and save the model: `python handwriting.py model.h5`
   - To train the model without saving: `python handwriting.py`

2. **recognition.py**:
   - To make predictions through the Pygame interface: `python recognition.py model.h5`

3. **app.py**:
   - To run the Streamlit app: `streamlit run app.py`

### 📊 Data Set
The app uses the MNIST dataset, which consists of 28x28 grayscale images of handwritten digits (0 to 9). The dataset is split into training and testing sets for model training and evaluation.

### ⚙️ Methodology
1. **Data Preprocessing**: Images are normalized and resized to fit the CNN input shape.
2. **Model Architecture**: A CNN is used for digit recognition, consisting of convolutional layers followed by pooling layers and fully connected layers.
3. **Model Training**: The model is trained using the training dataset with stochastic gradient descent (SGD) optimization.
4. **Prediction**: Users can draw digits in the Pygame window, and the trained model makes predictions on the drawn digits.
5. **Streamlit Interface**: The Streamlit app provides a user-friendly interface for interacting with the Pygame-based digit recognition functionality.

### 🎨✏️ How It Works
To use the Handwritten Digit Recognition App:
1. Click the "Start Drawing" button below to begin the drawing process.
2. A Pygame window will open where you can draw a digit using your mouse.
3. For better performance, use mouse clicks for the "Reset" and "Classify" buttons in the Pygame window.
4. Once you've drawn a digit, click the "Classify" button in the Pygame window to see the prediction.
5. You can reset the drawing at any time by clicking the "Reset" button in the Pygame window.

### 🛠️ Technologies Used
- Python
- TensorFlow
- Pygame
- Streamlit
- NumPy

Let your imagination run wild and dive into the fascinating world of handwritten digit recognition! 🎮🕹️✨

