import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# Reuse our image function (modified to return both original and processed)
def getBarnOwlImage():
    barnOwlPath = Path('cnn/Bird Speciees Dataset/BARN OWL')
    import os
    import random
    
    imageFiles = [f for f in os.listdir(barnOwlPath) if os.path.isfile(os.path.join(barnOwlPath, f))]
    
    if imageFiles:
        randomImage = random.choice(imageFiles)
        imagePath = os.path.join(barnOwlPath, randomImage)
        img = cv2.imread(str(imagePath))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Resize to MNIST dimensions (28x28)
        resized = cv2.resize(gray, (28, 28))
        return img, resized
    return None, None

# Load the Fashion MNIST dataset
def loadMnistData():
    (trainImages, trainLabels), (testImages, testLabels) = tf.keras.datasets.fashion_mnist.load_data()
    
    # Normalize pixel values to be between 0 and 1
    trainImages = trainImages / 255.0
    testImages = testImages / 255.0
    
    # Reshape for CNN input (add channel dimension)
    trainImages = trainImages.reshape((trainImages.shape[0], 28, 28, 1))
    testImages = testImages.reshape((testImages.shape[0], 28, 28, 1))
    
    return (trainImages, trainLabels), (testImages, testLabels)

# Build the CNN model
def buildCnnModel():
    model = models.Sequential()
    
    # First convolutional layer
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    
    # Second convolutional layer
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    
    # Third convolutional layer (adding an extra layer as suggested)
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    
    # Flatten and Dense layers
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(10))  # 10 classes for Fashion MNIST
    
    # Compile model
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )
    
    return model

# Function to test our barn owl image with the model
def testOurImage(model):
    # Get our image
    originalImg, processedImg = getBarnOwlImage()
    
    if processedImg is not None:
        # Normalize and reshape for prediction
        processedImg = processedImg / 255.0
        processedImg = processedImg.reshape(1, 28, 28, 1)
        
        # Make prediction
        predictions = model.predict(processedImg)
        predictedClass = np.argmax(predictions[0])
        
        # Class names for Fashion MNIST
        classNames = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                     'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        
        print(f"Our Barn Owl image is classified as: {classNames[predictedClass]}")
        
        # Display the image
        plt.figure(figsize=(6, 3))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(originalImg, cv2.COLOR_BGR2RGB))
        plt.title("Original Barn Owl Image")
        
        plt.subplot(1, 2, 2)
        plt.imshow(processedImg.reshape(28, 28), cmap='gray')
        plt.title(f"Processed (28x28)\nClassified as: {classNames[predictedClass]}")
        
        plt.tight_layout()
        plt.savefig('barn_owl_mnist_classification.png')
        plt.show()
    else:
        print("Failed to load Barn Owl image")

def main():
    # Load Fashion MNIST data
    (trainImages, trainLabels), (testImages, testLabels) = loadMnistData()
    
    # Build model
    model = buildCnnModel()
    
    # Train model (with a small subset for demonstration)
    print("Training model on Fashion MNIST data...")
    # Using a very small subset and few epochs for demonstration
    model.fit(
        trainImages[:1000], 
        trainLabels[:1000], 
        epochs=2,
        validation_data=(testImages[:100], testLabels[:100])
    )
    
    # Evaluate model
    testLoss, testAcc = model.evaluate(testImages[:100], testLabels[:100], verbose=2)
    print(f"Test accuracy: {testAcc:.4f}")
    
    # Test our barn owl image with the model
    testOurImage(model)

if __name__ == "__main__":
    main()
