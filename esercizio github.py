import pandas as pd
import numpy as np

np.random.seed(42)  
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

def highlight_columns(s):
    color = ''
    if s.name == 'A':
        color = 'background-color: lightblue'
    elif s.name == 'B':
        color = 'background-color: lightgreen'
    elif s.name == 'C':
        color = 'background-color: lightcoral'
    elif s.name == 'D':
        color = 'background-color: lightgoldenrodyellow'
    return [color] * len(s)

styled_df = df.style.apply(highlight_columns, axis=0)

styled_df
