import pandas as pd

import plotly.express as px

covid = pd.read_csv("./csv files/Covid-data.csv")

data = px.line(covid, x="Date", y="Cases",  
               color="Country", title='Covid Analyze')

data.show()
        