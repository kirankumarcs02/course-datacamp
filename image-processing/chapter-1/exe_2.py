import numpy as np
from matplotlib import pyplot as plt


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


flipped_seville = plt.imread('../data/chapter-1/sevilleup.jpg')
# Flip the image vertically
seville_vertical_flip = np.flipud(flipped_seville)

# Flip the image horizontally
seville_horizontal_flip = np.fliplr(flipped_seville)

# The original, flipped image
show_image(flipped_seville, 'Flipped Seville')

# Show the resulting image
show_image(seville_horizontal_flip, 'Seville')