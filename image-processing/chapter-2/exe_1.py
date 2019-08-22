# Import the color module
from skimage.color import rgb2gray

# Import the filters module and sobel function
from skimage.filters import sobel
from matplotlib import pyplot as plt

soaps_image = plt.imread('')
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
# Make the image grayscale
soaps_image_gray = rgb2gray(soaps_image)

# Apply edge detection filter
edge_sobel = sobel(soaps_image_gray)

# Show original and resulting image to compare
show_image(soaps_image, "Original")
show_image(edge_sobel, "Edges with Sobel")