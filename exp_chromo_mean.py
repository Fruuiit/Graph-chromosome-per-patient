import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.sparse import dok_matrix
import csv

pd.set_option('display.max_columns', 50)
df = pd.read_csv('patientlist.csv')
df1 = pd.read_csv('ENS Ids By Chromosome (all edited).csv')
df3 = df.join(df1.set_index('ENS ID'), on='ENS ID')
del df3['Transcript length (including UTRs and CDS)']
#df3.loc[df3['Chromosome/scaffold name'] == '1']
	#df3['Chromosome/scaffold name'].where(df3['ENS ID'] =)

#look1 = df3.groupby(['Chromosome/scaffold name']).mean()
look1 = df3.groupby(['Chromosome']).mean()
look1['meanp'] = look1.mean(axis=1)
new1 = look1[['meanp']].copy()
new1.plot()

#ax.set_xticks(look1.index)
#ax.set_xticks(df3.index)
#ax.set_xticks
print(look1)

plt.show()



#print(df1);

