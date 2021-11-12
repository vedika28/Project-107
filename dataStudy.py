import pandas as pd, plotly.graph_objects as pgo, random

data=pd.read_csv("data.csv")


studentId=data.loc[data['student_id']=='TRL_mno']
mean=studentId.groupby("level")["attempt"].mean()
print(mean)
fig=pgo.Figure(pgo.Bar(x=["Level 1","Level 2","Level 3","Level 4"],y=mean))
fig.show()
