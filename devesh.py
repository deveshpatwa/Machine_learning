import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def fix_col(df):   
    l = list(df.columns)
    l1 = []
    for i in l:
        a= i.lower().replace(' ','_')
        a = a.replace('-','_')
        l1.append(a)
    d = dict(zip(l,l1))
    df.rename(d, axis=1, inplace=True)
    return df

'''remove_outliers will remove the outliers from a givem column in a Data frame'''

def remove_outliers(df,col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3-q1                   # inter quirtile range quater 3 minus quater 1
    lb = q1 - 1.5*iqr                 # lower bound
    ub = q3 + 1.5*iqr                     # upper bound
    return df.loc[(df[col]>lb)&(df[col]<ub)]

'''histall function will make histogram of all the columns from the dataframe'''
def histall(df):
    cl = list(df.columns)
    ln = range(1,(len(cl)+1))
    l = zip(cl,ln)
    s=5
    plt.figure(figsize=(s,s*len(cl)))
    for i,j in l:
        plt.subplot(len(cl),1,j)
        plt.title( i)
        plt.xlabel('-'*100)
        sns.histplot(x=df[i])

# finding only numeric column name and return it list
def find_numeric_col_names(df):
    l = []
    for i in df.columns:
        if df[i].dtype == 'int64' or df[i].dtype == float:
            l.append(i)
    return l
  
  
 # this function will find all the outliers in the df    
def find_outliers(df,threshold=2.5):
    print("% of values outliers in each column")
    numerical_columns = [i for i in df.columns if df[i].dtype == int or df[i].dtype==float ]
    df = df[numerical_columns]
    columns = df.columns
    total_rows = df.shape[0]
    outliers = {}

    for i in columns:
        lower_bound = df[i].median() - df[i].std()*threshold
        upper_bound = df[i].median() + df[i].std()*threshold
        normal_rows_count = df[i].between(lower_bound,upper_bound).sum()
        outliers_rows = total_rows - normal_rows_count
        outlier_percentage = outliers_rows/total_rows*100
        outliers[i] = round(outlier_percentage,2)

    outliers = pd.Series(outliers).sort_values(ascending=False)
    return outliers



