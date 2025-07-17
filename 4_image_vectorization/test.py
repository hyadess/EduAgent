# open a dataframe and print its contents
import pandas as pd

df1 = pd.read_csv('../3_image_handling/resources/with_image_urls.csv')
df2 = pd.read_csv('./resources/image_with_topic_description.csv')


# match the name columns in both dataframes and see how many rows match

matched_rows = df1[df1['name'].isin(df2['name'])]
print(f"Number of matched rows: {len(matched_rows)}")


# replace image_url in df2 with the image_url from df1 where names match
df2.loc[df2['name'].isin(df1['name']), 'image_url'] = df1.set_index('name').loc[df2['name'], 'image_url'].values

# save the updated df2 to a new CSV file
df2.to_csv('./resources/image_with_topic_description_updated.csv', index=False)