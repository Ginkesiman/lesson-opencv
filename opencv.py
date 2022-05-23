import cv2

cascade = cv2.CascadeClassifier(
    r"C:\Users\sota1\Documents\haarcascades\haarcascade_frontalface_alt.xml")
img = cv2.imread(r"C:\Users\sota1\Documents\woman.jpg")
facerect = cascade.detectMultiScale(img)
for rect in facerect:
    cv2.rectangle(img, tuple(rect[0:2]), tuple(
        rect[0:2]+rect[2:4]), (255, 255, 255), thickness=2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
