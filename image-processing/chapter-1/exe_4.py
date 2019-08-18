# Import the otsu threshold function
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from matplotlib import pyplot as plt


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


chess_pieces_image = plt.imread('../data/chapter-1/bw.jpg')
# Make the image grayscale
chess_pieces_image_gray = rgb2gray(chess_pieces_image)

# Obtain the optimal threshold value
thresh = threshold_otsu(chess_pieces_image_gray)

# Apply thresholding to the image
binary = chess_pieces_image_gray > thresh

# Show the image
show_image(binary, 'Binary image')