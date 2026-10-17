import pandas as pd

def solution(df):

    df = df[df['status'] == 'completed']
    df = df.groupby('region').agg({'amount':'sum'})
    df = df.reset_index()
    df= df.sort_values('amount',ascending = False)[:10]

    return df
    pass
