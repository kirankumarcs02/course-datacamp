# Import the try all function
from skimage.filters import try_all_threshold
from matplotlib import pyplot as plt
# Import the rgb to gray convertor function
from skimage.color import rgb2gray


fruits_image = plt.imread('../data/chapter-1/fruit-2.jpg')
# Turn the fruits image to grayscale
grayscale = rgb2gray(fruits_image)

# Use the try all method on the grayscale image
fig, ax = try_all_threshold(grayscale, verbose=False)

# Show the resulting plots
plt.show()