import cv2
import os

def resize_image(input_image_path, output_image_path, new_width=None, new_height=None):
    
    image = cv2.imread(input_image_path)
    
    
    height, width, _ = image.shape
    
    
    aspect_ratio = width / height
    
    # Calculate new dimensions while preserving the aspect ratio
    if new_width is None and new_height is not None:
        new_width = int(new_height * aspect_ratio)
    elif new_height is None and new_width is not None:
        new_height = int(new_width / aspect_ratio)
    
    
    resized_image = cv2.resize(image, (new_width, new_height))
    
    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)

def batch_resize_images(input_folder, output_folder, new_width=None, new_height=None):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get the list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    
    # Resize each image in the input folder
    for image_file in image_files:
        input_image_path = os.path.join(input_folder, image_file)
        output_image_path = os.path.join(output_folder, image_file)
        resize_image(input_image_path, output_image_path, new_width, new_height)


input_folder = 'input'
output_folder = 'output'
new_width = 800
new_height = 600

# Single image resize
input_image = 'input.jpg'
output_image = 'output.jpg'
resize_image(input_image, output_image, new_width, new_height)

# Batch image resize
batch_resize_images(input_folder, output_folder, new_width, new_height)
