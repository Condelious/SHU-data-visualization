import time
import csv
import pandas as pd
import numpy as np


gdp=r'data/gdp.csv'
gdppc=r'data/gdppc.csv'

def get_excel_data(filename:str,i:int):
    df=pd.read_excel(filename)
    return(df.iloc[-i:])

def get_map_data(i):
     df = pd.read_excel(gdp)
     gdpa = df.iloc[-i:]
     df = pd.read_excel(gdppc)
     gdppca = df.iloc[-i:]
    
     return gdpa ,gdppca


def get_csv_column_data(filename:str,i:int):
    df=pd.read_csv(filename,dtype='str')
    df=df.fillna('NaN')
    return(df.iloc[:,i])

def get_csv_data(filename:str,i:int):
    df=pd.read_csv(filename)
    return(df.iloc[:-i])