import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar las dos imágenes
image1 = cv2.imread('1.png')
image2 = cv2.imread('2.png')

# Asegurarse de que las imágenes tengan el mismo tamaño
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# Sumar las dos imágenes
sum_image = cv2.add(image1, image2)

# Restar las dos imágenes
sub_image = cv2.subtract(image1, image2)

# Convertir las imágenes de BGR a RGB para mostrar correctamente con matplotlib
sum_image_rgb = cv2.cvtColor(sum_image, cv2.COLOR_BGR2RGB)
sub_image_rgb = cv2.cvtColor(sub_image, cv2.COLOR_BGR2RGB)
image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

# Mostrar las imágenes
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image1_rgb)
plt.title('Imagen 1')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(image2_rgb)
plt.title('Imagen 2')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(sum_image_rgb)
plt.title('Suma de Imágenes')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(sub_image_rgb)
plt.title('Resta de Imágenes')
plt.axis('off')

plt.tight_layout()
plt.show()