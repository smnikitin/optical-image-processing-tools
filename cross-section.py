# Example usage:
# Assuming you have a grayscale image stored in a numpy array called 'image'
# and you want to plot a cross-sections


import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


# Read your image here and store it in the 'image' variable
# Specify the path to the image file on your C drive
image_path = r'C:\Job\img_proc_tools\data_examples\test.bmp'

# Open the image using openCV and Convert to grayscale

image_gray= cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# Convert the grayscale image to a NumPy array
image_array = np.array(image_gray)

# Create global variables for the initial coordinates and cross-section lines
initial_y = image_array.shape[0] // 2
initial_x = image_array.shape[1] // 2
cross_section_horizontal = image_array[initial_y, :]
cross_section_vertical = image_array[:, initial_x]

# Create a figure and axes with subplots
fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(9, 9))

# Function to update the cross-sections
def update_cross_sections(y, x):
    global initial_y, initial_x, cross_section_horizontal, cross_section_vertical
    initial_y = y
    initial_x = x
    cross_section_horizontal = image_array[y, :]
    cross_section_vertical = image_array[:, x]
    ax1.lines[0].set_ydata(y)
    ax1.lines[1].set_xdata(x)
    ax2.lines[0].set_ydata(cross_section_horizontal)
    ax3.lines[0].set_ydata(cross_section_vertical)
    fig.canvas.draw()

# Function to handle keyboard events
def on_key(event):
    if event.key == 'up':
        new_y = max(0, initial_y - 10)
        update_cross_sections(new_y, initial_x)
    elif event.key == 'down':
        new_y = min(image_array.shape[0] - 1, initial_y + 10)
        update_cross_sections(new_y, initial_x)
    elif event.key == 'left':
        new_x = max(0, initial_x - 10)
        update_cross_sections(initial_y, new_x)
    elif event.key == 'right':
        new_x = min(image_array.shape[1] - 1, initial_x + 10)
        update_cross_sections(initial_y, new_x)

# Connect the keyboard event handler
fig.canvas.mpl_connect('key_press_event', on_key)

# Plot the original image on the left subplot
ax1.imshow(image_gray, cmap='gray')
ax1.axhline(initial_y, color='red', linestyle='--')
ax1.axvline(initial_x, color='blue', linestyle='--')
ax1.set_title('Original Image with Cross-Section Lines')

# Plot the initial horizontal cross-section on the top-right subplot
line1, = ax1.plot([0], [initial_y], color='red', linestyle='--')
line2, = ax2.plot(cross_section_horizontal)
ax2.set_xlabel('Pixel Index')
ax2.set_ylabel('Intensity')
ax2.set_title('Horizontal Cross-Section')

# Plot the initial vertical cross-section on the bottom-left subplot
line3, = ax1.plot([initial_x], [0], color='blue', linestyle='--')
line4, = ax3.plot(cross_section_vertical)
ax3.set_xlabel('Pixel Index')
ax3.set_ylabel('Intensity')
ax3.set_title('Vertical Cross-Section')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
