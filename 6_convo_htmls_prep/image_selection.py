import pandas as pd

df=pd.read_csv('../4_image_vectorization/resources/human_evaluation_retrieval.csv')


df = df[df['score'] > 110]

print(df.shape)

# randomize the rows
df = df.sample(frac=1).reset_index(drop=True)
print(df.shape)

df.to_csv('./resources/images.csv', index=False)

# set n = 2n-1 and 2n th image


## 187 images above the threshold