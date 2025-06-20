import cv2

# specify the location of the input image file
input_file = "C:\\Users\\FMorandotti\\OneDrive\\Documenti\\Phyton Scripts\\cheetah\\test.png" 

# read the input image using OpenCV
input_image = cv2.imread(input_file)

# upscale the input image by a factor of 8
upscaled_image = cv2.resize(input_image, None, fx=8, fy=8, interpolation=cv2.INTER_CUBIC)

# specify the location of the output image file
output_file = "C:\\Users\\FMorandotti\\OneDrive\Documenti\\Phyton Scripts\\cheetah\\test_out.png"

# save the output image to the specified location
cv2.imwrite(output_file, upscaled_image)