import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

# Initialize the Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def sanitize_filename(file_name):
    # Replace spaces with underscores
    return file_name.replace(" ", "_")

def upload_image(file_path):
    # Sanitize file name
    file_name = sanitize_filename(os.path.basename(file_path))
    bucket_name = 'images'
    with open(file_path, 'rb') as file:
        response = supabase.storage.from_(bucket_name).upload(f'public/{file_name}', file)
        print("Upload response:", response)
        if response.status_code != 200:
            print("Error uploading image:", response.status_code)
            return None
        return file_name

def get_image_url(file_name):
    response = supabase.storage.from_('images').get_public_url(f'public/{file_name}')
    print("Get public URL response:", response)
    # if response.:
    #     print("Error getting image URL:", response['error'])
    #     return None
    return response

def upload_and_get_image_url(file_path):
    file_name = upload_image(file_path)
    if file_name:
        return get_image_url(file_name)
    return None

# Test the functions
# image_path = './images/2-input-and-gate.png'
# image_url = upload_and_get_image_url(image_path)

# ----------------------------

#now, open the csv file, read the name column, retrieve the image with same name from the folder, upload it to supabase, and get the image url, add that url in a new column in the csv

import pandas as pd

# Read the CSV file
df = pd.read_csv('./resources/new2.csv')

# Get the names of the images from the folder with extension
image_names = os.listdir('./images')

# Get the names of the images from the CSV
csv_image_names = df['name'].tolist()

#create a new column in the csv
df=df[['name','explanation']]
df['image_url'] = None

# Iterate over the rows of the CSV, if duplicate arises, remove that row from csv
for index, row in df.iterrows():
    name = row['name']
    try:
        if name in image_names:
            image_path = f'./images/{name}'
            image_url = upload_and_get_image_url(image_path)
            if image_url:
                df.loc[index, 'image_url'] = image_url
            else:
                print(f"Error uploading image for {name}")
        else:
            print(f"non-existing  image name: {name}")
            df.drop(index, inplace=True)
    except Exception as e:
        print(f"Error uploading image for {name}: {e}")


# Save the updated CSV

df.to_csv('./resources/new_with_image_url.csv', index=False)

#length of the updated csv
print('Number of rows in the updated csv:', len(df))





