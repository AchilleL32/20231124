import numpy as np
from PIL import Image
import copy

# Load the image using PIL
image_path = 'Logo-Tesla.jpg'

image = Image.open(image_path)

# Convert the image to grayscale
image_gray = image.convert('L')

# Convert the grayscale image to a binary (black and white) image
# where pixels with a value greater than a threshold are white (0) 
# and the rest are black (1).
threshold = 128  # The threshold can be adjusted as needed
image_binary = image_gray.point(lambda x: 0 if x > threshold else 1, '1')

# Convert the binary image to a numpy array
numpy_array = np.array(image_binary, dtype=int)

# Save the numpy array to a file
np.save('numpy_array.npy', numpy_array)
np.set_printoptions(threshold=np.inf)
# Print the whole numpy array
print(numpy_array)

