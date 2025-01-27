import pandas as pd
import json
import ast

df = pd.read_csv('./resources/test_data_shareGPT.csv')


# Function to parse JSON and extract 'from' and 'value'
def extract_fields(list_of_dicts):
    # Convert string representation to list of dictionaries, if needed
    if isinstance(list_of_dicts, str):
        list_of_dicts = ast.literal_eval(list_of_dicts)  # Safely parse the string into a list
    
    # Extract 'from' and 'value' fields
    from_values = [d['from'] for d in list_of_dicts]
    value_values = [d['value'] for d in list_of_dicts]
    return pd.Series([from_values, value_values])


# iteration every row and 

def create_message_array(index):
    series=extract_fields(df['conversations'][index])
    # create a message list
    messages = []
    for i in range(len(series[0])):
        messages.append({"from": series[0][i], "value": series[1][i]})

    return messages



messages=create_message_array(1)
print(messages)


