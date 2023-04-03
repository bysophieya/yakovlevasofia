import os
import cv2
from PIL import Image
i=6
for image in os.listdir(r'C:\Users\User\Desktop\laba7'):
    image = cv2.imread(os.path.join(r'C:\Users\User\Desktop\laba7', image))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
gray_image.save(r'C:\Users\User\Desktop\laba7.1\filters/'+str(image))
