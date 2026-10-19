import pandas as pd
def solution(df):
    df = df.copy()
    df['name'] = df['name'].apply(lambda x : x.strip().title())
    df['date'] = df['date'].apply(lambda x : x.strip())
    df['date'] = pd.to_datetime(df['date'].str.strip()).dt.strftime('%Y-%m-%d')
    df = df.drop_duplicates(inplace = False)
    df.reset_index(drop = True,inplace = True)
    df['value'] = df['value'].fillna(df['value'].mean())
    # print( df)
    return df