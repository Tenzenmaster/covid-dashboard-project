import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("covid_data/country_wise_latest.csv")
print(data.corr)
sns.pairplot(data)
plt.savefig("out.png")