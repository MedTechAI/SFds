# from imports import *
from _additions_.imports import *



def info_toDF(df0):
    # import io
    df = df0.copy()
    df.columns = [j.replace(' ','_') for j in df.columns]
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    info_df = pd.DataFrame( [line.split() for line in s.splitlines()[3:-2]] ) .fillna('') .drop(0, axis=1)
    info_df.columns = info_df.loc[0].values
    info_df = info_df.iloc[2:]
    info_df['Non-Null'] = info_df['Non-Null'].astype(int)
    info_df['Null'] = df0.shape[0] - info_df['Non-Null']
    info_df['% Non-Null'] = (info_df['Non-Null'] * 100) / df0.shape[0] 
    return info_df .set_index('Column')














