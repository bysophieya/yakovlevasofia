import os
import cv2
for image in os.listdir(r'C:\Users\User\Desktop\laba7'):
    image = cv2.imread(os.path.join(r'C:\Users\User\Desktop\laba7', image))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(r'C:\Users\User\Desktop\laba7', image)