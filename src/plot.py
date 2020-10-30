import pandas as pd
import numpy as np
import pyreadstat
import matplotlib.pyplot as plt
import random
from scipy import stats
plt.style.use('ggplot')
import cleaned_df from data_analysis.py 

def conting_hist()

    labels = ['Does Not See Opportunity', 'See Opportunity']
    yes_fear_bar = df_FFPO[df_FFPO['fearfail'] == 1.0]['opport'].value_counts()
    no_fear_bar = df_FFPO[df_FFPO['fearfail'] == 0.0]['opport'].value_counts()
    x = np.arange(len(labels))
    width = 0.20
    fig, ax = plt.subplots(figsize=(8, 7))
    rects1 = ax.bar(x - width/2, yes_fear_bar, width, label="Cites Fearing Failure")
    rects2 = ax.bar(x + width/2, no_fear_bar, width, label="Does Cite Fearing Failure")

    # text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of People', fontsize=16)
    ax.set_xlabel('Sees Opportunity vs Does Not', fontsize=16)
    ax.set_title('Fear of Failure by Opportunity vs No Opportunity Globally', fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(fontsize=14)

    plt.savefig('img/fisher_hist.png')


if __name__ == '__main__':
    
    '''Fig 1. Compare fear of failure within opportunity vs no opportunity'''
