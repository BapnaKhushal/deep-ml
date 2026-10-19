import pandas as pd

def solution(df):

    df = df.pivot_table(index = 'date',columns = 'product',values = 'sales',aggfunc = 'sum')
    df = df.fillna(0)
    # print(df)
    df = df.reset_index()
    df = df.melt(id_vars = 'date',var_name = 'product',value_name = 'sales')

    df = df.sort_values(['date','product'])
    df['sales'] = df['sales'].astype(int)
    return df
    pass