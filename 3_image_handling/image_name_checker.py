
# a csv has name columns, a folder has images with the same names, check if all the images are in the csv
import os
import pandas as pd

# read the csv file
df = pd.read_csv('./resources/with_urls.csv')

# get the names of the images from the folder with extension
image_names = os.listdir('./images')



# get the names of the images from the csv
csv_image_names = df['name'].tolist()

# check their lengths
print('Number of images in the folder:', len(image_names))
print('Number of images in the csv:', len(csv_image_names))


print('Images in the folder but not in the csv:')
for image_name in image_names:
    if image_name not in csv_image_names:
        print(image_name)

# check if all the images in the csv are in the folder
print('Images in the csv but not in the folder:')
for csv_image_name in csv_image_names:
    if csv_image_name not in image_names:
        print(csv_image_name)



#double forward biasing circuit in csv, and double image in the folder