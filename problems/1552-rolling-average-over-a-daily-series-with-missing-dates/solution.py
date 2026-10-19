import pandas as pd
import numpy as np


def solution(df, window):
    # TODO: complete the daily calendar, keep NaN for missing days, trailing calendar-window mean
    df = df.copy()

    df = df.set_index('date').asfreq('D')
    # print(df)
    df['rolling_mean'] = df['value'].rolling(window,min_periods = 1).mean()


    return df.reset_index(inplace = False )
