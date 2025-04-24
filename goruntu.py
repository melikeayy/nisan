import cv2

# Görüntüyü oku
image = cv2.imread("image.png")

# Orijinal görüntü boyutu
print("Görüntü Boyutu:", image.shape)

# Orijinal görüntüyü göster
cv2.imshow("Orijinal Görüntü", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gri tonlama
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gri görüntüyü göster
cv2.imshow("Gri Tonlamalı Görüntü", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gri görüntüyü kaydet
cv2.imwrite("gray_image.jpg", image_gray)

# HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Görüntü:", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

