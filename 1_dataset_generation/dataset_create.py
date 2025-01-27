
import pandas as pd

df = pd.read_csv('resources/conversations.csv')
df2 = pd.read_csv('resources/questions_with_topic.csv')


df2 = df2.drop_duplicates(subset='questions')
df= df.drop_duplicates(subset='question1')
print(df2.shape)
print(df.shape)

df = pd.merge(df, df2, left_on='question1', right_on='questions', how='left')

df = df.drop(columns=['questions'])


print("nulls", df.isnull().sum())
print("duplicate", df.duplicated().sum())
print(df.shape)

df.to_csv('resources/dataset.csv', index=False)

# unique values of area and topic and their counts in a text file


area_counts = df['area'].value_counts()

# Write the counts to a text file
with open('info.txt', 'a') as f:
    f.write("Area counts\n")
    for value, count in area_counts.items():
        f.write(f"{value}: {count}\n")

    f.write("\n\n")


topic_counts = df['topic'].value_counts()

# Write the counts to a text file
with open('info.txt', 'a') as f:
    f.write("Topic counts\n")
    for value, count in topic_counts.items():
        f.write(f"{value}: {count}\n")

    f.write("\n\n")


# df = df.dropna()
# print("nulls",df.isnull().sum())





# df.to_csv('resources/questions.csv',index=False)
# print(df.shape)



