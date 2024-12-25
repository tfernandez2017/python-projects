# run python3 command
# takes 2 arguments
# 1st argument is to go in to Pokedex folder
# 2nd argument is to create a new folder
import sys
import os
from PIL import Image

# using sys grab 1st & 2nd argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check is new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All done!')
# Loop through Pokedex/
# Convert to PNG
# save them to the new folder