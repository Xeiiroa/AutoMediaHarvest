import pandas as pd

def pandas_settings():
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.max_rows', 50)
    pd.set_option('display.max_colwidth', 32)
    pd.set_option('display.width', 120)
    pd.set_option('expand_frame_repr', True)
    

if __name__ == '__main__':
    pandas_settings()