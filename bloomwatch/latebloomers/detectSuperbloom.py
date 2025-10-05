import cv2
import numpy as np



def isSuperBloom(image1,image2):
    def detect_color(image_path, lower_hsv, upper_hsv):
        image = cv2.imread(image_path)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
        return mask

    def testOverlap(image1, image2):
        mask_blue = detect_color(image1, np.array([95, 80, 40]), np.array([105, 110, 60]))
        mask_green = detect_color(image2, np.array([35, 50, 90]), np.array([85, 255, 255])) 
        overlap_mask = cv2.bitwise_and(mask_blue, mask_green)
        total_pixels= overlap_mask.size
        overlapping_pixels = cv2.countNonZero(overlap_mask)
        overlap_percentage = (overlapping_pixels / total_pixels) * 100

        return overlap_percentage
    
    if testOverlap(image1,image2) > 0:
        return True
    else:
        return False
        
