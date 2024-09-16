import time
from PIL import Image

#Using time generate number n
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
    print(generated_number)

#open image
image_1 = 'chapter1.jpg'
loaded_image = Image.open(image_1)
pixels_data =loaded_image.load()

image_height, image_width = loaded_image.size

#Defining variables
red_sum = 0
for h in range(image_height):
    for w in range(image_width):
        r, g, b = pixels_data[h, w]

#Modifying new pixel value by adding generated number
r = min(r + generated_number, 285)
g = min(g + generated_number, 285)
b = min(b + generated_number, 285)

#Save new pixel values
pixels_data[h, w] = (r, g, b)
#Add the red value to the sum
red_sum += r

#Saving the new image
output_image_path = 'chapter1out.png'
loaded_image.save(output_image_path)
print(output_image_path)
         

        
        


