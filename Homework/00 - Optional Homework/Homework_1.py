import pandas as pd
import numpy as np

def read_dataset():
    url='https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/interactive_data.csv'
    data=pd.read_csv(url,index_col=0)
    return data

def clean_dataset(data):
    data.loc[(data.Intent=='None selected')|(data.Intent=='Unknown'),'Intent']=np.nan
    data.loc[(data.Gender=='None selected'),'Gender']=np.nan
    data.loc[(data.Race=='None selected')|(data.Race=='Other'),'Race']=np.nan
    data.loc[(data.Age=='None selected'),'Age']=np.nan
    return data

def perform_tasks(data):
    # task 1 & 3
    task_1=data.groupby(['Intent'],as_index=False)[['Deaths']].sum()
    task_1['ratio']=round(task_1['Deaths']/sum(task_1.Deaths),2)
    print("Suicide rate: {}%".format(task_1.loc[task_1['Intent']=='Suicide'].iloc[0]['ratio']*100))
    print("Homicide rate: {}%".format(task_1.loc[task_1['Intent']=='Homicide'].iloc[0]['ratio']*100))
    
    # task 2
    task_2=data[data['Intent']=='Suicide'].groupby(['Gender'],as_index=False)[['Deaths']].sum()
    task_2['ratio']=round(task_2.Deaths/sum(task_2.Deaths),2)
    print("Suicide rate by males: {}%".format(task_2.loc[task_2['Gender']=='Male'].iloc[0]['ratio']*100))
    
    # task 4
    task_4=data[(data['Intent']=='Homicide')&(data['Age']=='15 - 34')&(data.Gender=='Male')].groupby(['Race'],as_index=False)[['Deaths']].sum()
    task_4['ratio']=round(task_4.Deaths/sum(task_4.Deaths),2)
    print('Rate of black homicide victims who are males in the age-group of 15--34: {}%'.format(task_4.loc[task_4['Race']=='Black'].iloc[0]['ratio']*100))
    
    # task 5
    task_5=data[data['Intent']=='Homicide'].groupby(['Gender'],as_index=False)[['Deaths']].sum()
    task_5['ratio']=round(task_5.Deaths/sum(task_5.Deaths),2)
    print('Rate of women homicide victims {}%'.format(task_5.loc[task_5['Gender']=='Female'].iloc[0]['ratio']*100))

if __name__=='__main__':
    data=read_dataset()
    data_clean=clean_dataset(data)
    perform_tasks(data_clean)
    