from PIL import Image
import matplotlib.pyplot as plt

image_1 = Image.open("hw_1_1.jpg")

plt.figure("image_1")
plt.imshow(image_1)
plt.show()