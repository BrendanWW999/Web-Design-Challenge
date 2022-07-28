import pandas as pd

df = pd.read_csv('Resources/cities.csv')
df.to_html("City.html", index = False, classes = "table")