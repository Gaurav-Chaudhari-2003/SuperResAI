import rasterio
import matplotlib.pyplot as plt

# Load LISS3 image
liss3_image = rasterio.open('path_to_liss3_image.tif')
liss3_data = liss3_image.read(1)

# Load LISS4 image
liss4_image = rasterio.open('path_to_liss4_image.tif')
liss4_data = liss4_image.read(1)

# Visualize the images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('LISS3 Image (23m Resolution)')
plt.imshow(liss3_data, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('LISS4 Image (5.8m Resolution)')
plt.imshow(liss4_data, cmap='gray')

plt.show()
