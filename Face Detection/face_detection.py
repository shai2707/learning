import cv2

imp_img = cv2.VideoCapture('elon.jpeg')

res, img = imp_img.read()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('Elon Image', gray)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()





