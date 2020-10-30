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
print( fishers_exact_test(col1_label, col2_label, cleaned_df) )

def bayes_AB_test(): 
    # distribution of fear for people who do not see opportunity around them
    no_opport_dist = np.random.beta(a=1+41192, b=1+51434, size=10000) #success = Opport: 0, Fear: 1 failure = Opport: 0, Fear: 0

    # distribution of fear for people who do see opportunity around them 
    yes_opport_dist = np.random.beta(a=1+22869, b=1+41437, size=10000)
    #success = Opport: 1, Fear: 1 failure = Opport: 1, Fear: 0

    # find propobility of fear of failure being greater when perception of opportunity is not present
    prob = (no_opport_dist > yes_opport_dist).mean() * 100
    return prob

def conting_hist(cleaned_df):
    labels = ['Does Not See Opportunity', 'See Opportunity']
    yes_fear_bar = cleaned_df[cleaned_df['fearfail'] == 1.0]['opport'].value_counts()
    no_fear_bar = cleaned_df[cleaned_df['fearfail'] == 0.0]['opport'].value_counts()
    x = np.arange(len(labels))
    width = 0.20
    fig, ax = plt.subplots(figsize=(8, 7))
    rects1 = ax.bar(x - width/2, yes_fear_bar, width, label="Cites Fearing Failure")
    rects2 = ax.bar(x + width/2, no_fear_bar, width, label="Does Cite Fearing Failure")
    ax.set_ylabel('Number of People', fontsize=16)
    ax.set_xlabel('Sees Opportunity vs Does Not', fontsize=16)
    ax.set_title('Fear of Failure by Opportunity vs No Opportunity Globally', fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(fontsize=14)
    plt.savefig('../img/fisher_hist.png')
    return fig 

def bayes_AB_dist(cleaned_df):
    probs = np.linspace(0.3, 0.6, 1000)
    # people who do not see opportunities around them - % of people who have a fear of failure
    no_opport_dist = stats.beta(a=1+41192, b=1+51434) #success = Opport: 0, Fear: 1 failure = Opport: 0, Fear: 0
    # people who do see opportunity around them - % of people who have a fear of failure
    yes_opport_dist = stats.beta(a=1+22869, b=1+41437)
    #success = Opport: 1, Fear: 1 failure = Opport: 1, Fear: 0
    densities_yes_opport = yes_opport_dist.pdf(probs)
    densities_no_opport = no_opport_dist.pdf(probs)
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(probs, densities_yes_opport, color='grey', label='Sees opportunity to start a business')
    ax.plot(probs, densities_no_opport, color='blue', label='Does not see opportunity to start a business')
    #ax.fill_between(probs, densities, color='lightseagreen', alpha=.8)
    ax.set_title(f'Posterior Belief About Fear of Failure for Opportunity Perception Groups', fontsize=20)
    ax.set_xlabel('Probability Fear of Failure ', fontsize=15)
    ax.set_ylabel('Probability Density', fontsize=15);
    ax.legend(loc="upper right", fontsize=14)
    plt.savefig('img/Bayes_AB_prob.png')
    return fig 

def edu_hist(cleaned_df): 
    labels = [0, 1, 2, 3, 4, 5, 6]

    yes_fear_bar = cleaned_df[cleaned_df['fearfail'] == 1.0]['UNEDUC'].value_counts()
    no_fear_bar = cleaned_df[cleaned_df['fearfail'] == 0.0]['UNEDUC'].value_counts()
    yes_fear_bar
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(15,10))
    rects1 = ax.bar(x - width/2, yes_fear_bar, width, label="Cites fear of failure")
    rects2 = ax.bar(x + width/2, no_fear_bar, width, label="Does not cite fear of failure")

    # text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of People', fontsize=16)
    ax.set_xlabel('Education Level', fontsize=16)
    ax.set_title('Fear of Failure by Education Level', fontsize=20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(fontsize=14)
    plt.savefig('img/Fear_education.png')
    return fig 

if __name__ == '__main__':
    
    # import data, index columns of interest, remove nan
    cols_name_lst = ['ctryalp', 'opport', 'fearfail', 'gender', 'age', 'UNEDUC', 'knowent', 'suskill', 'GEMHHINC']
    file_name = "data/GEM 2016 APS Global - Individual Level Data.sav"
    cleaned_df = cleaned_data(file_name, cols_name_lst)

    # Run Fisher's exact test using a contingency table 
    col1_label = 'opport'
    col2_label = 'fearfail'
    fishers_exact_test(col1_label, col2_label, cleaned_df)

    # create a histogram for fear of failure vs opportunity 
    '''Compare fear of failure for opportunity vs no opportunity groups'''
    conting_hist(cleaned_df)

    # calculate and plot a bayes A/B test comparing two 
    # groups (one that sees opportunity and one that doesn't) in if they cite fear 
    # as the reason that prevents them from starting a business
    '''Compare fear of failure for opportunity vs no opportunity groups'''
    bayes_AB_dist(cleaned_df)

    # What is the probability I will have fear of failure if I do not perceive opportunity?
    bayes_AB_test()

    # create a histogram for fear of failure vs education level
    '''Compare fear of failure with level of education'''
    edu_hist(cleaned_df)
