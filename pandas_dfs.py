import pandas as pd

def to_pandas_df(event_name):
    file_path = event_name + '.json'
    with open(file_path, 'r') as f:
        data = f.readlines()
    data = data[0][:-1]
    df = pd.read_json(data, lines=True)
    df['rank'] = df['Score'].rank(method='dense', ascending=False)
    df = df.set_index('Team')
    df.drop(columns=['Event'], inplace=True)
    df.sort_values(by=['rank'], inplace= True, ascending = True)
    df = df.rename(columns={"rank":"Points"})
    return df


def event_dfs(event):
    json_name = event + '.json'
    with open(json_name, 'r') as f:
        data = f.readlines()
    data = data[0][:-1]
    df = pd.read_json(data, lines=True)
    df['Points'] = df['Score'].rank(method='dense', ascending=False)
    df.drop(columns=['Event'], inplace=True)
    df.sort_values(by=['Points'], inplace= True, ascending = True)
    df = df.set_index('Team')
    return df


