# program to capture single image from webcam in python
  
# importing OpenCV library
import cv2

# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam = cv2.VideoCapture(0)
show_cam = cv2.VideoCapture(0)
  
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    #cv2.imshow("GeeksForGeeks", image)
  
    # saving image in local storage
    cv2.imwrite("getBike.png", image)
  
    cam.release()
    #cv2.destroyWindow("GeeksForGeeks")
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")

#time.sleep(3)
#cv2.destroyAllWindows

