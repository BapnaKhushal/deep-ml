import pandas as pd


def solution(df):
    # TODO: bucket scores, count per (grade, bucket), cumulative percentage within grade
    df = df.copy()
    df['bucket'] = df['score'].apply(lambda x : 10* (x // 10))
    df['count'] = df.groupby(['grade','bucket'])['score'].transform('count')
    # print(df)
    df = df[['grade', 'bucket', 'count']].drop_duplicates(subset = ['grade','bucket'])
    # print(df)
    df = df.sort_values(['grade','bucket'])
    df['cum_pct'] = df.groupby('grade')['count'].cumsum()
    df['max'] = df.groupby('grade')['cum_pct'].transform('max')
    # print(df)
    df['cum_pct'] = (df['cum_pct']*100/df['max']).round(2)
    df.drop(columns = ['max'],inplace = True)
    df = df.reset_index(drop = True,inplace = False)

    return df