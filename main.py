import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the original image
original_img = mpimg.imread('otter.jpg')

# Vertically slice the image by taking every second pixel
v_sliced_img = original_img[:, ::2, :]
v_sliced_img2 = original_img[:, 1::2, :]
v_sliced_imgs = np.concatenate((v_sliced_img, v_sliced_img2), axis=1)

# Horizontally slice the vertically sliced images by taking every second pixel
h_sliced_img1 = v_sliced_img[::2, :, :]
h_sliced_img2 = v_sliced_img[1::2, :, :]
h_sliced_img3 = v_sliced_img2[::2, :, :]
h_sliced_img4 = v_sliced_img2[1::2, :, :]
h_sliced_imgs_l = np.concatenate((h_sliced_img1, h_sliced_img2), axis=0)
h_sliced_imgs_r = np.concatenate((h_sliced_img3, h_sliced_img4), axis=0)
h_sliced_imgs = np.concatenate((h_sliced_imgs_l, h_sliced_imgs_r), axis=1)

# Combine all sliced images for comparison
sliced_imgs = np.concatenate((v_sliced_imgs, h_sliced_imgs), axis=0)
full_comp = np.concatenate((original_img, sliced_imgs), axis=0)

# plt.imsave('full_comp.jpg', full_comp)

# Display the combined image
plt.axis('off')  # Turn off axis labels
plt.imshow(full_comp)
plt.show()

