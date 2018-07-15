import matplotlib.pyplot as plt
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("\nThe dimension of train_images is: " + str(train_images.ndim))
print("\nThe shape of train_images is: " + str(train_images.shape))
print("\nThe data type of train_images is: " + str(train_images.dtype))
digit = train_images[4]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()
