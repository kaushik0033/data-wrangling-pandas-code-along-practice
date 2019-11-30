# --------------
import pandas as pd 
# Read the data using pandas module.
data=pd.read_csv(path)
data.info()
data.describe()
data.shape
data.isnull().sum()
data.columns
# Find the list of unique cities where matches were played
list(data['city'].unique())
# Find the columns which contains null values if any ?
data.columns[data.isna().any()].tolist()
# List down top 5 most played venues
data.groupby('venue').sum().sort_values('inning',ascending=True).head(5).index.tolist()
# Make a runs count frequency table
data.runs.value_counts()
data['date'] = pd.to_datetime(data['date'])
# How many seasons were played and in which year they were played 
print("how many Seasons are played=",len(data.date.dt.year.unique()))
# No. of matches played per season
print("Matches played in years=",data.date.dt.year.unique().tolist())
# Total runs across the seasons
data.groupby(data.date.dt.year)['runs'].sum()
# Teams who have scored more than 200+ runs. Show the top 10 results
filter_data=pd.DataFrame(data.groupby(['match_code','team1'])['total'].sum().reset_index().sort_values('total',ascending=False))
filter_data.head(10)
# What are the chances of chasing 200+ target
high_scores=data.groupby(['match_code','inning','batting_team'])['total'].sum().reset_index()
high_scores=high_scores[high_scores['total']>=200]
high_scores1=high_scores[high_scores['inning']==1]
high_scores2=high_scores[high_scores['inning']==2]
high_scores1=high_scores1.merge(high_scores2[['match_code','inning', 'total']], on='match_code')
high_scores1.rename(columns={'inning_x':'inning_1','inning_y':'inning_2',
                             'total_x':'inning1_runs','total_y':'inning2_runs'},inplace=True)

high_scores1=high_scores1[high_scores1['inning1_runs']>=200]
high_scores1['is_score_chased']=1
import numpy as np
high_scores1['is_score_chased'] = np.where(high_scores1['inning1_runs']<=high_scores1['inning2_runs'], 'yes', 'no')
len(high_scores1[high_scores1['is_score_chased']=='yes'])/high_scores1.shape[0]*100
# Which team has the highest win count in their respective seasons ?
data.winner.value_counts().idxmax()


