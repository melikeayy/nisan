import cv2

image = cv2.imread("image.png")
blue_channel, green_channel, red_channel = cv2.split(image)

cv2.imshow("Mavi kanal", blue_channel)
cv2.imshow("Yeşil kanal", green_channel)
cv2.imshow("Kırmızı kanal", red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Renk kanalı değiştirme R ile B
modified_image = cv2.merge([red_channel,green_channel,blue_channel])
cv2.imshow("Değiştirilmiş renkler", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Metin yazdırma
cv2.putText(image, "Melike Ay", (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imshow("Metin", image)
cv2.waitKey(0)
cv2.destroyAllWindows()