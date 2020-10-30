import pandas as pd
import numpy as np
import pyreadstat
import random
from scipy import stats


def cleaned_data(file_name, cols_name_lst):
    df, meta = pyreadstat.read_sav(file_name)
    indexed_df = df[cols_name_lst]
    cleaned_df = indexed_df.dropna()
    return cleaned_df 

def fishers_exact_test(col1_label, col2_label, cleaned_df): 
    conting_t = pd.crosstab(cleaned_df[col1_label], cleaned_df[col2_label])
    pvalue = stats.fisher_exact(conting_t)
    return pvalue 


if __name__ == '__main__':
    
    # import data, index columns of interest, remove nan
    cols_name_lst = ['ctryalp', 'opport', 'fearfail', 'gender', 'age', 'UNEDUC', 'knowent', 'suskill', 'GEMHHINC']
    file_name = "../data/GEM 2016 APS Global - Individual Level Data.sav"
    cleaned_df = cleaned_data(file_name, cols_name_lst)

    # create a contingency table for input to calculate the p-value using Fisher's exact test 
    col1_label = 'opport'
    col2_label = 'fearfail'
    print(fishers_exact_test(col1_label, col2_label, cleaned_df))