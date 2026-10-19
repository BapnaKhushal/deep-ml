import pandas as pd

def solution(df1, df2, df3):
    df = df1.merge(df2,on = 'emp_id', how = 'inner')
    df = df.merge(df3,on = 'emp_id', how = 'left')
    df.reset_index(drop = True,inplace = True)
    print(df)
    return df

    pass