import pandas as pd
def solution(df):
    for i in df.columns:
        if df[i].isna().sum() > len(df[i]) / 2:
            df = df.drop(columns =[i])
    
    if len(df.columns) % 2 == 1:
        thresh = len(df.columns) // 2 +1
    else : 
        thresh = len(df.columns) //2  
    df = df.dropna(axis = 0,thresh = thresh )
    # print(df)
    for i in df.columns : 
        if df[i].dtype in ('float64', 'int64') :
            df[i] = df[i].fillna(df[i].mean())
        else:
            # print(df[i].mode())
            df[i] = df[i].fillna(df[i].mode()[0])
    print(df)
    return df.reset_index(drop = True)