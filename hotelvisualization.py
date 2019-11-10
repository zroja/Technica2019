import csv
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#prints out the data for Las Vegas Hotels
data = pd.read_csv("lasvegas_tripadvisor.csv") 
data.head()

#violin plot which shows months that the SPA was more popular than others
import seaborn as sns
data = pd.read_csv("lasvegas_tripadvisor.csv") 
g= sns.catplot(x="Review month", y="Score", hue="Spa",
            kind="violin", split=True, data=data)
g.fig.set_figwidth(17.27)
g.fig.set_figheight(11.7)

#lists columns that are in the dataset
for col in data.columns: 
    print(col)
    
#Month that the hotel is reviewed vs the quality of the hotel     
data = pd.read_csv("lasvegas_tripadvisor.csv") 
g=sns.catplot(x="Review month", y="Hotel stars", hue="Score",
            kind="bar", data=data);
g.fig.set_figwidth(17.27)
g.fig.set_figheight(11.7)

#name of hotels and the ratings that people in the past gave them
data = pd.read_csv("lasvegas_tripadvisor.csv") 
g=sns.catplot(x="Hotel stars", y="Hotel name", hue="Score",
            kind="bar", data=data);
g.fig.set_figwidth(17.27)
g.fig.set_figheight(11.7)

