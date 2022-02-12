import cv2
import numpy as np
import matplotlib.pyplot as plt

# Helper Function
def transform(translate = True, scale = False, rotate = False, path = 'media/sword.jpg', display = True):
    
    # Read the image from path
    img = cv2.imread(path)

    # Copy the original so it does not get overwritten
    original = img.copy()
    
    # Get the dimensions of the image
    rows,cols  = img.shape[:2]
    
    # get two random numbers  for translation
    x,y = np.random.randint(30,50,size=(2,))
    
    # get a random angle for rotation
    angle = np.random.randint(10,180)
    
    # get random float value for resizing the image
    scale_value = round(np.random.uniform(0.6, 1.3),2)    
    
    # just randomly making positive values negative depending upon if there are even or odd (not important)
    if x % 2:
        x = -x
    if y % 2:
        y = -y
    
    # apply translation according to the random numbers
    if translate:
        
        # Creat a translation matrix
        M = np.float32([[1,0,x],[0,1,y]])
        
        # Apply translation
        img = cv2.warpAffine(img,M,(cols,rows), borderMode=1) 
        print("Applied Translation of x: {} , y: {}".format(x,y))
        
    # apply rotation according to the random angle
    if rotate:
        
        # Create a rotational matrix
        M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
        
        # Apply rotation
        img = cv2.warpAffine(img,M,(cols,rows), borderMode=1)
        print("Applied rotation of angle: {}".format(angle))

        
    if scale:
        
        # Resize the image while maintaining the dimensions
        img = cv2.resize(img, (0,0), fx=scale_value, fy=scale_value)
        print("Image resized to: {}%".format(scale_value*100))

    # Convert the image to gray-scale
    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # Create a binary image with thresholding 
    ret,binary = cv2.threshold(grayimg,220, 255, cv2.THRESH_BINARY_INV)  
    
    # Find the external contours
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    # Select a contour
    cnt = contours[0]
    
    # Display the images
    if display:
        plt.figure(figsize=[18,18])
        plt.subplot(121);plt.imshow(original[:,:,::-1]);plt.title("Original Image")
        plt.subplot(122);plt.imshow(img[:,:,::-1]);plt.title("Modified")   
    
    return cnt