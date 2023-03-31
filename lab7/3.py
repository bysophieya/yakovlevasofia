from PIL import Image
import cv2
image1 = cv2.imread(r'C:\Users\User\Desktop\1.jpg')
image2 = cv2.imread(r'C:\Users\User\Desktop\2.jpg')
image3 = cv2.imread(r'C:\Users\User\Desktop\3.jpg')
image4 = cv2.imread(r'C:\Users\User\Desktop\4.jpg')
image5 = cv2.imread(r'C:\Users\User\Desktop\5.jpg')
gray_image = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY) #это одноканальная версия изображения.
cv2.imshow("Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()