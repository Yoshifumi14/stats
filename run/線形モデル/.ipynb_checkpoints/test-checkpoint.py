#%%
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%
y=stats.norm.rvs(size=100)

#%%
plt.plot(y)

#%%
sns.distplot(y)

#%%
plt.plot([stats.norm.rvs(loc=i,scale=i) for i in range(1000)])

#%%


#%%
