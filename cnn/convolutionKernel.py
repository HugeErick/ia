import os
import random
import cv2
import numpy as np
from pathlib import Path

def getRandomBarnOwlImage():
    # Define the path to the Barn Owl directory
    barnOwlPath = Path('cnn/Bird Speciees Dataset/BARN OWL')
    
    # Get list of all files in the directory
    imageFiles = [f for f in os.listdir(barnOwlPath) if os.path.isfile(os.path.join(barnOwlPath, f))]
    
    # Select a random image
    if imageFiles:
        randomImage = random.choice(imageFiles)
        imagePath = os.path.join(barnOwlPath, randomImage)
        return cv2.imread(str(imagePath))
    else:
        return None

def applyConvolutionKernels(image):
    if image is None:
        print("No image provided")
        return
    
    # Convert to grayscale if the image is in color
    if len(image.shape) == 3:
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        grayImage = image

    # Define various kernels
    sobelXKernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    
    sobelYKernel = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    
    laplacianKernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])
    
    sharpenKernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    
    # Apply convolutions
    sobelX = cv2.filter2D(grayImage, -1, sobelXKernel)
    sobelY = cv2.filter2D(grayImage, -1, sobelYKernel)
    sobelCombined = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)
    laplacianResult = cv2.filter2D(grayImage, -1, laplacianKernel)
    sharpenResult = cv2.filter2D(grayImage, -1, sharpenKernel)
    
    # Create dictionary of results
    results = {
        'original': grayImage,
        'sobelX': sobelX,
        'sobelY': sobelY,
        'sobelCombined': sobelCombined,
        'laplacian': laplacianResult,
        'sharpen': sharpenResult
    }
    
    return results

def displayResults(results):
    if results is None:
        print("No results to display")
        return
    
    # Display all results
    for name, image in results.items():
        cv2.imshow(f'Filter: {name}', image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Get random image
    randomImage = getRandomBarnOwlImage()
    
    if randomImage is not None:
        # Apply convolution kernels
        filterResults = applyConvolutionKernels(randomImage)
        
        # Display results
        displayResults(filterResults)
    else:
        print("Failed to load image")

if __name__ == "__main__":
    main()
