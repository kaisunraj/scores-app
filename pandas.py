import pandas as pd

def to_pandas_df(event_name):
    file_path = event_name + '.json'
    with open(file_path, 'r') as f:
        data = f.readlines()
    data = data[0][:-1]
    df = pd.read_json(data, lines=True)
    df['rank'] = df['Score'].rank(method='dense', ascending=False)
    df.index += 1
    df.drop(columns=['Event'], inplace=True)
    df.sort_values(by=['rank'], inplace= True, ascending = True)
    return df