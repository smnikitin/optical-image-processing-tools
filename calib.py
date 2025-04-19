import numpy as np
import cv2

# Define the chessboard dimensions
num_corners_horizontal = 9
num_corners_vertical = 6

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points, like (0,0,0), (1,0,0), ..., (8,5,0)
objp = np.zeros((num_corners_horizontal * num_corners_vertical, 3), np.float32)
objp[:, :2] = np.mgrid[0:num_corners_horizontal, 0:num_corners_vertical].T.reshape(-1, 2)

# Arrays to store object points and image points
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# Load and process calibration images
# cal plate from https://github.com/opencv/opencv/blob/4.x/doc/pattern.png
# rendering in blender
# camera paramners : f = 15 mm, 1000 x 1000, 10 mm x 10 mm, pixel size 10 um
calibration_images = [r'C:\Job\img_proc_tools\data_examples\cal1.png',r'C:\Job\img_proc_tools\data_examples\cal2.png']

for image_file in calibration_images:
    # Load the calibration image
    
    image = cv2.imread(image_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (num_corners_horizontal, num_corners_vertical), None)

    # If corners are found, add object points and image points
    if ret == True:
        objpoints.append(objp)
        # refining pixel coordinates for given 2d points.
        corners2 = cv2.cornerSubPix(gray, corners, (11,11),(-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv2.drawChessboardCorners(image, (num_corners_horizontal, num_corners_vertical), corners, ret)
        cv2.imshow('Chessboard Corners', image)

        cv2.waitKey(0)

cv2.destroyAllWindows()

# Calibrate the camera

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Print the camera matrix and distortion coefficients
print("Camera Matrix:")
print(mtx)
print("\nDistortion Coefficients:")
print(dist)
print(gray.shape[::-1])