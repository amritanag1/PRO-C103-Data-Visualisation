import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

a = px.scatter(df, x="date", y="cases", color="country",  title='Covid Data')
a.show()