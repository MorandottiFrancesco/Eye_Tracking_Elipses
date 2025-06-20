import cv2
import numpy as np
import os


UPSCALE = 8

# path to the directory containing the input images
input_path = 'C:\\Users\\FMorandotti\\OneDrive\\Documenti\\Phyton Scripts\\cheetah\\input' #folder where to take the pictures
upscaled_path = 'C:\\Users\\FMorandotti\\OneDrive\\Documenti\\Phyton Scripts\\cheetah\\upscaled' #folder where to put just upscaled: ONLY 1 EVERY 15 TO SAVE MEMORY
blurred_path = 'C:\\Users\\FMorandotti\\OneDrive\\Documenti\\Phyton Scripts\\cheetah\\blurred' #folder where to put upscaled + gaussian blur 15 pixels: ONLY 1 EVERY 15 TO SAVE MEMORY

final_path = 'C:\\Users\\FMorandotti\\OneDrive\\Documenti\\Phyton Scripts\\cheetah' #folder where to put the final pictures

# read in all PNG images from the input directory
images = []
for filename in os.listdir(input_path):
    if filename.endswith('.png'):
        image_path = os.path.join(input_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        images.append(image)

# upscale all images by a factor of UPSCALE
upscaled_images = []
blurred_images = []
for i , image in enumerate(images):
    upscaled_image = cv2.resize(image, None, fx=UPSCALE, fy=UPSCALE, interpolation=cv2.INTER_CUBIC) #OPTIONAL: use INTER_LINEAR instead of INTER_CUBIC
    upscaled_images.append(upscaled_image)

    blurred_image = cv2.GaussianBlur(upscaled_image, (15,15), 0)
    blurred_images.append(blurred_image)


    if (i % 15 == 0):
        cv2.imwrite(os.path.join(upscaled_path, f'upscaled{i}.png'), upscaled_image)
        cv2.imwrite(os.path.join(blurred_path, f'blurred{i}.png'), blurred_image)


# generate the picture composed by the average of all the upscaled images OPTION: try other statistical combinations, like median etc etc...
average_image = np.mean(upscaled_images, axis=0)
average_blurred_image = np.mean(blurred_images, axis=0)


# define the sharpening kernel OPTION: try different kernels. this is just quick google search for sharpening kernel
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# apply the sharpening filter
average_blurred__sharpened_image = cv2.filter2D(average_blurred_image, -1, kernel)

#OPTION: increse the UPSCALE factor and use INTER_AREA to downscale back (if target is x8 use upscale x32 and then here divide by 4)
#average_image = cv2.resize(average_image, None, fx=1/4, fy=1/4, interpolation = cv2.INTER_AREA)
#average_blurred_image = cv2.resize(average_blurred_image, None, fx=1/8, fy=1/8, interpolation = cv2.INTER_AREA)
#average_blurred__sharpened_image = cv2.resize(average_blurred__sharpened_image, None, fx=1/8, fy=1/8, interpolation = cv2.INTER_AREA)



# save the final images 
cv2.imwrite(os.path.join(final_path, 'average.png'), average_image)
cv2.imwrite(os.path.join(final_path, 'blurred.png'), average_blurred_image)
cv2.imwrite(os.path.join(final_path, 'sharpened.png'), average_blurred__sharpened_image)

