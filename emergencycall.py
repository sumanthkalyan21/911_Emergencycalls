import pandas as pd
import seaborn as sns
from datetime import datetime
import calendar
import matplotlib.pyplot as plt
df = pd.read_csv('911.csv')

df['timeStamp'] = df['timeStamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
df['Year'] = df['timeStamp'].apply(lambda t: t.year)
df['Month'] = df['timeStamp'].apply(lambda t: calendar.month_name[t.month])
df['Day'] = df['timeStamp'].apply(lambda t: t.day)
df['Date'] = df['timeStamp'].apply(lambda t: t.date())
df['type'] = df['title'].apply(lambda t: t.split(':')[0])
print(df.columns)
#print(df.head())

print(df[['title','type']].head(5))
print(df[['timeStamp','Year','Month','Day','Date']].head(5))
print(df.drop('timeStamp', axis=1, inplace=True))
print(df.columns)
print(df.shape)
print(df.head())
df = df.dropna(how='any', axis=0)
print(df.head(10))
print(df.shape)


#Diffrent types of calls
print(df['type'].value_counts())
#visualizing the graph
plt.show(sns.countplot(x='Month' , data=df, hue='type'))

plt.show(sns.countplot(x='type',data=df))

